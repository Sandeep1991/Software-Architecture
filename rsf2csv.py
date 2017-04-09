#!/usr/bin/python
#{"name":"flare.analytics.cluster.AgglomerativeCluster","size":3938,"imports":["flare.animate.Transitioner","flare.vis.data.DataList","flare.util.math.IMatrix","flare.analytics.cluster.MergeEdge","flare.analytics.cluster.HierarchicalCluster","flare.vis.data.Data"]},

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
print len(d1)
print key
print d1[key]
print len(d1[key])


target = open('output_csv_2.5.csv', 'w')
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

