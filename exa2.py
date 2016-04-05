import csv
import pprint
import re
from googleapiclient.discovery import build
with open('input.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		#print (row['Title'], row['Url'], row['Director'], row['Alias'], row['Year'])
		query = row['Title']+' imdb '+row['Director']
		print 'Query :: ',query
		keys = ['AIzaSyBlU4hsYnl6oSvrKw8ZKiTrRmZzBUBANWs','AIzaSyB7BqsM_vljNSPOq4twbB7N3sUutyjoobE','AIzaSyCv6pMQ4ObhFbtWuM5Ge5CEmLZ5o_VcuXQ']	
		service = build("customsearch", "v1", developerKey="AIzaSyBlU4hsYnl6oSvrKw8ZKiTrRmZzBUBANWs")

  		res = service.cse().list(
      	q=query,cx='009241977094486741223:3agszpaq5sy',).execute()
  		#pprint.pprint(res)
  		# print "===================================="
  		# try:
  		# 	imdb_key = res['items'][0]['formattedUrl']
  		# 	imdb_key = re.search('^www.*?title/(.*?)/.*',imdb_key)
  		# 	print 'IMDB Key :: %s' % imdb_key.group(1)
  		# except Exception, e:
  		# 	print "Imdb key not found"
  		# 