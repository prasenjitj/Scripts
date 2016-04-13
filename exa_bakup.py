#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import csv
import mysql.connector
from googleapiclient.discovery import build

conn = mysql.connector.connect(host='localhost',database='test',user='root',password='')
print('Connected to MySQL database')
cursor = conn.cursor()
cursor.execute("SELECT * FROM api")
rows = cursor.fetchall()



count = 0
keycount = 0
key = 0
keycount = 0
keys = 1
key_id =''
with open('Book2.csv', 'rb') as csvinput:
	with open ('output3.csv', 'wb') as csvoutput: 
		reader = csv.DictReader(csvinput)
		fieldnames = ['Entity','url','Director','Year','Alias','IMDB_OLD','IMDB URL','genre','Runtime']
		writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)
		writer.writeheader()

		for row in reader:
			# print (row['Entity'], row['Url'], row['Director'], row['Alias'], row['Year'])
			
			t = row['Entity'].lower()
			d = row['Director'].lower()
			d = re.sub(r'(,\s.*)','',d).strip()
			print t, d
			year = row['Year']
			alias = row['Alias']
			url = row['url']
			genre = row['genre']
			runtime = row['Runtime']
			IMDB_OLD = row['IMDB_OLD']
			query = t + ' ' + d
			# print 'Tite:',title
			# print 'Director:',director
			# print 'Year:',year
			# print 'Alias:',alias
			# print 'URL:',url
			# print 'Genre:',genre
			# print 'Runtime:',runtime
			# print 'Query :: ',query
			# query = 'Showboy'

			keycount += 1
			if keycount == 99:
				keycount = 1
			if keycount == 1:
				keys	+= 1
				for i in rows:
					key_id = i[1]
					print key_id

			service = build("customsearch", "v1", developerKey=key_id)
			res = service.cse().list(q=query,cx='009241977094486741223:3agszpaq5sy',).execute()
			response = res.get('items')

			# pprint.pprint(res)
			response = res.get('items')

			imdb_key =''
			if response:
				


				for i in range(0,len(response)):
					flag = 0
					check = 0
					print "===================================="
					json_title = res['items'][i]['pagemap']['metatags'][0]['title'].lower()
					json_title = re.sub(r'<.*?>','',json_title)
					print 'fetched title:',json_title.encode('utf-8')
					json_director = res['items'][i]['snippet'].lower()
					print json_director.encode('utf-8')
					json_director = re.search(d,json_director)
				 
					if re.sub(r'\s+\(.*','',json_title).strip() == t:
						print "##"
						if json_director is None:
							print "###"
							try:
								print 'isnside try'
								json_director = res['items'][i]['pagemap']['metatags'][0].get('og:description').lower()
								print d
								print json_director.encode('utf-8')
								json_director = re.search(d,json_director)
								if json_director:
									print '####' 
									if json_director.group(0) == d:
										print '#####'
										imdb_key = res['items'][i]['link']
										print imdb_key
										writer.writerow({'Entity':t,'Director':row['Director'],'Year':year,'Alias':alias,'url':url,'genre':genre,'Runtime':runtime,'IMDB_OLD': IMDB_OLD,'IMDB URL':imdb_key})
										
										check = 1
										break
									else:
										print "######"
								else:
									print "director not found:"
									flag = 1		
									
							except:
								print "Exception caught, no og:description"
						else:
							if json_director.group(0) == d:
								print '#####'
								imdb_key = res['items'][i]['link']
								print imdb_key
								writer.writerow({'Entity':t,'Director':row['Director'],'Year':year,'Alias':alias,'url':url,'genre':genre,'Runtime':runtime,'IMDB_OLD': IMDB_OLD,'IMDB URL':imdb_key})
										
								check = 1
								break		
								
					else:
						print 'no key found'
						flag = 1
				if flag == 1 and check == 0:
					print "VO == VO == VO"
					print flag	
					writer.writerow({'Entity':t,'Director':row['Director'],'Year':year,'Alias':alias,'url':url,'genre':genre,'Runtime':runtime,'IMDB_OLD': IMDB_OLD,'IMDB URL':imdb_key})
			elif response is None:
				print 'No Response'
				writer.writerow({'Entity':t,'Director':row['Director'],'Year':year,'Alias':alias,'url':url,'genre':genre,'Runtime':runtime,'IMDB_OLD': IMDB_OLD,'IMDB URL':imdb_key})
conn.close()
