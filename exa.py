import csv
#import traceback
#import pprint
import re
from googleapiclient.discovery import build
ik =[]
with open('input.csv', 'rb') as csvinput:
	with open ('output.csv', 'w') as csvoutput: 
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
			service = build("customsearch", "v1", developerKey="AIzaSyCv6pMQ4ObhFbtWuM5Ge5CEmLZ5o_VcuXQ")
			res = service.cse().list(q=query,cx='009241977094486741223:3agszpaq5sy',).execute()
			#pprint.pprint(res)
			#print type(res)
			response = res.get('items')
			if response:
				for i in range(0,len(response)):

					json_title = res['items'][i]['htmlTitle']
					
					json_director =res['items'][i]['htmlSnippet']
					

					if re.search(title,json_title,re.IGNORECASE) and re.search(director,json_director,re.IGNORECASE):
						imdb_key = res['items'][i]['formattedUrl']
						imdb_key = re.search('^www.*?title/(.*?)/.*',imdb_key)
						print 'IMDB Key :: ', imdb_key.group(1)

						
						ik = imdb_key.group(1)
						
						writer.writerow({'Title':row['Title'],'Director':row['Director'],'Key':ik})

						break
					
						#writer.writerow({'Title':row['Title'],'Director':row['Director'],'Key':''}) 
	
			else:
			  	print "Imdb key not found"
			  	writer.writerow({'Title':row['Title'],'Director':row['Director'],'Key':''})
