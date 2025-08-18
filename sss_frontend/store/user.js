import { index, } from './'
export const state = () => ({
	user: []
});

export const getters = {
	
	user (state) {
		return state.user
	}
}

export const actions = {
	async actionUser ({ commit }){
		let serverApi = this.$axios.defaults.baseURL
		let urlRequest = `${serverApi}/api/Usuario/user`;
		if (typeof window !== 'undefined') {
			let loginData = { "user_id": window.localStorage.getItem('user_id'), "cc": window.localStorage.getItem('cc') }
			const responseUser = await this.$axios.$get(urlRequest, { params: loginData }).then( 
				function (response){
					commit('SET_USER', response)
					return response
				}
			)
			
		} else {
			console.log('You are on the server')
		}
	}
}

export const mutations = {
	SET_USER (state, user){
    	state.user = user;
	},

	ADD_USER (state, user){
    	state.user = [user, ...state.user]
	},

	REMOVE_USER (state, user){
		state.user = state.user.filter ( user => user.id !== id )
	}, 
};