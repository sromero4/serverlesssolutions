<template>
	<div class="autocomplete">
		<div
			class="sc-input-wrapper"
			:class="{
				'sc-input-wrapper-outline': mode === 'outline',
				'sc-input-wrapper-disabled': disabled,
				'sc-input-wrapper-danger': errorState,
				'sc-input-wrapper-danger': errorApi,
				'sc-input-wrapper-success': successState,
				'sc-input-filled': value !== '' || state === 'fixed',
				'sc-input-focus': inputFocused
			}"
			v-show="mostrarComponente && !errorApi"
		>
			<slot name="icon" ></slot>
			<a 
				slot="icon" 
				class="uk-form-icon uk-form-icon-flip" 
				@click="borrar"
				data-uk-icon="icon: close"
				v-if="busqueda"
			></a>
			<slot></slot>
			<input
				v-model="busqueda"
				:id="id"
				ref="input"
				:name="name"
				:placeholder="placeholder"
				:type="type"
				:value="value"
				:class="['uk-input', 'sc-vue-input', modeClass, inputErrorClass, inputSuccessClass, extraClasses]"
				:disabled="disabled"
				:readonly="readOnly"
				@focus="inputFocus"
				@blur="inputBlur"
				@change="inputChange"
				@input="onChange"
				@keyup="inputKeyUp"
			>
			<span v-if="mode !== 'outline'" class="sc-input-bar"></span>
			<slot name="help-inline"></slot>
		</div>

		<ScProgressCircular v-show="!mostrarComponente"></ScProgressCircular>
		<span class="uk-text-danger" v-show="errorApi">{{ msjErrorApi }} <span slot="icon" class="mdi mdi-alert-circle uk-text-danger"></span></span>

		<div class="uk-overflow-auto" v-show="isOpen">
			<table class="uk-table uk-table-divider uk-table-small uk-table-hover" >
				<thead>
					<tr>
						<th class="uk-text-center uk-width-small" v-for="(columna, i) in columnasNombre" :key="i">
							<label>{{columna}}</label>
						</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="(result, k) in resultadosPaginados" :key="k" class="uk-width-small" @click="setResult(result)">
						<td class="uk-text-nowrap" v-for="(columna, j) in result" :key="j" style="padding: 2px 6px">
							<label class="uk-text-small">
								{{ columna }}
							</label>
						</td>
					</tr>
				</tbody>
			</table>
			<ul class="uk-pagination" data-uk-margin>
				<li><a @click="getPaginaAnterior()"><span data-uk-pagination-previous></span></a></li>
				<li 
					v-show=" (totalPaginas() < 5) " 
					v-for="pagina in totalPaginas()" 
					:key="pagina"
					:class="{ 'uk-active': pagina === paginaActual }"
				>
					<a @click="getDataPagina(pagina)">{{pagina}}</a>
				</li>
				<li v-show=" (totalPaginas() > 5) " class="uk-active" >
					<span class="uk-label ">{{paginaActual}}/{{totalPaginas()}}</span>
				</li>
				<li><a @click="getPaginaSiguiente()"><span data-uk-pagination-next></span></a></li>
			</ul>
		</div>
		
	</div>
</template>

