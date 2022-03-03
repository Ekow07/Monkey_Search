
import json
from turtle import title
import requests
from bs4 import BeautifulSoup


# DONE:
# 1. Make HTTP GET request to the url
# 2. Parse Response and get all the available links <a href>
# 3. Follow the extacted links and repeat the same 
# 4. Break out of the loop either hitting the given depth


# TODO:
# 1. Break more links available 
# 2. Try to  avoid duplicate link responses
# 3. Try to draft a simple  pages to debug the crawler   





Start_url = "https://quotes.toscrape.com/"

data = []

def crawl(url,depth ):
    try:  
        print("crawling url: '%s' at depth '%d' " % (url,depth))
        responds = requests.get(url)
    except :
        print("Failed to perform HTTP GET request on '%s'\n" % url)
        return 


    content = BeautifulSoup(responds.text,"lxml")

    title = content.find("title").text 
    description= content.get_text()

    if description is None:
        description = ''
    else:
        description = description.strip().replace("\n", " ")

    result = {

        "url": url,
        "title": title,
        "description" : description
    
    } 
    
    data.append(result)
    #print("\n\nReturn: ", json.dumps(result, indent = 2) )
    
    
    if depth == 0:
        return 
    
    try:
        links = content.findAll("a")
    except:
        return  
          

    for link in links:
        try:
           if 'http' not in link['href']:
               
               follow_url = url + link['href']
           else: 
               follow_url = link['href']

           crawl( follow_url, depth -1)
        except KeyError:
            pass

    return  

crawl(Start_url, 1)
#print(json.dumps(data, indent= 2))
print(len(data))