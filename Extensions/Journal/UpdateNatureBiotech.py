import urllib, re
def natureX():
	url_data = urllib.urlopen("http://www.nature.com/nrm/archive/index.html")
	#http://www.nature.com/nrg/archive/index.html")
	#http://www.nature.com/nrc/archive/index.html")
	#http://www.nature.com/ng/archive/index.html")
	#http://www.nature.com/ncb/archive/index.html")
	#http://www.nature.com/ni/archive/index.html")
	#http://www.nature.com/nm/archive/index.html")
	#http://www.nature.com/nbt/archive/index.html#top")
	i=2281
	for each_x in url_data.readlines():
		if re.search('class="volume">(.*)<\/h3><ul xmlns="http://www.w3.org/1999/xhtml" class="vol">',each_x):
			for eax in each_x.split('<h4 class="month">'):
				if re.search('class="volume">(.*)</h3><ul xmlns="http://www.w3.org/1999/xhtml"',eax):
					yearInfo=re.search('class="volume">(.*)</h3><ul xmlns="http://www.w3.org/1999/xhtml"',eax).groups()
					year=yearInfo[0].split('|')[0]
				if re.search('(.*)</h4><p class="issue"><a href="/nrm/journal/(.*)/(.*)/"><span class="issue-no',eax):
					month=re.search('(.*)</h4><p class="issue"><a href="/nrm/journal/(.*)/(.*)/"><span class="issue-no',eax).groups()
					i+=1
					print str(i)+'\t'+month[0]+'\t'+year+'\t'+month[2]+'\t'+month[1]+'\t'+'unchecked'+'\t'+'nrm'+'\t'+'NULL'+'\t'+'NULL'

def nature():
	d=re.compile('\d+')
	w=re.compile('\w\w\w+')
	url_data = urllib.urlopen("http://www.nature.com/nature/archive/index.html?showyears=2008-2007-2006-2005-2004-2003-2002-2001-2000-1999-1998-1997-1996-1995-1994-1993-1992-1991-1990-1989-1988-1987-1986-1985-1984-1983-1982-1981-1980-1979-1978-1977-1976-1975-1974-1973-1972-1971-1970-1969-1968-1967-1966-1965-1964-1963-1962-1961-1960-1959-1958-1957-1956-1955-1954-1953-1952-1951-1950#y1950")
	i=2372
	for each_x in url_data.readlines():
		if re.search('<li><a href="\/nature\/journal\/.*index.html">(.*)<\/a><\/li>',each_x):
			info=re.search('<li><a href="\/nature\/journal\/.*index.html">(.*)<\/a><\/li>',each_x).groups()
			month=w.findall(info[0].split(';')[0])
			iss=d.findall(info[0].split(';')[1].split(':')[0])
			i+=1
			print str(i)+'\t'+month[0]+'\t'+month[1]+'\t'+iss[1]+'\t'+iss[0]+'\t'+'unchecked'+'\t'+'nature'+'\t'+'NULL'+'\t'+'NULL'
			

nature()
