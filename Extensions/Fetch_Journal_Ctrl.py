#!/usr/bin/python

import MySQLdb

def Fetch_Journal_Ctrl(journal):
	
	conn = MySQLdb.connect(host="localhost", user="root", passwd="changeme",db="HuPA")
        cursor = conn.cursor()
	
	#PubMed Indexed
	q="select * from journal_ctrl where journal_name='"+str(journal)+"'"
	cursor.execute(q)
        data=cursor.fetchall()
	out_str="^^"
	for each in data:
		out_str=out_str+"@@"+str(each[0])+"$$"+str(each[1])+"$$"+str(each[2])+"$$"+str(each[3])+"$$"+str(each[4])+"$$"+str(each[5])+"$$"+str(each[8])

	out_str=out_str.replace("^^@@","")

	cursor.close()
        conn.close()

	return out_str
