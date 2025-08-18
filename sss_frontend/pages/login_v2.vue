<template>
	<div class="container" 
		:class="{
			'sign-up-mode': sign_up_mode
		}"
	>
		<div class="forms-container">
			<div class="signin-signup">
				<form class="sign-in-form" @submit.prevent="validateUser($event)">
					<div class="container-logo">
						<img :src="appLogoLight" alt="">
						<!-- <div 
							class="uk-height-medium uk-flex uk-flex-center uk-flex-middle uk-background-cover uk-light" 
							:data-src="appLogoLight" 
							uk-img
							width="100%"
						>
						</div> -->
					</div>
					<h2 class="title">
						Bienvenido
					</h2>
					<div class="uk-margin-medium">
						<ScInput v-model="$v.usuario_login.$model"
							name="login"
							type="text"
							extra-classes="uk-form-width-medium"
							:error-state="$v.usuario_login.$error"
							:validator="$v.usuario_login"
						>
							<label>
								Usuario
							</label>
							<span slot="icon" class="uk-form-icon" data-uk-icon="icon: user"></span>
						</ScInput>
						<ul class="sc-vue-errors">
							<li v-if="!$v.usuario_password.required || $v.usuario_login.$model === '' ">
								El usuario es obligatorio.
							</li>
						</ul>
					</div>
					<div class="uk-margin-medium">
						<ScInput v-model="$v.usuario_password.$model"
							name="password"
							:type="typePassword"
							extra-classes="uk-form-width-medium"
							:error-state="$v.usuario_password.$error"
							:validator="$v.usuario_password"
						>
							<span slot="icon" class="uk-form-icon" data-uk-icon="icon: lock"></span>
							<label style="padding-left: 35px;">Contraseña</label>
							<a slot="icon" class="uk-form-icon uk-form-icon-flip" @click="seeKey">
								<i 
									class="mdi" 
									:class="{ 'mdi-eye-outline': isSeeKey, 'mdi-eye-off-outline': !isSeeKey}"
								></i>
							</a>
						</ScInput>
						<ul class="sc-vue-errors">
							<li v-if="!$v.usuario_password.required">
								La contraseña es obligatoria.
							</li>
						</ul>
					</div>

					<button type="submit" class="sc-button sc-button-custom md-bg-blue-500" :disabled="submitStatus === 'PENDING'">
						Iniciar sesión
					</button>
				</form>
				<form action="#" class="sign-up-form" @submit.prevent="login($event)">
					<div class="container-logo">
						<img :src="appLogoLight" alt="">
					</div>
					<h2 class="title uk-text-capitalize">
						Bienvenido {{ userName }}
					</h2>
					<h3>Selecciona tu centro de costo</h3>

					<div>
						<Cselect
							v-model="cencos_codigo"
							:options="apperanceCencos"
							:settings="{ 'width': '100%', 'placeholder': 'Seleccione el centro de costo...', 'minimumResultsForSearch': -1, 'allowClear': true }"
							:error-state="$v.cencos_codigo.$error"
							source="allCentrocosto"
							query-fields="cencosCodigo|cencosNombre"
							criteria="cencosCodigo_In"
							:criteria-fields='cencosArray'
						></Cselect>

						<ul class="sc-vue-errors">
							<li v-if="!$v.cencos_codigo.$required">
								El centro de costo es obligatorio.
							</li>
						</ul>
					</div>

					<br>

					<div>
						<button 
							class="sc-button sc-button-custom md-bg-blue-500 uk-margin-medium-right" 
							:disabled="submitStatus === 'PENDING'"
							@click="back" 
						>
							Volver 
						</button>
						<button 
							type="submit" 
							class="sc-button sc-button-custom md-bg-blue-500" 
							:disabled="submitStatus === 'PENDING'"
						> 
							Continuar
						</button>
					</div>
				</form>
			</div>
		</div>

		<div class="panels-container">
			<div class="panel left-panel">
				<div class="content">
					<div class="container-logo">
						<img :src="appLogoCs" alt="">
					</div>
					<p>Integra la información basica con la operación de transporte, el manejo de terceros, el proceso de predespacho, la facturación y la operación nacional en un solo sistema de gestión.</p>
				</div>
				<img :src="logImg" class="image" alt="">
			</div>
			<div class="panel right-panel">
				<div class="content">
					<h3></h3>
					<p></p>
				</div>
				<img :src="registerImg" class="image" alt="">
			</div>
		</div>
	</div>
