<template>
	<div id="sc-page-wrapper">
		<div id="sc-page-content">
			<ScCard>
				<ScCardTitle>
					{{ $t('Form') }}: {{ $t('User') }}
				</ScCardTitle>
				<ScCardBody>
					<div class="uk-child-width-1-3@m" data-uk-grid data-uk-match-height>
						<div>
							<a href="/app/basic/usuario/home/generico/home" class="sc-button sc-button-success">
								<i class="mdi mdi-plus md-color-indigo-50"></i>{{ $t('Create') }}
							</a>
						</div>
					</div>
					<hr>
					<ul class="uk-accordion-outline" data-uk-accordion="multiple: true">
						<li class="uk-open">
							<h3 class="uk-accordion-title">
								{{ $t('Filters') }}
							</h3>
							<div class="uk-accordion-content uk-child-width-1-4@m uk-flex uk-flex-bottom uk-grid" data-uk-grid>
								<!--Codigo-->
								<div>
									<ScInput id="settings-basic-code" 
										v-model="codigo" 
										name="codigo"
										extra-classes="uk-form-width-small" 
										mode="outline"
										type="number"
									>
										<label>{{ $t('Code') }}</label>
									</ScInput>
								</div>
								<!--Login-->
								<div>
									<ScInput id="settings-basic-usuarioLogin" 
										v-model="usuarioLogin" 
										extra-classes="uk-form-width-long" 
										mode="outline"
										name="usuarioLogin" 	
									>
										<label>
											{{ $t('Login') }}
										</label>
									</ScInput>
								</div>
								<!--Name-->
								<div>
									<ScInput id="settings-basic-name" 
										v-model="nombre"
										extra-classes="uk-form-width-long" 
										mode="outline"
										name="name"
									>
										<label>
											{{ $t('Name') }}
										</label>
									</ScInput>
								</div>
								<!--City-->
								<div>
									<label>
										{{ $t('City') }}
									</label>
									<client-only>
										<Select2
											id="settings-basic-ciudad"
											v-model="ciudad"
											:options="basicCiudad" 
											extra-classes="uk-form-width-medium" 
											mode="outline"
											:settings="{ 'width': '100%', 'placeholder': 'Seleccione la ciudad...', 'allowClear': true }"
										></Select2>
									</client-only>
								</div>
								<!--Cedula-->
								<div>
									<ScInput id="settings-basic-cedula" 
										v-model="cedula"
										name="usuarioCedula"
										extra-classes="uk-form-width-medium" 
										mode="outline"
										type="number"
									>
										<label>
											{{ $t('Identification Card') }}
										</label>
									</ScInput>
								</div>
								<!--ESTADO-->
								<div>
									<label>
										{{ $t('State') }} 
									</label>
									<client-only>
										<Select2
											id="settings-basic-estado"
											v-model="estado"
											:options="basicEstado"
											extra-classes="uk-form-width-medium" 
											mode="outline"
											:settings="{ 'width': '100%', 'placeholder': 'Seleccione el estado...', 'minimumResultsForSearch': -1, 'allowClear': true }"
										></Select2>
									</client-only>
								</div>
								<!--Email-->
								<div>
									<ScInput 
										id="settings-page-email" 
										v-model="email" 
										name="email" 
										extra-classes="uk-form-width-long" 
										mode="outline"
									>
										<label>
											{{ $t('Email') }}
										</label>
									</ScInput>
								</div>
								<!--Cliente-->
								<!--div>
									<label>
										{{ $t('Client') }}
									</label>
									<client-only>
										<Select2
											id="settings-basic-cliente"
											v-model="cliente"
											:options="basicCliente" 
											extra-classes="uk-form-width-medium" 
											mode="outline"
											:settings="{ 'width': '100%', 'placeholder': 'Seleccione el cliente...', allowClear: true }"
										></Select2>
									</client-only>
								</div-->
								<!--Tercero-->
								<!--div>
									<label>
										{{ $t('Third') }}
									</label>
									<client-only>
										<Select2
											id="settings-basic-tercero"
											v-model="tercero"
											:options="basicTercero" 
											extra-classes="uk-form-width-long" 
											mode="outline"
											:settings="{ 'width': '100%', 'placeholder': 'Seleccione el tercero...', allowClear: true }"
										></Select2>
									</client-only>
								</div-->
								<!--Fecha de Creacion-->
								<div>
									<label>
										{{ $t('Date created') }}
									</label>
									<client-only>
										<ScInput 
											v-model="fecha" 
											v-flatpickr 
											placeholder="Seleccione la fecha de creación..." 
											mode="outline"
										>
										</ScInput>
									</client-only>
								</div>
								<div>
									<button class="sc-button sc-button-primary" @click="operation('SEARCH')">
										{{ $t('Search') }}
									</button>
								</div>
							</div>
						</li>
					</ul>
					<hr>
					<VueGoodTable
						:columns="columns"
						:rows="basicListUser"
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
		</div>
	</div>
	<!--div id="process-2"></div-->
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
import { logErrorMessages } from '@vue/apollo-util'
if(process.client) {
	require('~/plugins/inputmask');
	require('~/plugins/flatpickr');
}

