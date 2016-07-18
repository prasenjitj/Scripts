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
flag = 0

service = build("customsearch", "v1", developerKey="AIzaSyCx09FBPm89P1ZVC5kMXMeFKmFmgQxAXuE")
with open(input_file, 'rb') as csvinput:
    with open(output_file, 'wb') as csvoutput:
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
                            print imdb_url
                            flag = 1
                        elif alias in title_match:
                            print "i'm here in alias <conditon>"
                            imdb_url = response[i]['pagemap']['metatags'][i]['og:url'].encode('utf-8')
                            print imdb_url
                            flag = 1
                        else:
                            print 'result not found'
                        if flag:
                            writer.writerow({'Entity': row['Entity'],'Director': row['Director'], 'Alias': row['Alias'], 'IMDB URL': imdb_url})
                        else:
                            writer.writerow({'Entity': row['Entity'],'Director': row['Director'], 'Alias': row['Alias'], 'IMDB URL': ""})

                            

                    except IndexError:
                        #print 'Index out of range'
                        pass
