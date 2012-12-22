#!/usr/bin/python

import MySQLdb
import time
def Add_PMID_Ann(search_engine, PI_int, ion_mode, PI, vendor, data_count, ms_instrument, label_tech, frag_mode, username, source_type, PI_email, red_alk, pmid, sample_source, in_gel):

	
	conn = MySQLdb.connect(host="192.168.5.215", user="root", passwd="changeme",db="HuPA")
        cursor = conn.cursor()
	#PubMed Anno
	q="insert into PubMed_Anno values ('"+str(pmid)+"', 'Mass spectrometry', '"+str(PI)+"', '"+str(PI_email)+"', '"+str(PI_int)+"', '"+str(search_engine)+"','"+str(ion_mode)+"', '"+str(vendor)+"', '"+str(data_count)+"',  '"+str(ms_instrument)+"', '"+str(label_tech)+"', '"+str(frag_mode)+"', '"+str(source_type)+"', '"+str(red_alk)+"', '"+str(sample_source)+"', '"+str(in_gel)+"', 'Annotated')"
	cursor.execute(q)
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
	conn.commit()
	cursor.close()
        conn.close()

	return "-"
