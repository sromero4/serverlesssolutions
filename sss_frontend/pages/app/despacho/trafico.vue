<template>
	<div id="sc-page-wrapper">
		<div id="sc-page-content">
			<div>
				<ul id="fancy-toolbar-switcher-items" class="uk-switcher uk-margin">
					<li>
						<div v-if="calculos">
							<ScTransition
								group
								stagger
								:speed="20"
								origin="50% 50%"
								class="uk-child-width-1-5@xl uk-child-width-1-3@l uk-child-width-1-2@s uk-grid uk-grid-match uk-sortable"
								data-uk-grid
								data-uk-sortable
							>
								<div v-show="showWidgets" key="widgetA">
									<ScCard class="sc-widget uk-flex">
										<div class="uk-width-1-4 md-bg-cyan-600 uk-flex-middle uk-flex uk-flex-center">
											<i class="mdi mdi-google-maps md-color-white sc-icon-24"></i>
										</div>
										<div class="uk-flex-1">
											<ScCardBody>
												<ScCardTitle>
													Total Viajes
												</ScCardTitle>
												<ScCardMeta>
													{{ detail.length }}
												</ScCardMeta>
											</ScCardBody>
										</div>
									</ScCard>
								</div>
								<div v-show="showWidgets" key="widgetB">
									<ScCard class="sc-widget uk-flex">
										<div class="uk-width-1-4 md-bg-red-600 uk-flex-middle uk-flex uk-flex-center">
											<i class="mdi mdi-map-marker-distance md-color-white sc-icon-24"></i>
										</div>
										<div class="uk-flex-1">
											<ScCardBody>
												<ScCardTitle>
													Viajes en ruta
												</ScCardTitle>
												<ScCardMeta>
													{{ calculos.status.enruta }}
												</ScCardMeta>
											</ScCardBody>
										</div>
									</ScCard>
								</div>
								<div v-show="showWidgets" key="widgetC">
									<ScCard class="sc-widget uk-flex">
										<div class="uk-width-1-4 md-bg-light-green-600 uk-flex-middle uk-flex uk-flex-center">
											<i class="mdi mdi-map-marker-check md-color-white sc-icon-24"></i>
										</div>
										<div class="uk-flex-1">
											<ScCardBody>
												<ScCardTitle>
													Viajes Finalizados
												</ScCardTitle>
												<ScCardMeta>
													{{ calculos.status.llegada }}
												</ScCardMeta>
											</ScCardBody>
										</div>
									</ScCard>
								</div>
								<div v-show="showWidgets" key="widgetD">
									<ScCard class="sc-widget uk-flex">
										<div class="uk-width-1-4 md-bg-amber-600 uk-flex-middle uk-flex uk-flex-center">
											<i class="mdi mdi-currency-eur md-color-white sc-widget-addon"></i>
										</div>
										<div class="uk-flex-1">
											<ScCardBody>
												<ScCardTitle>
													1.135873
												</ScCardTitle>
												<ScCardMeta>
													EUR to USD
												</ScCardMeta>
											</ScCardBody>
										</div>
									</ScCard>
								</div>
								<div v-show="showWidgets" key="widgetE">
									<ScCard class="sc-widget uk-flex">
										<div class="uk-width-1-4 md-bg-purple-600 uk-flex-middle uk-flex uk-flex-center">
											<i class="mdi mdi-server md-color-white sc-widget-addon"></i>
										</div>
										<div class="uk-flex-1">
											<ScCardBody>
												<ScCardTitle>
													99.95%
												</ScCardTitle>
												<ScCardMeta>
													Server Uptime
												</ScCardMeta>
											</ScCardBody>
										</div>
									</ScCard>
								</div>
							</ScTransition>
							<hr>
							<div>
								<ScCard>
									<ScCardTitle>
										Por Origen
									</ScCardTitle>
									<ScCardBody>
										<BillboardChart
											v-if="appMounted"
											:options="origen"
											class="sc-chart"	
										></BillboardChart>
									</ScCardBody>
								</ScCard>
							</div>
							<div>
								<ScCard>
									<ScCardTitle>
										Por Destino
									</ScCardTitle>
									<ScCardBody>
										<BillboardChart
											v-if="appMounted"
											:options="destino"
											class="sc-chargt"	
										></BillboardChart>
									</ScCardBody>
								</ScCard>
							</div>
							<div>
								<ScCard>
									<ScCardTitle>
										Sales report
									</ScCardTitle>
									<div class="sc-padding sc-padding-medium-ends md-bg-grey-100">
										<div class=" uk-flex-middle uk-grid-small uk-grid" data-uk-grid>
											<div class="uk-flex-1">
												<div class="uk-button-group sc-button-group-outline">
													<button class="sc-button sc-button-default sc-button-outline sc-button-small" :class="{'uk-active': activeType === 'origen'}" @click="setChart('origen')">
														Origen
													</button>
													<button class="sc-button sc-button-default sc-button-outline sc-button-small" :class="{'uk-active': activeType === 'destino'}" @click="setChart('destino')">
														Destino
													</button>	
												</div>
											</div>
										</div>
									</div>
									<ScCardContent>
										<div class="sc-padding-medium">
											<BillboardChart
												v-if="appMounted"
												:key="activeType"
												:options="cityReportChart"
												class="sc-chart-large"
											>
											</BillboardChart>
										</div>
									</ScCardContent>
								</ScCard>
							</div>
						</div>
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
													{{ $t('Form') }}:{{ $t('Traficc') }}
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
														Data
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
								{{ $t('Form') }}: {{ $t('Traficc') }}
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
												<DateRangePicker v-model="filter.rango" :config="{format: 'YYYY-MM-DD',autoClose: false}">
													<ScInput placeholder="Pick a date range...">
													</ScInput>
												</DateRangePicker>
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
										<span v-if="props.column.field === 'node.manifiestoCodigo' && props.row.node.despachoLlegada=='SI'">
											<i class="mdi mdi-checkbox-marked-circle-outline md-color-light-green-600"></i>
										</span>
										<span v-if="props.column.field == 'ruta'">
											{{ props.row.node.ciudadNombreOrigen }} - {{ props.row.node.ciudadNombreDestino }}
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

