# coding: utf-8

# HTTP 共享配置
HTTP_WEB_USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 " \
                      "(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"

# 头条 配置
TOUTIAO_BASE_URL = "https://www.toutiao.com"
TOUTIAO_FEEDS_URL_PATH = "/api/pc/feed/"
TOUTIAO_SCPIDER_INTERVAL = 100                                          # 每两次爬取之间的停留时间间隔 单位 毫秒
TOUTIAO_SCPIDER_COUNT = 100                                             # 每次爬取新闻条数
TOUTIAO_SIGNATURE_JAVASCRIPT_FILE_NAME = "src/common/new_sign.js"       # 头条_signature 字段生成的javascript代码文件
TOUTIAO_SIGNATURE_JAVASCRIPT_FUNCTION_NAME = "get_signature"            # 头条_signature 字段生成的javascript 函数入口名称
TOUTIAO_AS_CP_JAVASCRIPT_FILE_NAME = "src/common/new_sign.js"           # 头条 AS CP 字段生成的javascript 代码文件
TOUTIAO_AS_CP_JAVASCRIPT_FUNCTION_NAME = "get_as_cp"                    # 头条 AS CP 字段生成的javascript 函数入口名称



