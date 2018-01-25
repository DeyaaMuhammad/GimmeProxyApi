

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