import { provideApolloClient, useMutation, useQuery } from '@vue/apollo-composable';
import gql from 'graphql-tag'
import { validationMixin } from 'vuelidate'
import { required, minLength } from 'vuelidate/lib/validators'
import 'vue-good-table/dist/vue-good-table.css'
import { VueGoodTable } from 'vue-good-table';
import ScInput from '~/components/Input'
import moment from 'moment'
import { ScProgressCircular } from '~/components/progress'
import confirmDatePlugin from 'flatpickr/dist/plugins/confirmDate/confirmDate';
import DateRangePicker from '~/components/DateRangePicker'
import { scColors } from '~/assets/js/utils';
import { logErrorMessages } from '@vue/apollo-util'
import * as d3 from 'd3';

if(process.client) {
	require('~/plugins/inputmask')
	require('~/plugins/flatpickr')
}

export default {
	name: 'Trafico',
	
	components: {
		VueGoodTable,
		ScInput,
		ScProgressCircular,
		DateRangePicker,
		BillboardChart: process.client ? () => import('~/components/billboard-charts') : null
	},
	apollo: {
	},
	mixins: [validationMixin],
	data: () => ({
		showWidgets: false,
		appMounted: true,
		activeType: 'origen',
		cityReportChart: '',
		submitStatus: null,
		result:null,
		loading:null,
		mode:null,
		filter: {
			fechainicial: '',
			fechafinal: '',
					
		},
		status: {
			type: '',
			message:''
		},

		
		
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
		dpRange () {
			return {
				mode: "range",
				plugins: [confirmDatePlugin]
			}
		},
		detail () {
			if (this.result){
				if(this.result.value){
					var config = {};
					config.timeout =  3000;
					if(this.result.value.allTrafico.edges.length>0){
						config.status = "success";
						UIkit.notification('Consulta Ejecutada Correctamente. '+this.result.value.allTrafico.edges.length+' Registros', config);
					}
					else{
						config.status = "warning";
						UIkit.notification('Su Consulta No Arrojo Resultados. ', config);
					}
					
					return this.result.value.allTrafico.edges
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
					label: 'Manifiesto',
					field: 'node.manifiestoCodigo',
					sortable: true,
					sortFn: this.Sort,
					tdClass: 'uk-text-right',
					filterOptions: {
						styleClass: 'uk-form-width-small',
						enabled: true
					}
				},
				{
					label: 'Fecha',
					field: 'node.despachoFecha',
					tdClass: 'uk-text-center',
					filterOptions: {
						styleClass: 'uk-form-width-small',
						enabled: true
					}

				},
				{
					label: 'Placa',
					field: 'node.vehiculoPlaca',
					
					filterOptions: {
						styleClass: 'uk-form-width-small',
						enabled: true
					}
				},
				{
					label: 'Ruta',
					field: 'ruta',
					filterOptions: {
						styleClass: 'uk-form-width-small',
						enabled: true
					}
				},
				{
					label: 'Conductor',
					field: 'node.terceroNombreConductor',
					tdClass: 'uk-text-left',
					filterOptions: {
						styleClass: 'uk-form-width-large',
						enabled: true
					}
				},
			]
		},

		calculos () {
			let origen = []
			let destino = []
			let calculos = {
				status:{
					llegada:0,
					enruta:0
				},
				origen:{
				},
				destino:{
				}

			}
			if (this.result){
				if(this.result.value){
					if(this.result.value.allTrafico.edges.length>0){
						let nodo= this.result.value.allTrafico.edges
						for (let i in nodo) {
							//console.log(nodo[i].node.ciudadNombreOrigen);
							if(nodo[i].node.despachoLlegada=="SI")
								calculos.status.llegada+=1
							else
								calculos.status.enruta+=1

							if(destino[nodo[i].node.ciudadNombreDestino])
								destino[nodo[i].node.ciudadNombreDestino]+=1
							else
								destino[nodo[i].node.ciudadNombreDestino]=1

							if(origen[nodo[i].node.ciudadNombreOrigen])
								origen[nodo[i].node.ciudadNombreOrigen]+=1
							else
								origen[nodo[i].node.ciudadNombreOrigen]=1

						}
						
						calculos.origen=origen
						calculos.destino=destino

						console.log(calculos)
						
						return calculos
					}
				}
			}
			
			return false

		},

		origen () {
			const self = this
			let origen = []
			let x =[]
			let data1=[]
			
			if (this.calculos){
				
				x.push('x')
				data1.push('data1')
				for (let i in this.calculos.origen) {
					x.push(i)
					data1.push(this.calculos.origen[i])
				}
				
			}
			

			

			return {
				data: {
					x: "x",
					columns: [
						x, 
						data1
					],
					types: {
						data1: "bar"
					},
					colors: {
						data1: scColors.multi[3]
					}
				},
				axis: {
					x: {
						type: "category",
						tick: {
							rotate: 75,
							multiline: false,
							tooltip: true
						},
						height: 130
					},
					y: {
						show: true
					}
				},
				grid: {
					x: {
						show: false,
						
					},
					y: {
						show: true
					}
				},
				tooltip: {
					
				},
				transition: {
					duration: 0
				},
				legend: {
					show: false
				}
			}
		},
		destino () {
			const self = this
			let x =[]
			let data1=[]
			
			if (this.calculos){
				
				x.push('x')
				data1.push('data1')
				for (let i in this.calculos.destino) {
					x.push(i)
					data1.push(this.calculos.destino[i])
				}
				
			}
			
			return {
				data: {
					x: "x",
					columns: [
						x, 
						data1
					],
					types: {
						data1: "bar"
					},
					colors: {
						data1: scColors.multi[3]
					}
				},
				axis: {
					x: {
						type: "category",
						tick: {
							rotate: 75,
							multiline: false,
							tooltip: true
						},
						height: 130
					},
					y: {
						show: true
					}
				},
				grid: {
					x: {
						show: false,
						
					},
					y: {
						show: true
					}
				},
				tooltip: {
					
				},
				transition: {
					duration: 0
				},
				legend: {
					show: false
				}
			}
		}
	},
	mounted () {
		this.$store.commit('setFancyToolbarActive', true);
		this.$nextTick(() => {
			this.showWidgets = true;
		})
	},
	beforeDestroy () {
		this.$store.commit('setFancyToolbarActive', false);
	},
	created () {
		this.cityReportChart = this.origen
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
					//console.log(this.filter.rango)
				}
			}catch (err){
				console.log(err);
			}	

		},
		async search () {
			
			  let {result, loading, error }  =  provideApolloClient(this.$apollo)(() => useQuery(gql`
					query QUERY ($fechainicial: Date!, $fechafinal: Date!) {
						allTrafico(despachoFecha_Range: [$fechainicial, $fechafinal]){
							edges{
								node{
									despachoCodigo
									manifiestoCodigo
									despachoFecha
									despachoLlegada
									vehiculoPlaca
									ciudadNombreOrigen
									ciudadNombreDestino
									terceroNombreConductor
								}
							}	
						}
					}
				`, 

				
			{
				fechainicial: (Array.isArray(this.filter.rango) ? this.filter.rango[0] : null),
				fechafinal: (Array.isArray(this.filter.rango) ? this.filter.rango[1] : null),
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
		setChart (type) {
			if(type === 'origen') {
				this.cityReportChart = this.origen
			}
			if(type === 'destino') {
				this.cityReportChart = this.destino
			}
			
			this.activeType = type
		}
	},
}
</script>

<style lang="scss">
	@import '~scss/plugins/vue-good-table.scss';
	@import '~scss/components/progress';
</style>
