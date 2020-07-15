#Finished Web crawler with an index list
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
            entry[1].append(url)  
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

def web_crawler(seed):
    tocrawl=[seed]
    crawled=[]
    index=[]
    while tocrawl:
        page=tocrawl.pop()
        if page not in crawled:
            content=get_page(page)
            add_page_to_index(index,page,content)
            union(tocrawl,get_all_links(content))
            crawled.append(page)
    return index

print web_crawler('https://udacity.github.io/cs101x/index.html')