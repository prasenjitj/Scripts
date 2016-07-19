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

input_file = sys.argv[1]
output_file = sys.argv[2]
flag = 1

api_keys = ['AIzaSyB-N7c8zv6PVcrPJ50RCDoYPQeKlr2tILo',
            'AIzaSyCx09FBPm89P1ZVC5kMXMeFKmFmgQxAXuE',
            'AIzaSyAwecYEut4l0GjK2aEI6UnQWzObFr1AjCk',
            'AIzaSyAJxLufiXAHGBQ1QdkY4I0RiOUZ9gJGPe8',
            'AIzaSyD6cpIbG5BZz5fGo0NeHjPPgSu1PoWnS48',
            'AIzaSyBU49J2cMO9FDJBWwhNXP2OnsrFuOKU868',
            'AIzaSyCewOfpONm8JTWNSmfcqlopxQ8QDjq7fDs',
            'AIzaSyDmbZ0vNfEqMWekMdJqZDq6kUDhNqcaGss',
            'AIzaSyDv9U-pM63kX89yIqi9n7RvgPPoiEhgGY0',
            'AIzaSyCTTJjGybDdnuxgiveucaMLsYoAcxNV3mI',
            'AIzaSyAOdartvZVAihGF1PJ_X89zr7svC_DfCiw',
            'AIzaSyDf8-ZM0O8YBpTBC1B_4LlCFDaOijA1hYA',
            'AIzaSyBtLp3JXGmNRyv0UkPap7ICO9Q9l2-pnIY',
            'AIzaSyA0NqhIpSw3ISjCBCh67zGErKS_klpcmto',
            'AIzaSyADklDo8BRRj_Cndxig8Wb5iiRohAiBAts',
            'AIzaSyCYPUgSxVybrymMPnDtAoFxlD3wJw31JI8',
            'AIzaSyCAbGzazc2D2-XesEElpF6sGMhZn8pVW6Y']
count = 1
try:
  #service = build("customsearch", "v1", developerKey="AIzaSyADklDo8BRRj_Cndxig8Wb5iiRohAiBAts")
  with open(input_file, 'rb') as csvinput:
      with open(output_file, 'wb') as csvoutput:
        for i in api_keys:
          for j in range(count,81):
            service = build("customsearch", "v1", developerKey=i)
            reader = csv.DictReader(csvinput)
            fieldnames = ['Entity','url','Director','Year','Alias','IMDB URL','genre','Runtime']
            writer = csv.DictWriter(csvoutput, fieldnames)
            writer.writeheader()
            for row in reader:

                title = row['Entity'].lower().strip().decode('utf-8')
                director = row['Director'].lower().strip().decode('utf-8')
                director = re.sub(r'(,\s.*)', '', director).strip()
                year = row['Year']
                alias = row['Alias'].lower().strip().decode('utf-8')
                query = title + " " + director
                print query
                print alias
                res = service.cse().list(q=query,cx='009241977094486741223:3agszpaq5sy',).execute()
                response = res.get('items')
                if response:
                    for i in range(len(response)):
                        try:
                            title_match = response[i]['pagemap']['metatags'][i]['og:title']
                            title_match = re.findall(r'(^.*?)\s\(',title_match)
                            title_match = title_match[i].lower().strip().decode('utf-8')
                            director = response[i]['pagemap']['metatags'][i]['og:description']
                            director_match = re.findall(r'\wirected by\s(.*?)\.',director)
                            director_match =  director_match[i].lower().strip().decode('utf-8')
                            print type(title_match), title_match
                            print type(director_match), director_match
                            if title in title_match and director in director_match:
                                imdb_url = response[i]['pagemap']['metatags'][i]['og:url']
                                writer.writerow({'Entity': row['Entity'],'Director': row['Director'], 'Alias': row['Alias'], 'IMDB URL': imdb_url})
                                print imdb_url
                                break
                            elif alias in title_match:
                                print "i'm here in alias <conditon>"
                                imdb_url = response[i]['pagemap']['metatags'][i]['og:url'].encode('utf-8')
                                writer.writerow({'Entity': row['Entity'],'Director': row['Director'], 'Alias': row['Alias'], 'IMDB URL': imdb_url})
                                print imdb_url
                                break
                            else:
                                print 'result not found'
                                imdb_url = ''
                                flag = 0
                        except (IndexError, KeyError ) as e:
                            #print 'Index out of range or Key Error'
                            imdb_url = ''
                            flag = 0
                    if flag == 0:
                      writer.writerow({'Entity': row['Entity'],'Director': row['Director'], 'Alias': row['Alias'], 'IMDB URL': ""})

                else:
                  writer.writerow({'Entity': row['Entity'],'Director': row['Director'],'Alias': row['Alias'],'IMDB URL': ""})

except Exception as e:
  print e
  count = 1
