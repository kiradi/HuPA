import urllib, re
d=re.compile('\d+')
data=url_data = urllib.urlopen('http://www.pubmedcentral.nih.gov/tocrender.fcgi?journal=7&action=archive')
for each_x in data.readlines():
	if re.search('\<a class="arc-issue" href="tocrender.fcgi\?iid=(.*)"\>(.*)\<br\>(.*)\<\/a\>',each_x):
		gbInfo=re.search('\<a class="arc-issue" href="tocrender.fcgi\?iid=(.*)"\>(.*)\<br\>(.*)\<\/a\>',each_x).groups()
		gbAr=gbInfo[0].split('<td class="iss-cell">')
i=908
for each in gbAr:
	if re.search('<a class="arc-issue" href="tocrender.fcgi\?iid=(.*)">(.*)<br>(.*)<\/a>',each):
		info = re.search('<a class="arc-issue" href="tocrender.fcgi\?iid=(.*)">(.*)<br>(.*)<\/a>',each).groups()
		i+=1
		iss=d.findall(info[1])
		print str(i)+'\t'+'-'+'\t'+info[2]+'\t'+iss[1]+'\t'+iss[0]+'\t'+'unchecked'+'\t'+'genomeBiology'+'\t'+'NULL'+'\t'+info[0]
