import urllib, re

yearList='2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998,1997,1996,1995,1994,1993,1992,1991,1990'.split(',')
d=re.compile('\d+')
i=3894
for year in yearList:
	url_data=urllib.urlopen('http://www.cell.com/content/year?year='+year)
	for each_x in url_data.readlines():
		if re.search('<div class="generic_panel"><h3>',each_x):
			monthInfo=re.split('<div class="generic_panel"><h3>',each_x)
			for each in  monthInfo:
				if re.search('Previous year"><\/a>&nbsp;&nbsp;&nbsp;<strong>(.*)<\/strong>&nbsp;&nbsp;&nbsp;',each):
					yearInfo=re.search('Previous year"><\/a>&nbsp;&nbsp;&nbsp;<strong>(.*)<\/strong>&nbsp;&nbsp;&nbsp;',each).groups()
					#print yearInfo
				for eac in each.split('<dt>'):
					if re.search('<a href="\/content\/issue\?volume=.*&amp;issue=.*">(.*)</a>:<\/dt><dd>(.*)<\/dd>',eac):
						vol=re.search('<a href="\/content\/issue\?volume=.*&amp;issue=.*">(.*)<\/a>:<\/dt><dd>(.*)<\/dd>',eac).groups()
						#print yearInfo,vol
						year = yearInfo[0]
						mont=vol[0].split('&nbsp;')[0]
						iss=d.findall(vol[1].split(':')[0])
						i+=1
						print str(i)+'\t'+mont+'\t'+year+'\t'+iss[1]+'\t'+iss[0]+'\t'+'unchecked'+'\t'+'cell'+'\t'+'NULL'+'\t'+'NULL'

