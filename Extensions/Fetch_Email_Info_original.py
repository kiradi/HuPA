#!/usr/bin/python

import MySQLdb

def Fetch_Email_Info(pmid):
	conn = MySQLdb.connect(host="localhost", user="xxx", passwd="xxxx",db="HuPA")
	cursor = conn.cursor()
	#q = "SELECT *  FROM PubMed_Index WHERE pubmed="+str(pmid)
	q="SELECT PubMed_Index.authors,PubMed_Index.title,PubMed_Index.journal,PubMed_Index.pub_date,PubMed_Anno.PI,PubMed_Anno.PI_email FROM PubMed_Index INNER JOIN PubMed_Anno ON PubMed_Index.pubmed=PubMed_Anno.pubmed WHERE PubMed_Index.pubmed="+str(pmid)
	cursor.execute(q)
	data=cursor.fetchall()
	author=data[0][0].tostring().split('##')[1]
	title = data[0][1].tostring()
	journal=data[0][2]	#.tostring()
	pub_date = data[0][3]	#.tostring()
	PI = data[0][4]	#.split(',')[0]
	PI_dr = data[0][4].split(',')[0]		#.tostring()
	PI_email = data[0][5]	#.tostring()
	result=author.split(',')[0]+'#'+title+'#'+journal+'#'+pub_date+'#'+PI+'#'+PI_email+'#'+str(pmid)+'#'+PI_dr
	print data1
	cursor.close()
	conn.close()
	print result
	#return result
#Fetch_Email_Info(16083281)
