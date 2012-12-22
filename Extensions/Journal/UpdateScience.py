import urllib,re

def UpdateScience():
	out=open('scienceToUpdate','w')
	yearList=['1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008']
	d=re.compile('\d+')
	w=re.compile('(\w+)')
	i=330
	for each_y in yearList:
		url_data = urllib.urlopen('http://www.sciencemag.org/archive/'+each_y+'.dtl')
		for each_x in url_data.readlines():
			#i+=1
			if re.search('<p><span>(.*)</span><br><strong>&quot;.*&quot;</strong><br>Vol.(.*)</p>',each_x):
				i+=1
				info=re.search('<p><span>(.*)</span><br><strong>.*</strong><br>(.*)</p>',each_x).groups()
				issInfo= w.findall(info[0])
				day=issInfo[0]
				month=issInfo[1]
				year=issInfo[2]
				vol = info[1].split('Page')[0]
				volIss = d.findall(vol)
				print >>out,str(i)+'\t'+str(day)+' '+str(month)+'\t'+year+'\t'+str(volIss[1])+'\t'+volIss[0]+'\t'+'unchecked'+'\t'+'science'+'\t'+'NULL'
			elif re.search('<p><span>(.*)</span><br>(.*)</p>',each_x):
				i+=1
				info=re.search('<p><span>(.*)</span><br>(.*)</p>',each_x).groups()
				issInfo= w.findall(info[0])
				day=issInfo[0]
				month=issInfo[1]
				year=issInfo[2]
				vol = info[1].split('Page')[0]
				volIss = d.findall(vol)
				print >>out,str(i)+'\t'+str(day)+' '+str(month)+'\t'+year+'\t'+str(volIss[1])+'\t'+volIss[0]+'\t'+'unchecked'+'\t'+'science'+'\t'+'NULL'
			else:
				a=1
UpdateScience()
