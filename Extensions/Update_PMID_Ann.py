#!/usr/bin/python

import MySQLdb
import time

def Update_PMID_Ann(search_engine, PI_int, ion_mode, PI, vendor, data_count, ms_instrument, label_tech, frag_mode, username, source_type, PI_email, red_alk, pmid, sample_source, in_gel):
	
	conn = MySQLdb.connect(host="localhost", user="xxx", passwd="xxxx",db="HuPA")
        cursor = conn.cursor()
	
	#PubMed Anno
	q="update PubMed_Anno set PI= '"+str(PI)+"', PI_email='"+str(PI_email)+"', PI_int='"+str(PI_int)+"', search_engine='"+str(search_engine)+"',ion_mode='"+str(ion_mode)+"', vendor='"+str(vendor)+"', data_count='"+str(data_count)+"',  ms_instrument='"+str(ms_instrument)+"', label_tech='"+str(label_tech)+"', frag_mode='"+str(frag_mode)+"', source_type='"+str(source_type)+"', red_alk='"+str(red_alk)+"', sample_source='"+str(sample_source)+"', in_gel='"+str(in_gel)+"' where pubmed="+str(pmid)
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
        q="insert into Entry_Log values (0, '"+str(pmid)+"', '"+str(username)+"', '"+str(final_time)+"',  'PubMed_Anno', 'Annotated_Edited')"
	cursor.execute(q)
	conn.commit()
	cursor.close()
        conn.close()

	return "-"
