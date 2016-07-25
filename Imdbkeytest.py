"""
This script takes two arguments input file and output file in csv format,
and creates custom serach queries.
It fetches google custom search api keys from api table.
"""
from pprint import pprint
import re
import csv
import sys
from googleapiclient.discovery import build

reload(sys)
sys.setdefaultencoding("utf-8")

def searchMovie(response, Entity, Director, Alias, title,director,alias):
  flag = 1
  # title_match = ''
  director_match = ''
  print "searchMovie called"
  if response:
    for i in range(len(response)):
        try:

            title_match = response[i].get('pagemap').get('metatags')[0].get('og:title')
            print "title_match is ::",title_match
            if title_match:
                title_match = re.findall(r'(^.*?)\s\(', title_match)
                print title_match
                title_match = title_match[i].lower().strip().decode('utf-8')
                print title_match
            director_match = response[i].get('pagemap').get('metatags')[0].get('og:description')
            print "director_match  is ::",director_match
            if director_match is not None:
                print director_match
                director_match = re.findall(r'\wirected by\s(.*?)\.', director_match)
                print director_match
                director_match =  director_match[i].lower().strip().decode('utf-8')
                print director_match
            print  Entity, Director, Year, Alias
            if title in title_match and director_match is not None and director in director_match:
                imdb_url = response[i].get('pagemap').get('metatags')[i].get('og:url')
                writer.writerow({'Entity': Entity, 'Director': Director, 'Alias': Alias, 'IMDB URL': imdb_url})
                print imdb_url
                break
            elif alias in title_match and director_match is not None and director in director_match:
                print "i'm here in alias <conditon>"
                imdb_url = response[i]['pagemap']['metatags'][i].get('og:url')
                writer.writerow({'Entity': Entity, 'Director': Director, 'Alias': Alias, 'IMDB URL': imdb_url})
                print imdb_url
                break
            else:
                print 'result not found'
                imdb_url = ''
                flag = 0
        except (IndexError, KeyError ) as e:
            print e
            print "exception in function"
            imdb_url = ''
            flag = 0
    if flag == 0:
      writer.writerow({'Entity': Entity, 'Director': Director, 'Alias': Alias, 'IMDB URL': ""})
      print "level2"

  else:
    writer.writerow({'Entity': Entity, 'Director': Director, 'Alias': Alias, 'IMDB URL': ""})
    print "leve;l2"

input_file = sys.argv[1]
output_file = sys.argv[2]


api_keys = ['AIzaSyADklDo8BRRj_Cndxig8Wb5iiRohAiBAts',
            'AIzaSyA0NqhIpSw3ISjCBCh67zGErKS_klpcmto',
            'AIzaSyCYPUgSxVybrymMPnDtAoFxlD3wJw31JI8',
            'AIzaSyADklDo8BRRj_Cndxig8Wb5iiRohAiBAts',
            'AIzaSyCAbGzazc2D2-XesEElpF6sGMhZn8pVW6Y',
            'AIzaSyB-N7c8zv6PVcrPJ50RCDoYPQeKlr2tILo',
            'AIzaSyCx09FBPm89P1ZVC5kMXMeFKmFmgQxAXuE',
            'AIzaSyAJxLufiXAHGBQ1QdkY4I0RiOUZ9gJGPe8',
            'AIzaSyD6cpIbG5BZz5fGo0NeHjPPgSu1PoWnS48',
            'AIzaSyBU49J2cMO9FDJBWwhNXP2OnsrFuOKU868',
            'AIzaSyCewOfpONm8JTWNSmfcqlopxQ8QDjq7fDs',
            'AIzaSyDmbZ0vNfEqMWekMdJqZDq6kUDhNqcaGss',
            'AIzaSyDv9U-pM63kX89yIqi9n7RvgPPoiEhgGY0',
            'AIzaSyCTTJjGybDdnuxgiveucaMLsYoAcxNV3mI',
            'AIzaSyAOdartvZVAihGF1PJ_X89zr7svC_DfCiw',
            'AIzaSyDf8-ZM0O8YBpTBC1B_4LlCFDaOijA1hYA',
            'AIzaSyBtLp3JXGmNRyv0UkPap7ICO9Q9l2-pnIY'
            ]

#service = build("customsearch", "v1", developerKey="AIzaSyADklDo8BRRj_Cndxig8Wb5iiRohAiBAts")
with open(input_file, 'rb') as csvinput:
    with open(output_file, 'wb') as csvoutput:
      reader = csv.DictReader(csvinput)
      fieldnames = ['Entity', 'url', 'Director', 'Year', 'Alias', 'IMDB URL', 'genre', 'Runtime']
      writer = csv.DictWriter(csvoutput, fieldnames)
      writer.writeheader()
      try:
        for i in api_keys:
          for j in range(1, 81):
            service = build("customsearch", "v1", developerKey=i)
            # print "key :", i
            # print "j here", j
            for row in reader:
                Entity = row['Entity']
                Director = row['Director']
                Year = row['Year']
                Alias = row['Alias']
                print "Details ::", Entity, Director, Year, Alias
                title = row['Entity'].lower().strip().decode('utf-8')
                director = row['Director'].lower().strip().decode('utf-8')
                director = re.sub(r'(, \s.*)', '', director).strip()
                year = row['Year']
                alias = row['Alias'].lower().strip().decode('utf-8')
                query = title + " " + director + " " + year
                print "quesry is :: ",query
                # print alias
                try:
                  print "##"
                  res = service.cse().list(q=query, cx='009241977094486741223:3agszpaq5sy', ).execute()
                  response = res.get('items')
                  print "###"
                  searchMovie(response, Entity, Director, Alias, title, director, alias)
                except Exception, err:
                  print str(err)
                  print "exception in main"
                  # searchMovie(response)
      except Exception as e:
        print e
