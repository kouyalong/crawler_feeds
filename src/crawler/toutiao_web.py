# coding: utf-8

import time

import requests
from urllib.parse import urljoin

from src.settings.base import (
	TOUTIAO_BASE_URL,
	TOUTIAO_FEEDS_URL_PATH,
	TOUTIAO_SIGNATURE_JAVASCRIPT_FILE_NAME,
	TOUTIAO_SIGNATURE_JAVASCRIPT_FUNCTION_NAME,
	TOUTIAO_AS_CP_JAVASCRIPT_FILE_NAME,
	TOUTIAO_AS_CP_JAVASCRIPT_FUNCTION_NAME
)
from src.common.util import load_javascript
from src.crawler.spider import Spider


class SpiderTouTiaoWeb(Spider):
	# 爬取头条PC WEB数据

	def __init__(self, query=None, headers=None):
		self.query = query or {}
		self.headers = headers or {}
		self.category = "__all__"
		url = urljoin(TOUTIAO_BASE_URL, TOUTIAO_FEEDS_URL_PATH)
		super(SpiderTouTiaoWeb, self).__init__(url, self.query, self.headers)

	def fake_headers(self):
		tt_headers = {
			'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'zh-CN,zh;q=0.9',
			'cache-control': 'no-cache',
			'content-type': 'application/x-www-form-urlencoded',
			'pragma': 'no-cache',
			'referer': TOUTIAO_BASE_URL,
			'x-requested-with': 'XMLHttpRequest',
			"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
		}
		tt_headers.update(self.headers)
		self.headers = tt_headers
		self.headers["cookie"] = "tt_webid={}".format(self.get_web_id())

	def fake_url_args(self, max_behot_time=0):
		tt_query = {
			"category": self.category,
			"widen": 1,
			"utm_source": 'toutiao',
			"tadrequire": "true",
		}
		if max_behot_time:
			tt_query["max_behot_time_tmp"] = max_behot_time
			tt_query["max_behot_time"] = max_behot_time
		else:
			tt_query["min_behot_time"] = int(time.time())

		tt_query.update(self.query)
		self.query = tt_query
		self.query.update(self.get_signature(*[max_behot_time, self.headers["user-agent"]]))
		self.query.update(self.get_as_cp())

	def get_signature(self, *args):
		# 头条接口  _signature参数
		result = load_javascript(TOUTIAO_SIGNATURE_JAVASCRIPT_FILE_NAME, TOUTIAO_SIGNATURE_JAVASCRIPT_FUNCTION_NAME, *args)
		return {"_signature": result}

	def get_as_cp(self):
		# 头条接口 as， cp参数
		result = load_javascript(TOUTIAO_AS_CP_JAVASCRIPT_FILE_NAME, TOUTIAO_AS_CP_JAVASCRIPT_FUNCTION_NAME)
		return result

	def get_web_id(self):
		# 头条接口 cookie里面tt_webid信息
		r = requests.get(TOUTIAO_BASE_URL, headers=self.headers)
		return r.cookies.get('tt_webid')

	def get_news_with_category(self, category):
		self.category = category
		self.pre_request()
		return self.do_request()

	def get_news_hot(self):
		return self.get_news_with_category("news_hot")

	def get_all_news(self):
		return self.get_news_with_category("__all__")