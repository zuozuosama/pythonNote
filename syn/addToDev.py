import openpyxl
import pymysql

def addToDBGeneral(worksheet,col):
    column = worksheet.max_column
    time=2000
    for cases in list(worksheet.rows)[1:]:
        country_name = cases[0].value
        for x in range(1, column, 1):
            data = cases[x].value
            try:
                cls = 'insert into %s (area,time,price)value ("%s","%s","%s")' % (
                    col,str(country_name), str(time), str(data))
                cursor.execute(cls)
            except Exception as e:
                print(e)
                print(len(country_name))
                print(cls)
                return
            time += 1
        time = 2000
    return


if __name__ == '__main__':
    wb = openpyxl.load_workbook('C:\\Users\\lizongqi\\Desktop\\牛奶价格.xlsx')
    # 第二步：选取表单
    ws = wb['price']
    # 链接sql
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='syndata', charset='utf8')
    cursor = db.cursor()

    addToDBGeneral(ws,'milk_price')

    db.commit()
    db.close()
    # 关闭工作薄
    wb.close()