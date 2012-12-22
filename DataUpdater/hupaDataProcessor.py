import MySQLdb
class hupaDataConverter:
    def __init__(self,masterMapFile,hprdEntMapFile,writeExpressionFile,writeSpectrumFile):
        self.Conn = MySQLdb.connect(host="localhost",port=3306,user='prashanth',passwd="password",db="HUPAMyISAM")
        self.Cursor=self.Conn.cursor()
        self.masterMapFile=masterMapFile
        self.hprdEntMapFile=hprdEntMapFile
        self.writeToExpressionFile=writeExpressionFile
        self.writeToSpectrumFile=writeSpectrumFile
        self.masterMapDic={}
        self.hprdEntrezDic={}
        self.hprdDic={}
        #Note:value for expression_id and spectrum_id should come from MySQL database
        self.sqlExpression_id="SELECT max(expression_id) from expression"
        self.Cursor.execute(self.sqlExpression_id)
        self.expression_id=self.Cursor.fetchall()[0][0]
        self.sqlSpectrum_id="SELECT max(spectrum_id) from ms_expression2"
        self.Cursor.execute(self.sqlSpectrum_id)
        self.spectrum_id=self.Cursor.fetchall()[0][0]
        #print self.expression_id
        #print self.spectrum_id
        #If tables are empty
        if self.expression_id is None:
            self.expression_id=0
        if self.spectrum_id is None: 
            self.spectrum_id=0
        masterMapData=self.masterMapFile.xreadlines()
        for eachm in masterMapData:
            eachmId = eachm.strip('\n').split('\t')
            mKey=eachmId[0]
            mVal=eachmId[1]
            self.masterMapDic[mKey]=mVal
        hprdEntrezData=self.hprdEntMapFile.xreadlines()
        for eache in hprdEntrezData:
            eacheId = eache.strip('\n').split('\t')
            eKey=eacheId[0]
            eVal = eacheId[1]
            self.hprdEntrezDic[eKey]=eVal
    def hupaHprdMapper(self,parsedData):
        #Conn = MySQLdb.connect(host="localhost",port=3306,user='prashanth',passwd="password",db="HUPAMyISAM")
        #Cursor=Conn.cursor()

        parsedData_spt =parsedData.strip('\n').split('\t')
        #NOTE: removal of gi text should come in tsvReader itself
        gi = parsedData_spt[0].replace('gi|','')
        pep=parsedData_spt[3]
        mass=parsedData_spt[1]
        score=parsedData_spt[5]
        charge=parsedData_spt[2]
        modification = parsedData_spt[4]
        #lab_id and exp_id shold come from user_details table
        lab_id=500
        tissue='"serum"'
        #pubmed id from data file
        pubmed='"11001010"'
        # constant value
        inst='"Mass spectrometry"'
        exp_id=100
        
        if self.masterMapDic.has_key(gi):
            entrz=self.masterMapDic[gi]
            entrezList=entrz.split('#')
            for entrezId in entrezList:
                if self.hprdEntrezDic.has_key(entrezId):
                    hprdId =self.hprdEntrezDic[entrezId]
                    if self.hprdDic.has_key(hprdId):
                        a=1
                    else:
                        self.expression_id+=1
                        self.hprdDic[hprdId]=self.expression_id
                        sqlexp="INSERT INTO expression VALUES ("+str(self.expression_id)+","+str(hprdId)+","+str(lab_id)+','+str(tissue)+","+str(pubmed)+","+str(inst)+","+str(exp_id)+")"
                        self.Cursor.execute(sqlexp)
                        #self.writeToExpressionFile.writelines(str(self.expression_id)+'#'+str(hprdId)+'#'+str(lab_id)+'#'+str(tissue)+'#'+str(pubmed)+'#'+str(inst)+'#'+str(exp_id)+'\n')
                    self.spectrum_id+=1
                    #self.writeToSpectrumFile.writelines(str(self.spectrum_id)+'#'+str(self.hprdDic[hprdId])+'#'+pep+'#'+str(score)+'#'+str(mass)+'#'+charge+'#'+str(gi)+'#'+str(modification)+'\n')
                    sqlexp1 = "INSERT INTO ms_expression2 VALUES ("+str(self.spectrum_id)+','+str(self.hprdDic[hprdId])+',"'+str(pep)+'","'+str(float(score))+'","'+str(mass)+'","'+str(charge)+'","'+str(gi)+'","'+str(modification)+'")'
                    self.Cursor.execute(sqlexp1)
                    #print str(self.spectrum_id)+'#'+str(self.hprdDic[hprdId])+'#'+pep+'#'+str(score)+'#'+str(mass)+'#'+charge+'#'+str(gi)+'#'+str(modification)
                else:
                    if self.hprdDic.has_key(entrezId):
                        a=1
                    else:
                        self.expression_id+=1
                        self.hprdDic[entrezId]=self.expression_id
                        sqlexp="INSERT INTO expression VALUES ("+str(self.expression_id)+","+str(entrezId)+","+str(lab_id)+','+tissue+","+pubmed+","+inst+","+str(exp_id)+")"
                        self.Cursor.execute(sqlexp)
                        #self.writeToExpressionFile.writelines(str(self.expression_id)+'#'+str(entrezId)+'#'+std(lab_id)+'#'+std(tissue)+'#'+str(pubmed)+'#'+str(inst)+'#'+str(exp_id)+'\n')
                    self.spectrum_id+=1
                    #self.writeToSpectrumFile.writelines(str(self.spectrum_id)+'#'+str(self.hprdDic[entrezId])+'#'+pep+'#'+score+'#'+mass+'#'+charge+'#'+gi+'#'+modification+'\n')
                    #print str(self.spectrum_id)+'#'+str(self.hprdDic[entrezId])+'#'+pep+'#'+score+'#'+mass+'#'+charge+'#'+gi+'#'+modification
                    sqlexp1 = "INSERT INTO ms_expression2 VALUES ("+str(self.spectrum_id)+','+str(self.hprdDic[entrezId])+',"'+str(pep)+'","'+str(float(score))+'","'+str(mass)+'","'+str(charge)+'","'+str(gi)+'","'+str(modification)+'")'
                    self.Cursor.execute(sqlexp1)
        else:
            if self.hprdDic.has_key(gi):
                a=1
            else:
                self.expression_id+=1
                self.hprdDic[gi]=self.expression_id
                sqlexp="INSERT INTO expression VALUES ("+str(self.expression_id)+","+str(gi)+","+str(lab_id)+','+str(tissue)+","+str(pubmed)+","+str(inst)+","+str(exp_id)+")"
                self.Cursor.execute(sqlexp)
                #self.writeToExpressionFile.writelines(str(self.expression_id)+'#'+str(gi)+'#'+str(lab_id)+'#'+str(tissue)+'#'+str(pubmed)+'#'+str(inst)+'#'+str(exp_id)+'\n')
            self.spectrum_id+=1
            #self.writeToSpectrumFile.writelines(str(self.spectrum_id)+'#'+str(self.hprdDic[gi])+'#'+pep+'#'+score+'#'+mass+'#'+charge+'#'+gi+'#'+modification+'\n')
            #print str(self.spectrum_id)+'#'+str(self.hprdDic[gi])+'#'+pep+'#'+score+'#'+mass+'#'+charge+'#'+gi+'#'+modification
            sqlexp1 = "INSERT INTO ms_expression2 VALUES ("+str(self.spectrum_id)+','+str(self.hprdDic[gi])+',"'+str(pep)+'","'+str(float(score))+'","'+str(mass)+'","'+str(charge)+'","'+str(gi)+'","'+str(modification)+'")'
            self.Cursor.execute(sqlexp1)
        ###################################################################################
        #Dont execute sql by line by line, Print to a temp file then use Load SQL systax to upload file. then call a shell script to delte temp file.
