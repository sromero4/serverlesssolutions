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
				</ul>
			</div>
		</div>
		<div>
			Loading..........jhjhj
			<button class="sc-fab sc-fab-small" @click="query()">
				buttona
			</button>
			<button class="sc-fab sc-fab-small" @click="query()">
				buttona
			</button>
			<button class="sc-fab sc-fab-small" @click="query()">
				buttona
			</button>
			<button class="sc-fab sc-fab-small" @click="query()">
				buttona
			</button>
			<button class="sc-fab sc-fab-small" @click="query()">
				buttona
			</button>
			<button class="sc-fab sc-fab-small" @click="query()">
				buttona
			</button>
			<button class="sc-fab sc-fab-small" @click="editForm(props.row,'view')">
				<i class="mdi  mdi-eye-outline md-color-red-600" data-uk-tooltip="View"></i>
			</button>
		</div>
	</div>
</template>

<script>
import { provideApolloClient, useQuery } from '@vue/apollo-composable';

import gql from 'graphql-tag'


const ALL_COLOR = gql`
  query  ALL_COLOR{
    allColor{
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
`;

export default {
	name: 'Color',
	data: () => ({
		submitStatus: null,
		colorCodigo: '',
		colorNombre: '',
		colorCodigoMinisterio: '',
		colorFechacreacion: '',
		colorFechamodificacion: '',
		usuarioCodigo: '',
		filter: {
			codigo: '',
			nombre: '',
					
		}
	}),
	apollo: {
	},
	
	computed: {
		
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

	methods: {

		query (){
			const { result, loading, error } = provideApolloClient(this.$apollo)(() => useQuery(gql`
					query  ALL_COLOR{
						allColor{
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
				`));// -------- Computeds -------- //
			console.log(error);
			console.log(loading);
			console.log(result);
			var config = {};
			config.timeout =  3000;
			
			config.status = "success";
			
			UIkit.notification('Consulta ejecutada', config);
			return {
				result,
				loading,
				error
			};
		},
		submitForm (e) {
			e.preventDefault();
			this.$v.$touch();
			if (this.$v.$invalid) {
				this.submitStatus = 'ERROR'
			} else {
				this.submitStatus = 'OK';
				this.create();
				/*setTimeout(() => {
					this.submitStatus = 'OK'
				}, 500)*/
			}
		},
		priorityLabel (priority) {
			let priorityClass = null;
			switch (priority) {
			case 'minor':
				priorityClass = 'uk-label-success';
				break;
			case 'major':
				priorityClass = '';
				break;
			case 'critical':
				priorityClass = 'uk-label-warning';
				break;
			case 'blocker':
				priorityClass = 'uk-label-danger';
				break;
			default:
			}
			return priorityClass;
		},
		Sort (x, y, col, rowX, rowY) {
			const _x = parseInt(x.replace("sc-", ""));
			const _y = parseInt(y.replace("sc-", ""));
			return (_x < _y ? -1 : (_x > _y ? 1 : 0));
		},
		async findColor () {
      		try {
				
        		console.log('notification successful')
				
      		} catch (error) {
        		
      		}
    	},
		async search () {
			
			try {
				const res = await this.$apollo.query({
					query: COLOR_FILTER,
					variables: {
						codigo: (this.filter.codigo.trim()!="" ? this.filter.codigo.toUpperCase() : null),
						nombre: (this.filter.nombre.trim()!="" ? this.filter.nombre.toLocaleUpperCase() : null),
					},
				});
				if (res) {
					this.allColor=res.data.allColor.edges;
				}
			} catch (err) {
				console.log(err);
			}
  		},
		async create () {
        	
			try{
				res = await this.$apollo.mutate({
					mutation: gql`mutation createColor($colorNombre: String!, $colorCodigoMinisterio: String!, $usuarioCodigo: Int!,$colorFechacreacion: Date!,$colorFechamodificacion: Date!){
						createColor(colorNombre: $colorNombre, colorCodigoMinisterio: $colorCodigoMinisterio, usuarioCodigo: $usuarioCodigo, colorFechacreacion: $colorFechacreacion, colorFechamodificacion: $colorFechamodificacion) {
							color{
								colorCodigo
								colorNombre
								colorCodigoMinisterio
								usuarioCodigo
								colorFechacreacion
								colorFechamodificacion
							}
						}
					}`,
					variables:{
						colorNombre: this.$data.colorNombre,
						colorCodigoMinisterio: this.$data.colorCodigoMinisterio,
						usuarioCodigo: this.$data.usuarioCodigo,
						colorFechacreacion: this.$data.colorFechacreacion,
						colorFechamodificacion: this.$data.colorFechamodificacion

					}
				});
				

				if (res) {
					objeto=res.data.createColor.color;
					this.allColor=res.data.createColor.color;
				}
			}catch (err) {
				console.log(err);
			}
		},

		createForm () {
			var currentDate = new Date();
			var fecha=moment(currentDate, 'YYYY-MM-DD', true).format('YYYY-MM-DD');
			this.$data.colorCodigo="";
			this.$data.colorNombre=""
			this.$data.colorCodigoMinisterio="";
			this.$data.colorFechacreacion=fecha;
			this.$data.colorFechamodificacion=fecha;
			this.$data.usuarioCodigo="1";
			var modal = UIkit.modal("#modal-container");
    		modal.show(); 
  		},
		editForm (row, prop) {
			this.$data.colorCodigo=row.node.colorCodigo+"";
			this.$data.colorNombre=row.node.colorNombre;
			this.$data.colorCodigoMinisterio=row.node.colorCodigoMinisterio+"";
			this.$data.colorFechacreacion=row.node.colorFechacreacion;
			this.$data.colorFechamodificacion=row.node.colorFechamodificacion;
			this.$data.usuarioCodigo=row.node.usuarioCodigo+"";
			var modal = UIkit.modal("#modal-container");
    		modal.show(); 
			
  		},
	}
}
</script>