<script>
import { ScProgressCircular } from '~/components/progress'
export default {
	name: 'CAutocomplete',
	components: {
		ScProgressCircular
	},
	props: {
		items: {
			type: Array,
			required: false,
			default: () => [],
		},
		isAsync: {
			type: Boolean,
			required: false,
			default: false,
		},
		id: {
			type: String,
			default: null,
		},
		name: {
			type: String,
			default: null
		},
		type: {
			type: String,
			default: 'text'
		},
		value: {
			type: [String, Object],
			default: ''
		},
		disabled: {
			type: Boolean,
			default: false
		},
		readOnly: {
			type: Boolean,
			default: false
		},
		mode: {
			type: String,
			default: ''
		},
		state: {
			type: String,
			default: ''
		},
		extraClasses: {
			type: String,
			default: ''
		},
		successState: {
			type: Boolean,
			default: false
		},
		errorState: {
			type: Boolean,
			default: false
		},
		placeholder: {
			type: String,
			default: null
		},
		ukTooltip: {
			type: Object,
			default: null
		},
		focus: {
			type: Function,
			default: null
		},
		blur: {
			type: Function,
			default: null
		},
		change: {
			type: Function,
			default: null
		},
		keyUp: {
			type: Function,
			default: null
		},
		validator: {
			type: Object,
			default: null
		},

		nombreComponente: {
			type: String,
			default: ''
		},
		source: {
			type: String,
			default: ''
		},
		where: {
			type: String,
			default: ''
		},
		camposConsultar: {
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
		}


	},
	data: () => ({
		mostrarComponente: false,
		isOpen: false,
		errorApi: false,
		msjErrorApi: '',

		registros: [], 
		busqueda: '', 
		resultados: [],
		resultadosPaginados: [],
		columnasNombre: [],

		isLoading: false,
		inputFocused: false,

		/*Paginador*/
		elementosPorPagina: 5,
		paginaActual: 1
		
	}),
	computed: {
		modeClass () {
			return this.$props.mode === 'outline' ? 'sc-input-outline' : ''
		},
		inputErrorClass () {
			return this.$props.errorState ? 'uk-form-danger' : ''
		},
		inputSuccessClass () {
			return this.$props.successState ? 'uk-form-success' : ''
		}
	},
	watch: {
		registros: function (value, oldValue) {
			if (value.length !== oldValue.length) {
				this.resultados = value;
				this.isLoading = false;
				this.getDataPagina (1);
			}
		},
	},
	mounted () {
		let consulta = this.ejecutarconsulta().then( response =>  {
			if(response.success){
				this.registros = response.data;
				this.mostrarComponente = true;
			}else{
				this.msjErrorApi = `Error al cargar el componente ${this.nombreComponente}`;
				this.errorApi = true;
				this.mostrarComponente=true;
			}
			
		}).catch(function (error) {
			console.log ('errorApi '+error);
		});

		
		document.addEventListener('click', this.handleClickOutside)
		var self = this;
		if(self.ukTooltip) {
			UIkit.tooltip(self.$refs.input, self.ukTooltip);
		}
		
		this.datosTablaConsulta();

	},
	destroyed () {
		document.removeEventListener('click', this.handleClickOutside)
	},
	methods: {
		setResult (result) {
			this.busqueda = result.nombre;
			this.isOpen = false;
			this.$emit('value-changed', result);
		},
		
		filtroResultados () {
			this.resultados = this.registros.filter((item) => {
				if(this.busqueda === '%'){
					return item;
				}
				return item.nombre.toLowerCase().indexOf(this.busqueda.toLowerCase()) > -1;
			});
		},
		onChange () {
			this.$emit('input', this.busqueda);
			if(this.busqueda === ''){
				this.isOpen = false;
				return;
			}

			if (this.isAsync) {
				this.isLoading = true;
			} else {
				this.filtroResultados();
				this.isOpen = true;
				this.getDataPagina (1);
			}
		},
		handleClickOutside (event) {
			if (!this.$el.contains(event.target)) {
				this.isOpen = false;
			}
		},
		
		inputBlur () {
			this.inputFocused = false;
			if(this.blur) {
				this.blur();
			}
			if(this.validator) {
				this.validator.$touch();
			}
			this.$emit('blur');
		},
		inputFocus () {
			this.inputFocused = true;
			if(this.focus) {
				this.focus();
			}
			this.$emit('focus');
		},
		inputChange () {
			if(this.change) {
				this.change();
			}
			this.$emit('change');
		},
		inputKeyUp () {
			if(this.keyUp) {
				this.keyUp();
			}
			this.$emit('keyUp');
		},
		borrar (){
			this.busqueda = '';
		},
		async ejecutarconsulta (){
			let peticion = `${process.env.API_BASE_URL}?api=servicio.Util.autocompletarSelect&source=${this.source}&camposConsultar=${this.camposConsultar}&where=${this.where}&orderBy=${this.orderBy}&aliasCampos=${this.aliasCampos}`;
			let nombreComponenteConsultar = this.nombreComponente;

			return await this.$axios.$get(peticion).then( function (response){
				if(response.success){
					return response;
				}else{
					return false;
				}
			}).catch(function (error) {
				return error;
			});
		},

		datosTablaConsulta (){
			this.columnasNombre = this.aliasCampos.split("|")
		},

		/** Paginador */
		totalPaginas (){
			return Math.ceil(this.resultados.length / this.elementosPorPagina);
		},

		getDataPagina (pagina){
			let ini = (pagina * this.elementosPorPagina) - this.elementosPorPagina;
			let fin = (pagina * this.elementosPorPagina)
			this.resultadosPaginados = this.resultados.slice(ini, fin)
			this.paginaActual = pagina;
		},

		getPaginaAnterior (){
			if(this.paginaActual > 1){
				this.paginaActual--;
				this.getDataPagina (this.paginaActual);
			}
		},
		getPaginaSiguiente (){
			if(this.paginaActual < this.totalPaginas ()){
				this.paginaActual++;
				this.getDataPagina (this.paginaActual);
			}
		}
	},
};
</script>

<style>
.autocomplete {
	position: relative;
}


</style>