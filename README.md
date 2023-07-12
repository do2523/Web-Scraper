# Web Scraper for Hacker News

This Python program performs web scraping on the Hacker News website (https://news.ycombinator.com/news) to gather and display information about the top news stories based on user votes.

## How to Use

1. Ensure that you have Python 3 installed on your machine.

2. Install the required libraries by running the following command:
```
pip install requests beautifulsoup4
```

3. Clone this repository or download the source code file.

4. Open the terminal or command prompt and navigate to the project directory.

5. Run the `web_scraper.py` file using the Python interpreter.

6. The program will make requests to the Hacker News website and gather information about the top news stories.

7. It will print the title, link, and number of votes for each news story that has more than 99 votes.

## How it Works

The program uses the `requests` library to grab HTML files from the Hacker News website. It then utilizes the `BeautifulSoup` library to parse the HTML and extract the desired data.

The `create_custom_hn` function extracts the title, link, and number of votes for each news story. It filters out stories with less than 100 votes and sorts the stories based on the number of votes in descending order.

## Example Output

Here's an example of the program's output:

```
[
    {'title': 'Example Title 1', 'link': 'https://example.com/1', 'votes': 250},
    {'title': 'Example Title 2', 'link': 'https://example.com/2', 'votes': 180},
    {'title': 'Example Title 3', 'link': 'https://example.com/3', 'votes': 120},
    ...
]
```

The output includes a list of dictionaries, where each dictionary represents a news story with its title, link, and number of votes.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please feel free to submit a pull request.
