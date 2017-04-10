#!/usr/bin/python
'''
{
 "name": "apache",
 "children": [
  {
   "name": "analytics*cluster*log4j",
   "children": [
      {"name": "AgglomerativeCluster", "size": 3938},
      {"name": "CommunityStructure", "size": 3812},
      {"name": "HierarchicalCluster", "size": 6714},
      {"name": "MergeEdge", "size": 743}
	]
	}
 ]
}

'''
import os
import random as rand
import json

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
keylist = d1.keys()
keylist.sort()
print len(d1)
print key
print d1[key]
print len(d1[key])


target = open('output_react.json', 'w')
target.truncate()
target.write('{')
target.write("\n")
target.write('"name":"apache",')
target.write("\n")
target.write('"children":[')
target.write("\n")
target.truncate()
cnt_d=0
for k in keylist:
	cnt_d += 1
	word_d=k.replace('.','*')
	#word_d=wrd.replace('.','*')
	m=d1[k]
	l='{"name":"'+word_d+'('+str(len(m))+')",'
	#n_l='apache.'+word_d+'('+str(len(m))+').'
	target.write(l)
	target.write("\n")
	target.write('"children":[')
	target.write("\n")
	word_v=''
	cnt=0
	for j in m:
		cnt += 1
		word_v=j
		wvr=word_v.replace('.','*')
		if cnt != len(m):
			target.write('{"name":"'+wvr+'","size":100},')
			target.write("\n")
		else:
			target.write('{"name":"'+wvr+'","size":100}')
			target.write("\n")
			target.write(']')
			target.write("\n")
	if cnt_d != len(d1):
		target.write('},')
		target.write("\n")
	else:
		target.write('}')
		target.write("\n")
target.write("]")
target.write("\n")
target.write("}")
			
