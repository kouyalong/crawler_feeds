# coding: utf-8

import requests
from urllib.parse import urlencode

from common.util import (
	url_add_query,
	response_parse_json,
)


class Spider:

	def __init__(self, url, query=None, headers=None):
		self.url = url
		self.query = query or {}
		self.headers = headers or {}

	def fake_url_args(self):
		pass

	def fake_headers(self):
		pass

	def pre_request(self):
		self.fake_headers()
		self.fake_url_args()
		if self.query:
			query = urlencode(self.query)
			self.url = url_add_query(self.url, query)

	@response_parse_json
	def do_request(self):
		result = requests.get(self.url, headers=self.headers)
		return result
