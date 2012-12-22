#!/usr/bin/python

import MySQLdb

def Fetch_Annotated_PMID():
	
	conn = MySQLdb.connect(host="xxx.xxx.x.xxx", user="xxx", passwd="xxxx",db="HuPA")
        cursor = conn.cursor()
	
	#PubMed Indexed
	q="select PubMed_Index.pubmed,PubMed_Index.title,PubMed_Index.authors,PubMed_Index.journal,PubMed_Index.pub_date,PubMed_Index.status,Entry_Log.author,Entry_Log.date_ad,PubMed_Anno.exp_type,PubMed_Anno.PI,PubMed_Anno.PI_email,PubMed_Anno.PI_int,PubMed_Anno.ms_instrument,PubMed_Anno.sample_source,PubMed_Anno.contribution_status,PubMed_Anno.ion_mode,PubMed_Anno.frag_mode,PubMed_Anno.data_count,PubMed_Anno.in_gel from PubMed_Index, Entry_Log, PubMed_Anno where PubMed_Index.status='Annotated' and PubMed_Index.pubmed=Entry_Log.pubmed and PubMed_Index.pubmed=PubMed_Anno.pubmed and PubMed_Anno.pubmed=Entry_Log.pubmed and Entry_Log.status='Annotated' and PubMed_Anno.status='Annotated'"
	cursor.execute(q)
        data=cursor.fetchall()
	out_str="^^"
	for each in data:
		out_str=out_str+"@@"+str(each[0])+"$$"+str(each[1].tostring())+"$$"+str(each[2].tostring())+"$$"+str(each[3])+"$$"+str(each[4])+"$$"+str(each[5])+"$$"+str(each[6])+"$$"+str(each[7])+"$$"+str(each[8])+"$$"+str(each[9])+"$$"+str(each[10])+"$$"+str(each[11].tostring())+"$$"+str(each[12])+"$$"+str(each[13])+"$$"+str(each[14])+"$$"+str(each[15])+"$$"+str(each[16])+"$$"+str(each[17])+"$$"+str(each[18])
	out_str=out_str.replace("^^@@","")
	cursor.close()
        conn.close()

	return out_str
