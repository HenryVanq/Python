# Exercise 14

import urllib2
import json


# dimiourgia adeias listas
s=[]
a=[]

# diaperasei ton klirosewn toy joker
for i in range(1779,1867):
    # webservices opap 
    response = urllib2.urlopen('http://applications.opap.gr/DrawsRestServices/joker/%d.json'%(i))
    html = response.read()
    data=json.loads(html)
    # lista me ton arithmo tou joker
    s=(data['draw']['results'])
    # arithmo emfanisewn
    a.append(s[1])

print("Poses fores emfanistikan oi arithmoi tou joker gia to 2017: \n")
for i in range(1,21):
    print i,': ', 'Emfanistike', a.count((i)),'fores', 'Pososto ', round((float)(a.count((i))*100)/88), '%'
