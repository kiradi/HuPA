
class mascotSpectrumMapper:
	def __init__(self):
		self.SPEC_DIC={}
		self.pklMascotDic={}
		self.mascotPklDic={}
	def mapper(self,pklFile):
		data=pklFile.xreadlines()
		j=0
		ar=[]
		for each in data:
			header=each.strip('\n').strip('\r').split(' ')
			if len(header) == int(3):
				j+=1
				val = (float(header[0])-1.0079)*float(header[2])
				if self.SPEC_DIC.has_key(val):
					lists= [self.SPEC_DIC[val]]
					lists+=[str(j)]
					self.SPEC_DIC[val]='$'.join(lists)
				else:
					self.SPEC_DIC[val]=str(j)
				ar.append(val)
		lis = self.SPEC_DIC.keys()
		lis.sort()
		i=0
		for xv in lis:
			for spt in str(self.SPEC_DIC[xv]).split('$'):
				i+=1
				#print str(i)+'\t'+spt+'\t'+str(xv)
				self.pklMascotDic[str(i)]=spt
		self.reverseMapper(self.pklMascotDic)
		return self.pklMascotDic
	def reverseMapper(self,dic):
		for ki,val in dic.iteritems():
			self.mascotPklDic[val]=ki
		return self.mascotPklDic
			
		
		
#x=mascotSpectrumMapper(open('AnophelesFr22.pkl'))
#print x. mapper()
