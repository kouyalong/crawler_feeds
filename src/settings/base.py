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

# 头条APP 配置
TOUTIAO_APP_FEED_URL_V2 = "http://is.snssdk.com/api/news/feed/v2/"      # 头条app v2版本feeds流接口
TOUTIAO_APP_FEED_CATEGORY = \
    "https://is.snssdk.com/article/category/get_subscribed/" \
    "v4/?iid=45032656046&aid=13&version_code=693"                       # 头条app 获取feeds流 分类接口
TOUTIAO_APP_FEED_DETAIL = \
    "http://a3.pstatp.com/article/content/21/1/" \
    "{group_id}/{group_source}/1/0/?"                                   # 头条app feeds流 详情
TOUTIAO_APP_DEFAULT_CATEGORY = \
    ['关注', '__all__', 'news_hot', 'news_local', 'nineteenth',
     'video', '组图', 'news_entertainment', 'question_and_answer',
     'news_tech', 'news_car', 'news_finance', 'news_military',
     'live', 'news_sports', 'news_world', 'news_health',
     'news_house', '冬奥会', 'traditional_culture', 'news_history',
     'news_regimen', 'funny', 'news_food', 'emotion', 'movie',
     'news_baby', 'weitoutiao', 'fangxingou', 'NBA', '漫画']              # 头条app feeds流默认分类
