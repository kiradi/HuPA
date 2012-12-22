#!/usr/bin/python

import MySQLdb
import time

def Contacted_PMID(pmids, username):
	present_time=time.localtime()
        ###print present_time
        year=present_time[0]
        date=present_time[2]
        month=present_time[1]
        hour=present_time[3]
        minute=present_time[4]
        seconds=present_time[5]
        final_date=str(month)+"/"+str(date)+"/"+str(year)
        final_time=final_date+" "+str(hour)+":"+str(minute)+":"+str(seconds)
	
	conn = MySQLdb.connect(host="xxx.xx.xx.xxx", user="xxx", passwd="xxxx",db="HuPA")
        cursor = conn.cursor()
	pmidList=pmids.split(',')
	#PubMed Indexed
	for pmid in pmidList:
		q="update PubMed_Index set status='Contacted' where pubmed="+str(pmid)
		cursor.execute(q)
		q="insert into  Entry_Log values (0, '"+str(pmid)+"', '"+str(username)+"', '"+str(final_time)+"',  'PubMed_Mail', 'Contacted')"
        	cursor.execute(q)
		q="update PubMed_Anno set status='Contacted' where pubmed="+str(pmid)
        	cursor.execute(q)

	conn.commit()
	cursor.close()
        conn.close()

	return "done"
