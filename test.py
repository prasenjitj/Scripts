import requests
import json
import csv
import re
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
			# url = 'http://www.omdbapi.com/?t='+title+'&y='+year+'&plot=full&r=json'
			url = 'http://www.omdbapi.com/?t='+title+'&plot=full&r=json'

			print url
			res = requests.get(url)
			result = res.content
			obj = json.loads(result)
			print obj
			print obj['Response']
			# print type(obj)
			if obj['Response'] == 'True':
				print '$$'
				imdb_key = obj.get('imdbID')
				print imdb_key
								
			# 	json_director =result.Director
				writer.writerow({'Entity':title,'Director':row['Director'],'Year':year,'Alias':alias,'url':url,'genre':genre,'Runtime':runtime,'IMDB URL':imdb_key})
			else:
				writer.writerow({'Entity':title,'Director':row['Director'],'Year':year,'Alias':alias,'url':url,'genre':genre,'Runtime':runtime,'IMDB URL':''})
	
