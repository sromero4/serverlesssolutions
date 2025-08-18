import { scHelpers } from "~/assets/js/utils";
import { index, } from './'
const { uniqueID } = scHelpers;


export const state = () => ({
	menu: []
});

export const getters = {
	
	menu (state) {
		//return state.menu;
		//return state.auth.modulos
		return state.menu
	}
}

export const actions = {

	async actionMenu ({ commit }){
		let serverApi = this.$axios.defaults.baseURL
		let urlRequest = `${serverApi}/api/Usuario/user`;

		if (typeof window !== 'undefined') {
			console.log(window.localStorage.getItem('cc'))
			let loginData = { "user_id": window.localStorage.getItem('user_id'), "cc": window.localStorage.getItem('cc') }
			const responseMenu = await this.$axios.$get(urlRequest, { params: loginData }).then( 
				function (response){
					commit('SET_MENU', response.modulos)
					return response.modulos
				}
			)	
		} else {
			console.log('You are on the server')
			// 👉️ can't use localStorage
		}

	}
}


export const mutations = {
	SET_MENU (state, menu){
    	state.menu = menu;
	},

	ADD_MENU (state, menu){
    	state.menu = [menu, ...state.menu]
	},

	REMOVE_MENU (state, menu){
		state.menu = state.menu.filter ( menu => menu.id !== id )
	}, 

	SET_ITEM_OPEN (state, item){
		console.log(item);
		item.isOpen = !item.isOpen;
		//console.log(state.menu.filter (menu => menu.id === id) )
		
	}

};