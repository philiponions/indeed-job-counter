from bs4 import BeautifulSoup

with open('indeed_list.html', 'r') as f:
	contents = f.read()

	soup = BeautifulSoup(contents, 'html.parser')

	header = soup.findAll('header', {"class":"atw-JobInfo"})
	
	company_list = []	
	for item in header:
		name_tag = item.find('div', {"class": "atw-JobInfo-companyLocation"})		
		name = name_tag.span.extract().text.strip()

		status_tag = item.find('div', {"class": "atw-JobInfo-statusTag"})
		status = status_tag.span.extract().text.strip()		

		company = {"name": name, "status": status}
		company_list.append(company)
		print(company)
	
	reached_count = 0
	ghosted_count = 0
	reject_count = 0
	for company in company_list:
		if (company["status"] == "Not selected by employer"):
			reject_count += 1
		elif (company["status"] == "Applied"):
			ghosted_count += 1
		elif (company["status"] == "Employer reached out"):
			reached_count += 1
		

	print("You've applied to {job_count} companies.".format(job_count=len(company_list)))
	print("You've been rejected {count} times.".format(count=reject_count))
	print("You've been ghosted {count} times.".format(count=ghosted_count))
	print("{count} employers ACTUALLY reached out to you... wow".format(count=reached_count))
