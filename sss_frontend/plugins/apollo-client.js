import { provide, onGlobalSetup, defineNuxtPlugin } from '@nuxtjs/composition-api';
import { DefaultApolloClient } from '@vue/apollo-composable/dist';
export default defineNuxtPlugin(({ app }) => {
	onGlobalSetup(() => {
		//const apolloClient = app.apolloProvider.defaultClient;
		provide(DefaultApolloClient, app.apolloProvider?.defaultClient);
		//provide(DefaultApolloClient, apolloClient);
	});
});

