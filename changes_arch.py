#!/usr/bin/python
#{"name":"flare.analytics.cluster.AgglomerativeCluster","size":3938,"imports":["flare.animate.Transitioner","flare.vis.data.DataList","flare.util.math.IMatrix","flare.analytics.cluster.MergeEdge","flare.analytics.cluster.HierarchicalCluster","flare.vis.data.Data"]},

import os
import random as rand
import json

LINE_LIST=[]
d={}
with open('apache-log4j-2.5-src_deps.rsf','r') as f:  
	for line in f:
		LINE_LIST.append(line)
	for i in range(0,len(LINE_LIST)):
		key=LINE_LIST[i].rstrip().split(' ')[1]
		if key not in d:
			d.setdefault(key,[])
		value=LINE_LIST[i].rstrip().split(' ')[2]
		d[key].append(value)
print len(d)
print key
print d[key]
print len(d[key])

target = open('output_2.5.txt', 'w')
target.truncate()