</template>

<script>
import ScInput from '~/components/Input'
import { validationMixin } from 'vuelidate'
import { required, minLength, email, sameAs } from 'vuelidate/lib/validators'

import { mapGetters } from 'vuex'

export default {
	name: 'LoginPage',
	components: {
		ScInput,
		Cselect: process.client ? () => import('~/components/CSelect') : null,
	},
	mixins: [validationMixin],
	layout: 'login_page',
	data: () => ({
		isSeeKey: true,
		typePassword: 'password',
		responseUser:[],
		userName:'',
		cencos_codigo:'',
		cencosArray:'["1","2"]',
		submitStatus: null,
		recoverPassEmail: '',
		usuario_login: '',
		usuario_password: '',
		sign_up_mode: false,
		apperanceCencos: [
			{ id : "MUY PEQUENO", text : "MUY PEQUENO" },
			{ id : "PEQUENO", text : "PEQUENO" },
			{ id : "MEDIANO", text : "MEDIANO" },
			{ id : "GRANDE", text : "GRANDE" },
			{ id : "MUY GRANDE", text : "MUY GRANDE" }
		],
	}),
	head () {
		return {
			'title': 'Scutum Admin Login Page'
		}
	},
	computed: {
		
		appLogoCs () {
			return require('~/assets/img/logo-cs.svg');
		},
		appLogoLight () {
			return require('~/assets/img/silogproject-logo.png');
		},

		logImg () {
			return require('~/assets/img/Logistics-pana.svg');
		},
		registerImg () {
			return require('~/assets/img/Business-merger-rafiki.svg');

		},
		...mapGetters([
			'isAuthenticated', 'loggedInUser'
		]),
		
	},
	mounted () {
		console.log('login_page');
		//console.log(this.$axios.defaults.baseURL)
	},

	validations: {
		usuario_login:{
			required
		},
		usuario_password:{
			required
		},
		cencos_codigo:{
			required
		}
	},

	methods: {
		login (e) {
			console.log('todo ok login')

			e.preventDefault();
			this.$v.$touch();

			if (this.$v.$invalid) {
				this.submitStatus = 'ERROR'
				console.log('error');
			} else {
				this.submitStatus = 'PENDING';
				console.log('else l230');
				console.log(this.responseUser)
				let loginData = {
					usuario_login: this.responseUser.login,
					password: this.usuario_password,
					cencos_codigo:this.cencos_codigo
				}
				
				let request = this.logInUserApi(loginData).then(
					response => {
						console.log(response)
					}
				)
				setTimeout(() => {
					this.submitStatus = 'OK'
				}, 500)
			}
		},

		async logInUserApi (loginData) {
      		try {
				
        		//let response=await this.$auth.loginWith('auth0', {
				let response=await this.$auth.loginWith('local', {
          			data: loginData,
        		}).then(
					response => {
						console.log(response)
						this.$auth.setUser(response.data.user)
						localStorage.setItem('user_id', response.data.user.usuario_codigo);
						localStorage.setItem('cc', response.data.user.centro_costo.cencos_codigo);

					}
				)
				this.sign_up_mode = true
				return response;
      		} catch (error) {
        		//console.log('notification unsuccessful')
      		}
    	},

		validateUser (e){
			
			e.preventDefault();
			this.$v.$touch();
			if(this.$v.usuario_login.$error && this.$v.usuario_password.$error){
				this.submitStatus = 'ERROR'
			} else {
				this.submitStatus = 'PENDING';
				let loginData = {
					login: this.usuario_login,
					password: this.usuario_password
				}

				let consulta = this.validateUserApi(loginData).then(
					response => {
						console.log(response)
						if(!response.success){
							this.showNotification(`<div class="uk-flex uk-flex-middle"><i class="mdi mdi-alpha-x-circle uk-margin-right"></i>${response.message}</div>`, 'bottom-right', 'danger');
							this.submitStatus = 'OK';
							return
						}
						this.userName = response.data.name.toLowerCase()
						
						if(response.data.cencos.length == 0){
							this.showNotification(`<div class="uk-flex uk-flex-middle"><i class="mdi mdi-alpha-x-circle uk-margin-right"></i>El usuario ${this.userName} no tiene centros de costo asignados</div>`, 'bottom-right', 'danger');
							this.submitStatus = 'OK';
							return
						}

						let arrayCencos = response.data.cencos.map(function (cencos) {
							let empresaNombre = cencos.empresa_nombreabreviado ? cencos.empresa_nombreabreviado : cencos.empresa_nombre
							return {"id":cencos.cencos_codigo, "text": cencos.cencos_nombre +' '+empresaNombre};
						});


						this.apperanceCencos = JSON.parse(JSON.stringify(arrayCencos))
						this.showNotification(`<div class="uk-flex uk-flex-middle"><i class="mdi mdi-check-all uk-margin-right"></i><span class="uk-text-capitalize">Hola ${this.userName}</span></div>`, 'bottom-right', 'success');
						this.responseUser = response.data
						this.submitStatus = 'OK';
						this.sign_up_mode = true
					}
				).catch(function (error) {
					this.showNotification(`<div class="uk-flex uk-flex-middle"><i class="mdi mdi-alpha-x-circle uk-margin-right"></i>Ocurrio un error al intentar iniciar sesion </div>`, 'bottom-right', 'danger');
					this.submitStatus = 'OK';
					return
					//return error.response.data;
				});
				
			}

		},


		async validateUserApi (loginData){
			let serverApi = this.$axios.defaults.baseURL
			let urlRequest = `${serverApi}/api/Usuario/get_user_exists`;
			//console.log(urlRequest)

			try {
				return await this.$axios.$post(urlRequest, loginData).then( function (response){
					//console.log(response)
					return response
				}).catch(function (error) {
					console.log(error.response.data)
					if (!error.response) {
						// network error
						return 'Error: Network Error';
					} else {
						return error.response.data;
					}

				});
			} catch (error) {
				response = {"success":false, 'message':"Error de conexion", error: error}
				console.log(response)
				return response
			
			}

			
		},

		
		showNotification (text, pos, status, persistent) {
			var config = {};
			config.timeout = persistent ? !persistent : 3000;
			if(status) {
				config.status = status;
			}
			if(pos) {
				config.pos = pos;
			}
			UIkit.notification(text, config);
		},

		seeKey (){
			this.isSeeKey = !this.isSeeKey
			this.typePassword= !this.isSeeKey ? 'text' : 'password'
			//console.log('ver clave: '+this.isSeeKey)
		},

		back (){
			//console.log('back')
			this.sign_up_mode = false
		},

	}

}
</script>

