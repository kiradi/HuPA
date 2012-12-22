#!/usr/bin/python

import MySQLdb
import time
def Add_PMID_Ann(search_engine, PI_int, ion_mode, PI, vendor, data_count, ms_instrument, label_tech, frag_mode, username, source_type, PI_email, red_alk, pmid, sample_source, in_gel):
	li = ['LIST']
	if type(ms_instrument)==type(li):
		ms_instrument=', '.join(ms_instrument)
	if  type(frag_mode)==type(li):
		frag_mode =', '.join(frag_mode)
	if type(vendor)==type(li):
		vendor = ', '.join(vendor)
	if type(search_engine)==type(li):
		search_engine=', '.join(search_engine)
	if type(ion_mode)==type(li):
		ion_mode=', '.join(ion_mode)

	conn = MySQLdb.connect(host="192.168.5.232", user="xxx", passwd="xxxx",db="HuPA")
        cursor = conn.cursor()
	# To check Whether PI is all ready contibuted or not
	piCheckSql ="SELECT pi_name FROM Contributer_info WHERE pi_name='"+str(PI)+"'"
	cursor.execute(piCheckSql)
	rPi=cursor.fetchall()
	if rPi==():
		#PubMed Anno
		q="insert into PubMed_Anno values ('"+str(pmid)+"', 'Mass spectrometry', '"+str(PI)+"', '"+str(PI_email)+"', '"+str(PI_int)+"', '"+str(search_engine)+"','"+str(ion_mode)+"', '"+str(vendor)+"', '"+str(data_count)+"',  '"+str(ms_instrument)+"', '"+str(label_tech)+"', '"+str(frag_mode)+"', '"+str(source_type)+"', '"+str(red_alk)+"', '"+str(sample_source)+"', '"+str(in_gel)+"', 'Annotated', 'New contributer')"
		cursor.execute(q)
		subFunction(pmid,username)
	else:
		q="insert into PubMed_Anno values ('"+str(pmid)+"', 'Mass spectrometry', '"+str(PI)+"', '"+str(PI_email)+"', '"+str(PI_int)+"', '"+str(search_engine)+"','"+str(ion_mode)+"', '"+str(vendor)+"', '"+str(data_count)+"',  '"+str(ms_instrument)+"', '"+str(label_tech)+"', '"+str(frag_mode)+"', '"+str(source_type)+"', '"+str(red_alk)+"', '"+str(sample_source)+"', '"+str(in_gel)+"', 'Annotated','Already contributed')"
		cursor.execute(q)
		subFunction(pmid,username)
	conn.commit()
	cursor.close()
        conn.close()

	return "-"

def subFunction(pmid,username):
	conn = MySQLdb.connect(host="192.168.5.232", user="xxx", passwd="xxxx",db="HuPA")
	cursor = conn.cursor()
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
	q="insert into Entry_Log values (0, '"+str(pmid)+"', '"+str(username)+"', '"+str(final_time)+"',  'PubMed_Anno', 'Annotated')"
	cursor.execute(q)
	q="update PubMed_Index set status='Annotated' where pubmed="+str(pmid)
	cursor.execute(q)

	

"""
search_engine='SEQUEST'
PI_int='instititititi'
ion_mode='ESI'
PI='test pi'
vendor='Thermotest'
data_count=''
ms_instrument=''
label_tech=''
frag_mode=''
username=''
source_type=''
PI_email=''
red_alk=''
sample_source=''
in_gel=''
pmid='111'
Add_PMID_Ann(search_engine, PI_int, ion_mode, PI, vendor, data_count, ms_instrument, label_tech, frag_mode, username, source_type, PI_email, red_alk, pmid, sample_source, in_gel)
"""
