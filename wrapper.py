#!/usr/bin/python
import sys,traceback
import os
import json

print "Enter the file path"
file1=raw_input()
print "Enter the second file path"
file2=raw_input()
if file1=='' and file2=='':
	print "No file paths provided ....... Exited!"
	sys.exit(0)

if file1=='' and file2!='':
	file1,file2=file2,file1
	
#Read the file and write to local temporary file


if file1!='':
	target1 = open('temp1.txt', 'w')
	target1.truncate()
	with open(file1,'r') as f1:
		for line in f1:
			target1.write(line)
	target1.close()
	

	LINE_LIST=[]
	d1={}
	with open('apache-log4j-2.5-src_deps.rsf','r') as f1:  
		for line in f1:
			LINE_LIST.append(line)
		for i in range(0,len(LINE_LIST)):
			key=LINE_LIST[i].rstrip().split(' ')[1]
			if key not in d1:
				d1.setdefault(key,[])
			value=LINE_LIST[i].rstrip().split(' ')[2]
			d1[key].append(value)
	print len(d1)
	print key
	print d1[key]
	print len(d1[key])


	target = open('output_csv1.csv', 'w')
	target.truncate()
	target.write('id,value')
	target.write("\n")
	target.write('apache,')
	target.write("\n")
	target.truncate()
	for k in d1:
		word_d=k.replace('.','*')
		#word_d=wrd.replace('.','*')
		m=d1[k]
		l='apache.'+word_d+'('+str(len(m))+'),'
		n_l='apache.'+word_d+'('+str(len(m))+').'
		target.write(l)
		target.write("\n")
		word_v=''
		for j in m:
			word_v=j
			wvr=word_v.replace('.','*')
			target.write(n_l+wvr+',100')
			target.write("\n")
		
	
	
	
	
if file2!='':
	target2 = open('temp2.txt', 'w')
	target2.truncate()
	with open(file2,'r') as f2:
		for line in f2:
			target2.write(line)
	target2.close()
	
