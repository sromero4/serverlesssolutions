<template>
	<div id="sc-page-wrapper">
		<div id="sc-page-content">
			<div>
				<ul id="fancy-toolbar-switcher-items" class="uk-switcher uk-margin">
					<li>
						<ScCard>
							<ScCardTitle>
								Reportes
							</ScCardTitle>
							<ScCardBody>
							</ScCardBody>
						</ScCard>
					</li>
					<li>
						<ScCard>
							<ScCardTitle>
								Procedimientos
							</ScCardTitle>
							<ScCardBody>
							</ScCardBody>
						</ScCard>
					</li>
					<li>
						<ScCard>
							<ScCardBody>
								<div id="modal-container" class="uk-modal-container uk-modal" data-uk-modal="esc-close:false; bg-close:false">
									<div class="uk-modal-dialog uk-modal-body">	
										<ScCardHeader class="sc-padding">
											<div class="uk-flex uk-flex-middle">
												<ScCardTitle>
													{{ $t('Form') }}:{{ $t('Color') }}
												</ScCardTitle>
											</div>
											<div v-if="infoloadingform">
												<ScProgressCircular size="lg"></ScProgressCircular>
											</div>
											<div v-else-if="infosuccessform">
												<ScCard>
													<div class="uk-alert-attached-top uk-alert-success" data-uk-alert>
														<a class="uk-alert-close" data-uk-close></a>
														<h4>Proceso Exitoso</h4>
														<div class="uk-flex uk-flex-middle" data-uk-alert>
															<i class="mdi mdi-check-circle sc-icon-32 uk-margin-right md-color-light-green-600"></i>
															<ScCardBody>
																{{ infosuccessform.message }}
															</ScCardBody>
														</div>
													</div>
												</ScCard>
											</div>
											<div v-else-if="infoerrorform">
												<ScCard>
													<div class="uk-alert-attached-top uk-alert-danger" data-uk-alert>
														<a class="uk-alert-close" data-uk-close></a>
														<h4>Ha Ocurrido un Error</h4>
														<div class="uk-flex uk-flex-middle" data-uk-alert>
															<i class="mdi mdi-bullhorn sc-icon-32 uk-margin-right"></i>
															<ScCardBody>
																<h5>Error:</h5>
																{{ infoerrorform.message }}
															</ScCardBody>
														</div>
														<div class="uk-alert-attached-bottom" data-uk-alert>
															Corregir evento y enviar solicitud nuevamente
														</div>
													</div>
												</ScCard>
											</div>
										</ScCardHeader>
										<form action="">
											<ul class="uk-accordion-outline uk-accordion" data-uk-accordion="multiple: true">
												<li class="uk-open">
													<h3 class="uk-accordion-title">
														{{ $t('Basic data') }}
													</h3>
													<div class="uk-accordion-content">
														<div class="uk-child-width-1-2@m uk-grid" data-uk-grid>
															<div>
																<ScInput v-model="colorCodigo" extra-classes="uk-form-width-small" :disabled="true">
																	<label>
																		{{ $t('Code') }}
																	</label>
																</ScInput>
															</div>
															<div>
																<ScInput v-model="$v.colorNombre.$model" 
																	name="colorNombre" 
																	mode="outline" 
																	:error-state="$v.colorNombre.$error" 
																	:validator="$v.colorNombre" 
																>
																	<label>
																		{{ $t('Name') }}
																	</label>
																</ScInput>
																<ul class="sc-vue-errors">
																	<li v-if="!$v.colorNombre.required">
																		{{ $t('Field is required') }}
																	</li>
																</ul>
															</div>
														</div>
														<div class="uk-child-width-1-2@m uk-grid" data-uk-grid>
															<div>
																<ScInput v-model="$v.colorCodigoMinisterio.$model" 
																	v-input-mask="{ 'mask': '9', 'repeat': 10, 'greedy' : false }" 
																	extra-classes="uk-form-width-small" 
																	mode="outline"
																	:error-state="$v.colorCodigoMinisterio.$error" 
																	:validator="$v.colorCodigoMinisterio"
																>
																	<label>
																		{{ $t('Code') }} RNDC 
																	</label>
																</ScInput>
																<ul class="sc-vue-errors">
																	<li v-if="!$v.colorCodigoMinisterio.required">
																		{{ $t('Field is required') }}
																	</li>
																</ul>
															</div>
															<div>
																<ScInput v-model="usuarioCodigo" extra-classes="uk-form-width-small" :disabled="true">
																	<label>
																		{{ $t('User') }}
																	</label>
																</ScInput>
															</div>
														</div>
														<div class="uk-child-width-1-2@m uk-grid" data-uk-grid>
															<div>
																<ScInput v-model="colorFechacreacion" extra-classes="uk-form-width-small" :disabled="true">
																	<label>
																		{{ $t('Date created') }}
																	</label>
																</ScInput>
															</div>
															<div>
																<ScInput v-model="colorFechamodificacion" extra-classes="uk-form-width-small" :disabled="true">
																	<label>
																		{{ $t('Date modified') }}
																	</label>
																</ScInput>
															</div>
														</div>
													</div>
												</li>
											</ul>
											<div v-if="mode=='EDIT'">
												<button class="sc-button sc-button-success" :disabled="submitStatus === 'PENDING'" @click="submitForm($event,'EDIT')">
													{{ $t('Update') }}
												</button>
												<button class="sc-button sc-button-secondary uk-modal-close">
													{{ $t('Close') }}
												</button>
											</div>
											<div v-else-if="mode=='CREATE'">
												<button class="sc-button sc-button-success" :disabled="submitStatus === 'PENDING'" @click="submitForm($event,'CREATE')">
													{{ $t('Save') }}
												</button>
												<button class="sc-button sc-button-secondary uk-modal-close">
													{{ $t('Close') }}
												</button>
											</div>
											<div v-else>
												<button class="sc-button sc-button-secondary uk-modal-close">
													{{ $t('Close') }}
												</button>
											</div>	
										</form>
									</div>
								</div>
							</ScCardBody>
						</ScCard>
						<ScCard>
							<ScCardTitle>
								{{ $t('Form') }}: {{ $t('Color') }}
							</ScCardTitle>
							<ScCardBody>
								<div class="uk-child-width-1-3@m" data-uk-grid data-uk-match-height>
									<div>
										<button class="sc-button sc-button-success" @click="createForm()">
											<i class="mdi mdi-plus md-color-indigo-50"></i>{{ $t('Create') }}
										</button>
										<button class="sc-button sc-button-primary" @click="operation('SEARCH')">
											{{ $t('Search') }}
										</button>
									</div>
									<div v-if="infoloading">
										<ScProgressCircular size="lg"></ScProgressCircular>
									</div>
									<div v-else-if="infoerror">
										<div class="uk-alert uk-alert-icon" data-uk-alert>
											<a class="uk-alert-close" data-uk-close></a>
											<div class="uk-flex uk-flex-middle">
												<i class="mdi mdi-bullhorn sc-icon-32 uk-margin-right"></i>
												<div class="uk-alert-content">
													<h5>Error:</h5>
													<p>{{ infoerror.message }}</p>
													<p>{{ infoerror.networkError.result.errors }}.</p>
												</div>
											</div>
										</div>
									</div>
								</div>
								<hr>
								<ul class="uk-accordion-outline" data-uk-accordion="multiple: true">
									<li class="uk-open">
										<h3 class="uk-accordion-title">
											{{ $t('Filters') }}
										</h3>
										<div class="uk-accordion-content uk-child-width-1-2@m uk-flex-bottom" data-uk-grid data-uk-match-height>
											<div>
												<ScInput id="sc-filter-code" 
													v-model="filter.codigo" 
													v-input-mask="{ 'mask': '9', 'repeat': 10, 'greedy' : false }" 
													extra-classes="uk-form-width-small" 
													mode="outline"
												>
													<label>{{ $t('Code') }}</label>
												</ScInput>
											</div>
											<div>
												<ScInput id="sc-filter-name" v-model="filter.nombre" extra-classes="uk-form-width-medium" mode="outline">
													<label>{{ $t('Name') }}</label>
												</ScInput>
											</div>
										</div>
									</li>
								</ul>
								<hr>
								<VueGoodTable
									:columns="columns"
									:rows="detail"
									:pagination-options="{ enabled: true }"
									style-class="uk-table uk-table-divider vgt-table striped bordered condensed"
									:search-options="{
										enabled: true
									}"
									compact-mode
								>
									<template slot="table-row" slot-scope="props">
										<span v-if="props.column.field == 'actions'">
											<div class="uk-grid-small uk-width-auto uk-grid" data-uk-grid>
												<div>
													<button class="sc-fab sc-fab-small" @click="editForm(props.row,'EDIT')">
														<i class="mdi mdi-pencil md-color-cyan-600" data-uk-tooltip="Edit"></i>
													</button>
												</div>
												<div>
													<button class="sc-fab sc-fab-small" @click="editForm(props.row,'VIEW')">
														<i class="mdi  mdi-eye-outline md-color-red-600" data-uk-tooltip="View"></i>
													</button>
												</div>
											</div>
										</span>
										<span v-else>
											{{ props.formattedRow[props.column.field] }}
										</span>
									</template>
								</VueGoodTable>
							</ScCardBody>
						</ScCard>
					</li>
					<li>
						<ScCard>
							<ScCardTitle>
								Tablas Maestras
							</ScCardTitle>
							<ScCardBody>
							</ScCardBody>
						</ScCard>
					</li>
					<li>
						<ScCard>
							<ScCardTitle>
								Ayuda
							</ScCardTitle>
							<ScCardBody>
							</ScCardBody>
						</ScCard>
					</li>
				</ul>
			</div>
		</div>
	</div>
