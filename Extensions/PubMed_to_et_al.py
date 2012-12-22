import re, time, urllib

def main(pmid):
	pmid=pmid.strip().replace("and",";").replace(",",";")
	fin_str=""
	res_str="^^"
	y = re.compile('\d\d\d\d\d\d*\S*')
	au = re.compile('(.*)<')
	dpau = re.compile('.*>')
	sp = re.compile('\s.*$')
	opener = urllib.FancyURLopener({})
	url_id= "http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?db=pubmed&cmd=Retrieve&dopt=medline&list_uids="+str(pmid)+""
	au_list=[]
	dp=""
	try :
		page = opener.open(url_id)
		xml = page.readlines()
		
		for each_line1 in xml:
			temp=each_line1.split("</tr>")
			for each_line in temp:
				if each_line.find(">AU<")!=-1 and au.match(each_line):
					au_name = au.match(each_line).groups()[0]
					au_name = dpau.sub("", au_name)
					au_name= au_name.replace("'", " ")
					au_list.append(au_name)
				if each_line.find(">DP<")!=-1 and au.match(each_line):
					dp = au.match(each_line).groups()[0]
					dp = dpau.sub("", dp)
					dp = sp.sub("", dp)
		if len(au_list) > 1:
			fin_str=str(au_list[0])+" <i>et al</i>., "+str(dp)
		else:
			fin_str=str(au_list[0])+", "+str(dp)
		fin_str="<a href=\"http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?db=pubmed&cmd=Retrieve&dopt=AbstractPlus&list_uids="+str(pmid)+"\" class=\"blusmll\">"+fin_str
		res_str=res_str+";</a> "+fin_str
	except IOError, error_code :
		print "error\n"
	res_str=res_str.replace("^^;</a> ","")
	res_str=res_str+"</a>"
	pub_pat = re.compile(pmid)
	return res_str
print main('11956316')