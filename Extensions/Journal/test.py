#!/usr/bin/python
# -*- coding: utf-8 -*-

#################################
#PubMed XML information Fetcher
#created on Feb 18 th 2008
#By PHK
##################################

import MySQLdb
import elementtree.ElementTree as ET
import re, urllib

conn = MySQLdb.connect(host="localhost", user="root", passwd="changeme",db="HuPA")
cursor = conn.cursor()
u='Guo, Ailan##Villén, Judit##Kornhauser, Jon##Lee, Kimberly A##Stokes, Matthew P##Rikova, Klarisa##Possemato, Anthony##Nardone, Julie##Innocenti, Gregory##Wetzel, Randall##Wang, Yi##MacNeill, Joan##Mitchell, Jeffrey##Gygi, Steven P##Rush, John##Polakiewicz, Roberto D##Comb, Michael J'
v = u.decode('utf-8')
w= 'XXXXX'
sql ="insert into test values('"+v+"', '"+str(w)+"')"
cursor.execute(sql)
print 'YYYY'
#for i,c in enumerate(v):
#    print i,c

