from os import listdir
import re

class outParser:
    def __init__(self,pathToOutFiles):
        self.pathToOutFiles=pathToOutFiles
        self.outDict = {}
    def parse(self,rankIn):
        outFileList=[eachFile for eachFile in listdir(self.pathToOutFiles) if eachFile.endswith('.out')]
        for eachOutFile in outFileList:
            outData=open(self.pathToOutFiles+eachOutFile,'r').xreadlines()
            newline=0
            modflag=0
            getCharge=re.compile('(\+\d|-\d)')

            getMod = re.compile('(\w+\*\s\+\d+\.\d+|\w+\*\s-\d+\.\d+|\w+#\s\+\d+\.\d+|\w+#\s-\d+\.\d+)')
            modChar = re.compile('\*|#|\^|\$|\[|\]')
            remIonSpace = re.compile('(\s+\/\s+|\/\s+|\s+\/)')    
            remSpace = re.compile('\s+')
            for eachData in outData:
                eachD=eachData.strip('\n')
                if eachD.find(' '):
                    newline=0
                if newline==1:
                    if re.search('\s\(M\+H\)\+ mass =(.*)(AVG\/AVG|MONO\/MONO)',eachD):
                        mass = re.search('\s\(M\+H\)\+ mass =(.*)(AVG\/AVG|MONO\/MONO)',eachD).groups()
                        charge = getCharge.findall(mass[0].split(',')[0])
                        charge = charge[0]
                    if re.search('\s#\s\s\sRank\/Sp*',eachD):
                        modflag=0
                    if modflag==1:
                        x = eachD.replace('(','/').replace(')','/')
                        mods=getMod.findall(x)
                        specialMod={}
                        for eachM in mods:
                            special = modChar.findall(eachM)
                            specialMod[special[0]]=eachM
                        mods = ';'.join(mods)
                    if re.search('\sdisplay\stop*',eachD):
                        modflag=1
                    for rnk in range(rankIn):
                        if re.search('\s'+str(rnk+1)+'\.\s\s(.*)',eachD):
                            outInf=re.search('\s'+str(rnk+1)+'\.\s\s(.*)',eachD).groups()
                            outInfo = remIonSpace.sub('/',outInf[0])
                            outInfos=[y for y in remSpace.split(outInfo) if y!='']
                            if len(outInfos)>9:
                                #print outInfos
                                rank = outInfos[0]
                                id = outInfos[1]
                                mass = outInfos[2]
                                deltCn = outInfos[3]
                                xCorr = outInfos[4]
                                sp = outInfos[5]
                                ions = outInfos[6]
                                refer = outInfos[7]
                                peptide = outInfos[-1]
                                #print rank,id,mass,deltCn,xCorr,sp,ions,refer,peptide
                                if '*' in peptide or '^' in peptide or  '#' in peptide:
                                    listSpecialChar = modChar.findall(peptide)
                                    ar=[]
                                    for specialChar in listSpecialChar:
                                        if specialMod.has_key(specialChar):
                                            ar.append(specialMod[specialChar])
                                        else:
                                            #Scenario: special character will be found in but not defined in .out file
                                            print 'Modification for '+specialChar+' is not defined in '+eachOutFile+' file'
                                            break
                                    outPepInfo = refer+'\t'+mass+'\t'+charge+'\t'+xCorr+'\t'+peptide+'\t'+';'.join(ar)
                                    self.makeDic(eachOutFile,outPepInfo)
                                else:
                                    outPepInfo = refer+'\t'+mass+'\t'+charge+'\t'+xCorr+'\t'+peptide+'\t'+'-'
                                    self.makeDic(eachOutFile,outPepInfo)
                        elif re.search('^\s\s\s\s+(.*)',eachD):
                            out=re.search('^\s\s\s\s+(.*)',eachD).groups()
                            print str(rnk+1),out
                        else:
                            a=1
                if eachD.find(' '):
                    newline=1
        return self.outDict
    def makeDic(self,eachOutFile,outPepInfo):
        if self.outDict.has_key(eachOutFile):
            listOutPepInfo=[self.outDict[eachOutFile]]
            listOutPepInfo+=[outPepInfo]
            joinListOutPepInfo='$$'.join(listOutPepInfo)
            self.outDict[eachOutFile]=joinListOutPepInfo
        else:
            self.outDict[eachOutFile]=outPepInfo

#from sequestOutParser import outParser
#x=outParser('/home/prashanth/WORK/DATA_PROCCESS/TESTOUT/')
#x.parse(2)
