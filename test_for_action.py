# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import re
import datetime
import time
import xlsxwriter
import xlwt
 
L=()
L1=[]
L2=[]
f=open('case_log.txt')

#Extract time and name for each action
for lines in f.readlines():
    if re.findall('ACTION',lines):
        L=lines
        L_split=L.split()
        for i in range(len(L_split)): 
            for j in range(len(L[i])):  
                continue
            continue
        L1.append(L_split[j+ 1]+ L_split[j+ 4])
        L2.append(L_split[j+ 4])
        continue
    continue
print(len(L1),L1)
print(len(L2),L2)
i=0
for x in range(len(L1)):
    print('L1[',i,']',L1[x])
    i=i+1
j=0
for y in range(len(L2)):
    print('L2[',j,']',L2[y])
    j=j+1
#delete the same item in L2
L2 = list(set(L2))
print('L2 no item is same ','\n',len(L2),'\n',L2)####!!!
########################################################################
#L1 including time and action eg : L1[ 194 ] 19:04:48,202VerifyFSATcp
#classify L1 using different actions
#L2[0:len[L2]]
class_for_each=[]
class_for_each_list=[]
times_for_each=[]
k=0
dutation=[]
dutation_all_action=[]
dutation_for_each_action=[]
average_for_all_action=[]
dic_average_for_all_action=[]
create_dict={}
for n in range(len(L2)):
    class_for_each=L2[n] 
    print(class_for_each)
    for item in L1:
        if re.findall(class_for_each,item):
            class_for_each_list.append(item)
            l=len(class_for_each_list)
            print(l)
    #n=n+1
    for i in range(len(class_for_each_list)):
        times_for_each.append(class_for_each_list[i][0:12])
        i=i+1
    while k<=len(times_for_each):
        time_start=datetime.datetime.strptime(times_for_each[k], '%H:%M:%S,%f')
        time_end=datetime.datetime.strptime(times_for_each[k+1], '%H:%M:%S,%f')
        k=k+2
        dutation.append(time_end-time_start)
        dutation_sec=(time_end-time_start).seconds+(time_end-time_start).microseconds/1000000 
        dutation_for_each_action.append(dutation_sec)
        if(k>=len(times_for_each)):
            break
    print(time_end-time_start)
    print('dutation for',class_for_each,dutation,)
    print('dutation_for_each_action for',class_for_each,dutation_for_each_action)
	   ###!!!use the size of each action in create a excel-->size_for_action
    size_for_action=len(dutation_for_each_action)
    average_for_each_action=sum(dutation_for_each_action)/len(dutation_for_each_action)
    print('average_for_each_action',class_for_each,average_for_each_action)
	
	   ###create a dict for 'class_for_each' and 'average_for_each_action'
	   #m=0;
	   ######length=len(class_for_each)
	   dit=[]
	   dit={class_for_each[n]:average_for_each_action[n]}
	   dict.update(dit)
	   #create_dict=dict(zip(class_for_each,average_for_each_action))
	   #dic_average_for_all_action.append(create_dict)
    average_for_all_action.append(average_for_each_action)
	
    print('average_for_all_action',average_for_all_action)
	   #print('dic_average_for_all_action',dic_average_for_all_action)
    #sort_average_for_all_action=sorted(average_for_all_action)
    
    class_for_each_list=[]
    class_for_each=[]
    times_for_each=[]
    k=0
    dutation=[]
   	n=n+1
sort_average_for_all_action=sorted(average_for_all_action)
sort_dic_for_all_action=sorted(dic_average_for_all_action)

print('sort_average_for_all_action',sort_average_for_all_action)
print('sort_dic_average_for_all_action',sort_dic_for_all_action)
##sort_average_for_all_action should contanst with its name "class_for_each"
##verify need to find out more correctly
##!!!

#生成excel文件
def generate_excel(action_log):
    excel_init_file = xlsxwriter.Workbook('./action_log.xlsx')
    worksheet = excel_init_file.add_worksheet('action_log')
	title_bold = excel_init_file.add_format({'bold': True, 'border': 2, 'bg_color':'blue'})
	style=xlwt.easyxf('pattern: pattern solid, fore_color red')
	worksheet.write(0,0,'action_name')
	worksheet.write(0,1,'average_for_each_action')
	worksheet.write(0,2,'rank')
	
	for i,date in enumerate(sort_dic_for_all_action):
        for j, each_line in enumerate(date): 
            if float(each_line[1]) >= 2:
                for k,value in enumerate(each_line):
                    worksheet.write(j+1, k, value, style)
            else:
                for k,value in enumerate(each_line):
                    worksheet.write(j+1, k, value)     
	
	





    
    
