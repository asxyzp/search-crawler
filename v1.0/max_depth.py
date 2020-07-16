#Web crawler with a paramter of maximum depth to which the links can be searched through
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

def crawl_web(seed,max_depth):
    tocrawl=[seed]
    crawled=[]
    next_depth = []
    depth = 0
    while tocrawl and depth<max_depth:
        page=tocrawl.pop()
        if (page not in crawled) : 
            union(next_depth,get_all_links(get_page(page)))      #All next links extracted from a given page would be stored in next_depth
            crawled.append(page)                                 #page would move on to crawled
        if not tocrawl:                                          #Untill crawl isn't empty
            tocrawl, next_depth = next_depth, []                 #tocrawl=next_depth and next_depth=[]
            depth = depth + 1                                    #Increment depth value
    return crawled                                                 

seed_url=raw_input("Url? ")
max_depth=int(input("Max depth to be crawled ? "))
print 'The crawled pages are :\n',crawl_web(seed_url,max_depth)
