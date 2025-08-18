import { HttpLink } from 'apollo-link-http'
import { setContext } from 'apollo-link-context'
import { from } from 'apollo-link'
import { InMemoryCache } from 'apollo-cache-inmemory'
import { onError } from "@apollo/client/link/error"
import { logErrorMessages } from "@vue/apollo-util"


export default ctx => {
	const ssrMiddleware = setContext((_, { headers }) => {
		if (process.client) 
			return headers
		return {
      		headers
    	}
  	})
	var http
	if (process.client){
		const protocol = window.location.protocol
		const hostname = window.location.hostname
		const port = 8001
		const url = `${protocol}//${hostname}:${port}/graphql/`
		http = new HttpLink({
			uri: url,
		  })
	}
	else{
		http = new HttpLink({
    		uri: '',
  		})
	}

	const errorLink = onError((error) => {
		if (process.env.NODE_ENV !== "production") {
			logErrorMessages(error)
		}
	})
	const httpLink = http
	const link = from([ssrMiddleware, errorLink.concat(httpLink)])
  	const cache = new InMemoryCache()

  	return {
    	link,
    	cache,
    	defaultHttpLink: false
  	}
}
