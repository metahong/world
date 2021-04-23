
import configparser
import MySQLdb
import pandas as pd

config = configparser.ConfigParser() 
config.read('../datas.ini')
datas = config["mysql"]

connect_datas = {"host": datas["PUBLIC_IP"], "user": datas["USER"], "passwd": datas["PASSWORD"], "db": "world", "charset": "utf8"}
client = MySQLdb.connect(**connect_datas)
df = pd.read_sql("SELECT code, name, population FROM country", client) 
print(df.tail())