import confirmDatePlugin from 'flatpickr/dist/plugins/confirmDate/confirmDate';
import { French } from "flatpickr/dist/l10n/fr.js"
import { watch } from 'vue'

/*import htmlImport from '/src/assets/htmlimport.html'

vue.component('#process-2',htmlImport);*/

export default {
	name: 'Buscar',
	
	components: {
		Select2: process.client ? () => import('~/components/Select2') : null,
		VueGoodTable,
		ScInput
	},
	apollo: {
	},
	mixins: [validationMixin],
	data: () => ({
		submitStatus: null,
		result:null,
		loading:null,
		mode:null,
		basicCiudad: [{ id: 1, text: 'Roboto, sans-serif' }],
		basicEstado: [], //READY
		basicCliente: [], //READY
		basicTercero: [],
		basicListUser: [],
		settings: { //Datos por defecto de las secciones
			basic: { 
				pageOnline: true,
				pageTitle: 'Creacion de Usuarios',
				pageKeywords: [1, 2],
				accessAllow: ['US', 'CN', 'BR', 'PL', 'ES', 'IN'],
				codigo: '',
				usuarioLogin: '',
				nombre: '',
				ciudad: '',
				cedula: '',
				estado: '',
				email: '',
				cliente: '',
				tercero: '',
				fecha: '',
			},
		},
		codigo: '',
		usuarioLogin: '',
		nombre: '',
		ciudad: '',
		cedula: '',
		estado: '',
		email: '',
		cliente: '',
		tercero: '',
		fecha: '',
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
					field: 'node.id',
					sortable: true,
					sortFn: this.Sort,
					tdClass: 'uk-text-center uk-text-nowrap'
				},
				{
					label: 'Login',
					field: 'node.usuarioLogin',
					tdClass: 'uk-text-center',
					filterOptions: {
						styleClass: 'uk-form-width-medium',
						enabled: true
					}

				},
				{
					label: 'Nombre',
					field: 'node.name',
					tdClass: 'uk-text-center',
					filterOptions: {
						styleClass: 'uk-form-width-medium',
						enabled: true
					}

				},
				{
					label: 'Ciudad',
					field: 'node.ciudadCodigo',
					
					filterOptions: {
						styleClass: 'uk-form-width-medium',
						enabled: true
					}
				},
				{
					label: 'Email',
					field: 'node.email',
					filterOptions: {
						styleClass: 'uk-form-width-medium',
						enabled: true
					}
				},
				{
					label: 'Estado',
					field: 'node.estadoCodigo',
					filterOptions: {
						styleClass: 'uk-form-width-small',
						enabled: true
					}
				},
				{
					label: 'Usuario Autoriza',
					field: 'node.usuarioAutoriza',
					filterOptions: {
						styleClass: 'uk-form-width-small',
						enabled: true
					}
				},
				{
					label: 'Usuario',
					field: 'node.usuarioCodigoCreacion',
					filterOptions: {
						styleClass: 'uk-form-width-small',
						enabled: true
					}
				},
				{
					label: 'Created On',
					field: 'node.usuarioFechacreacion',
					type: 'date',
					dateInputFormat: 'yyyy-MM-dd',
					dateOutputFormat: 'yyyy-MM-dd',
					tdClass: 'uk-text-nowrap uk-text-left'
				},
				{
					label: 'Modified On',
					field: 'node.usuarioFechamodificacion',
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
		//this.$store.commit('setFancyToolbarActive', true);
	},
	beforeDestroy () {
		//this.$store.commit('setFancyToolbarActive', false);
	},
	methods: {
		async onLoad () {
			await this.ArregloBasicEstado();
			await this.ArregloBasicCliente();
			await this.search();
		},
		ArregloBasicEstado () {
			//ESTADO
			console.log("entre en busqueda de estado");
			const GET_ESTADO = gql`
				query QUERY ($codigo: Float, $nombre: String, $modulo: Int, $estado: String) {
					allEstado(estadoCodigo: $codigo, estadoNombre: $nombre, moduloCodigo: $modulo, estadoVisible: $estado){
						edges{
							node{
								estadoCodigo
								estadoNombre
								moduloCodigo
							}
						}	
					}	
				}
				`;
			let {result, loading, error }  =  provideApolloClient(this.$apollo)(() => useQuery(GET_ESTADO, 
				{
					modulo: (17),
					estado: ("SI"),
				},
				{
					errorPolicy: 'all',
					fetchPolicy: 'no-cache'
				}));
			
			this.result=result;
			this.loading=loading;
			this.error=error;

			watch(result, value => {
				value.allEstado.edges.forEach(obj => {
					this.basicEstado.push({ id: obj.node.estadoCodigo, text: obj.node.estadoNombre },);
				});

				var config = {};
				config.timeout =  3000;
				config.status = "success";
				UIkit.notification('Consulta Ejecutada Correctamente con estados. '+value.allEstado.edges.length+' Registros', config);
			});
		},
		ArregloBasicCliente () {
			//Cliente
			const GET_CLIENTE = gql`
				query QUERY ($codigo: Float, $nombre: String) {
					allCliente(clienteCodigo: $codigo, clienteNombre1: $nombre){
						edges{
							node{
								clienteCodigo
								clienteNombre1
							}
						}	
					}	
				}
				`;
			let {result, loading, error }  =  provideApolloClient(this.$apollo)(() => useQuery(GET_CLIENTE, 
				{
					//modulo: (17),
					//estado: ("SI"),
				},
				{
					errorPolicy: 'all',
					fetchPolicy: 'no-cache'
				}));
			
			this.result=result;
			this.loading=loading;
			this.error=error;

			watch(result, value => {
				value.allCliente.edges.forEach(obj => {
					this.basicCliente.push({ id: obj.node.clienteCodigo, text: obj.node.clienteNombre1 },);
				});

				var config = {};
				config.timeout =  3000;
				config.status = "success";
				UIkit.notification('Consulta Ejecutada Correctamente con clientes. '+value.allCliente.edges.length+' Registros', config);
			});
		},
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
			console.log(this.$data.nombre.trim());
			
			let {result, loading, error }  =  provideApolloClient(this.$apollo)(() => useQuery(gql`
				query QUERY ($name: String, $usuarioLogin: String, $ciudadCodigo: Int, $email: String, $usuarioCedula: String, $estadoCodigo: Int, $usuarioFechacreacion: Date) {
					allUsuariocs(name_Contains: $name, usuarioLogin_Contains: $usuarioLogin, ciudadCodigo_Contains: $ciudadCodigo, email_Contains: $email, usuarioCedula_Contains: $usuarioCedula, estadoCodigo: $estadoCodigo, usuarioFechacreacion: $usuarioFechacreacion){
						edges{
							node{
								id
								name
								usuarioLogin
								ciudadCodigo
								email
								usuarioCedula
								estadoCodigo
								usuarioAutoriza
								usuarioFechacreacion
								usuarioFechamodificacion
							}
						}	
					}	
				}

			`, 
			{
				name: (this.$data.nombre.trim()!="" ? this.$data.nombre.toUpperCase() : null),
				usuarioLogin: (this.$data.usuarioLogin.trim()!="" ? this.$data.usuarioLogin.toUpperCase() : null),
				usuarioCedula: (this.$data.cedula.trim()!="" ? this.$data.cedula : null ),
				email: (this.$data.email.trim()!="" ? this.$data.email : null),
				usuarioFechacreacion: (this.$data.fecha.trim()!="" ? this.$data.fecha : null),
			},
			{
				errorPolicy: 'all',
				fetchPolicy: 'no-cache'
			}));

			this.result=result;
			this.loading=loading;
			this.error=error;

			watch(result, value => {
				this.basicListUser = value.allUsuariocs.edges;

				var config = {};
				config.timeout =  3000;
				config.status = "success";
				UIkit.notification('Consulta Ejecutada Correctamente con bodegas. '+value.allUsuariocs.edges.length+' Registros', config);
			});
			
			
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