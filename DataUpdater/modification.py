import re

class modificationFormat:
    """
        ###############################################################
        Essential parameters for ModificationFormat class are,
        1)      peptide
        2)      residue that modified
        3)      Terminology of modification
        4)      previous residue
        5)      Next residue
        6)      Search Engine
        ################################################################
    """

    def __init__(self,reader):
        self.reader=reader
        self.uniModDic={}
        """
        Here modification dictionary will be created (only once) when class get initilized.
        """
        modData=self.reader.xreadlines()
        for each in modData:
            eachS = each.strip('\n').split('\t')
            modVal="%2.2f" % float(eachS[1])
            self.uniModDic[eachS[0]]=modVal
            
    def mascot(self,preRes,modPep,lastRes,modRes,modTerm,srchEng):
        d=re.compile('[1-9]|X')
        iterRes = d.finditer(modRes)
        resPosDic={}
        modPep = preRes+'.'+modPep+'.'+lastRes
        #print modTerm,modRes
        stdTerm={'Acetyl':'Acetylation','Oxidation':'Oxidation','Gln->Glu':'Pyro-glu from Q','Carbamidomethyl':'Carbamidometylation','Asp->Asn':'Asp->Asn substitution','Met->Leu':'Met->Leu substitution'}
        modTerms = modTerm.split(';')
        for res in iterRes:
            resPosDic[res.span()[1]]=modPep[int(res.span()[0])]
        #print resPosDic
        w = re.compile('\((\w+)\)')
        resModDic={}
        for each in modTerms:
            resInModTerm=w.finditer(each)
            for eachRes in resInModTerm:
                resModDic[eachRes.group().replace(')','').replace('(','')]=each
        toSort=[(k1, v1) for k1, v1 in resPosDic.items()]
        toSort.sort()
        step=0
        modTermAr=[]
        for k,v in toSort:
            modPep=list(modPep)
            if resModDic.has_key(v):
                modPep.insert(k+step,self.uniModDic[resModDic[v]])
                step+=1
                if k!=0:
                    modTermAr.append(v+str(k-step)+'#'+stdTerm[resModDic[v].split(' ')[0]])
                else:
                    modTermAr.append(v+str(k)+'#'+stdTerm[resModDic[v].split(' ')[0]])
            else:

                modTermAr.append(v+str(k)+'#'+'Acetylation')
                modPep.insert(k+step,self.uniModDic['Acetyl (S)'])
                #signature of Acetyle (S) is left in N- terminal
                step+=1
        modifiedPep=''.join(modPep)
        formattedTerm=';'.join(modTermAr)
        return modifiedPep+'\t'+formattedTerm
        #ar+=[getRes.findall(eachMod)[0]+str(self.modDic[eachMod]) for eachMod in mod]
    def spectrumMill(self,preRes,modPep,lastRes,modTerm,srchEng):
        modTerm =';'.join(modTerm.split(' '))
        #print preRes,modPep,lastRes,modTerm,srchEng
        #Here I have to make a std dictionary
        stdDic={'m:Oxidized-Methionine':'Oxidation (M)','k:LysAcetyl':'Acetyl (K)','C:carbamidomethylation':'Carbamidomethyl (C)','q:pyroGlu':'Gln->Glu (Q)'}
        stdTerm={'Acetyl':'Acetylation','Oxidation':'Oxidation','Gln->Glu':'Pyro-glu from Q','Carbamidomethyl':'Carbamidometylation'}
        #valDic={'Oxidation (M)':'15.9949','Acetyl (K)':'42.0105','Carbamidomethyl (C)':'57.021','Gln->Glu (Q)':'0.984016'}
        d=re.compile('[a-z]')
        iterRes = d.finditer(modPep)
        resPosDic={}
        for res in iterRes:
            resPosDic[res.span()[1]]=res.group()
        resValDic={}
        modTermDic={}
        for k,v in stdDic.iteritems():
            resValDic[k.split(':')[0]]=self.uniModDic[v]
            modTermDic[k.split(':')[0]]=v
        toSort=[(k1, v1) for k1, v1 in resPosDic.items()]
        toSort.sort()
        step=0
        modTermAr=[]
        for k1,v1 in toSort:
            modPep = list(modPep)
            modTermAr.append(resPosDic[k1].upper()+str(k1)+'#'+stdTerm[modTermDic[resPosDic[k1]].split(' ')[0]])
            modPep.insert(k1+step,resValDic[resPosDic[k1]])
            step+=1
        modifiedPep = preRes+'.'+''.join(modPep).upper()+'.'+lastRes
        formattedTerm=';'.join(modTermAr)
        #return ''.join(modPep).upper()+'\t'+';'.join(modTermAr)
        return modifiedPep+'\t'+formattedTerm

    def inspect(self,preRes,modPep,lastRes,modTerm,srchEng):
        a= preRes+'.'+modPep+'.'+lastRes
        return a
    def omssa(self,preRes,modPep,lastRes,modTerm,srchEng):
        a= preRes+'.'+modPep+'.'+lastRes
        #A std dictionary for OMSSA need to be created
        stdDic={'oxidation of M':'Oxidation (M)'}
        stdTerm={'Acetyl':'Acetylation','Oxidation':'Oxidation','Gln->Glu':'Pyro-glu from Q','Carbamidomethyl':'Carbamidometylation'}
        #valDic={'Oxidation (M)':'15.9949'}
        modTerm=modTerm.split(',')
        modPosDic={}
        for mod in modTerm:
            mod=mod.strip().split(':')
            modPosDic[mod[1]]=mod[0]
        #print modPosDic
        toSort=[(k1, v1) for k1, v1 in modPosDic.items()]
        toSort.sort()
        step=0
        modTermAr=[]
        for k,v in toSort:
            modPep = list(modPep)
            modTermAr.append(modPep[int(k)+step-1].upper()+str(k)+'#'+stdTerm[stdDic[v].split(' ')[0]])
            modPep.insert(int(k)+step,self.uniModDic[stdDic[v]])
            step+=1
        modifiedPep = ''.join(modPep)
        formattedTerm=';'.join(modTermAr)
        return preRes+'.'+modifiedPep.upper()+'.'+lastRes+'\t'+formattedTerm

    def sequest(self,preRes,modPep,lastRes,modTerm,srchEng):
        a= preRes+'.'+modPep+'.'+lastRes
        return a
    def xtandem(self,preRes,modPep,lastRes,modTerm,srchEng):
        a= preRes+'.'+modPep+'.'+lastRes
        return a
