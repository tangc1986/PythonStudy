from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://xiaonei.com'
req = Request(old_url)
reponse = urlopen(req)
print 'old_url: ' + old_url
print 'Real_url: ' + reponse.geturl()
