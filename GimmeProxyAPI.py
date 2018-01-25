
"""
# Request Parameters

Parameter		Value					Description													Example request
api_key			string					API key, if you have one, allows to scrape faster			http://gimmeproxy.com/api/getProxy?api_key=xxxxx
get 			true/false				GET requests support										http://gimmeproxy.com/api/getProxy?get=true
post			true/false				POST requests support										http://gimmeproxy.com/api/getProxy?post=true
cookies			true/false				Cookies support												http://gimmeproxy.com/api/getProxy?cookies=true
referer			true/false				referer header support										http://gimmeproxy.com/api/getProxy?referer=true
user-agent		true/false				user-agent header support									http://gimmeproxy.com/api/getProxy?user-agent=false
supportsHttps	true/false				HTTPS support												http://gimmeproxy.com/api/getProxy?supportsHttps=false
anonymityLevel	0/1						Anonymity level, 1 - anonymous, 0 - not anonymous			http://gimmeproxy.com/api/getProxy?anonymityLevel=1
protocol		http/socks4/socks5		Proxy protocol												http://gimmeproxy.com/api/getProxy?protocol=http
port			integer					Proxy port													http://gimmeproxy.com/api/getProxy?port=80
country			string, comma separated	Return only proxies with specified country/countries 		http://gimmeproxy.com/api/getProxy?country=US,GB
maxCheckPeriod	integer, seconds		Return only proxies checked in last maxCheckPeriod seconds	http://gimmeproxy.com/api/getProxy?maxCheckPeriod=300
minSpeed		float, kb				Return only proxies with speed more than specified in KB	http://gimmeproxy.com/api/getProxy?minSpeed=50
notCountry		string					Exclude proxies from some country from search				http://gimmeproxy.com/api/getProxy?notCountry=US
websites 		string, website name 	Return only proxies allowed by particular websites. 		http://gimmeproxy.com/api/getProxy?websites=google
				(amazon, google)		Currently only Amazon and Google supported,
										more to be added soon.

# Response Example

{
  "supportsHttps": true,
  "protocol": "http",
  "ip": "200.21.21.157",
  "port": "8080",
  "get": true,
  "post": true,
  "cookies": true,
  "referer": true,
  "user-agent": true,
  "anonymityLevel": 1,
  "websites": {
    "example": true,
    "google": false,
    "amazon": false
  },
  "country": "CO",
  "tsChecked": 1514460042,
  "curl": "http://200.21.21.157:8080",
  "ipPort": "200.21.21.157:8080",
  "type": "http",
  "speed": 18.78,
  "otherProtocols": {}
}

"""

import json
import requests

class GimmeProxyAPI(object):
	"""docstring for proxy"""
	def __init__(self, **args):
		self.base_url = "https://gimmeproxy.com/api/getProxy"
		self.response = None

		if self.response is None:
			self.response = self.get_proxy(args=args)


	def response(self):
		return self.response


	def base_url(self):
		return self.base_url


	def get_proxy(self, **args):

		request = requests.get(self.base_url, params=args)

		if request.status_code == 200:
			self.response = request.json()
		else:
			raise Exception("An unknown error occured, status_code = {}".format(r.status_code))

		return self.response


	def get_curl(self):
		curl = self.response["curl"]
		return curl


	def get_ip_port(self):
		ip_port = self.response["ipPort"]
		return ip_port


	def get_port(self):
		port = self.response["port"]
		return port


	def get_ip(self):
		ip = self.response["ip"]
		return ip


