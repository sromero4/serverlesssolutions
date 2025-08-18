<template>
	<div id="sc-page-wrapper">
		<div id="sc-page-content" class="uk-height-1-1 uk-flex uk-flex-center sc-page-over-header">
			<iframe :src="iframeSrc" style="border: 0; width: 100%; height: 100%">
			</iframe>
		</div>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'PagesBlankHeaderExpanded',
	async sendData () {
		
	},
	data: () => ({
		
		iframeSrc: "",
		
	}),
	computed: {
		token () {
			let token = this.$auth.strategy.token.get().replace("Bearer", "")
			token=token.trim()
			return token
		}
	},
	mounted () {
		if (this.$store.state.silogtran == 'NO'){
			this.iframeSrc="https://tevsa.colombiasoftware.net/index.php?page=LoginPage&bearer="+this.token
			this.$store.commit('setSilogtran', 'SI');
		}
		else{
			this.iframeSrc="https://tevsa.colombiasoftware.net/index.php";
		}
		
		this.$store.commit('setCardFixed', true);
		this.$store.commit('setHeaderExpanded', true);
		
		/*this.$axios.get('https://tevsa.colombiasoftware.net/index.php?page=LoginPage')
			.then((response) => {
				console.log(response);
			}, (error) => {
				console.log(error);
			});
		*/
			
		
	},
	beforeDestroy () {
		this.$store.commit('setCardFixed', false);
		this.$store.commit('setHeaderExpanded', false);
	}
}
</script>
