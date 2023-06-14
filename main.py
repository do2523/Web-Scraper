import requests  # For grabbing HTML files
from bs4 import BeautifulSoup  # To use HTML and grab the gathered data

res = requests.get('https://news.ycombinator.com/news')  # Access browser without need of a window
soup_obj = BeautifulSoup(res.text, 'html.parser')
# print(soup_obj.find(id='score_36329483'))
links = soup_obj.select('.titleline')
votes = soup_obj.select(".score")

def create_custom_hn(links, votes):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText() 
        href = links[index].get('href', None)  # if no href then it will default to None
        points = votes[index].getText()
        print(points)
        hn.append({'title': title, 'link':href})
    return hn

create_custom_hn(links,votes)
# print(create_custom_hn(links, votes))