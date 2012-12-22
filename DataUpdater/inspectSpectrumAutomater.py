import os
class inspectSpectrum:
    def __init__(self,inFile,outFile):
        self.inFile=inFile
        self.outFile=outFile
        self.folder=os.system("mkdir "+inFile+"")

    def generateSpectrum(self):
        spectrum=self.inFile.xreadlines()

        #specIn = open('spectrumIndex.html','w')
        #spectrum = open('PValuedResults.txt','r')

        spectrum.next()
        for each in spectrum:
    	    each_spt = each.strip('\n').split('\t')
	    try:
	        os.system("python Label.py -r "+self.inFile+" -b "+each_spt[-1]+" -a "+each_spt[2]+" -w "+self.folder+"/"+each_spt[-1]+".png -v "+self.folder+'/'+each_spt[-1]+".txt")
	    except AttributeError:
		pass
