import re
import sys
from collections import defaultdict
from collections import OrderedDict

infile = sys.argv[1]
#outfile = sys.argv[2]

f=open(infile,'r')

data=f.read().strip()
data=data.split('\n')
header=data[0]
d={}
d1={}
dd=defaultdict(list)
#print data
list1=[]
list2=[]
values=[]

for i in data:
	key=re.findall(r'.*2016\thttp',i)
	key=tuple(key)
	print key
	value=re.findall(r'http:\/.*',i)
	value=''.join(value)
	value=re.sub(r'\s*REC#.*','',value).split()
	#print type(value)
	#print value
	new=OrderedDict(zip(key,value))
	#print new
	list1.append(new)
	#print list1
	
	for x in range(0,len(key)):
		dd[key[x]]=[]
		dd=OrderedDict(dd)
#print dd
tag=dd.keys()
#print tag

dd2=defaultdict(list)

with open ('2.tsv','w') as f1:
	f1.write(header+'\n')
	for row in list1:
		for k in tag:
			
			if k not in row.keys():
				#dd[k]=''
				#print 'false'
				continue
			else:
				dd[k]=row[k]
				#print 'true', row[k]
			dd2[k].append(dd[k])
	#print dd2
	
	for v1, v2 in dd2.items():
		f1.write(v1+', '.join(v2)+'\n')
