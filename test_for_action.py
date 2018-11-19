# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import re
import datetime
import time
 
L=()
L1=[]
L2=[]
f=open('case_log.txt')
for lines in f.readlines():
    if re.findall('ACTION',lines):
        L=lines
        print(L)
        print('######')
        L_split=L.split()
        print(L_split)
        print('aaaaaaa')
        for i in range(len(L_split)): 
            for j in range(len(L[i])):  
                continue
            continue
        L1.append(L_split[j+ 1]+ L_split[j+ 4])
        L2.append(L_split[j+ 4])
        continue
    continue
print(L1)
print('-------------------------')
print(L2)

LENG_TIME=len(L1)
print(LENG_TIME)
LENG_ACTION=len(L2)
print(LENG_ACTION)
print(L1[0])

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
print('L2 no item is same ')
print(L2)
print(len(L2))

########################################################################
#L1 including time and action eg : L1[ 194 ] 19:04:48,202VerifyFSATcp
#classify L1 using different actions
#L2[0:len[L2]]
class_for_each=[]
times_for_each=[]
k=0
dutation=[]
for n in range(len(L2)):
    #class_for_each.append(L2[n])
    class_for_each=L2[n]
    n=n+1
    print(class_for_each)
    #print(class_for_each[0],class_for_each.[1])
    for item in L1:
        if re.findall(class_for_each,item):
            class_for_each.append(item)
            print('class_for_each',n,class_for_each)
            l=len(class_for_each)
            print(l)
            for i in range(len(class_for_each)):
                times_for_each.append(class_for_each[i][0:12])
                i=i+1
                print('times_for_each=',times_for_each)
                while k<=len(times_for_each):
                    time_start=datetime.datetime.strptime(times_for_each[k], '%H:%M:%S,%f')
                    time_end=datetime.datetime.strptime(times_for_each[k+1], '%H:%M:%S,%f')
                    k=k+2
                    dutation.append(time_end-time_start)
                    print(time_end-time_start)
                    if(k>=len(times_for_each)):
                        break
                print(dutation)
##########################################################################        
Delay=[]
Verify=[]
SendLINMSG=[]
VerifyFSATcp=[]
Press=[]
Comments=[]
InputText=[]
StopCommand=[]
Click=[]
UIAClick=[]
ExecCommand=[]
UIAVerify=[]

print(L1)
for item in L1:
    if re.findall('Delay',item):
        Delay.append(item)
    if re.findall('SendLINMSG',item):
        SendLINMSG.append(item)
    if re.findall('VerifyFSATcp',item):
        VerifyFSATcp.append(item)
    if re.findall('Press',item):
        Press.append(item)
    if re.findall('Comments',item):
        Comments.append(item)
    if re.findall('InputText',item):
        InputText.append(item)
    if re.findall('StopCommand',item):
        StopCommand.append(item)
    if re.findall('Click',item):
        Click.append(item)
    if re.findall('UIAClick',item):
        UIAClick.append(item)
    if re.findall('ExecCommand',item):
        ExecCommand.append(item)
    if re.findall('UIAVerify',item):
        UIAVerify.append(item) 
    if re.findall('Verify',item):
        Verify.append(item)
  
print('Delay',Delay)
print('SendLINMSG',SendLINMSG)
print('VerifyFSATcp',VerifyFSATcp)
print('Press',Press)
print('Comments',Comments)
print('InputText',InputText)
print('StopCommand',StopCommand)
print('Click',Click)
print('UIAClick',UIAClick)
print('ExecCommand',ExecCommand)
print('UIAVerify',UIAVerify)
print('Verify',Verify)    

#work out with each class
times=[]
l=len(Verify)
print(l)
for i in range(len(Verify)):
    times.append(Verify[i][0:12])
    i=i+1
print('time=',times)

sum=0
k=0
chazhilist=[]
while k<=len(times):
    time1=datetime.datetime.strptime(times[k], '%H:%M:%S,%f')
    time2=datetime.datetime.strptime(times[k+1], '%H:%M:%S,%f')
    k=k+2
    chazhi=time2-time1
    chazhilist.append(chazhi)
    print(chazhi)
    if(k>=len(times)):
        break
print(chazhilist)


# for t in range(len(chazhilist)):
#     each=chazhilist[t]
#     each.split('.')


#字典方法： {action:time}
# 时间差：https://blog.csdn.net/sunjinjuan/article/details/79113120
# https://blog.csdn.net/alvin930403/article/details/54022338




    
    
