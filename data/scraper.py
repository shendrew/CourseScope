from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


def generate_json(url):
    """
    
    param: string of url to scrape
    type: string
    rtype: list of dictionaries
    return: dictionaries represent course info (json)
    """
    ret = []
    
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    courses = soup.find_all(attrs={'class':'courseInfo'})
    
    for i in range(len(courses)):
        number = courses[i].find(attrs={'class':'courseNumber'}).text
        title = courses[i].find(attrs={'class':'courseTitle'}).text
        description = courses[i].find(attrs={'class':'courseDescription'}).text
        
        ret.append({
            'number': number[:-1],
            'title': title,
            'description': description
        })
        
    return ret


stanford_cs = 'https://explorecourses.stanford.edu/print?filter-catalognumber-CS=on&filter-catalognumber-CS=on&q=CS&descriptions=on'
res = generate_json(stanford_cs)

with open('data.json', 'w') as file:
    json.dump(res, file, indent=4, ensure_ascii=False)