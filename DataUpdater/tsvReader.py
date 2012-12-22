import csv
from modification import modificationFormat
from hupaDataProcessor import hupaDataConverter

"""
    Parameters to be given:
    1)read file
    2)write file
    3)delimiter (TSV/CSV)
    4)search engine

"""

class tsvProcessor:
    def __init__(self,reader,delim,eng):
        self.reader = reader
        self.dicts = []
        self.delim = delim
        self.delimiter_DIC = {'tsv':'\t','csv':','}
        self.eng = eng
        self.engine = {
                'spectrumMill':['filename','accession_number','parent_m_over_z','parent_charge','previous_aa','sequence','next_aa','varMods','fixedMods','score','discriminant'],
                'mascot':['prot_acc','pep_exp_mz','pep_exp_z','pep_res_before','pep_seq','pep_res_after','pep_var_mod','pep_var_mod_pos','pep_score','pep_expect'],
                'omssa':['Filename/id','Start','Peptide','Stop','E-value','Mass','gi','Mods','Charge','P-value','Accession'],
                #'sequest':['','','',''],
                'inspect':['#SpectrumFile','Annotation','Protein','Charge','p-value','SpecFilePos']
                }
        self.modTermDic=modificationFormat(open('MASTER_UNIMOD'))
        """
        modificationFormat(open('MASTER_UNIMOD')) will initilize MASTER_UNIMOD DICTIONARY in modification.py
        """
        self.masterMapDic=hupaDataConverter(open('MASTER_MAP.txt'),open('HPRD_ENTREZ_MAP.txt'),open('EXPRESSION.txt','a'),open('SPECTRUM.txt','a'))
        """
        ################################################################################################################
            INSPECT: InSpect does not provide mass information in .tsv file. So, we have to fetch it from spectrum file.
                     Annotation field contains peptide info., first and last residue info, and modification term info.
                     Using modificaton term we need to find the site and modified residue.
            SpectrumMill:

            Mascot: 
            
            OMSSA:

            X!TANDEM: 
        #################################################################################################################
        """
    def process(self):
        """
        Here delimiter_DIC takes 'self.delim', which takes optional .tsv('\t') or .csv(,) delimiter
        """
        parser = csv.reader(self.reader,delimiter=self.delimiter_DIC[self.delim])
        firstRec = True
        for fields in parser:
            if firstRec:
                fieldNames = fields
                firstRec   = False
            else:
                self.dicts.append({})
                for i,f in enumerate(fields):
                    try:
                        self.dicts[-1][fieldNames[i]] = f
                    except:
                        import pdb
                        pdb.set_trace()
        if self.eng is "spectrumMill":
            for i,row in enumerate(self.dicts):
                fileSM = row[self.engine[self.eng][0]]
                acNoSM = row[self.engine[self.eng][1]]
                masSM=row[self.engine[self.eng][2]]
                chrgeSM=row[self.engine[self.eng][3]]
                preAmSM=row[self.engine[self.eng][4]].replace('(','').replace(')','')
                pepSM=row[self.engine[self.eng][5]]
                nAmSM=row[self.engine[self.eng][6]].replace('(','').replace(')','')
                modSM=row[self.engine[self.eng][7]].split('\s')+row[self.engine[self.eng][8]].split('\s')
                modLis = [mod.strip() for mod in modSM if mod!=' ']
                modSM = ';'.join(modLis)
                scoreSM=row[self.engine[self.eng][9]]
                descrimentSM=row[self.engine[self.eng][10]]
                if modSM !='':
                    modPepInHupaFormat=self.modTermDic.spectrumMill(preAmSM,pepSM,nAmSM,modSM,self.eng)
                    parsedData=acNoSM+'\t'+masSM+'\t'+chrgeSM+'\t'+modPepInHupaFormat+'\t'+scoreSM+'\n'
                    data = self.mapCaller(parsedData,self.eng)
                    #print >>self.writer,data
                else:
                    parsedData=acNoSM+'\t'+masSM+'\t'+chrgeSM+'\t'+preAmSM+'.'+pepSM+'.'+nAmSM+'\t'+'-'+'\t'+scoreSM+'\n'
                    data = self.mapCaller(parsedData,self.eng)
                    #print >>self.writer,data

        if self.eng is "mascot":
            """
            In Mascot, under every gi (protein) corresponding peptide information will be there
            """
            giFound=True
            for i,row in enumerate(self.dicts):
                if row[self.engine[self.eng][0]]!='':
                    giAsKey = row[self.engine[self.eng][0]]
                    giFound=False
                if giFound==False:
                    massM=row[self.engine[self.eng][1]]
                    chargeM=row[self.engine[self.eng][2]]
                    preAmM=row[self.engine[self.eng][3]]
                    pepM=row[self.engine[self.eng][4]]
                    nAmM = row[self.engine[self.eng][5]]
                    modM=row[self.engine[self.eng][6]]
                    modSiteM=row[self.engine[self.eng][7]]
                    scoreM=row[self.engine[self.eng][8]]
                    evalM=row[self.engine[self.eng][9]]
                    if modM !='':
                        """
                         modificationFormat from modification.py creates a MASTER_UNIMOD dictionary 
                         Where all modifications of unimod would be available. 
                         At same time formatMod function in modificationFormat class would convert modification format                                """
                        modPepInHupaFormat=self.modTermDic.mascot(preAmM,pepM,nAmM,modSiteM,modM,self.eng)
                        parsedData=giAsKey+'\t'+massM+'\t'+chargeM+'\t'+modPepInHupaFormat+'\t'+scoreM+'\n'
                        data=self.mapCaller(parsedData,self.eng)
                        #print >>self.writer,data
                    else:
                        
                        parsedData=giAsKey+'\t'+massM+'\t'+chargeM+'\t'+preAmM+'.'+pepM+'.'+nAmM+'\t'+'-'+'\t'+scoreM+'\n'
                        data=self.mapCaller(parsedData,self.eng)
                        #print >>self.writer,data

        if self.eng is "inspect":
            """
                InSpect does not have mass information in TSV file
                So we need to fetch it from spectrum file (this is not yet done)
            """
            for i,row in enumerate(self.dicts):
                data = row[self.engine[self.eng][0]]+'\t'+row[self.engine[self.eng][1]]+'\t'+row[self.engine[self.eng][2]]+'\t'+row[self.engine[self.eng][3]]+'\t'+row[self.engine[self.eng][4]]+'\t'+row[self.engine[self.eng][5]]+'\n'
                #return data
                #data = self.mapCaller(data)
                #self.writer.write(data)

        if self.eng is "omssa":
            #OMSSA csv doesnot contain start and last residue of the peptide, instead contains position. So start and last residue need to fetch from protein sequence
            for i,row in enumerate(self.dicts):
                giO = row[self.engine[self.eng][6]]
                massO= row[self.engine[self.eng][5]]
                chargeO=row[self.engine[self.eng][8]]
                preAmO = row[self.engine[self.eng][1]]#position in protein
                pepO = row[self.engine[self.eng][2]]
                nextAmO = row[self.engine[self.eng][3]] #position in protein
                scoreO= row[self.engine[self.eng][4]]
                modO=row[self.engine[self.eng][7]]
                if modO !='':
                    #parsedData=giO+'#'+massO+'#'+chargeO+'#'+preAmO+'.'+pepO+'.'+nextAmO+'#'+modO+'#'+scoreO
                    modPepInHupaFormat=self.modTermDic.omssa(preAmO,pepO,nextAmO,modO,self.eng)
                    parsedData=giO+'\t'+massO+'\t'+chargeO+'\t'+modPepInHupaFormat+'\t'+scoreO+'\n'
                    self.mapCaller(parsedData,self.eng)
                else:
                    parsedData=giO+'\t'+massO+'\t'+chargeO+'\t'+preAmO+'.'+pepO+'.'+nextAmO+'\t'+'-'+'\t'+scoreO+'\n'
                    self.mapCaller(parsedData,self.eng)
            
    def mapCaller(self,data,eng):
        data=self.masterMapDic.hupaHprdMapper(data)
        return data
#-----------------------------------------------------------------------------------------------
#from tsvReader import tsvProcessor
#x=tsvProcessor(open('toread'),open('towrite','w'),'CSV','mascot')
#x.process()
