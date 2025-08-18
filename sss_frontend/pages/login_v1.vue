<template>
	<div class="uk-flex uk-flex-center uk-flex-middle sc-login-page-wrapper">
		<div class="uk-width-2-3@s uk-width-1-2@m uk-width-1-3@l uk-width-1-4@xl uk-margin-auto-vertical">
			LOGIN
			<ScCard>
				<ScCardBody>
					<div class="sc-login-page-logo">
						<img v-rjs="require('~/assets/img/logo_alt@2x.png')" :src="appLogo" alt="">
					</div>
					<div class="sc-login-page-logo sc-login-page-logo-light">
						<img v-rjs="require('~/assets/img/logo_alt.png')" :src="appLogoLight" alt="">
					</div>
					<div id="sc-login-form" class="sc-toggle-login-register sc-toggle-login-password">
						<div class="sc-login-page-inner">
							<div class="uk-margin-medium">
								<ScInput v-model="loginData.email">
									<label>
										Email/Login
									</label>
								</ScInput>
							</div>
							<div class="uk-margin-medium">
								<ScInput v-model="loginData.password" type="password">
									<label>
										Password
									</label>
								</ScInput>
								<div class="uk-margin-small-top uk-text-small uk-text-right@s">
									<a href="javascript:void(0)" class="sc-link" data-uk-toggle="target: .sc-toggle-login-password; animation: uk-animation-scale-up">
										Forgot Password?
									</a>
								</div>
							</div>
							<div class="uk-margin-large-top">
								<button class="sc-button sc-button-large sc-button-block sc-button-secondary" @click="logInUser(loginData)">
									Sign Up
								</button>
								
								<div class="uk-margin-large-top uk-text-center">
									<span class="sc-color-secondary">
										Don't have an account?
									</span>
									<div>
										<a href="javascript:void(0)" class="sc-text-semibold" data-uk-toggle="target: .sc-toggle-login-register; animation: uk-animation-scale-up">
											Sign Up
										</a>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div id="sc-register-form" class="sc-toggle-login-register" hidden>
						<div class="sc-login-page-inner">
							<div class="uk-margin-medium">
								<ScInput v-model="registerData.name">
									<label>
										Name
									</label>
								</ScInput>
							</div>
							<div class="uk-margin-medium">
								<ScInput v-model="registerData.email">
									<label>
										Email
									</label>
								</ScInput>
							</div>
							<div class="uk-margin-medium">
								<ScInput v-model="registerData.password">
									<label>
										Password
									</label>
								</ScInput>
							</div>
							<div class="uk-margin-large-top">
								<button class="sc-button sc-button-large sc-button-block sc-button-secondary">
									Sign Up
								</button>
								<div class="uk-margin-large-top uk-flex uk-flex-middle uk-flex-center">
									<a href="javascript:void(0)" class="sc-text-semibold" data-uk-toggle="target: .sc-toggle-login-register; animation: uk-animation-scale-up">
										Back to login form
									</a>
								</div>
							</div>
						</div>
					</div>
					<div id="sc-password-form" class="sc-toggle-login-password" hidden>
						<div class="sc-login-page-inner">
							<div class="uk-margin-medium">
								Please enter your email address. You will receive a link to reset your password.
							</div>
							<div class="uk-margin-medium">
								<ScInput v-model="recoverPassEmail">
									<label>
										Email
									</label>
								</ScInput>
							</div>
							<div class="uk-margin-large-top">
								<button class="sc-button sc-button-large sc-button-block sc-button-primary">
									Reset Password
								</button>
								<div class="uk-margin-large-top uk-flex uk-flex-middle uk-flex-center">
									<a href="javascript:void(0)" class="sc-text-semibold" data-uk-toggle="target: .sc-toggle-login-password; animation: uk-animation-scale-up">
										Back to login form
									</a>
								</div>
							</div>
						</div>
					</div>
				</ScCardBody>
			</ScCard>
		</div>
	</div>
</template>

<script>
import ScInput from '~/components/Input'

export default {
	name: 'LoginPageV1',
	components: {
		ScInput
	},
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
		recoverPassEmail: ''
	}),
	head () {
		return {
			'title': 'Scutum Admin Login Page'
		}
	},
	computed: {
		appLogo () {
			return require('~/assets/img/logo_alt.png');
		},
		appLogoLight () {
			return require('~/assets/img/logo.png');
		}
	},
	methods: {
    	async logInUser (loginData) {
      		try {
				
        		let response=await this.$auth.loginWith('auth0', {
          			data: loginData,
        		})
        		console.log('notification successful')
				console.log(response.data)
				//this.$auth.setUser(response.data.user)
				
				
				
				//this.$router.push(this.localePath({ name: 'dashboard' }))
				//this.$router.push("/pages/contact_list")
      		} catch (error) {
        		console.log('notification unsuccessful')
      		}
    	},
  	},
}
</script>


