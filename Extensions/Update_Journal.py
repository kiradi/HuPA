#!/usr/bin/python

import MySQLdb

def Update_Journal(journal, pri_id, username):
	
	conn = MySQLdb.connect(host="localhost", user="xxx", passwd="xxxx",db="HuPA")
        cursor = conn.cursor()
	
	#PubMed Indexed
	q="update journal_ctrl set status='checked', author='"+str(username)+"' where pri_id="+str(pri_id)
	cursor.execute(q)
        conn.commit()
	cursor.close()
        conn.close()

	return "-"
