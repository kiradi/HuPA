#!/usr/bin/python
import time
import MySQLdb
def Update_MailManager(mail_no,pi_reply,pi_comment,ap_reply,ap_comment,data_req_snt,data_req_pi_reply,data_req_pi_rep_commnt,data_received):
	conn = MySQLdb.connect(host="localhost", user="xxx", passwd="xxxx",db="HuPA")
        cursor = conn.cursor()
	if pi_reply is not 'off':
		pi_reply = timer()	#time.strftime("%Y-%m-%d", time.localtime(time.time()))
		upSql="UPDATE mailManagerInfo SET contributer_reply='"+str(pi_reply)+"' where mail_no="+str(mail_no)
		cursor.execute(upSql)
	#if pi_comment is not 'off':
	#	upSql="UPDATE mailManagerInfo SET contributer_comment='"+str(pi_comment)+"' where mail_no="+str(mail_no)
	
	if ap_reply is not 'off':
		ap_reply = timer()
		upSql="UPDATE mailManagerInfo SET ap_reply='"+str(ap_reply)+"' where mail_no="+str(mail_no) 
		cursor.execute(upSql)
	if data_req_snt is not 'off':
		data_req_snt= timer()
		upSql="UPDATE mailManagerInfo SET data_request_sent='"+str(data_req_snt)+"' where mail_no="+str(mail_no)
		cursor.execute(upSql)
	if data_req_pi_reply is not 'off':
		data_req_pi_reply = timer()
		upSql= "UPDATE mailManagerInfo SET contributer_reply_to_data_req='"+str(data_req_pi_reply)+"' where mail_no="+str(mail_no)
		cursor.execute(upSql)

	if data_received is not 'off':
		data_received= timer()	
		upSql="UPDATE mailManagerInfo SET data_recieved='"+str(data_received)+"' where mail_no="+str(mail_no)
		cursor.execute(upSql)
	if pi_comment is not 'off':
		upSql="UPDATE mailManagerInfo SET contributer_comment='"+str(pi_comment)+"' where mail_no="+str(mail_no)
		cursor.execute(upSql)
	if ap_comment is not 'off':
		upSql="UPDATE mailManagerInfo SET ap_comment='"+str(ap_comment)+"' where mail_no="+str(mail_no)
		cursor.execute(upSql)
	if data_req_pi_rep_commnt is not 'off':
		upSql="UPDATE mailManagerInfo SET data_req_comment='"+str(data_req_pi_rep_commnt)+"' where mail_no="+str(mail_no)
		cursor.execute(upSql)

def timer():
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
	return final_time	
