import openpyxl
import pymysql

def addToDBGeneral(worksheet,col):
    column = worksheet.max_column
    time=2000
    index = 1
    for cases in list(worksheet.rows)[1:]:
        country_name = cases[0].value
        for x in range(1, column, 1):
            data = cases[x].value
            try:
                cls = 'insert into %s (area,`index`,time,%s)value ("%s",%d,"%s","%s")' % (
                    col,str(col),str(country_name), index, str(time), str(data))
                cursor.execute(cls)
            except Exception as e:
                print(e)
                print(cls)
                return
            time += 1
        time = 2000
        index+=1
    return


if __name__ == '__main__':
    # 链接sql
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='syn_asia', charset='utf8')
    cursor = db.cursor()

    wb = openpyxl.load_workbook('C:\\Users\\lizongqi\\Desktop\\亚洲国家乳制品归总数据处理四.xlsx')
    # 第二步：选取表单
    ws_names=['aging_degree','avg_gdp','birth_rate','milk_consume','milk_price','urbanization_level']


    for ws_name in ws_names:
        ws = wb[ws_name]
        addToDBGeneral(ws,ws_name)

    db.commit()
    db.close()
    # 关闭工作薄
    wb.close()