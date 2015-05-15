#! /bin/python
#
# Created by: Matthew Drabick
# Last updated: Dec. 14, 2014
#
# This program crawls through the Princeton College Facebook data grabbing 
# all the student information available, including name, class year, 
# and major (if applicable). It processes that data and creates first a 
# json file with person objects. This json file is then read to create text 
# files containing names for each group found.

from bs4 import BeautifulSoup
from urllib2 import urlopen, Request
from os.path import isfile, join, expanduser
import time
import base64
import json

# urls
base_url = "https://www.princeton.edu/collegefacebook/"
colleges = ["mathey", "rockefeller", "butler", "whitman", "forbes", "wilson"]
page_url = "/?order=last_name&sort=asc&view=photo&page="
entries_limit = "&limit=1500"

# credentials
netid = "tylerh"
password = "" ####### not shown for privacy reasons
student_count = 1

# make html requests
def makeSoup(url):
    request = Request(url)
    base64string = base64.encodestring('%s:%s' % (netid, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)   
    html = urlopen(request).read()
    return BeautifulSoup(html, "lxml")

def processResult(result):
    global student_count
    print student_count
    email = ""
    name = ""
    student_count = student_count + 1
    for result_child in result.children:
        if result_child.get("class")[0]=="name":
            name = result_child.contents[0]                           # name
            name_fields = (name.string).split()
            name = name_fields[0]
            for i in range(1, len(name_fields) - 1):
                name += ' ' + name_fields[i]
            year = (int)((name_fields[len(name_fields) - 1])[1:]) + 2000    # year
        if result_child.get("class")[0]=="email":
            email = ((result_child.contents)[0].contents)[0]          # email            # major
    person = name.encode('ascii','ignore'), year, email.encode('ascii','ignore')
    return person

def writeToJSON(filename, obj):
    start_time = time.time()
    with open(filename, 'w') as outfile:  # write data as json object for future processing if necessary
        json.dump(obj, outfile)
    print(time.time() - start_time)

def writeDict(dictionary, folder):
    writeToJSON(folder + ".json", dictionary)
    for key in dictionary:
        output = open(join(folder, str(key) + ".txt"), 'w')
        for name in dictionary[key]:
            output.write(name + '\n')

def main():
    students = [] # list of students
    page = base_url + "1" + entries_limit
    num_pages = 1 
    for college in colleges:
        for i in range(1, num_pages + 1):  
            print i
            time.sleep(1)
            soup = makeSoup(base_url + college + page_url + str(i) + entries_limit) # put a different page number in each time it is iterated
            results = soup.find_all("div", { "class" : "result-meta" }) # grab results from the page
            for result in results: # look at each person and process the relevant info
                students.append(processResult(result))
        # writeList(students, college, "ResColleges")

    writeToJSON('students.json', students)

if __name__ == "__main__":
    main()

