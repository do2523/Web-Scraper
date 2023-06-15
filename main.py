import requests  # For grabbing HTML files
from bs4 import BeautifulSoup  # To use HTML and grab the gathered data
import pprint


res = requests.get('https://news.ycombinator.com/news')  # Access browser without need of a window
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup_obj = BeautifulSoup(res.text, 'html.parser')
soup_obj2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup_obj.find(id='score_36329483'))
links = soup_obj.select('.titleline > a')
links2 = soup_obj2.select('.titleline > a')
subtext = soup_obj.select(".subtext")
subtext2 = soup_obj2.select(".subtext")

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText() 
        href = item.get('href', None)  # if no href then it will default to None
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href , 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links,mega_subtext))
# print(create_custom_hn(links, votes))

