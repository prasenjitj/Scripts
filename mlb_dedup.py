import re
import sys
from collections import defaultdict
from collections import OrderedDict

infile = sys.argv[1]
outfile = sys.argv[2]

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

key=header.split('\t')
#print key
#
for i in range(1,len(data)):
    value=data[i]
    value=value.split('\t')
    if value[3] == '':
    	#print 'test'
    	value = ''
    #print value[3]
    #print value
    new=OrderedDict(zip(key,value))
    #print new
    list1.append(new)
record= list1
#print record


for j in record:
	print j['player']
	x_id = j['transaction_id']+'#'+j['player']+'#'+j['team']+'#'+j['type']
	#print  ex_id
	description = '*Find or create each transaction and curate as per guidelines* Player Name: '+j['player']+' # Team Name: '+j['team']+' # Type: '+j['type']+' # Transaction: '+j['note']+' # Transaction date: '+j['trans_date']
	task_type = '/common/topic'
	j['Description']=description
	j['external_id']=ex_id
	j['Task_Type'] = task_type
	list2.append(j)
#print list2