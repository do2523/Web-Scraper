import requests  # For grabbing HTML files
from bs4 import BeautifulSoup  # To use HTML and grab the gathered data

res = requests.get('https://news.ycombinator.com/news')  # Access browser without need of a window
soup_obj = BeautifulSoup(res.text, 'html.parser')
# print(soup_obj.find(id='score_36329483'))
links = soup_obj.select('.titleline')
votes = soup_obj.select(".score")