'''
Shorten URL v1.5

Github: https://github.com/hzlzh/Alfred-Workflows
Author: hzlzh (hzlzh.dev@gmail.com)
Twitter: @hzlzh
Blog: https://zlz.im/Alfred-Workflows/
'''
from feedback import Feedback

import urllib
import urllib2
import json
import sys

query = sys.argv[1]

api = {
'goo.gl' : {'api_url':'https://www.googleapis.com/urlshortener/v1/url','title':'goo.gl','des':'http://goo.gl/'},
'git.io' : {'api_url':'http://git.io','title':'git.io','des':'http://git.io/'}
}

fb = Feedback()
for title in api:
    fb.add_item(api[title]['title'],
        subtitle="Using %s" % api[title]['des'],
        arg='{"type":"'+title+'","api_url":"'+api[title]['api_url']+'","long_url":"'+query+'"}',icon='favicons/'+title+'.png')
print fb
