# coding: utf-8

from functools import wraps
from json.decoder import JSONDecodeError
import os
import time
import math
import hashlib

import execjs
import requests


def url_add_query(url: str, query: str) -> str:
	if "?" in url:
		if url[-1] == "?":
			return url + query
		else:
			return url + "&" + query
	else:
		return url + "?" + query


def response_parse_json(func):
	@wraps(func)
	def parse_result(*args, **kwargs):
		result = func(*args, **kwargs)
		if isinstance(result, requests.Response):
			try:
				return result.json()
			except JSONDecodeError:
				return result.content
		else:
			return result

	return parse_result


def load_javascript(javascript_file_name, main_name, *args):
	# 执行javascript脚本里面的main函数

	load_js = execjs.get()
	if not os.path.exists(javascript_file_name):
		path = os.getcwd()
		javascript_file_name = os.path.join(path, javascript_file_name)
	content = open(javascript_file_name, encoding='utf-8', errors='ignore').read()
	ctx = load_js.compile(content)
	result = ctx.call(main_name, *args)
	return result


def get_ascp():
	result = {"as": "", "cp": ""}
	t = int(math.floor(time.time()))
	e = hex(t).upper()[2:]
	m = hashlib.md5()
	m.update(str(t).encode(encoding='utf-8'))
	i = m.hexdigest().upper()
	if len(e) != 8:
		result["as"] = '479BB4B7254C150'
		result["cp"] = '7E0AC8874BB0985'
		return result
	n = i[0:5]
	a = i[-5:]
	s = ''
	r = ''
	for o in range(5):
		s += n[o] + e[o]
		r += e[o + 3] + a[o]
	result["as"] = 'A1' + s + e[-3:]
	result["cp"] = e[0:3] + r + 'E1'
	return result
