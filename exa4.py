import csv
with open('input.csv', 'rb') as csvinput:
	with open ('output.csv', 'wb') as csvoutput: 
		reader = csv.DictReader(csvinput)
		fieldnames = ['Title', 'Director']
		writer = csv.DictWriter(csvoutput,fieldnames=fieldnames)
		writer.writeheader()
		for row in reader:
			print (row['Title'], row['Url'], row['Director'], row['Alias'], row['Year'])		
			writer.writerow({'Title':row['Title'],'Director':row['Director']})