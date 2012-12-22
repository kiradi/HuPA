#!/usr/bin/python
import MySQLdb
def tes():
	conn = MySQLdb.connect(host="localhost", user="xxx", passwd="xxxx",db="HuPA")
	cursor = conn.cursor()
	piSql = "select pi_name,pi_address from Contributer_info"
	cursor.execute(piSql)
	rPi=cursor.fetchall()
	piDic={}
	for each in rPi:
		piName=each[0]
		piInst=each[1].tostring()
		piDic[piName]=piInst
	print piDic
	
tes()
