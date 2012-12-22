#!/usr/bin/python
# -*- coding: latin-1 -*-

import MySQLdb

def Fetch_Anno_PMID(pmid):
	
	conn = MySQLdb.connect(host="xxx.xxx.x.xxx", user="xxx", passwd="xxxx",db="HuPA")
        cursor = conn.cursor()
	
	#PubMed Indexed
	q="select * from PubMed_Index where pubmed='"+str(pmid)+"'"
	cursor.execute(q)
        data=cursor.fetchall()
	out_str="^^"
	eachSpt = str(data[0][2].tostring()).split('##')
	piAr=[]
	for piName in eachSpt:
		uniName = unicode(piName,'latin-1')
		q1="select pi_name,pi_address,email from Contributer_info where pi_name='"+uniName+"'"
		cursor.execute(q1)
		res1=cursor.fetchall()
		#############################################################################
		#In case PI is not there in contribution_info table, look in Pubmed_anno table
		#############################################################################
		if res1!=():
			piName=res1[0][0]
			piAdd=res1[0][1].tostring()
			piEmail=res1[0][2]
			piAr.append(piName+'##'+piEmail+'##'+piAdd)
		else:
			uniName = unicode(piName,'latin-1')
			q2="select PI,PI_int,PI_email from PubMed_Anno where PI='"+uniName+"'"
			cursor.execute(q2)
			res2=cursor.fetchall()
			if res2!=():
				piName=res2[0][0]
				piAdd=res2[0][1].tostring()
				piEmail=res2[0][2]
				piAr.append(piName+'##'+piEmail+'##'+piAdd)
			else:
				piName='None'
				piAdd='None'
				piAr.append('None##None##None')
	piInfo='::'.join([piName for piName in piAr if piName!='None##None##None'])
	if piInfo!='':
		for each in data:
			out_str=out_str+"@@"+str(each[0])+"$$"+str(each[1].tostring())+"$$"+str(each[2].tostring())+"$$"+str(each[3])+"$$"+str(each[4])+"$$"+str(each[5])+'$$'+piInfo
	else:
		for each in data:
			out_str=out_str+"@@"+str(each[0])+"$$"+str(each[1].tostring())+"$$"+str(each[2].tostring())+"$$"+str(each[3])+"$$"+str(each[4])+"$$"+str(each[5])+'$$'+'None##None##None'
	out_str=out_str.replace("^^@@","")
	cursor.close()
        conn.close()
	return out_str


#print Fetch_Anno_PMID('17189379')	
#print Fetch_Anno_PMID('12376572')	#17934176')	#17137333')	#17934176')	#'17137333')
