#!/usr/bin/python# -*- coding: utf-8 -*-import reimport csvfrom googleapiclient.discovery import build# class Hasher(dict):# 		# http://stackoverflow.com/a/3405143/190597# 		def __missing__(self, key):# 				value = self[key] = type(self)()# 				return valueik =[]count = 0keycount = 0key = 0with open('Book1.csv', 'rb') as csvinput:	with open ('output2.csv', 'wb') as csvoutput: 		reader = csv.DictReader(csvinput)		fieldnames = ['Entity','url','Director','Year','Alias','IMDB URL','genre','Runtime']		writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)		writer.writeheader()		for row in reader:			# print (row['Entity'], row['Url'], row['Director'], row['Alias'], row['Year'])						t = row['Entity']			d = row['Director']			print t, d			year = row['Year']			alias = row['Alias']			url = row['Url']			genre = row['genre']			runtime = row['Runtime']			query = t + " imdb"			# print 'Tite:',title			# print 'Director:',director			# print 'Year:',year			# print 'Alias:',alias			# print 'URL:',url			# print 'Genre:',genre			# print 'Runtime:',runtime			# print 'Query :: ',query			# query = 'Showboy'			service = build("customsearch", "v1", developerKey='AIzaSyDmbZ0vNfEqMWekMdJqZDq6kUDhNqcaGss')			res = service.cse().list(q=query,cx='009241977094486741223:3agszpaq5sy',).execute()			response = res.get('items')			# pprint.pprint(res)			response = res.get('items')			if response:				imdb_key =''				for i in range(0,len(response)):					flag = 0					check = 0					print "===================================="					json_title = res['items'][i]['pagemap']['metatags'][0]['title']					json_title = re.sub(r'<.*?>','',json_title)					# print 'fetched title:',json_title					json_director = res['items'][i]['snippet']					json_director = re.sub(r'...','',json_director)					json_director = re.search(d,json_director)				 					if re.sub(r'\s+\(.*','',json_title).strip() == t:						print "##"						if json_director is None:							print "###"							try:								print 'isnside try'								json_director = res['items'][i]['pagemap']['metatags'][0].get('og:description')								json_director = re.search(d,json_director)								if json_director:									print '####' 									if json_director.group(0) == d:										print '#####'										imdb_key = res['items'][i]['link']										print imdb_key										writer.writerow({'Entity':t,'Director':row['Director'],'Year':year,'Alias':alias,'url':url,'genre':genre,'Runtime':runtime,'IMDB URL':imdb_key})																				check = 1										break									else:										print "######"																except:								print "director not found"													else:						print 'no key found'						flag = 1				if flag == 1 and check == 0:					print "VO == VO == VO"					print flag						writer.writerow({'Entity':t,'Director':row['Director'],'Year':year,'Alias':alias,'url':url,'genre':genre,'Runtime':runtime,'IMDB URL':imdb_key})			elif response is None:				print 'No Response'				writer.writerow({'Entity':t,'Director':row['Director'],'Year':year,'Alias':alias,'url':url,'genre':genre,'Runtime':runtime,'IMDB URL':imdb_key})