<style>
.container-logo{
	width: 140px;
	display: inline-block;
}

.container {
  position: relative;
  width: 100%;
  background-color: #fff;
  min-height: 100vh;
  overflow: hidden;
}

.forms-container {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}

.signin-signup {
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  left: 75%;
  width: 50%;
  transition: 1s 0.7s ease-in-out;
  display: grid;
  grid-template-columns: 1fr;
  z-index: 5;
}

form {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0rem 5rem;
  transition: all 0.2s 0.7s;
  overflow: hidden;
  grid-column: 1 / 2;
  grid-row: 1 / 2;
}

form.sign-up-form {
  opacity: 0;
  z-index: 1;
}

form.sign-in-form {
  z-index: 2;
}

.panels-container {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}

.container:before {
  content: "";
  position: absolute;
  height: 2000px;
  width: 2000px;
  top: -10%;
  right: 48%;
  transform: translateY(-50%);
  background-image: linear-gradient(-45deg, #4481eb 0%, #04befe 100%);
  transition: 1.8s ease-in-out;
  border-radius: 50%;
  z-index: 6;
}

.image {
  width: 100%;
  transition: transform 1.1s ease-in-out;
  transition-delay: 0.4s;
}

.panel {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: space-around;
  text-align: center;
  z-index: 6;
}

.left-panel {
  pointer-events: all;
  padding: 3rem 17% 2rem 12%;
}

.right-panel {
  pointer-events: none;
  padding: 3rem 12% 2rem 17%;
}

.panel .content {
  color: #fff;
  transition: transform 0.9s ease-in-out;
  transition-delay: 0.6s;
}

.panel h3 {
  font-weight: 600;
  line-height: 1;
  font-size: 1.5rem;
}

.panel p {
  font-size: 0.95rem;
  padding: 0.7rem 0;
}


.right-panel .image,
.right-panel .content {
  transform: translateX(800px);
}

/* ANIMATION */

.container.sign-up-mode:before {
  transform: translate(100%, -50%);
  right: 52%;
}

.container.sign-up-mode .left-panel .image,
.container.sign-up-mode .left-panel .content {
  transform: translateX(-800px);
}

.container.sign-up-mode .signin-signup {
  left: 25%;
}

.container.sign-up-mode form.sign-up-form {
  opacity: 1;
  z-index: 2;
}

.container.sign-up-mode form.sign-in-form {
  opacity: 0;
  z-index: 1;
}

.container.sign-up-mode .right-panel .image,
.container.sign-up-mode .right-panel .content {
  transform: translateX(0%);
}

.container.sign-up-mode .left-panel {
  pointer-events: none;
}

.container.sign-up-mode .right-panel {
  pointer-events: all;
}

@media (max-width: 870px) {
  .container {
    min-height: 800px;
    height: 100vh;
  }
  .signin-signup {
    width: 100%;
    top: 95%;
    transform: translate(-50%, -100%);
    transition: 1s 0.8s ease-in-out;
  }

  .signin-signup,
  .container.sign-up-mode .signin-signup {
    left: 50%;
  }

  .panels-container {
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 2fr 1fr;
  }

  .panel {
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    padding: 2.5rem 8%;
    grid-column: 1 / 2;
  }

  .right-panel {
    grid-row: 3 / 4;
  }

  .left-panel {
    grid-row: 1 / 2;
  }

  .image {
    width: 200px;
    transition: transform 0.9s ease-in-out;
    transition-delay: 0.6s;
  }

  .panel .content {
    padding-right: 15%;
    transition: transform 0.9s ease-in-out;
    transition-delay: 0.8s;
  }

  .panel h3 {
    font-size: 1.2rem;
  }

  .panel p {
    font-size: 0.7rem;
    padding: 0.5rem 0;
  }

   .container:before {
    width: 1500px;
    height: 1500px;
    transform: translateX(-50%);
    left: 30%;
    bottom: 68%;
    right: initial;
    top: initial;
    transition: 2s ease-in-out;
  }

  .container.sign-up-mode:before {
    transform: translate(-50%, 100%);
    bottom: 32%;
    right: initial;
  }

  .container.sign-up-mode .left-panel .image,
  .container.sign-up-mode .left-panel .content {
    transform: translateY(-300px);
  }

  .container.sign-up-mode .right-panel .image,
  .container.sign-up-mode .right-panel .content {
    transform: translateY(0px);
  }

  .right-panel .image,
  .right-panel .content {
    transform: translateY(300px);
  }

  .container.sign-up-mode .signin-signup {
    top: 5%;
    transform: translate(-50%, 0);
  }
}

@media (max-width: 570px) {
  form {
    padding: 0 1.5rem;
  }

  .image {
    display: none;
  }
  .panel .content {
    padding: 0.5rem 1rem;
  }
  .container {
    padding: 1.5rem;
  }

  .container:before {
    bottom: 72%;
    left: 50%;
  }

  .container.sign-up-mode:before {
    bottom: 28%;
    left: 50%;
  }
}

</style>
