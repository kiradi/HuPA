import urllib, re

opener = urllib.FancyURLopener({})
pmid=17263361
urlId= opener.open("http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?db=pubmed&cmd=Retrieve&dopt=xml&list_uids="+str(pmid)+"")
spt = re.compile('\<s>|\<\/s>')
au = re.compile('(.*)<\/b>')
dpau = re.compile('.*>')
for each in urlId.readlines():
	print each

