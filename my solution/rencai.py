# -*- coding: utf-8 -*-
"""
新道人才 
"""
import requests
import json
import xlwt
import random
import pymysql

headers = {
    # 'Referer':'http://talents.seentao.com/',   #需要根据实际 ip 修改采集页面IP
    'Referer': '${zuulIp}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
postData = {
    'cityCode': '',  # 城市
    'position': '',  # 职位
    'salary': '',  # 月薪范围,仅限 页面展示的 月薪范围 内容,作为可选项.
    'experience': '',  # 工作年限
    'education': '',  # 学历
    'pageIndex': '1',  # 起始页
    'pageSize': '5'  # 查询总条数
}


def get_page(postUrl):
    try:
        rsp = requests.post(postUrl, data=postData, headers=headers)
        if (rsp.status_code == 200):
            print('数据源获取成功')
        rsp.raise_for_status()
        rsp.encoding = rsp.apparent_encoding
        return json.loads(rsp.text)
    except Exception as e:
        print(e)


postUrl = '${zuulIp}/talents/talents.position.selectpositionbyparam'  # 采集的 请求接口,用于获取数据
rsps = get_page(postUrl)

rztJson = rsps['result']

# 链接sql
db = pymysql.connect(host='10.10.16.39', port=3306, user='root', passwd='ufida!@#', db='spider', charset='utf8')
# 优化之后 配置不可见
# db = pymysql.connect(${dbConnect})
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 先清除 之前 采集的 旧数据
try:
    cls = "delete from rencai where teach_class_id = '${teachClassId}' and member_id = '${memberId}'"
    cursor.execute(cls)
except:
    db.rollback()
    print("数据清除 失败!")
data = []

# 注意 下面的格式， Python 脚本尤其注意 缩进 
for i in range(len(rztJson)):
    try:
        salary = '面议' if 'salaryStart' not in rztJson[i] else str(rztJson[i]['salaryStart']) + '-' + str(
            rztJson[i]['salaryEnd'])
        rzt = (
        '${teachClassId}', '${memberId}', rztJson[i]['posName'], rztJson[i]['company'], rztJson[i]['cityCode'], salary,
        rztJson[i]['releaseTime']
        )
        data.append(rzt)
    except:
        print("-----error 采集失败")
try:
    print("-----------开始采集------------")
    cursor.executemany("INSERT INTO rencai VALUES(%s,%s,%s,%s,%s,%s,%s)", data)
    db.commit()
    print("-----------采集成功------------")
except:
    db.rollback()
    print('sql error 采集失败')
db.close()
