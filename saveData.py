#coding:utf-8
import pickle
import pymysql
int_nums=[1,2,3,4,5]
#序列化
with open("12222030.dat","wb") as f:
    pickle.dump(int_nums,f)
#反序列化
with open("12222030.dat","rb") as g:
    load_nums = pickle.load(g)
    print(load_nums)
sql1 = """create table cluster(
       id int,
       name varchar(20))"""
sql2 = """
       insert into cluster values
       (1111,"dws-test");
       """
table_name = "cluster"
try:
    conn = pymysql.connect("127.0.0.1","root","123456","pyTest")
    cursor = conn.cursor()
    cursor.execute("drop table  if exists  cluster;")
    cursor.execute(sql1)
    cursor.execute(sql2)
    conn.commit()
    cursor.execute("select * from cluster;")
    values = cursor.fetchall()
    print(values)
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()
    print("Close connection sucess.")

