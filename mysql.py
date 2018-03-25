import pymysql


def insert(sql):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "coin",charset='utf8mb4')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()


    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    print('添加成功')


    # 关闭数据库连接
    db.close()

def query(stri):
    # 打开数据库连接
    i=1
    db = pymysql.connect(host="118.190.175.23", port=3306, user='root',password="2MbANhiG0w623rEw", db="blockfuture")
    try:
        with db.cursor() as cursor:
            sql = stri
            count = cursor.execute(sql)  # 影响的行数
            #print(count)
            result = cursor.fetchall()  # 取出所有行
            for i in list(result):  # 打印结果
                if i[1] == '':
                    continue
                #print(i[0])
                fh = open('github_url.text', 'a')
                fh.write(str(i[0]))
                fh.write('|')
                fh.write(i[1])
                fh.write('\n')

    except:
        db.rollback()  # 若出错了，则回滚

    finally:
        db.close()
        fh.close()

