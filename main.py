# coding: utf-8


#  所有城市 https://www.toutiao.com/stream/widget/local_weather/city/
#  精彩图片 https://www.toutiao.com/api/pc/hot_gallery/?widen=1
#  24小时新闻 https://www.toutiao.com/api/pc/realtime_news/
#  头条feed流 https://www.toutiao.com/api/pc/feed/?max_behot_time=1582708956&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1C5BE65C6C3A02&cp=5E56B3FAB0C22E1&_signature=ZH6tbgAgEBBdgH.Ve0hm2WR-7HAADosmm7kMnTllTqnq-ylE4DEVae16mP6BVu5xxorUBktt2C6EzYutCrbQrtGFT0dz5nOb0Gtho7EnBM6xlnoj35Z98yk7wcELwpAzfL0
#  头条feed流 https://www.toutiao.com/api/pc/feed/?min_behot_time=1582708704&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1B5DE6506038BC&cp=5E568308ABFCBE1&_signature=1cfpRgAgEBDsOTv9mWYUrNXHqFAAIuaqVizG5X1aPh6Cz--w-8CoDOooMKyiqGwKBleslYEDn46ZXo7QtNngBZSeVUmRUxXsifNaeZnWWvDAmItvqAUB9QHGZs2tV7vNivb
#  头条feed流 https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1958EB57623B2D&cp=5E56E35B720D8E1&_signature=BaanuAAgEBA8WHUD2-QTFAWm5qAAFv2jjTfs0nuDsi3zr2X3f7F1T10pQmNXm0rAQgfP9ctgznvAxVzqP5wUn31DCxssEmGL.tmfkkUiZPQi.9hYAo3dg4farnaPI2nXl8b
#            https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A115AEF5D6E3C67&cp=5E56C32C76679E1&_signature=AM9IyAAgEBA5MZpzgixKmwDPCdAAF6f


from src.crawler.toutiao_web import SpiderTouTiaoWeb
from src.crawler.toutiao_app import SpiderTouTiaoApp, SpiderTouTiaoAppFeedsDetail


def main():
	s = SpiderTouTiaoWeb()
	r = s.get_all_news()

	tt_app = SpiderTouTiaoApp()
	result = tt_app.get_all_news()
	gid_and_gsr_list = tt_app.analytics_news(result)
	print(gid_and_gsr_list)
	for gid, gsr in gid_and_gsr_list:
		tt_feed_detail = SpiderTouTiaoAppFeedsDetail(gid, gsr)
		feed_detail = tt_feed_detail.do_request()
		print(feed_detail)


if __name__ == "__main__":
	main()