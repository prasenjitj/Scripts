# -*- coding: utf-8 -*-
import imdb
import re
imdb_access = imdb.IMDb()
movie_list = imdb_access.search_movie('democracy in the driver’s seat')
for item in range(0,len(movie_list)):
    ak = []
    result = movie_list[item]
    imdb_access.update(result)
    summary = result.summary()

    print summary.encode('utf-8')

    Title = result.get('title').lower().strip()
    Title = Title.encode('utf-8')
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



    Director = re.search(r'Director:\s+(.*?)\n',summary) or []
    if Director:
        Director = Director.group(1).replace('.$','').replace('-','').strip()
        Director = Director.lower().encode('utf-8')
        print 'Result Director ::',Director
    else:
        print 'Director not found'
    
    imdb_key = ''
    flag = 0
    if Title == 'democracy in the driver’s seat' and Director == 'gail gilbert':
        print 'movie found (Director match)'
        imdb_key = movie_list[item].movieID
        imdb_key = 'www.imdb.com/title/tt'+imdb_key
        print imdb_key
        # writer.writerow({'Entity':row['Entity'],'Director':row['Director'],'Year':year,'url': row['url'],'IMDB_OLD': row['IMDB_OLD'],'IMDB URL':imdb_key})
        break
    elif Title == 'democracy in the driver’s seat' and Year == '2014':
        print 'movie found (Year match)'
        imdb_key = movie_list[item].movieID
        imdb_key = 'www.imdb.com/title/tt'+imdb_key
        print imdb_key
        # writer.writerow({'Entity':row['Entity'],'Director':row['Director'],'Year':year,'url': row['url'],'IMDB_OLD': row['IMDB_OLD'],'IMDB URL':imdb_key})
        break
    elif 'democracy in the driver’s seatt' in ak and Director == 'gail gilbert':
        print 'movie found (AKA match)'
        imdb_key = movie_list[item].movieID
        imdb_key = 'www.imdb.com/title/tt'+imdb_key
        print imdb_key
        # writer.writerow({'Entity':row['Entity'],'Director':row['Director'],'Year':year,'url': row['url'],'IMDB_OLD': row['IMDB_OLD'],'IMDB URL':imdb_key})
        break                    
    else:
        print 'movie not found'
        flag = 1
if flag == 1:
    # writer.writerow({'Entity':row['Entity'],'Director':row['Director'],'Year':year,'url': row['url'],'IMDB_OLD':row['IMDB_OLD'],'IMDB URL':imdb_key})
    print 'movie not found 2'