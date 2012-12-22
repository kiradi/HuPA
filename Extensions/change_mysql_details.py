import os,re

file_list = os.listdir(os.getcwd())


file_list.remove('change_mysql_details.py')
file_list.remove('original')
file_list.remove('Journal')

for each_file in file_list:
	each_file = each_file.strip()
	main_data = open(each_file,'r').readlines()
	
	out_str = []
	for m in main_data:
		#print m
		#connection=Connection(conv=my_conv, host="localhost", user="root", passwd="password", db="pid")
		if m.find('host=') != -1:
			m = m.replace('xxx.xxx.x.xxx','localhost')
			#print m
		out_str.append(m)
	file_w = file(each_file,'w')
	file_w.write(str(''.join(out_str)))
	file_w.close()
	#break
	
