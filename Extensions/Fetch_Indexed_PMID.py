#!/usr/bin/python

import MySQLdb

def Fetch_Indexed_PMID():
	
	conn = MySQLdb.connect(host="localhost", user="xxx", passwd="xxxx",db="HuPA")
        cursor = conn.cursor()
	
	#PubMed Indexed
	q="select * from PubMed_Index, Entry_Log where PubMed_Index.status='Indexed' and PubMed_Index.pubmed=Entry_Log.pubmed"
	cursor.execute(q)
        data=cursor.fetchall()
	out_str="^^"
	for each in data:
		out_str=out_str+"@@"+str(each[0])+"$$"+str(each[1].tostring())+"$$"+str(each[2].tostring())+"$$"+str(each[3])+"$$"+str(each[4])+"$$"+str(each[5])+"$$"+str(each[6])+"$$"+str(each[9])+"$$"+str(each[10])

	out_str=out_str.replace("^^@@","")

	cursor.close()
        conn.close()

	return out_str

#a=Fetch_Indexed_PMID()
#print a
