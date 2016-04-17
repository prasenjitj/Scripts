# -*- coding: utf-8 -*-
import imdb
import csv
import re
with open('Book2.csv', 'rb') as csvinput:
    with open ('output2.csv', 'wb') as csvoutput: 
        reader = csv.DictReader(csvinput)
        fieldnames = ['Entity','url','Director','Year','Alias','IMDB_OLD','IMDB URL','genre','Runtime']
        writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            #print (row['Title'], row['Url'], row['Director'], row['Alias'], row['Year'])
            print "===================================="
            
            query = row['Entity']+' '+row['Year']
            title = row['Entity'].lower().strip()

            director = row['Director'].lower().strip()
            director = director
            year = row['Year'].strip()
            # alias = row['Alias'].rstrip()
            # url = row['Url'].rstrip()
            # genre = row['genre'].rstrip()
            # runtime = row['Runtime'].rstrip()
            # IMDB = row['IMDB'].strip()

            print 'Query:',query
            print 'Search Title:',title
            print 'Search Year:',year
            print 'Search Director:',director


            imdb_access = imdb.IMDb()
            movie_list = imdb_access.search_movie(title)
            for item in range(0,len(movie_list)):
                ak = []
                result = movie_list[item]
                imdb_access.update(result)
                result = result.summary()

                print result.encode('utf-8')

                Title = movie_list[item].get('title').lower().strip()
                # Title = re.search(r'Title:(.*?)\n',result)
                # Title = Title.group(1)
                # Title = re.sub(r'\(.*?\)','',Title).lower().strip()

                # Year = re.search(r'Title:(.*?)\n',result)
                # Year = Year.group(1)
                # Year = re.sub(r'^.*?\(','',Year)
                # Year = Year.replace(')','').strip()
                Year = movie_list[item].get('year')
                print 'Result Year ::',Year 

                print 'Result Title ::',Title.encode('utf-8')
                
                ak = []
                akas = movie_list[item].get('akas') or []
                aka_list = []
                for aka in akas:
                    aka_split = aka.split('::', 1)
                    if len(aka_split) < 2:
                        continue
                    aka_list.append(aka_split)
                print 'AKA LIST::',aka_list

                for i in range(0,len(aka_list)):
                    ak_low = aka_list[i][0].lower()
                    ak.append(ak_low)
                print ak



                Director = re.search(r'Director:(.*?)\n',result) or []
                if Director:
                    Director = Director.group(1).replace('.','').strip()
                    Director = Director.lower().encode('utf-8')
                    print 'Result Director ::',Director
                else:
                    print 'Director not found'
                
                imdb_key = ''
                flag = 0
                if Title == title and director in Director:
                    print 'movie found (Director match)'
                    imdb_key = movie_list[item].movieID
                    imdb_key = 'www.imdb.com/title/tt'+imdb_key
                    print imdb_key
                    writer.writerow({'Entity':row['Entity'],'Director':row['Director'],'Year':year,'url': row['url'],'IMDB_OLD': row['IMDB_OLD'],'IMDB URL':imdb_key})
                    break
                elif Title == title and Year == year:
                    print 'movie found (Year match)'
                    imdb_key = movie_list[item].movieID
                    imdb_key = 'www.imdb.com/title/tt'+imdb_key
                    print imdb_key
                    writer.writerow({'Entity':row['Entity'],'Director':row['Director'],'Year':year,'url': row['url'],'IMDB_OLD': row['IMDB_OLD'],'IMDB URL':imdb_key})
                    break
                elif title in ak and director in Director:
                    print 'movie found (AKA match)'
                    imdb_key = movie_list[item].movieID
                    imdb_key = 'www.imdb.com/title/tt'+imdb_key
                    print imdb_key
                    writer.writerow({'Entity':row['Entity'],'Director':row['Director'],'Year':year,'url': row['url'],'IMDB_OLD': row['IMDB_OLD'],'IMDB URL':imdb_key})
                    break                    
                else:
                    print 'movie not found'
                    flag = 1
            if flag == 1:
                writer.writerow({'Entity':row['Entity'],'Director':row['Director'],'Year':year,'url': row['url'],'IMDB_OLD':row['IMDB_OLD'],'IMDB URL':imdb_key})