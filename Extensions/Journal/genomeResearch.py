import urllib, re
year = ['2000','2001','2002','2003','2004','2005','2006','2007','2008']
out = open('genomeResearch','w')
i=4778
for eachYear in year:
	mainURL = urllib.urlopen('http://www.genome.org/contents-by-date.'+str(eachYear)+'.shtml')
	for each in mainURL:
		if re.search('<STRONG>Archive of (.*) Online Issues:</STRONG>',each):
			jYear=re.search('<STRONG>Archive of (.*) Online Issues:</STRONG>',each).groups()
			#print jYear
		if re.search('<A HREF="/content/vol(.*)/issue(.*)/"><STRONG>.*</STRONG></A>; <FONT SIZE="-2">(.*)<BR>',each):
			iss = re.search('<A HREF="/content/vol(.*)/issue(.*)/"><STRONG>(.*)</STRONG></A>; <FONT SIZE="-2">.*<BR>',each).groups()
			#print iss
			i+=1
			print >>out,str(i)+'\t'+iss[2]+'\t'+jYear[0]+'\t'+iss[1]+'\t'+iss[0]+'\t'+'unchecked'+'\t'+'genomeRes'+'\t'+'NULL'
			
			
