#!/usr/bin/python
#{"name":"flare.analytics.cluster.AgglomerativeCluster","size":3938,"imports":["flare.animate.Transitioner","flare.vis.data.DataList","flare.util.math.IMatrix","flare.analytics.cluster.MergeEdge","flare.analytics.cluster.HierarchicalCluster","flare.vis.data.Data"]},

import os
import random as rand
import json

LINE_LIST=[]
d1={}
with open('apache-log4j-2.3-src_deps.rsf','r') as f1:  
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

d2={}
with open('apache-log4j-2.5-src_deps.rsf','r') as f2:  
	for line in f2:
		LINE_LIST.append(line)
	for i in range(0,len(LINE_LIST)):
		key=LINE_LIST[i].rstrip().split(' ')[1]
		if key not in d2:
			d2.setdefault(key,[])
		value=LINE_LIST[i].rstrip().split(' ')[2]
		d2[key].append(value)
print len(d2)
print key
print d2[key]
print len(d2[key])
print "----------------------------------------------"
del_set=set([])
target = open('output_cmp.txt', 'w')
target.truncate()
target.write("Deletions: ")
target.write("\n")
target.truncate()
for arch_class in d1:
	if arch_class not in d2:
		#print arch_class
		del_set.add(arch_class)
		target.write(arch_class)
		target.write("\n")
		
print "-----------------------------------------------"
add_set=set([])
target.truncate()
target.write("Additions: ")
target.write("\n")
target.truncate()
for arch_class in d2:
	if arch_class not in d1:
		#print arch_class
		add_set.add(arch_class)
		target.write(arch_class)
		target.write("\n")
	
print len(add_set)
