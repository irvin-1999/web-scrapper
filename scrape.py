import requests
from bs4 import BeautifulSoup


res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select(".subtext")


def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            hn.append({"title": title, "link": href, "Votes": points})
    return hn


print(create_custom_hn(links, subtext))
