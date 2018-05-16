#!/usr/bin/python2

from metar import Metar
import sys
import time
import urllib2

METAR_SITE = 'KLAF'

metar_url = 'http://tgftp.nws.noaa.gov/data/observations/metar/stations/' + METAR_SITE + '.TXT'

class UrlNotModifiedHandler(urllib2.BaseHandler):
    '''
    Cleanly handle when the URL isn't modified
    '''
    def http_error_304(self, req, fp, code, message, headers):
        addinfourl = urllib2.addinfourl(fp, headers, req.get_full_url())
        addinfourl.code = code
        return addinfourl

timestamp = time.time() - 600
ifModifiedSince = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(timestamp))
print "------------------\nChecking since %s" % ifModifiedSince
opener = urllib2.build_opener(UrlNotModifiedHandler())
request = urllib2.Request(metar_url)
request.add_header("If-Modified-Since", ifModifiedSince)

result = opener.open(request)

headers = result.info()
if result.code == 304:
    print 'Not updated in the last 10 minutes, skipping'
    sys.exit(1)

observation = Metar.Metar(result.readlines()[1])
print observation.code

if 'thunder' in observation.present_weather():
    print "THUN-DAH!"
    sys.exit(0)
else:
    print 'Boring wx'
    sys.exit(2)
