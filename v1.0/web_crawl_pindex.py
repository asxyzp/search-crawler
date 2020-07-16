#Web crawler with improved index to avoid adding multiple same urls
#Created by Aashish Loknath Panigrahi 29Aug2018
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

def get_next_link(page):
   start_link=page.find("<a href=")
   if start_link==-1:                           #If a web page has no hyperlinks
       return None,-1
   start_quote=page.find('"',start_link)
   end_quote=page.find('"',start_quote+1)
   url=page[start_quote+1:end_quote]
   return url,end_quote


def get_all_links(page):
    link_list=[]
    while True:
        url,end_quote=get_next_link(page)
        if url:
                link_list.append(url)
                page=page[end_quote:]      #To begin from next end_quote value
        else:
            break
    return link_list

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0]==keyword :
            if url not in entry[1]:
               entry[1].append(url)    #URLs not added when they already exist in the index
            return
    index.append([keyword,[url]])      

def lookup(index,keyword):
    for entry in index:
        if entry[0]==keyword:
            return entry[1]
    return []

def add_page_to_index(index,url,content):
    content_list=content.split()
    for e in content_list:
        add_to_index(index,e,url)

def web_crawler(seed,max_pages):
    tocrawl=[seed]
    crawled=[]
    index=[]
    while tocrawl:
        page=tocrawl.pop()
        if page not in crawled and len(crawled)<max_pages:
            content=get_page(page)
            add_page_to_index(index,page,content)
            union(tocrawl,get_all_links(content))
            crawled.append(page)
    return index

url=raw_input("Seed URL? ")
maxp=int(raw_input("Max pages to be crawled? "))
indx=web_crawler(url,maxp)
print indx
cont='y'
while cont=='y':
    key=raw_input("Search keyword? ")
    print lookup(indx,key)
    cont=raw_input("Continue (y/n): ")

#https://en.wikipedia.org/wiki/Computer_program