# GimmeProxyApi
Python API Package for gimmeproxy.com .


# API Parameters

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