</template>

<script>

import { provideApolloClient, useMutation, useQuery } from '@vue/apollo-composable/dist';
import gql from 'graphql-tag'
import { validationMixin } from 'vuelidate'
import { required, minLength } from 'vuelidate/lib/validators'
import 'vue-good-table/dist/vue-good-table.css'
import { VueGoodTable } from 'vue-good-table';
import ScInput from '~/components/Input'
import moment from 'moment'
import { ScProgressCircular } from '~/components/progress'
import { logErrorMessages } from '@vue/apollo-util'

if(process.client) {
	require('~/plugins/inputmask')
}

export default {
	name: 'Color',
	
	components: {
		VueGoodTable,
		ScInput,
		ScProgressCircular
	},
	apollo: {
	},
	mixins: [validationMixin],
	data: () => ({
		submitStatus: null,
		result:null,
		loading:null,
		mode:null,
		filter: {
			codigo: '',
			nombre: '',
					
		},
		status: {
			type: '',
			message:''
		},

		colorCodigo: '',
		colorNombre: '',
		colorCodigoMinisterio: '',
		colorFechacreacion: '',
		colorFechamodificacion: '',
		usuarioCodigo: '',
		
	}),
	validations: {
		colorNombre: {
			required,
			minLength: minLength(3)
		},
		colorCodigoMinisterio: {
			required,
		},
	},
	computed: {
		detail () {
			if (this.result){
				if(this.result.value){
					var config = {};
					config.timeout =  3000;
					if(this.result.value.allColor.edges.length>0){
						config.status = "success";
						UIkit.notification('Consulta Ejecutada Correctamente. '+this.result.value.allColor.edges.length+' Registros', config);
					}
					else{
						config.status = "warning";
						UIkit.notification('Su Consulta No Arrojo Resultados. ', config);
					}

					return this.result.value.allColor.edges
				}
			}
			return null;
		},
		infoloading () {
			if (this.loading)
				if(this.loading.value){
					return this.loading.value
				}
			return false
		},
		infoerror () {
			if (this.error)
				if(this.error.value){
					var config = {};
					config.timeout =  5000;
					config.status = "danger";
					UIkit.notification('A Ocurrido un Error ', config);
					return this.error.value
				}
			return false
		},
		infoloadingform () {
			if (this.loading)
				if(this.loading.value){
					return this.loading.value
				}
			return false

		},
		infoerrorform () {
			if (this.status.type=="ERROR"){
				return this.status			
			}
			return false

		},
		infosuccessform () {
			if (this.status.type=="SUCCESS"){
				return this.status
			}
			return false

		},
		columns () {
			return [
				{
					label: 'Codigo',
					field: 'node.colorCodigo',
					sortable: true,
					sortFn: this.Sort,
					tdClass: 'uk-text-center uk-text-nowrap'
				},
				{
					label: 'Nombre',
					field: 'node.colorNombre',
					tdClass: 'uk-text-center',
					filterOptions: {
						styleClass: 'uk-form-width-large',
						enabled: true
					}

				},
				{
					label: 'Codigo Rndc',
					field: 'node.colorCodigoMinisterio',
					
					filterOptions: {
						styleClass: 'uk-form-width-small',
						enabled: true
					}
				},
				{
					label: 'Usuario',
					field: 'node.usuarioCodigo',
					filterOptions: {
						styleClass: 'uk-form-width-small',
						enabled: true
					}
				},
				{
					label: 'Created On',
					field: 'node.colorFechacreacion',
					type: 'date',
					dateInputFormat: 'yyyy-MM-dd',
					dateOutputFormat: 'yyyy-MM-dd',
					tdClass: 'uk-text-nowrap uk-text-left'
				},
				{
					label: 'Modified On',
					field: 'node.colorFechamodificacion',
					type: 'date',
					dateInputFormat: 'yyyy-MM-dd',
					dateOutputFormat: 'yyyy-MM-dd',
					tdClass: 'uk-text-nowrap uk-text-left'
				},
				{
					label: 'Actions',
					field: 'actions',
					
				}
			]
		}
	},
	mounted () {
		this.$store.commit('setFancyToolbarActive', true);
	},
	beforeDestroy () {
		this.$store.commit('setFancyToolbarActive', false);
	},
	methods: {
		async submitForm (e, operation) {
			e.preventDefault();
			this.$v.$touch();
			if (this.$v.$invalid) {
				this.submitStatus = 'ERROR'
			} else {
				this.submitStatus = 'OK';
				
				if(operation=="CREATE")
					await this.create();
				else 
					await this.edit();
				
			}
		},
		Sort (x, y, col, rowX, rowY) {
			const _x = parseInt(x.replace("sc-", ""));
			const _y = parseInt(y.replace("sc-", ""));
			return (_x < _y ? -1 : (_x > _y ? 1 : 0));
		},
		async operation (operation){
			try {

				if(operation=="SEARCH"){
					await this.search()
				}
			}catch (err){
				console.log(err);
			}	

		},
		async search () {
			
			  let {result, loading, error }  =  provideApolloClient(this.$apollo)(() => useQuery(gql`
					query QUERY ($codigo: Float, $nombre: String) {
						allColor(colorCodigo: $codigo, colorNombre_Contains: $nombre){
							edges{
								node{
									colorCodigo
									colorNombre
									colorCodigoMinisterio
									usuarioCodigo
									colorFechacreacion
									colorFechamodificacion
									edit
									save
									look
								}
							}	
						}
					}
				`, 
			{
				codigo: (this.filter.codigo.trim()!="" ? this.filter.codigo.toUpperCase() : null),
				nombre: (this.filter.nombre.trim()!="" ? this.filter.nombre.toLocaleUpperCase() : null),
			},
			{
      			errorPolicy: 'all',
				fetchPolicy: 'no-cache'
    		}));
			this.result=result;
			this.loading=loading;
			this.error=error;
			
			
		},

		async create () {
			this.status.type='';
        	let {mutate: createColor, loading: colorLoading, error: colorError, onDone, onError}  =   provideApolloClient(this.$apollo)(() => useMutation(gql`
			
				mutation createColor($colorNombre: String!, $colorCodigoMinisterio: String!, $usuarioCodigo: Int!){
						createColor(colorNombre: $colorNombre, colorCodigoMinisterio: $colorCodigoMinisterio, usuarioCodigo: $usuarioCodigo ) {
							node{
								colorCodigo
								colorNombre
								colorCodigoMinisterio
								usuarioCodigo
								colorFechacreacion
								colorFechamodificacion
							}
						}
					}
					`));

			createColor({
				colorNombre: this.$data.colorNombre,
				colorCodigoMinisterio: this.$data.colorCodigoMinisterio,
				usuarioCodigo: this.$data.usuarioCodigo
			})
			
			this.loading=colorLoading;
			this.submitStatus="PENDING"

			onDone(result => {
  				this.submitStatus="OK"
				this.status.type="SUCCESS"
				this.status.message="Registro creado exitosamente con codigo "+result.data.createColor.node.colorCodigo
			})
			
			onError(error => {
  				//logErrorMessages(error)
				this.submitStatus="OK"
				this.status.type="ERROR"
				this.status.message=colorError.value
			})
			
		},
		async edit () {
			this.status.type='';
        	let {mutate: updateColor, loading: colorLoading, error: colorError, onDone, onError}  =   provideApolloClient(this.$apollo)(() => useMutation(gql`
			
				mutation updateColor($colorCodigo: Int!,$colorNombre: String, $colorCodigoMinisterio: String){
						updateColor(colorCodigo: $colorCodigo, colorNombre: $colorNombre, colorCodigoMinisterio: $colorCodigoMinisterio) {
							color{
								colorCodigo
								colorNombre
								colorCodigoMinisterio
								usuarioCodigo
								colorFechacreacion
								colorFechamodificacion
							}
						}
					}
					`));

			updateColor({
				colorCodigo: this.$data.colorCodigo,
				colorNombre: this.$data.colorNombre,
				colorCodigoMinisterio: this.$data.colorCodigoMinisterio,
			})
			
			this.loading=colorLoading;
			this.submitStatus="PENDING"

			onDone(result => {
  				this.submitStatus="OK"
				this.status.type="SUCCESS"
				this.status.message="Registro actualizado Correctamente "
			})
			
			onError(error => {
  				//logErrorMessages(error)
				this.submitStatus="OK"
				this.status.type="ERROR"
				this.status.message=colorError.value
			})
			
			
		},

		createForm () {
			var currentDate = new Date();
			var fecha=moment(currentDate, 'YYYY-MM-DD', true).format('YYYY-MM-DD');
			if(this.$data.mode=="EDIT"){
				this.$data.colorCodigo="";
				this.$data.colorNombre=""
				this.$data.colorCodigoMinisterio="";
			}
			this.$data.colorFechacreacion=fecha;
			this.$data.colorFechamodificacion=fecha;
			this.$data.usuarioCodigo="1";
			this.$data.mode="CREATE"
			var modal = UIkit.modal("#modal-container");
    		modal.show(); 
  		},
		editForm (row, prop) {
			this.$data.mode=prop
			this.$data.colorCodigo=row.node.colorCodigo+""
			this.$data.colorNombre=row.node.colorNombre
			this.$data.colorCodigoMinisterio=row.node.colorCodigoMinisterio+""
			this.$data.colorFechacreacion=row.node.colorFechacreacion
			this.$data.colorFechamodificacion=row.node.colorFechamodificacion
			this.$data.usuarioCodigo=row.node.usuarioCodigo+""
			var modal = UIkit.modal("#modal-container")
    		modal.show()
			
  		},
	}
}
</script>

<style lang="scss">
	@import '~scss/plugins/vue-good-table.scss';
	@import '~scss/components/progress';
</style>