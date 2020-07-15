#Web crawler program
#Created by Aashish Loknath Panigrahi 24Aug2018
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

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def crawl_web(seed):
    tocrawl=[seed]
    crawled=[]
    while tocrawl:
        page=tocrawl.pop()
        if page not in crawled: 
            union(tocrawl,get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

seed=raw_input("URL? ")
print crawl_web(seed)
