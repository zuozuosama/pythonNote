import pymysql
import math

def find():
    # 链接sql
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='syndata', charset='utf8')
    cursor = db.cursor()
    try:
        cls = 'SELECT c.*,b.avg_price FROM (SELECT *,AVG(price) as avg_price ' \
              'FROM syn_all_data WHERE area IN (SELECT area FROM ( SELECT area, count( 1 ) ' \
              'AS count FROM syn_all_data WHERE price IS NOT NULL GROUP BY area HAVING count >= 9 ) a) ' \
              'and price is not NULL GROUP BY area) b LEFT JOIN syn_all_data c on b.area=c.area WHERE c.price is null;'
        cursor.execute(cls)
        data = cursor.fetchall()
        print(data)
        # print(type(data))
        for row in data:
            length = len(row)
            id = row[0]
            avgPrice = row[length-1]
            update_sql = 'update syn_all_data_process set price = ' + str(avgPrice) + ' where id = ' + str(id)
            print(update_sql)
            cursor.execute(update_sql)

    except Exception as e:
        print(e)
        print(cls)
    finally:
        cursor.close()
        # 一定要提交
        db.commit()
        db.close()

def update():
    # 链接sql
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='syndata', charset='utf8')
    cursor = db.cursor()
    try:
        cls = 'SELECT * FROM syn_all_data_process WHERE area IN ( SELECT area FROM( SELECT area, count( 1 ) AS count FROM syn_all_data_process WHERE price IS NOT NULL GROUP BY area HAVING count >= 9 ) a );'
        cursor.execute(cls)
        data = cursor.fetchall()
        # print(data)
        # print(type(data))
        x = 1
        for row in data:
            length = len(row)
            id = row[0]
            mod = x / 18
            mod = math.ceil(mod)
            update_sql = 'update syn_all_data_process set `index` = ' + str(mod) + ' where id = '+ str(id)
            print(update_sql)
            cursor.execute(update_sql)
            x+=1

    except Exception as e:
        print(e)
        print(update_sql)
    finally:
        cursor.close()
        # 一定要提交
        db.commit()
        db.close()

if __name__ == '__main__':
    update()
