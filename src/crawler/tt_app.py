# coding: utf-8

import requests
import re
import json
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import pandas as pd

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  ###禁止提醒SSL警告


def ttapi(url):  ####APP模式
	channel = re.search('ch/(.*?)/', url).group(1)
	s = requests.session()
	headers = {
		'Accept': 'image/webp,image/*;q=0.8',
		'User-Agent': 'News/6.9.8.36 CFNetwork/975.0.3 Darwin/18.2.0',
		'Accept-Language': 'zh-cn'
	}
	s.headers.update(headers)
	df = pd.DataFrame(columns=(
		'abstract 简报', 'title 标题', 'keywords 关键词', 'read_count 阅读量', 'share_count 分享数量',
		'ban_comment 可评论', 'publish_time 推送时间', 'share_url url 链接', 'user_info_name 用户名',
		'user_id 用户 id', 'description 用户描述', 'user_verified 官方账号', 'time 抓取时间', 'category 频道'
	))
	t2 = int(time.time()) - 500
	x = 0
	for i in range(10):  ###爬取页数
		time.sleep(3)
		t = int(time.time())
		params = {
			'category': channel,  ###频道名
			'refer': '1',  ###???，固定值1
			'count': '20',  ####返回数量，默认为20
			'min_behot_time': t2,  ####上次请求时间的时间戳，例:1491981025
			'last_refresh_sub_entrance_interval': t - 10,  #####本次请求时间的时间戳，例:1491981165
			'loc_time': int(t / 1000) * 1000,  ###本地时间
			'latitude': '',  ###经度
			'longitude': '',  ###纬度
			'city': '',  ###当前城市
			'iid': '1234876543',  ###某个唯一 id，长度为10
			'device_id': '42433242851',  ###设备id，长度为11
			'abflag': '3',
			'ssmix': 'a',
			'language': 'zh',
			'openudid': '1b8d5bf69dc4a561',  ####某个唯一id，长度为16

		}
		url = 'http://is.snssdk.com/api/news/feed/v51/'
		app = s.get(url=url, params=params, verify=False).json()
		print(app)
		t2 = t - 10
		total_number = app['total_number']
		# print(total_number)
		for j in range(0, total_number):
			content = json.loads(app['data'][j]['content'])
			try:
				abstract = content['abstract']  ##简报
			except:
				abstract = ''
			try:
				title = content['title']  ##标题
			except:
				title = ''
			try:
				keywords = content['keywords']  ##关键词
			except:
				keywords = ''
			try:
				read_count = content['read_count']  ##阅读量
			except:
				read_count = ''
			try:
				share_count = content['share_count']  ##分享数量
			except:
				share_count = ''
			try:
				ban_comment = content['ban_comment']  ###是否可以评论，0为可评论，1不可评论
			except:
				ban_comment = ''
			try:
				publish_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(content['publish_time']))  ##推送时间
			except:
				publish_time = ''
			try:
				share_url = content['share_url']  ###分享 url 链接
			except:
				share_url = ''
			try:
				user_info_name = content['user_info']['name']  ##用户名
			except:
				user_info_name = ''
			try:
				user_id = content['user_info']['user_id']  ##用户 id
			except:
				user_id = ''
			try:
				description = content['user_info']['description']  ##用户描述
			except:
				description = ''
			try:
				user_verified = content['user_info']['user_verified']  ###是否官方账号
			except:
				user_verified = ''

			nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
			df.loc[x] = [abstract, title, keywords, read_count, share_count, ban_comment,
			             publish_time, share_url, user_info_name, user_id, description,
			             user_verified, nowtime, channel]
			x = x + 1

	df.to_csv('tt.csv', index=False, encoding="GB18030")
	s.close()


if __name__ == '__main__':
	url = 'https://www.toutiao.com/ch/news_sports/'
	ttapi(url)
	print()

"""
http://is.snssdk.com/api/news/feed/v2/
https://is.snssdk.com/article/category/get_subscribed/v4/?iid=45032656046&aid=13&version_code=693

http://a3.pstatp.com/article/content/21/1/{}/{}/1/0/?iid=37457543399&device_id=55215909025&ac=wifi&channel=tengxun2&aid=13&app_name=news_article&version_code=682&version_name=6.8.2&device_platform=android

http://a3.pstatp.com/article/content/21/1/6797950930609242631/2/1/0/?iid=37457543399&device_id=55215909025&ac=wifi&channel=tengxun2&aid=13&app_name=news_article&version_code=682&version_name=6.8.2&device_platform=android
"""

