#!/usr/bin/python

import re, time, urllib

def main(pmid):
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
		out_str=au_name+"\t"+ti

	except IOError, error_code :
		print "error\n"
	
	return out_str


file= open('pmid', 'r')
for each in file:
	each=each.strip().replace("\n", "")
	out=main(each)
	print out

