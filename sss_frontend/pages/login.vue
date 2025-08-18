<template>
	<div class="uk-flex uk-flex-center uk-flex-middle sc-login-page-wrapper">
		<div class="main"
			:class="{
				'sign-up-mode': sign_up_mode
			}"
		>
			<div class="box">
				<div class="inner-box">
					<div class="forms-wrap">
						<form autocomplete="off" class="sign-up-form" @submit.prevent="validateUser($event)">
							<div class="logo">
								<img :src="appLogoEmpresa" alt="easyclass">
							</div>
							<!--  -->
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
							
							<input type="submit" value="Iniciar" class="sign-btn" :disabled="submitStatus === 'PENDING'">
						</form>

						<form autocomplete="off" class="sign-in-form" @submit.prevent="login($event)">
							<div class="logo">
								<img :src="appLogoEmpresa" alt="easyclass">
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
							<div class= "group-buttons" style="display: inline-flex;">
								<input type="submit" value="Continuar" class="sign-btn" :disabled="submitStatus === 'PENDING'" >
								<button class="sign-btn" :disabled="submitStatus === 'PENDING'" @click="backLogin" style="margin-left: 20px;">
									Volver 
								</button>
							</div>
							
							
						</form>

						
					</div>

					<div class="carousel"
						:class="{
							'carousel-left': sign_up_mode,
							'carousel-right': !sign_up_mode
						}"
					>
						<div class="images-wrapper">
							<img :src="imgLogin" class="image img-1 show" alt="">
						</div>
					</div>
				</div>
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
		loginData: {
			email: '',
			password: ''
		},
		registerData: {
			name: '',
			email: '',
			password: ''
		},
		recoverPassEmail: '',

		isSeeKey: true,
		typePassword: 'password',
		submitStatus: null,		
		usuario_login: '',
		usuario_password: '',
		sign_up_mode: true,
		apperanceCencos: [
			{ id : "0", text : "CC" }
		],
		cencosArray:'["1","2"]',
		cencos_codigo:'',
		userName:'',
	}),
	head () {
		return {
			'title': 'Scutum Admin Login Page'
		}
	},
	computed: {
		appLogoEmpresa () {
			return require('~/assets/img/silogproject-logo.png');
		},
		imgLogin () {
			return require('~/assets/img/img_login.png');
		},
		...mapGetters([
			'isAuthenticated', 'loggedInUser'
		]),
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
		backLogin (){
			this.sign_up_mode = true
			console.log('backLogin')
		},

		validateUser (e){
			console.log('validateUser ')
			e.preventDefault();
			this.$v.$touch();

			console.log(this.$v)

			if(this.$v.usuario_login.$error && this.$v.usuario_password.$error){
				this.submitStatus = 'ERROR'
			} else {
				//this.submitStatus = 'PENDING';
				let loginData = {
					login: this.usuario_login,
					password: this.usuario_password
				}

				let consulta = this.validateUserApi(loginData).then(
					response => {
						console.log('response', response)
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
						this.sign_up_mode = false
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
			console.log('user api')

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
		},

		back (){
			this.sign_up_mode = true
		},



  	},
}
</script>

<style>
.main {
  width: 100%;
  min-height: 90%;
  overflow: hidden;
  /* background-color: #ff8c6b; */
  padding: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.box {
  position: relative;
  width: 100%;
  max-width: 1020px;
  height: 640px;
  background-color: #fff;
  border-radius: 3.3rem;
  box-shadow: 0 60px 40px -30px rgba(0, 0, 0, 0.27);
}

.forms-wrap {
  position: absolute;
  height: 100%;
  width: 45%;
  top: 0;
  left: 0;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr;
  transition: 0.8s ease-in-out;
}

form {
  max-width: 260px;
  width: 100%;
  margin: 0 auto;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  grid-column: 1 / 2;
  grid-row: 1 / 2;
  transition: opacity 0.02s 0.4s;
}

form.sign-up-form {
  opacity: 0;
  pointer-events: none;
}

.logo {
  display: flex;
  align-items: center;
}

.logo img {
  width: 100px;
  margin-right: 0.3rem;
}
/* BOTONES */
.sign-btn {
  display: inline-block;
  width: 100%;
  height: 43px;
  background-color: #e94561;
  color: #fff;
  border: none;
  cursor: pointer;
  border-radius: 0.8rem;
  font-size: 0.8rem;
  margin-bottom: 2rem;
  transition: 0.3s;
}

.sign-btn:hover {
  /*background-color: #8371fd;*/
  background-color: #151111;
}
/* BOTONES */

.main.sign-up-mode form.sign-in-form {
  opacity: 0;
  pointer-events: none;
}

.main.sign-up-mode form.sign-up-form {
  opacity: 1;
  pointer-events: all;
}

.main.sign-up-mode .forms-wrap {
  left: 55%;
}

.main.sign-up-mode .carousel {
  left: 0%;
}

.carousel {
  position: absolute;
  height: 95%;
  width: 55%;
  left: 45%;
  top: 0;
  /*background-color: #ffe0d2;*/
  /* derecha*/
  /*background: linear-gradient(-45deg, #df4adf, #520852);*/
  background: rgb(0,0,0);
  /*izq*/
  display: grid;
  grid-template-rows: auto 1fr;
  padding-bottom: 2rem;
  overflow: hidden;
  transition: 0.8s ease-in-out;
}

.carousel-left {
	border-radius: 2rem 0rem 0rem 2rem; 
}

.carousel-right {
	border-radius: 0rem 2rem 2rem 0rem;
}


.images-wrapper {
  
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr;
  justify-items: center;
  padding-top: 80px;
}

.image {
  /*width: 100%;*/
  max-height: 561px;
  grid-column: 1/2;
  grid-row: 1/2;
  /*opacity: 0;*/
  transition: opacity 0.3s, transform 0.5s;
}

.img-1 {
  transform: translate(0, -50px);
}

.text-wrap {
  max-height: 2.2rem;
  overflow: hidden;
  margin-bottom: 2.5rem;
}

.text-group {
  display: flex;
  flex-direction: column;
  text-align: center;
  transform: translateY(0);
  transition: 0.5s;
}

.text-group h2 {
  line-height: 2.2rem;
  font-weight: 600;
  font-size: 1.6rem;
}

.bullets {
  display: flex;
  align-items: center;
  justify-content: center;
}

.bullets span {
  display: block;
  width: 0.5rem;
  height: 0.5rem;
  background-color: #aaa;
  margin: 0 0.25rem;
  border-radius: 50%;
  cursor: pointer;
  transition: 0.3s;
}

.bullets span.active {
  width: 1.1rem;
  background-color: #151111;
  border-radius: 1rem;
}

@media (max-width: 850px) {
  .box {
    height: auto;
    max-width: 550px;
    overflow: hidden;
  }

  .forms-wrap {
    position: revert;
    width: 100%;
    height: auto;
  }

  form {
    max-width: revert;
    padding: 1.5rem 2.5rem 2rem;
    transition: transform 0.8s ease-in-out, opacity 0.45s linear;
  }

  form.sign-up-form {
    transform: translateX(100%);
  }

  .main.sign-up-mode form.sign-in-form {
    transform: translateX(-100%);
  }

  .main.sign-up-mode form.sign-up-form {
    transform: translateX(0%);
  }

  .carousel {
    position: revert;
    height: auto;
    width: 100%;
    padding: 3rem 2rem;
    display: flex;
  }

  .images-wrapper {
    display: none;
  }

}

@media (max-width: 530px) {
  .main {
    padding: 1rem;
  }

  .box {
    border-radius: 2rem;
  }

  .carousel {
    padding: 1.5rem 1rem;
    border-radius: 1.6rem;
  }

}

</style>

