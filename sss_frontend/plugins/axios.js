export default function ({$axios}) {
	if (process.client) {
		const protocol = window.location.protocol
  		const hostname = window.location.hostname
  		const port = 8001
		const url = `${protocol}//${hostname}:${port}`
		$axios.defaults.baseURL = url
		//$axios.defaults.baseURL = 'http://tevsa.colombiasoftware.com.co/'
	}
}