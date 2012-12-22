#!/usr/bin/python

import MySQLdb

def Fetch_Edit_Anno_PMID(pmid):
	
	conn = MySQLdb.connect(host="localhost", user="xxx", passwd="xxxx",db="HuPA")
        cursor = conn.cursor()
	
	#PubMed Indexed
	q="select * from Entry_Log, PubMed_Anno where PubMed_Anno.pubmed=Entry_Log.pubmed and Entry_Log.status='Annotated' and PubMed_Anno.pubmed="+str(pmid)
	cursor.execute(q)
        data=cursor.fetchall()
	out_str=""
	for each in data:
		out_str=str(each[2])+"$$"+str(each[3])+"$$"+str(each[7])+"$$"+str(each[8])+"$$"+str(each[9])+"$$"+str(each[10].tostring())+"$$"+str(each[11])+"$$"+str(each[12])+"$$"+str(each[13])+"$$"+str(each[14])+"$$"+str(each[15])+"$$"+str(each[16])+"$$"+str(each[17])+"$$"+str(each[18])+"$$"+str(each[19])+"$$"+str(each[20])+"$$"+str(each[21])

	cursor.close()
        conn.close()
	
	return out_str

#print Fetch_Edit_Anno_PMID(16457587)
