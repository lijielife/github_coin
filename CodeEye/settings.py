# -*- coding: utf-8 -*-

# Scrapy settings for Codeeye project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'CodeEye'

SPIDER_MODULES = ['CodeEye.spiders']
NEWSPIDER_MODULE = ['CodeEye.spiders']


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Codeeye (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 30
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Codeeye.middlewares.CodeeyeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Codeeye.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Codeeye.pipelines.CodeeyePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False
# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
BOT_NAME = 'mysql'

SPIDER_MODULES = ['CodeEye.spiders']
NEWSPIDER_MODULE = 'CodeEye.spiders'
MYSQL_HOST = '118.190.175.23'
MYSQL_PORT = 3306
MYSQL_DBNAME = 'blockfuture'
MYSQL_USER = 'root'
MYSQL_PASSWD = '2MbANhiG0w623rEw'
#RETRY_HTTP_CODES = [429]
RETRY_TIMES = 0
ITEM_PIPELINES = {
    'CodeEye.pipelines.CodeeyePipeline': 301,
}

DOWNLOADER_MIDDLEWARES = {
#    'youx.middlewares.MyCustomDownloaderMiddleware': 543,
    'CodeEye.middlewares.CodeeyeSpiderMiddleware': 700,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
}
UPPOOL = [
{"ipaddr": "60.167.133.54:43159"},
{"ipaddr": "183.144.202.77:20004"},
{"ipaddr": "117.86.16.219:37770"},
{"ipaddr": "125.104.242.95:42879"},
{"ipaddr": "49.85.1.91:28615"},
{"ipaddr": "125.104.237.244:23004"},
{"ipaddr": "115.202.68.80:26460"},
{"ipaddr": "117.86.12.125:43866"},
{"ipaddr": "218.73.130.175:30155"},
{"ipaddr": "49.64.22.17:26886"}
 ]
COOKIES_ENABLED = False

IPPOOL = [
     "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
 ]
# 配置下载中间件的连接信息
DOWNLOADER_MIDDLEWARES = {
     #'scrapy.contrib.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
     #'modetest.middlewares.IPPOOlS' : 125,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 2,
    'CodeEye.middlewares.Uamid': 1,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
    'CodeEye.middlewares.IPPOOlS' : 125
}
