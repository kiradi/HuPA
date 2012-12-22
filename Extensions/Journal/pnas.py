import urllib, re
yearList='2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998,1997,1996,1995,1994,1993,1992,1991,1990'.split(',')
w=re.compile('\w+')
i=3316
for year in yearList:
	url_data=urllib.urlopen('http://www.pnas.org/contents-by-date.'+year+'.shtml')
	for each_x in url_data.readlines():
		if re.search('<STRONG>Archive of (.*) Online Issues:<\/STRONG>',each_x):
			info=re.search('<STRONG>Archive of (.*) Online Issues:<\/STRONG>',each_x).groups()
			year=info[0]
		if re.search('<STRONG><A HREF="\/content\/vol(.*)\/issue(.*)\/">(.*)</A><\/STRONG>',each_x):
			infoMonth=re.search('<STRONG><A HREF="\/content\/vol(.*)\/issue(.*)\/">(.*)<\/A><\/STRONG>',each_x).groups()
			vol=infoMonth[0]
			iss=infoMonth[1]
			month=w.findall(infoMonth[2])[0]
			i+=1
			print str(i)+'\t'+month+'\t'+year+'\t'+iss+'\t'+vol+'\t'+'unchecked'+'\t'+'pnas'+'\t'+'NULL'+'\t'+'NULL'
		
		
