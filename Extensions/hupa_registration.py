#!/usr/bin/python

import MySQLdb

def hupa_registration (fName, lName, username, password):
	conn = MySQLdb.connect(host="localhost", user="xxx", passwd="xxxx",db="HuPA")
        curs = conn.cursor()
	username_check_query="select count(*) from User_Details where username = '"+str(username)+"'"
	curs.execute(username_check_query)
	data = curs.fetchall()
	verify_user=data[0][0]
	
	
	if verify_user != 0:
		curs.close()
		conn.close()
		return "exists"
	if verify_user == 0:
		input_str="insert into User_Details values (0, '"+str(fName)+"', '"+str(lName)+"', '"+str(username)+"', '"+str(password)+"')"
		curs.execute(input_str)
		conn.commit()
	curs.close()
	conn.close()
	return "a"

