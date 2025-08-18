<template>
	<div
		:class="{
			'select2-wrapper-danger': errorState,
			'select2-wrapper-success': successState
		}"
	>
		<select 
			v-show="mostrarComponente && !errorApi"
			:id="id"
			class="form-control" 
			:placeholder="placeholder"
			:disabled="disabled"
		>
			<slot></slot>
		</select>
		
		<ScProgressCircular v-show="!mostrarComponente"></ScProgressCircular>
		<span v-show="errorApi" class="uk-text-danger">{{ msjErrorApi }} <span slot="icon" class="mdi mdi-alert-circle uk-text-danger"></span></span>
		
	</div>
</template>

<script>
import { provideApolloClient, useMutation, useQuery } from '@vue/apollo-composable/dist';
import gql from 'graphql-tag'
import { scValidation } from '~/assets/js/utils';
import { ScProgressCircular } from '~/components/progress'

require('~/plugins/jquery');
require('select2');
require('select2/dist/css/select2.min.css');

export default {
	name: 'Cselect',
	components: {
		ScProgressCircular
	},
	model: {
		event: 'change',
		prop: 'value'
	},
	props: {
		id: {
			type: String,
			default: ''
		},
		placeholder: {
			type: String,
			default: ''
		},
		options: {
			type: Array,
			default: () => []
		},
		disabled: {
			type: Boolean,
			default: false
		},
		settings: {
			type: Object,
			default: () => {}
		},
		multiple: {
			type: Boolean,
			'default': false
		},
		value: {
			type: [String, Array],
			default: null
		},
		successState: {
			type: Boolean,
			default: false
		},
		errorState: {
			type: Boolean,
			default: false
		},

		nombreComponente: {
			type: String,
			default: ''
		},
		source: {
			type: String,
			default: ''
		},
		/*where: {
			type: String,
			default: ''
		},*/
		criteria: {//_in, 'exact', 'iexact', 'contains' 'icontains', 'startswith','istartswith','in','gt','lt'
			type: String,
			default: ''
		},
		criteriaFields:{//_in '["A", "b", "C"]'
			type: String,
			default: ''
		},
		queryFields: {//A|B
			type: String,
			default: ''
		},
		ordenBusqueda: {
			type: String,
			default: ''
		},
		/*valorBusqueda: {
			type: String,
			default: ''
		},
		aliasCampos: {
			type: String,
			default: ''
		},
		orderBy: {
			type: String,
			default: ''
		},*/
		loadApi:{
			type: Boolean,
			default: false
		}
	},
	data: () => ({
		select2: null,
		mostrarComponente: false,

		errorApi: false,
		msjErrorApi: '',

		resultQuery:null,
		loading:null,
		mode:null,
	}),
	computed: {
		userSettings () {
			var config = {};
			const self = this;
			Object.keys(this.settings).forEach(function (k) {
				if (k === 'createTag' && self.settings[k] === 'emailAddress') {
					config[k] = function (params) { return !scValidation.emailAddress(params.term) ? null : { id: params.term, text: params.term } };
				}
				// country flags
				else if (k === 'templateResult' && self.settings[k] === 'formatCountryResult') {
					config[k] = function (country) {
						if (!country.id) { return country.text; }
						return $('<span class="select2-search__flags"><span class="flag flag-' + country.id.toLowerCase() + '"></span><span>' + country.text + '</span>');
					}
				}
				else if (k === 'templateSelection' && self.settings[k] === 'formatCountrySelection') {
					config[k] = function (data, container) {
						if (!data.id) { return data.text; }
						return $('<span class="select2-selection__flag"><span class="flag flag-' + data.id.toLowerCase() + '"></span><span>' + data.text + '</span>');
					}
				}
				else {
					config[k] = self.settings[k]
				}
			});
			return config
		},
	},
	watch: {
		options (val) {
			this.setOption(val);
		},
		value (val) {
			this.setValue(val);
		},
		loadApi ( val ){
			if(val){
				let queryResult = this.search().then( response => {
					if(response){
						this.loadSelectOptions(response)
					}
				})
			}
		}
	},
	mounted () {
		if(this.options.length > 0){
			this.select2 = $(this.$el)
				.find('select')
				.select2({
					...this.userSettings,
					data: this.options,
					multiple: this.multiple
				})
				.on('select2:select select2:unselect', ev => {
					this.$emit('change', this.select2.val());
					this.$emit('select', ev['params']['data']);
				})
				.on('select2:open', ev => {
					var $dropdown = $('.select2-dropdown');
					if ($dropdown.hasClass('select2-dropdown--above')) {
						$dropdown.removeClass('uk-animation-slide-top-small').addClass("uk-animation-slide-bottom-small");
					} else {
						$dropdown.removeClass('uk-animation-slide-bottom-small').addClass("uk-animation-slide-top-small");
					}
				});
			this.setValue(this.value);
			this.mostrarComponente = true;

		}else{
			if(this.source){
				console.log('ingresa al else')
				if(this.loadApi){
					let queryResult = this.search().then( response => {
						this.loadSelectOptions(response)
					})
				}
			}
		}
		
	},
	beforeDestroy () {
		this.select2.select2('destroy');
		this.$el.style.height = '45px';
		this.$el.style.visibility = 'hidden';
	},
	methods: {
		setOption (val = []) {
			this.select2.empty();
			this.select2.select2({
				...this.userSettings,
				data: val
			});
			this.setValue(this.value);
		},
		setValue (val) {
			if (val instanceof Array) {
				this.select2.val([...val]);
			} else {
				this.select2.val([val]);
			}
			this.select2.trigger('change');
		},

		loadSelectOptions (response){
			this.mostrarComponente = false;
			if(response.success){
				console.log( response )
				this.select2 = $(this.$el)
					.find('select')
					.select2({
						...this.userSettings,
						data: response.data,
						multiple: this.multiple
					})
					.on('select2:select select2:unselect', ev => {
						this.$emit('change', this.select2.val());
						this.$emit('select', ev['params']['data']);
					})
					.on('select2:open', ev => {
						var $dropdown = $('.select2-dropdown');
						if ($dropdown.hasClass('select2-dropdown--above')) {
							$dropdown.removeClass('uk-animation-slide-top-small').addClass("uk-animation-slide-bottom-small");
						} else {
							$dropdown.removeClass('uk-animation-slide-bottom-small').addClass("uk-animation-slide-top-small");
						}
					});
				this.setValue(this.value);
				this.mostrarComponente = true;
			}else{
				this.msjErrorApi = `Error al cargar el componente ${this.nombreComponente}`;
				this.errorApi = true;
				this.mostrarComponente=true;
			}
		},

		async search () {
			let queryFields = this.queryFields.split("|")

			var myHeaders = new Headers();
			myHeaders.append("Content-Type", "application/json");
			myHeaders.append("Cookie", "csrftoken=gYEgUBGulRmP2o478Ue6ISNwcympEh8eyIRXV435PEouT0p0oAxxfDWd8CrzbhGR");

			let query = `{
					result:${this.source}(${this.criteria}: ${this.criteriaFields}){
						edges{
							node{
								id:${queryFields[0]}
								text:${queryFields[1]}
							}
						}
					}
				}`;
			// API CALL
			try {
				let res = await fetch(`${this.$axios.defaults.baseURL}/graphql/`, {
					method: 'POST',
					headers: myHeaders,
					body: JSON.stringify({ query }),
				});
				res = await res.json();
				if(res){
					console.log(res)
					let datosSearch = res.data.result.edges.map(function (detail){
						if(detail.node){
							return { id : detail.node.id, text : detail.node.text }
						}
					});
					console.log(datosSearch)
					return { 'success': true, data: datosSearch}

				}
			} catch (error) {
				return { 'false': true, data: error}
			}
		}
		
	}
};
</script>
<style lang="scss">
	@import '../assets/scss/plugins/select2.scss';
</style>
