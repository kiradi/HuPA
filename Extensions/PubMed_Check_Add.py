#!/usr/bin/python
# -*- coding: latin-1 -*-


#################################
#PubMed XML information Fetcher
#created on Feb 18 th 2008
#By PHK
##################################

import MySQLdb
import elementtree.ElementTree as ET
import re, urllib, time


def PubMed_Check_Add(pubmed, username,ms_inst):
	conn = MySQLdb.connect(host="localhost", user="xxx", passwd="xxxx",db="HuPA")
        cursor = conn.cursor()
        #pubmed
        pubmed=pubmed.strip()
        q="select status, author, date_ad from Entry_Log where pubmed="+str(pubmed)
        cursor.execute(q)
        data=cursor.fetchall()
        if data==():
                out_str=main(pubmed, username,ms_inst)
        else:
                out_str="Present^^"
                for each in data:
                        out_str=out_str+"@@"+str(each[0])+"##"+str(each[1])+"##"+str(each[2])
			#print out_str
        out_str=out_str.replace("^^@@", "^^")
        cursor.close()
        conn.close()
        return out_str

def main(pmid,username,ms_inst):
	conn = MySQLdb.connect(host="localhost", user="xxx", passwd="xxxx",db="HuPA")
	cursor = conn.cursor()
	opener = urllib.FancyURLopener({})
	try :
		urlId= opener.open("http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?db=pubmed&cmd=Retrieve&dopt=xml&list_uids="+str(pmid)+"")
		spt = re.compile('\<s>|\<\/s>')
		au = re.compile('(.*)<\/b>')
		dpau = re.compile('.*>')
		for each in urlId.readlines():
			#print each
			if re.search('<tt class="xmlrep">(.*)<\/tt>',each):
				xml=re.search('<tt class="xmlrep">(.*)<\/tt>',each).groups()
				xml=xml[0].replace('&lt;','<').replace('&gt;','>').replace('<i>','').replace('</i>','').replace('<b>','').replace('</b>','')
				temp=''.join(spt.split(xml))
				open('temp.xml','w').write(temp)
				tree = ET.parse('temp.xml')
				root = tree.getroot()
				Ar=[]
				for element in root.getchildren():
					#print element.tag
					for child in element.getchildren():
						if child.tag == 'Article':
							for ch in child.getchildren():
								if ch.tag=='ArticleTitle':
									articleTit=ch.text
									Ar.append(articleTit)
									######
									#print 'Article title:',articleTit
									#######
								if ch.tag=='Journal':			
									for ch1 in ch.getchildren():
										if ch1.tag=='JournalIssue':
											issAr=[]
											for ch2 in ch1.getchildren():
												if ch2.tag=='Volume' or ch2.tag=='Issue':
													issAr.append(ch2.text)
											
												if ch2.tag=='PubDate':
													pubAr=[]
													for ch3 in ch2.getchildren():
														pubAr.append(ch3.text)
													datePub=' '.join(pubAr)
													Ar.append(datePub)
													######
													#print datePub
													########
											jIssue=','.join(issAr) #Issue info
											Ar.append(jIssue)
											#############
											#print jIssue
											#############
										if ch1.tag=='Title':
											title= ch1.text #journal
											Ar.append(title)
											#######
											#print title
											########
										if ch1.tag=='ISOAbbreviation':
											isoAb = ch1.text #journal	
											Ar.append(isoAb)
											#######
											#print isoAb
											#####
								if ch.tag=='AuthorList':
									auList=[]
									#dbAu=[]
									for chAu in ch.getchildren():
										if chAu.tag=='Author':
											auAr=[]
											for chAuNam in chAu.getchildren():
												if chAuNam.tag=='LastName':
													x=chAuNam.text
													auAr.append(x)
												if chAuNam.tag=='ForeName' or chAuNam.tag=='FirstName':
													y=chAuNam.text
													auAr.append(y)
											auList.append(', '.join(auAr))
									authors='##'.join(auList) #Authors list
									Ar.append(authors)
									#Ar.append('##'.join(dbAu))
									#########
									#print authors
									############
				#print '$$'.join(Ar)
				#print str(pmid)+'$$'+Ar[3]+'$$'+Ar[-1]+'$$'+Ar[1]+'$$'+Ar[0]
				ti=Ar[4].replace("'","")
				#print Ar
				u = Ar[-1]
				jt=Ar[2]
				dp=Ar[0]
				if type(u) is unicode:
					q="insert into PubMed_Index values('"+str(pmid)+"', '"+str(ti)+"', '"+u+"', '"+str(jt)+"', '"+str(dp)+"', 'Indexed', '"+str(ms_inst)+"')"
					cursor.execute(q)
				else:
					q="insert into PubMed_Index values('"+str(pmid)+"', '"+str(ti)+"', '"+str(u)+"', '"+str(jt)+"', '"+str(dp)+"', 'Indexed', '"+str(ms_inst)+"')"
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

			
#y = main('17957819','Prashantha','LTQ')
#print y
