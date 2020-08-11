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
                cls = 'insert into %s (country_name,time,data)value ("%s","%s","%s")' % (
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
    wb = openpyxl.load_workbook('C:\\Users\\lizongqi\\Desktop\\论文数据.xlsx')
    # 第二步：选取表单
    sh = wb['api']
    # 链接sql
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='syndata', charset='utf8')
    cursor = db.cursor()

    wsName = ['人均GDP','城镇化水平','粗出生率','65和65岁以上人口比重']
    cols = ['avg_gdp','urbanization_level','birth_rate','aging_degree']
    for i,x in enumerate(wsName):
        ws = wb[x]
        addToDBGeneral(ws,cols[i])
    # addToDB(sh)
    # addToDB(sh1)
    # selectAndWriteExcel()

    db.commit()
    db.close()
    # 关闭工作薄
    wb.close()