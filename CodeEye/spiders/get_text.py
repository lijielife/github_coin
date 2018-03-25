import scrapy
import json
import read_url
from scrapy.selector import Selector
from scrapy.http import Request
from CodeEye.items import CodeeyeItem
import time

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Cookie': '_octo=GH1.1.1955068987.1507636359; _ga=GA1.2.1539611283.1507636359; user_session=iPAW63b7h304DMj_diZnPGiehAMW8yixocVPgSgKHw91lu_Q; __Host-user_session_same_site=iPAW63b7h304DMj_diZnPGiehAMW8yixocVPgSgKHw91lu_Q; logged_in=yes; dotcom_user=j785786058; tz=Asia%2FShanghai; _gid=GA1.2.1660851411.1521864305; _gh_sess=L29aeWxvNWlON2tnUXRGVmR4Y0xSeVVTV3BiTGxyTUVid0k0ZlNvaGtZUjdkemRsVithMXlTYkFiTlAzSGMwZEJUK1lzZlIzUFVoOHJ5U2ROWXVtSW1NWVhSclpmbkpMaGhQd0R6T3liWUxTVjZqaFduYmpOc3pLb29tVXpVWEQ5YXpwTFYwNWdzY2FtOVlBeUVOY2VtR2tiK3M3ZHRyc3BRQVVxcG9NUzE4eFhGUk5JWG43UHliNUhlRXN6eW5RSzUrS2F5bWJzbk1EeXpWWjFpRnBWYjd2aVRwMFM3UDVjZkpJVzRLZEhmODEzMisyT0VFSmc3akdRL3N1VEM5Sm5HQXQzUlUyMDNkbUZjNThKSmFjb2lzTy9ocGV0YmR0cnZmMTBOR3YzbFhxWWhoc0doSU5TZzc2K3RZeksvYU12dC9jK1NpaGlXd1pnSUd5cjNja3l5ZW8wS3h5blZTQVJkRWk0N3EvZHRyR3g3elluMy9OT1lIK0xJczlvbzVIZXNGOUFaMXUwNDhDTDBpcVAxaDU5b2VBYWFzVzV5emFBcnpHb21BaDVxWT0tLVU2eFhJR1I3UngyRTBPRW9kU1ZhTHc9PQ%3D%3D--5b32bf355da53644656e5b0a9970486fbc63562c',
'Host':'github.com',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}
class Myspider1(scrapy.Spider):
    info = []
    name = 'get_text'
    key_list = read_url.read_file()
    start_urls = []
    #print(key_list)
    for i in key_list:
        url = 'https://api.github.com/users/%s/repos?access_token=b418bc6bf92730ea09be5f0813eb143b24f0541c&%s' % (i['keyword'],i['coin_id'])
        start_urls.append(url)



    def parse(self, response):
        judge = []
        coin_id = response.url
        coin_id = str(coin_id)
        result = json.loads(response.body.decode())

        result = read_url.get_type(result,coin_id)
        for i in range(0, len(result)):
            yield Request(url=result[i]['html_url'], meta={'item': result[i]},callback=self.parse_page1)


    def parse_page1(self,response):
        selector = Selector(response)
        x = response.meta["item"]
       
        top_info = selector.xpath("//ul[@class='pagehead-actions']/li//a/text()").extract()
        mid_info = selector.xpath("//nav[@itemtype='http://schema.org/BreadcrumbList']//span/text()").extract()
        low_info = selector.xpath("//div[@class='stats-switcher-wrapper']//ul//li//span/text()").extract()
        try:
            x['Watch'] = top_info[2].strip()
        except:
            x['Watch'] = 0
        try:
            x['Star'] = top_info[5].strip()
        except:
            x['Star'] = 0
        try:
            x['Fork'] = top_info[8].strip()
        except:
            x['Fork'] = 0
        if ('Issues' in mid_info):
            index = mid_info.index('Issues')
            x['Issues'] = mid_info[index + 1]
        else:
            x['Issues'] = 0
        if ('Pull requests' in mid_info):
            index = mid_info.index('Pull requests')
            x['Pull_requests'] = mid_info[index + 1]
        else:
            x['Pull_requests'] = 0
        if (mid_info[-1].isdigit()):
            x['Projects'] = mid_info[-1]
        else:
            x['Projects'] = 0
        try:
            x['commits'] = low_info[0].strip()
        except:
            x['commits'] = 0
        try:
            x['branches'] = low_info[1].strip()
        except:
            x['branches'] = 0
        try:
            x['releases'] = low_info[2].strip()
        except:
            x['releases'] = 0
        #x['contributors'] = low_info[3].strip()  #contributors 有的时候获取不到
        s = x['description']

        if(s!= None):
            s.replace('\"', '\'')
        yield Request(url=x['html_url'] + '/contributors_size', meta={'item': x},
                      callback=self.parse_page2,headers=headers)

    def parse_page2(self,response):
        selector = Selector(response)
        x = response.meta["item"]
        a = selector.xpath("/html/body/a/span/text()").extract()[0].strip()
        x['contributors'] = a
        if (str(x['description']).find('"')):
            x['description'] = str(x['description']).replace(chr(34), chr(39))
        x['Watch']=read_url.str_to_int(str(x['Watch']))
        x['Star']=read_url.str_to_int(str(x['Star']))
        x['Fork']=read_url.str_to_int(str(x['Fork']))
        x['Issues']=read_url.str_to_int(str(x['Issues']))
        x['Pull_requests']=read_url.str_to_int(str(x['Pull_requests']))
        x['Projects']=read_url.str_to_int(str(x['Projects']))
        x['commits']=read_url.str_to_int(str(x['commits']))
        x['branches']=read_url.str_to_int(str(x['branches']))
        x['releases']=read_url.str_to_int(str(x['releases']))
        x['contributors']=read_url.str_to_int(str(x['contributors']))
        item = CodeeyeItem()
        #print(x['type'])
        # sqlstr = 'select coin_id from coin_people where coin_name = "%s"' % x['owner']['login']
        # print(sqlstr)
        # coin_id = read_url.query(sqlstr)
        # print(coin_id)
        #sql_insert = 'insert into coin_github(coin_id,coin_name,name,base_url,type,description,language,core_code,watch,star,fork,issues,pull_requests,projects,commits,branches,releases,contributors,updated_at,created_at,pushed_at) values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (
        item['coin_id']=x['coin_id']
        item['coin_name'] = x['owner']['login']
        item['name'] = x['name']
        item['base_url'] = x['owner']['html_url']
        item['type'] =  x['type']
        item['description'] =x['description']
        item['language'] = x['language']
        item['core_code'] =  x['html_url']
        item['watch'] = x['Watch']
        item['star'] =x['Star']
        item['fork'] =x['Fork']
        item['issues'] = x['Issues']
        item['pull_requests'] =x['Pull_requests']
        item['projects'] =x['Projects']
        item['commits'] =x['commits']
        item['branches']=x['branches']
        item['releases'] = x['releases']
        item['contributors'] =x['contributors']
        item['updated_at'] =read_url.utc_to_local(x['updated_at']),
        item['created_at'] = read_url.utc_to_local(x['created_at']),
        item['pushed_at'] = read_url.utc_to_local(x['pushed_at'])
        return item
        #read_url.insert(sql_insert)











