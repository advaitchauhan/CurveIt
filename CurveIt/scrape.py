#!/usr/bin/env python
"""
Python routines for scraping data from Princeton's registrar.
by Alex Ogier '13.

Kept limping along by Brian Kernighan, with bandaids every year
as the registrar makes format changes.

If run as a python script, the module will dump information on all the courses available
on the registrar website as a JSON format.

Check out LIST_URL to adjust what courses are scraped.

Useful functions are scrape_page() and scrape_all().
"""

from datetime import datetime
import json
import re
import string
import sqlite3
import sys
import urllib2
from bs4 import BeautifulSoup

TERM_CODE = 1122  # seems to be fall 11-12
TERM_CODE = 1124  # so 1124 would be spring 11-12
                  # 1134 is definitely spring 13 (course offerings link)`
TERM_CODE = 1134
TERM_CODE = 1142  # fall 2013; spring 2014 will be 1144
TERM_CODE = 1144  # spring 2014
TERM_CODE = 1154  # spring 2015

URL_PREFIX = "http://registrar.princeton.edu/course-offerings/"
LIST_URL = URL_PREFIX + "search_results.xml?term={term}"
COURSE_URL = URL_PREFIX + "course_details.xml?courseid={courseid}&term={term}"

COURSE_URL_REGEX = re.compile(r'courseid=(?P<id>\d+)')
PROF_URL_REGEX = re.compile(r'dirinfo\.xml\?uid=(?P<id>\d+)')
LISTING_REGEX = re.compile(r'(?P<dept>[A-Z]{3})\s+(?P<num>\d{3}[A-Z]?)')

def get_course_list(search_page):
  "Grep through the document for a list of course ids."
  soup = BeautifulSoup(search_page)
  links = soup('a', href=COURSE_URL_REGEX)
  courseids = [COURSE_URL_REGEX.search(a['href']).group('id') for a in links]
  return courseids

def clean(str):
  "Return a string with leading and trailing whitespace gone and all other whitespace condensed to a single space."
  return re.sub('\s+', ' ', str.strip())

def get_course_details(soup):
  "Returns a dict of {courseid, area, title, descrip, prereqs}."

#  print "DEBUG"
#  s = soup('h2')
#  print "s = "
#  print s
#  s1 = s[0].string
#  print "s1 = "
#  print s1
#  print "END DEBUG"

  return {
    'title': clean(soup('h2')[0].string),  # was [1]
  }

def flatten(dd):
  s = ""
  try:
    for i in dd.contents:
      try:
        s += i
      except:
        s += flatten(i)
  except:
    s += "oh, dear"
  return s

def get_course_listings(soup):
  "Return a list of {dept, number} dicts under which the course is listed."
  listings = soup('strong')[1].string
  return [{'dept': match.group('dept'), 'number': match.group('num')} for match in LISTING_REGEX.finditer(listings)]

def get_course_profs(soup):
  "Return a list of {name} dicts for the professors teaching this course."
  prof_links = soup('a', href=PROF_URL_REGEX)
  return [{'name': clean(link.string)} for link in prof_links]

def scrape_page(page):
  "Returns a dict containing as much course info as possible from the HTML contained in page."
  soup = BeautifulSoup(page).find('div', id='timetable') # was contentcontainer
  course = get_course_details(soup)
  course['listings'] = get_course_listings(soup)
  course['profs'] = get_course_profs(soup)
  return course

def scrape_id(id):
  page = urllib2.urlopen(COURSE_URL.format(term=TERM_CODE, courseid=id))
  return scrape_page(page)

def scrape_all():
  """
  Return an iterator over all courses listed on the registrar's site.
  
  Which courses are retrieved are governed by the globals at the top of this module,
  most importantly LIST_URL and TERM_CODE.

  To be robust in case the registrar breaks a small subset of courses, we trap
  all exceptions and log them to stdout so that the rest of the program can continue.
  """
  search_page = urllib2.urlopen(LIST_URL.format(term=TERM_CODE))
  courseids = get_course_list(search_page)

  n = 0
  for id in courseids:
    try:
      if n > 99999:
        return
      n += 1
      yield scrape_id(id)
    except Exception:
      import traceback
      traceback.print_exc(file=sys.stderr)
      sys.stderr.write('Error processing course id {0}\n'.format(id))

if __name__ == "__main__":
  first = True
  for course in scrape_all():
    if first:
      first = False
      print '['
    else:
      print ','
    json.dump(course, sys.stdout)
  print ']'