#!/usr/bin/python2.7 -Wd

'''
file: pystatus.py
author: Ty Talmadge
contact: ty.talmadge@gmail.com
date: 20131007
description: python script that logs into a website, sets a status message
description2: pulls down variable number of notifications
overall: Because it shows a knowledge of python and why not?
'''
# denotes a comment
## denotes a major section
### denotes something to ponder

## set imports and any includes
### Why would a cow attempt to jump over the moon?
from bs4 import BeautifulSoup
import cookielib, os, os.path, requests, sys, urllib, urllib2

def main():
  #login()
  curl_home()

payload = {'m_nm': 'test1234',
           'm_pd': 'test1234'}

def login():
  #url='http://localhost/alternasocial/fork/bling.php'
  #r = requests.post(url, data=user_dict)  
  #print '%s' % r
  #url2='http://localhost/alternasocial/home.php?id=%s' % user_dict['m_nm']
  #result = requests.get(url2)
  #print '%s' % result
  # Store the cookies and create an opener that will hold them
  cj = cookielib.CookieJar()
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  # Add our headers
  opener.addheaders = [('User-agent', 'AlternasocialTesting')]
  # Install our opener (note that this changes the global opener to the one
  # we just made, but you can also just call opener.open() if you want)
  urllib2.install_opener(opener)
  # The action/ target from the form
  authentication_url = 'http://localhost/alternasocial/fork/bling.php'
  # Input parameters we are going to send
  #payload = {
  #'op': 'login-main',
  #'user': '<username>',
  #'passwd': '<password>'
  #}
  # Use urllib to encode the payload
  data = urllib.urlencode(payload)
  # Build our Request object (supplying 'data' makes it a POST)
  req = urllib2.Request(authentication_url, data)
  # Make the request and read the response
  resp = urllib2.urlopen(req)
  contents = resp.read()

def curl_home():
  ## curl facebook homepage
  #url="http://www.facebook.com"
  #page = urllib2.urlopen(url)
  #soup = BeautifulSoup(page.read())
  #global login_url
  mytest=requests.post('http://localhost/alternasocial/fork/bling.php', auth=(payload['m_nm'], payload['m_pd']), allow_redirects=True)
  print "test: %s\n" % mytest
  url2='http://localhost/alternasocial/home.php?id=%s' % payload['m_nm']
  page = urllib2.urlopen(url2)
  soup = BeautifulSoup(page.read())
  #result = requests.get(url2)
  #print '%s' % result
  #for f in soup.findAll('form'):
  #  login_url = f['action']
  print "soup: %s\n" % soup



if __name__ == "__main__":
  main()
