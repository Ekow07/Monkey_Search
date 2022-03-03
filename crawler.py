
import json
from turtle import title
import requests
from bs4 import BeautifulSoup

Start_url = "https://quotes.toscrape.com/"

data = []

def crawl(url,depth ):
    try:  
        print("crawling url: '%s'" % url)
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
           print(" URL depth '%d' : " % depth)
           
           if 'http' not in link['href']:
               
               follow_url = url + link['href']
           else: 
               follow_url = link['href']

           crawl( follow_url, depth -1)
        except KeyError:
            pass

    return  

crawl(Start_url, 2)
#print(json.dumps(result, indent= 2))
print(len(data))