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
	journal=data[0][2]
	pub_date = data[0][3]
	PI = data[0][4]	#.split(',')[0]
	drPi = data[0][4].split(',')[0]
	PI_email = data[0][5]
	#result=author.split(',')[0]+'#'+title+'#'+journal+'#'+pub_date+'#'+PI+'#'+PI_email+'#'+str(pmid)+'#'+PI_dr
	#Get PI's all approved Article and send it for email page
	#
	###########################################################################################################
	q1="SELECT PubMed_Index.pubmed,PubMed_Index.authors,PubMed_Index.title,PubMed_Index.journal,PubMed_Index.pub_date,PubMed_Anno.PI,PubMed_Anno.PI_email FROM PubMed_Index INNER JOIN PubMed_Anno ON PubMed_Index.pubmed=PubMed_Anno.pubmed WHERE PubMed_Anno.PI='"+str(PI)+"' and PubMed_Anno.status ='"+str('Approved')+"'"
	cursor.execute(q1)
	data1=cursor.fetchall()
	Ar=[]
	pmidAr=[]
	for each in data1:
		pmid=str(each[0])
		fauthors=each[1].tostring().split('##')[1]
		articleTit=each[2].tostring()
		journalName=each[3]
		pubDate=each[4]
		pi= each[5]
		email=''.join(each[6].lower().split())
		pmidAr.append(pmid)
		Ar.append(fauthors+'#'+articleTit+'#'+journalName+'#'+pubDate)
	pmids = [','.join(pmidAr)]
	piAr=[pi,drPi]
	piEid=[email]
	pubInfo=['$$'.join(Ar)]
	piPubInfo= '@@@'.join(piAr+piEid+pubInfo+pmids)
	cursor.close()
	conn.close()
	#print piPubInfo 
	return piPubInfo
#Fetch_Email_Info('16083295')
