# coding: utf-8

import time


from src.settings.base import (
	TOUTIAO_APP_FEED_URL_V2,
	TOUTIAO_APP_FEED_DETAIL,
	TOUTIAO_APP_DEFAULT_CATEGORY,
)
from src.crawler.spider import Spider

INIT_TIME = int(time.time())


class SpiderTouTiaoAppFeedsDetail(Spider):
	# 头条手机客户端 爬取feed详情

	def __init__(self, group_id, group_source, query=None, headers=None):
		self.query = query or {}
		self.headers = headers or {}
		url = TOUTIAO_APP_FEED_DETAIL.format(group_id=group_id, group_source=group_source)
		super(SpiderTouTiaoAppFeedsDetail, self).__init__(url, self.query, self.headers)

	def fake_url_args(self):
		tt_app_query = {
			"iid": "37457543399",
			"device_id": "55215909025",
			"ac": "wifi",
			"channel": "tengxun2",
			"aid": "13",
			"app_name": "news_article",
			"version_code": "682",
			"version_name": "6.8.2",
			"device_platform": "android"
		}
		tt_app_query.update(self.query)
		self.query = tt_app_query

	def fake_headers(self):
		pass

	def get_news_detail(self, category):
		self.pre_request()
		return self.do_request()


class SpiderTouTiaoApp(Spider):
	# 头条手机客户端 爬取feeds流

	def __init__(self, query=None, headers=None):
		self.query = query or {}
		self.headers = headers or {}
		self.category = "__all__"
		self.last_time = INIT_TIME
		super(SpiderTouTiaoApp, self).__init__(TOUTIAO_APP_FEED_URL_V2, self.query, self.headers)

	def fake_url_args(self):
		local_time = int(time.time())
		tt_app_query = {
			'category': self.category,
			'refer': '1',                                               ###???，固定值1
			'count': '20',                                              ####返回数量，默认为20
			'min_behot_time': self.last_time,                           ####上次请求时间的时间戳，例:1491981025
			'last_refresh_sub_entrance_interval': local_time,           #####本次请求时间的时间戳，例:1491981165
			'loc_time': local_time,                                     ###本地时间
			'iid': '1234876543',                                        ###某个唯一 id，长度为10
			'device_id': '42433242851',                                 ###设备id，长度为11
			'abflag': '3',
			'ssmix': 'a',
			'language': 'zh',
			'openudid': '1b8d5bf69dc4a561',                             ####某个唯一id，长度为16
		}
		tt_app_query.update(self.query)
		self.query = tt_app_query
		global INIT_TIME
		INIT_TIME = local_time

	def fake_headers(self):
		pass

	def get_news_with_category(self, category):
		if category in TOUTIAO_APP_DEFAULT_CATEGORY:
			self.category = category
			self.pre_request()
			return self.do_request()

	def get_news_hot(self):
		return self.get_news_with_category("news_hot")

	def get_all_news(self):
		return self.get_news_with_category("__all__")

	def analytics_news(self, news):
		# 解析news 返回group_id 以及 group_source
		return [(new["group_id"], new["group_source"]) for new in news["data"]]
