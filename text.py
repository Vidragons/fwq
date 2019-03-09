"""
from bs4 import BeautifulSoup
import requests

URL = "http://www.nationalgeographic.com.cn/animals/"

html = requests.get(URL).text

soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('ul', {"class": "img_list"})

import os

os.makedirs('./img/', exist_ok=True)

for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)
        
        
 """

"""
class Caculator:
   
    def __init__ (self,name,price):
        self.na=name
        self.pr=price
    #self.hi=hight
    #self.wi=width
    def a(self):
        print(self.na)
        print(self.pr)

name=input('please input num ')
price=input('please input num ')

p=Caculator(name,price)
p.a()



"""
"""
import pickle

a_dict={'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}

file=open('pickle_example.pickle','wb')
pickle.dump(a_dict,file)
file.close()
file=open('pickle_example.pickle','rb')
a_dict=pickle.load(file)
file.close()
print(a_dict)

"""

"""

import random

max=int(input('请输入最大值'))
min=int(input('请输入最小值'))
items=[]

x=random.randint(min,max)
y=random.randint(min,max)

for i in range(min,max):
    for j in range(min,max):
       item=[i,j]
3       items.append(item)
items
print(items)




class DD:
    

    def dic(self):
        a=[]
        for i in range(1,10):
            a.append(i)
        return a
    def ggo(self,a):
        print(a)
m=DD()
a=m.dic()
m.ggo(a)
print(a)

bbc(1,a[])
#car.bbc(a)
def bbc(x,a[]):
        print(x)
        print(a)

it=[]

i=0
while i<5:
    x=0
    it.append(x)
    i=i+1
print(it)
"""
"""
import multiprocessing as mp
import time
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import re

base_url = "https://morvanzhou.github.io/"
# base_url = 'https://morvanzhou.github.io/'

# DON'T OVER CRAWL THE WEBSITE OR YOU MAY NEVER VISIT AGAIN
if base_url != "https://morvanzhou.github.io/":
    restricted_crawl = True
else:
    restricted_crawl = False


def crawl(url):
    response = urlopen(url)
    time.sleep(0.1)             # slightly delay for downloading
    return response.read().decode()


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])   # 去重
    url = soup.find('meta', {'property': "og:url"})['content']
    return title, page_urls, url



unseen = set([base_url,])
seen = set()

pool = mp.Pool(4)                       
count, t1 = 1, time.time()
while len(unseen) != 0:                 # still get some url to visit
    if restricted_crawl and len(seen) > 20:
            break
    print('\nDistributed Crawling...')
    crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
    htmls = [j.get() for j in crawl_jobs]                                       # request connection

    print('\nDistributed Parsing...')
    parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
    results = [j.get() for j in parse_jobs]                                     # parse html

    print('\nAnalysing...')
    seen.update(unseen)         # seen the crawled
    unseen.clear()              # nothing unseen

    for title, page_urls, url in results:
        print(count, title, url)
        count += 1
        unseen.update(page_urls - seen)     # get new url to crawl
print('Total time: %.1f s' % (time.time()-t1, ))    # 16 s !!!
"""

"""
search = '168'
num = '1686-216-2564'
print(str(num.find(search)))
print('{a} a word is {b}'.format(a='with',b='came'))
#print(len(search))


a=[i*i*i for i in range(1,10)]
print(a)
g = {i:j.upper() for i,j in zip(range(1,6),'abcd')}
print(g)

lyric = 'The night begin to shine , the night begin to shine'
words = lyric.split()
print(words)
"""

"""

import string
import time
t0 = time.clock()
path = 'C:/Users/V/Desktop/fwq.txt'
with open(path,'r')as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    wordss = set(words)
    counts_d = {index:words.count(index) for index in wordss}

for word in sorted(counts_d,key=lambda x:counts_d[x],reverse=True):
    #将出现的次数进行排序，从大到小排序
    print('{}--{} times'.format(word,counts_d[word]))
 

print(time.clock()-t0)

list1 = [3,5,-4,-1,0,-2,-6]
list2 = sorted(list1, key=lambda x: abs(x),reverse=True)
print(list2)
"""


"""

def fun():
    for i in range(0,5):
        print(str(i)+'text1')

def fun1():
    for i in range(0,5):
        return i
def fun2():
    for i in range(0,5):
        yield i
fun()
u = fun1()
a = []
a = fun2()
print(u)
for y in a:
    print(y)
"""

"""
class Solution:
    def twoSum(self):
        nums = [1,11,23,16,58,79,7,26,99]
        target = 102
        change = 0
        for i in range(0,8):
            change = change + 1
            for j in range(change , 9):
                if nums[i] + nums[j] == target:
                    print(str(nums[i])+"+"+str(nums[j])+"="+str(target))
                    break

text = Solution()
text.twoSum()

"""

"""
class LinearMap(object):
   # 线性表结构
    def __init__(self):
        self.items = []
    
    def add(self, k, v):    # 往表中添加元素
        self.items.append((k,v))
        return self.items
        
        
    def get(self, k):
               # 线性方式查找元素
        for key,val in self.items:
            if key==k:      # 键存在，返回值，否则抛出异常
                return val
        raise KeyError


c = LinearMap()
for i in range(0,10):
    items = c.add(i,i)
print(items)
p = c.get(10)
print(p)

"""



"""
class BetterMap(object):
    利用LinearMap对象作为子表，建立更快的查询表
    def __init__(self,n=100):
        self.maps = []          # 总表格
        for i in range(n):      # 根据n的大小建立n个空的子表
            self.maps.append(LinearMap())
    
    def find_map(self,k):       # 通过hash函数计算索引值
        index = hash(k) % len(self.maps)
        return self.maps[index] # 返回索引子表的引用     

    # 寻找合适的子表（linearMap对象）,进行添加和查找
    def add(self, k, v):
        m = self.find_map(k)        
        m.add(k,v)
    
    def get(self, k):
        m = self.find_map(k)
        return m.get(k)
if __name__=="__main__":
 2     table = BetterMap()
 3     pricedata = [("Hohner257",257),
 4                  ("SW1664",280),
 5                  ("SCX64",1090),
 6                  ("SCX48",830),
 7                  ("Super64",2238),
 8                  ("CX12",1130),
 9                  ("Hohner270",620),
10                  ("F64C",9720),
11                  ("S48",1988)]
12     
13     for item, price in pricedata:
14         table.add(k=item, v=price)



class HashMap(object):
    def __init__(self):
        # 初始化总表为，容量为2的表格（含两个子表）
        self.maps = BetterMap(2)
        self.num = 0        # 表中数据个数
    
    def get(self,k):        
        return self.maps.get(k)
    
    def add(self, k, v):
        # 若当前元素数量达到临界值（子表总数）时，进行重排操作
        # 对总表进行扩张，增加子表的个数为当前元素个数的两倍！
        if self.num == len(self.maps.maps): 
            self.resize()
        
        # 往重排过后的 self.map 添加新的元素
        self.maps.add(k, v)
        self.num += 1
        
    def resize(self):
        重排操作，添加新表, 注意重排需要线性的时间
        # 先建立一个新的表,子表数 = 2 * 元素个数
        new_maps = BetterMap(self.num * 2)
        
        for m in self.maps.maps:  # 检索每个旧的子表
            for k,v in m.items:   # 将子表的元素复制到新子表
                new_maps.add(k, v)
        
        self.maps = new_maps      # 令当前的表为新表
"""
import time 

def sun(n):
    start = time.time()
    print((n*(n+1))/2)
    end = time.time()
    x = end-start
    return x


print(sun(10))



