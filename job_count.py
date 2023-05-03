from bs4 import BeautifulSoup

with open('indeed_list.html', 'r') as f:
	contents = f.read()

	soup = BeautifulSoup(contents, 'html.parser')

	div = soup.findAll('div', {"class":"atw-JobInfo-companyLocation"})
	
	for item in div:
		print(item.span)

	print('You have applied to {item_count} jobs.'.format(item_count = str(len(div))))
