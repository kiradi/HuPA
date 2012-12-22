#!/usr/bin/python

import MySQLdb

def Fetch_Annotated_PMID():
	
	conn = MySQLdb.connect(host="192.168.5.215", user="root", passwd="changeme",db="HuPA")
        cursor = conn.cursor()
	
	#PubMed Indexed
	q="select * from PubMed_Index, Entry_Log, PubMed_Anno where PubMed_Index.status='Annotated' and PubMed_Index.pubmed=Entry_Log.pubmed and PubMed_Index.pubmed=PubMed_Anno.pubmed and PubMed_Anno.pubmed=Entry_Log.pubmed and Entry_Log.status='Annotated' and PubMed_Anno.status='Annotated'"
	cursor.execute(q)
        data=cursor.fetchall()
	out_str="^^"
	for each in data:
		out_str=out_str+"@@"+str(each[0])+"$$"+str(each[1])+"$$"+str(each[2])+"$$"+str(each[3])+"$$"+str(each[4])+"$$"+str(each[5])+"$$"+str(each[8])+"$$"+str(each[9])+"$$"+str(each[13])+"$$"+str(each[14])+"$$"+str(each[15])+"$$"+str(each[16])+"$$"+str(each[21])+"$$"+str(each[26])

	out_str=out_str.replace("^^@@","")

	cursor.close()
        conn.close()

	return out_str
