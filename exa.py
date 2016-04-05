import csv
import pprint
import re
from googleapiclient.discovery import build
with open('input.csv', 'rb') as csvinput:
	with open ('output.csv', 'wb') as csvoutput: 
		reader = csv.DictReader(csvinput)
		fieldnames = ['Title', 'Director','Key']
		writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)
		writer.writeheader()
		for row in reader:
			#print (row['Title'], row['Url'], row['Director'], row['Alias'], row['Year'])
			print "===================================="
			query = row['Title']+' imdb '+row['Director']
			title = row['Title']
			print 'Tite:',title
			director = row['Director']
			director = re.sub(r', ','|',director)
			print 'Director:',director
			print 'Query :: ',query
			keys = ['AIzaSyBlU4hsYnl6oSvrKw8ZKiTrRmZzBUBANWs','AIzaSyB7BqsM_vljNSPOq4twbB7N3sUutyjoobE','AIzaSyCv6pMQ4ObhFbtWuM5Ge5CEmLZ5o_VcuXQ']	
			service = build("customsearch", "v1", developerKey="AIzaSyB7BqsM_vljNSPOq4twbB7N3sUutyjoobE")
			res = service.cse().list(q=query,cx='009241977094486741223:3agszpaq5sy',).execute()
			#pprint.pprint(res)
			#print type(res)

			try:
				for i in range(0,len(res['items'])):

					print i
					json_title = res['items'][i]['htmlTitle']
					#print json_title.encode('utf8')
					json_director =res['items'][i]['htmlSnippet']
					#print json_director.encode('utf8')

					if re.search(title,json_title) and re.search(director,json_director):
						imdb_key = res['items'][i]['formattedUrl']
						imdb_key = re.search('^www.*?title/(.*?)/.*',imdb_key)
						print 'IMDB Key :: ', imdb_key.group(1)
						ik = ''.join(imdb_key.group(1))
						writer.writerow({'Title':row['Title'],'Director':row['Director'],'Key':ik})
						break
					else:
						print 'KEY NOT FOUND'  


			except Exception, e:
				print "Exception",e



	
  	



