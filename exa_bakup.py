import csv
#import traceback
#import pprint
import re
from googleapiclient.discovery import build
ik =[]
flag_1 = 0
flag_2 = 0
count = 0
keycount = 0
key = 0
with open('input.csv', 'rb') as csvinput:
	with open ('output.csv', 'wb') as csvoutput: 
		reader = csv.DictReader(csvinput)
		fieldnames = ['Entity','url','Director','Year','Alias','IMDB URL','genre','Runtime']
		writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)
		writer.writeheader()

		for row in reader:
			#print (row['Title'], row['Url'], row['Director'], row['Alias'], row['Year'])
			print "===================================="
			
			query = row['Entity']+' '+row['Director']+' '+row['Year']+' imdb'
			title = row['Entity']
			
			director = row['Director']
			director = re.sub(r', ','|',director)
			year = row['Year']
			alias = row['Alias']
			url = row['url']
			genre = row['genre']
			runtime = row['Runtime']
			print 'Tite:',title
			print 'Director:',director
			print 'Year:',year
			print 'Alias:',alias
			print 'URL:',url
			print 'Genre:',genre
			print 'Runtime:',runtime
			print 'Query :: ',query
			
			Api_keys = ['AIzaSyBlU4hsYnl6oSvrKw8ZKiTrRmZzBUBANWs','AIzaSyB7BqsM_vljNSPOq4twbB7N3sUutyjoobE','AIzaSyCv6pMQ4ObhFbtWuM5Ge5CEmLZ5o_VcuXQ']
			if count >= 81:
				keycount = 1
				if keycount == 1:
					service = build("customsearch", "v1", developerKey=Api_keys[key])
					res = service.cse().list(q=query,cx='009241977094486741223:3agszpaq5sy',).execute()
					response = res.get('items')
					key =+ 1
				count += 1
			else:
				count = 0
			
			#pprint.pprint(res)
			# response = res.get('items')
			if response:
				for i in range(0,len(response)):

					json_title = res['items'][i]['htmlTitle']
					json_title = re.sub(r'<.*?>','',json_title)
					print 'fetched title:',json_title.encode('utf8')
					
					json_director =res['items'][i]['htmlSnippet']
					json_director = re.sub(r'<.*?>','',json_director)
					print 'fetched director:',json_director.encode('utf8')
					

					if re.search(title,json_title,re.IGNORECASE) and re.search(director,json_director,re.IGNORECASE):
						imdb_key = res['items'][i]['formattedUrl']
						imdb_key = re.search('^www.*?title/(.*?)/.*',imdb_key)
						print 'IMDB Key :: ', imdb_key.group(1)

						
						ik = imdb_key.group(1)
						writer.writerow({'Entity':title,'Director':row['Director'],'Year':year,'Alias':alias,'url':url,'genre':genre,'Runtime':runtime,'IMDB URL':ik})
						flag_1 = 1
						break
					else:
						flag_2 = 1
						pass
							
						#writer.writerow({'Title':row['Title'],'Director':row['Director'],'Key':''}) 
	
			else:
			  	print "Imdb key not found"
			if flag_1 == 0 and flag_2 == 1:
				writer.writerow({'Entity':title,'Director':row['Director'],'Year':year,'Alias':alias,'url':url,'genre':genre,'Runtime':runtime,'IMDB URL':''})
