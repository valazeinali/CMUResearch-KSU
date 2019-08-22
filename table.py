import csv 

second_year_alive = []

status = []

easy_count = 1

mentor_count = 1

validlabels = ["E-easy"]

outcsv = csv.writer(open("linearRegAlgoData.csv","w"))
outcsv.writerow(['User','effort','additions','deletions','num_easy_y1','num_mentor_y1','year','status'])

for row in csv.DictReader(open("/Users/valazeinali/Desktop/New Stuff CMU/newbie_activity.csv")):


	actor = row["actor"]
	temp = row["time"] # only getting the year from when author makes a commit
	time = temp[0:4] # only getting the year of the time when an author makes a commit
	labels = row["tags"].split(",") # getting all labels of the commit
	temp1 = row["actors_first_action"] # only getting the year from when author made their first action
	first_action = temp1[0:4] # only getting the year of the time when an author made their first action
	additions = row["insertions"]
	deletions = row["deletions"]
	effort = (int(row["insertions"]) + int(row["deletions"])) # total amount of effort put into the commit
	

	
	#second_year_alive = int(first_action) + 1 # we are creating a range of 2 years for the linear regression. 

	#if first_action == "2010": #and actor == "pnkfelix":

		#for i in actor:
	if time == first_action: # comparing the commit time and authors first action
		status = "new" # they are classified "old" if they have commited in a year that is not the year they made thier "first_action"
	elif int(time) == int(first_action) +1:
		status = "2nd_year"
	else:
		status = "old" # they are classified "new" if they have commited in a year that is not the year they made thier "first_action"

	if "E-easy" in labels:
		easy_count = 1 # where there is a E-easy label present we add 1 to the list 
	else:
		easy_count = 0 # we dont add a count to the list if ! present 

	if "E-mentor" in labels:
		mentor_count = 1 # where there is a E-easy label present we add 1 to the list 
	else:
		mentor_count = 0 # we dont add a count to the list if ! present 
		

	outcsv.writerow([actor,effort,additions,deletions,easy_count,mentor_count,time,status])

