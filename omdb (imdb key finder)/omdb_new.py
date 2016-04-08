import requests
import json
import csv
# import re
with open('2015 Seattle Lesbian & Gay Film Festival - Film Festival.csv', 'rb') as csvinput:
	with open ('output.csv', 'wb') as csvoutput: 
		reader = csv.DictReader(csvinput)
		fieldnames = ['Entity','Url','Director','Year','Alias','IMDB_OLD','IMDB URL','genre','Runtime']
		writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)
		writer.writeheader()
		for row in reader:
			#print (row['Title'], row['Url'], row['Director'], row['Alias'], row['Year'])
			print "===================================="
			
			query = row['Entity']+' '+row['Director']+' '+row['Year']+' imdb'
			title = row['Entity'].strip()

			director = row['Director']
			year = row['Year'].strip()
			alias = row['Alias'].rstrip()
			url = row['Url'].rstrip()
			genre = row['genre'].rstrip()
			runtime = row['Runtime'].rstrip()
			imdb = row['IMDB'].strip()
			URL = 'http://www.omdbapi.com/?t='+title+'&plot=full&r=json'

			print URL
			print 'Search Title:',title
			print 'Search Year:',year
			print 'Search Director:',director
			res = requests.get(URL)
			result = res.content
			obj = json.loads(result)
			#print obj
			print obj['Response']
			#print len(obj)
			if obj['Response'] == 'True':
				print obj['Title'].encode('utf-8')
				print obj['Director'].encode('utf-8')
				print obj['Year'].encode('utf-8')
				print 'www.imdb.com/title/'+obj.get('imdbID')
				if obj['Title'].lower() == title.lower() and obj['Director'].lower() == director.lower():
					imdb_key = obj.get('imdbID')

					print 'Imdb url:'+'www.imdb.com/title/'+imdb_key
					writer.writerow({'Entity':title,'Director':row['Director'],'Year':year,'Alias':alias,'Url':url,'genre':genre,'Runtime':runtime,'IMDB_OLD': imdb,'IMDB URL':imdb_key})
				else:
					print 'key not found'
					writer.writerow({'Entity':title,'Director':row['Director'],'Year':year,'Alias':alias,'Url':url,'genre':genre,'Runtime':runtime,'IMDB_OLD': imdb,'IMDB URL':''})				
				
			else:
				writer.writerow({'Entity':title,'Director':row['Director'],'Year':year,'Alias':alias,'Url':url,'genre':genre,'Runtime':runtime,'IMDB_OLD': imdb,'IMDB URL':''})
				print 'no response'