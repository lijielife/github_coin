import re
import datetime
import pytz
import pymysql
from operator import itemgetter

def read_file():
    list = []
    with open('github_url.text','r') as f:
         for line in f.readlines():
            str = line.strip()
            result = str.split('|')
            coin_id = result[0]
            coin_url = result[1]
            split_str = re.split('([/])', coin_url)
            dir = {}
            try:
                keyword = split_str[6]  # 关键字
            except:
                continue
            dir['coin_id'] = coin_id
            dir['keyword'] = keyword
            list.append(dir)
    return list


def utc_to_local(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%SZ'):
    local_tz = pytz.timezone('Asia/Chongqing')
    local_format = "%Y-%m-%d %H:%M"
    utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    time_str = local_dt.strftime(local_format)
    return time_str

def insert(sql):
    # 打开数据库连接
    db = pymysql.connect(host="118.190.175.23", port=3306, user='root',password="2MbANhiG0w623rEw", db="blockfuture", charset='utf8mb4')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    print('insert successful')

    # 关闭数据库连接
    db.close()

def query(sql):
    # 打开数据库连接
    db = pymysql.connect(host="118.190.175.23", port=3306, user='root',password="2MbANhiG0w623rEw", db="blockfuture")
    try:
        with db.cursor() as cursor:
            count = cursor.execute(sql)  # 影响的行数
            result = cursor.fetchall()  # 取出所有行
            db.commit()  # 提交事务
            return result
    except:
        db.rollback()  # 若出错了，则回滚

    finally:
        db.close()

def get_type(list,coin_id):
    n = 1
    myid = coin_id.split('&')[-1]
    sort_list = sorted(list, key=itemgetter('stargazers_count'), reverse=True)
    for i in sort_list:
        i['type'] = n
        i['coin_id'] = myid
        n = n+1
    return sort_list

def str_to_int(str):
    s =str.split(',')
    int2 = ''
    for i in s:
        int2 += i

    return int(int2)

if __name__ == '__main__':
    print(len(query('select coin_id from coin_people where coin_name = "BOScoin"') ) )


