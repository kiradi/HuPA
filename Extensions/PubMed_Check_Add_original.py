#!/usr/bin/python

import MySQLdb
import re, time, urllib

def PubMed_Check_Add(pubmed, username):
	
	conn = MySQLdb.connect(host="localhost", user="XXX", passwd="XXXX",db="HuPA")
        cursor = conn.cursor()
	
	#pubmed
	pubmed=pubmed.strip()
	q="select status, author, date_ad from Entry_Log where pubmed="+str(pubmed)
	cursor.execute(q)
	data=cursor.fetchall()
	if data==():	
		out_str=main(pubmed, username)
	else:
		out_str="Present^^"
		for each in data:
			out_str=out_str+"@@"+str(each[0])+"##"+str(each[1])+"##"+str(each[2])
	out_str=out_str.replace("^^@@", "^^")
	cursor.close()
        conn.close()
	
	return out_str

def main(pmid, username):
	conn = MySQLdb.connect(host="localhost", user="XXX", passwd="XXXX",db="HuPA")
        cursor = conn.cursor()
	pmid=pmid.strip().replace("and",";").replace(",",";")
	y = re.compile('\d\d\d\d\d\d*\S*')
	au = re.compile('(.*)<')
	dpau = re.compile('.*>')
	au_list=""
	opener = urllib.FancyURLopener({})
	url_id= "http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?db=pubmed&cmd=Retrieve&dopt=medline&list_uids="+str(pmid)+""
	try :
		page = opener.open(url_id)
		xml = page.readlines()
		jt=""
		ta=""
		ti=""
		ta=""
		for each_line1 in xml:
			temp=each_line1.split("</tr>")
			for each_line in temp:
				if each_line.find(">FAU<")!=-1 and au.match(each_line):
					au_name = au.match(each_line).groups()[0]
					au_name = dpau.sub("", au_name)
					au_name= au_name.replace("'", " ")
					au_list=au_list+"##"+au_name
				if each_line.find(">DP<")!=-1 and au.match(each_line):
					dp = au.match(each_line).groups()[0]
					dp = dpau.sub("", dp)
				if each_line.find(">JT<")!=-1 and au.match(each_line):
                                        jt = au.match(each_line).groups()[0]
                                        jt = dpau.sub("", jt)
				if each_line.find(">TA<")!=-1 and au.match(each_line):
                                        ta = au.match(each_line).groups()[0]
                                        ta = dpau.sub("", ta)
				if each_line.find(">TI<")!=-1 and au.match(each_line):
                                        ti = au.match(each_line).groups()[0]
                                        ti = dpau.sub("", ti)
		au_list=au_list+"##"
		if jt=="":
			jt=ta
		jt=jt.replace("'", "")
		ti=ti.replace("'", "")
		cu_list=au_list.replace("'","")
		dp=dp.replace("'", "")

		q="insert into PubMed_Index values('"+str(pmid)+"', '"+str(ti)+"', '"+str(au_list)+"', '"+str(jt)+"', '"+str(dp)+"', 'Indexed')"
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
		q1="insert into Entry_Log values (0, '"+str(pmid)+"', '"+str(username)+"', '"+str(final_time)+"', 'PubMed_Index', 'Indexed')"
		cursor.execute(q1)

		conn.commit()
		cursor.close()
	        conn.close()


	except IOError, error_code :
		print "error\n"
	
	return "Added^^-"
