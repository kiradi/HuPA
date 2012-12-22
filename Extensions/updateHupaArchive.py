#import os
import subprocess
def updateHupaArchive():
	#doScp="scp hupalist@mail.ibioinformatics.org:/var/spool/mail/hupalist /var/lib/mailman/archives/private/hupalist.mbox/hupalist.mbox"
	#os.system(doScp)
	#doArchive="/usr/lib/mailman/bin/arch --wipe hupalist"
	#os.system(hupalistArchive.sh)
	subprocess.call("hupalistArchive.sh",shell=True)
	#print 'test Print'
	return None

#print updateHupaArchive()
