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

query = '{query}'

#Change the sort number 0,1,2,3,4,5 into your own.

api = {
0 : {'api_url':'https://api-ssl.bitly.com/v3/shorten?format=json&login=hzlzh&apiKey=R_e8bcc43adaa5f818cc5d8a544a17d27d&longUrl=','title':'bit.ly','des':'http://bit.ly/'}
}

fb = Feedback()
for title in api:
    fb.add_item(api[title]['title'],
        subtitle="Using %s" % api[title]['des'],
        arg='{"type":"'+api[title]['title']+'","api_url":"'+api[title]['api_url']+'","long_url":"'+query+'"}',icon='favicons/'+api[title]['title']+'.png')
print fb
