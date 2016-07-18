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

input_file = sys.argv[1]
output_file = sys.argv[2]

service = build("customsearch", "v1", developerKey="AIzaSyCx09FBPm89P1ZVC5kMXMeFKmFmgQxAXuE")

with open(input_file, 'rb') as csvinput:
    with open(output_file, 'wb') as csvoutput:
        reader = csv.DictReader(csvinput)
        # writer = csv.DictWriter(csvoutput)
        # writer.writeheader()
        for row in reader:

            title = row['Entity'].lower().strip()
            director = row['Director'].lower().strip()
            director = re.sub(r'(,\s.*)', '', director).strip()
            year = row['Year']
            alias = row['Alias'].lower().strip()
            query = title + " " + director
            print query
            res = service.cse().list(q=query,cx='009241977094486741223:3agszpaq5sy',).execute()
            response = res.get('items')
            if response:
              for i in range(len(response)):
                try:
                  title_match = response[i]['pagemap']['metatags'][i]['og:title']
                  title_match = title_match[i].lower().strip()
                  director = response[i]['pagemap']['metatags'][i]['og:description']
                  director_match = re.findall(r'\wirected by\s(.*?)\.',director)
                  director_match =  director_match[i].lower().strip()
                  if title_match and director_match:
                    imdb_url = response[i]['pagemap']['metatags'][i]['og:url']
                    print imdb_url
                  else:
                    print 'result not found'
                except IndexError:
                  #print 'Index out of range'
                pass
