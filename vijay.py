import urllib2
import bs4
url='http://learnpythonthehardway.org/book/ex40.html'
opn=urllib2.urlopen(url).read()
soup=bs4.BeautifulSoup(opn,'html')
t=soup.find_all('td',{'class':'code'})
print t
m={}
f=open('vijay.txt','r+')
for i in t:
    f.write(i.text)
