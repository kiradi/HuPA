import MySQLdb

def Fetch_MailManager():
        conn = MySQLdb.connect(host="localhost", user="xxx", passwd="xxxx",db="HuPA")
        cursor = conn.cursor()
	fSQL = "SELECT * FROM mailManagerInfo"
	cursor.execute(fSQL)
	data=cursor.fetchall()
	ar=[]
	for each_d in data:
		id=each_d[0]
		pi_name=each_d[1]
		email_id=each_d[2]
		pubmed=each_d[3].tostring()
		inv_sent=each_d[4]
		cont_rep=each_d[5]
		if each_d[6] is not None:
			cont_comt=each_d[6].tostring()
		else:
			cont_comt=each_d[6]
		#print cont_comt
		ap_rep=each_d[7]
		if each_d[8] is not None:
			ap_comt=each_d[8].tostring()
		else:
			ap_comt=each_d[8]

		data_req_snt=each_d[9]
		cont_rep_to_data_req=each_d[10]
		if each_d[11] is not None:
			data_req_comt = each_d[11].tostring()
		else:
			data_req_comt = each_d[11]
		data_reci = each_d[12]
		ar.append(str(id)+'#'+pi_name+'#'+email_id+'#'+pubmed+'#'+str(inv_sent)+'#'+str(cont_rep)+'#'+str(cont_comt)+'#'+str(ap_rep)+'#'+str(ap_comt)+'#'+str(data_req_snt)+'#'+str(cont_rep_to_data_req)+'#'+str(data_req_comt)+'#'+str(data_reci))
	return '$$'.join(ar)
	#print '$$'.join(ar)

#Fetch_MailManager()
