import requests as rq
import json as js
from bs4 import BeautifulSoup

number = 34
# nameList = []


def getUserInfo(url):
    nameList = []
    response = rq.get(url, headers={'User-agent': "Mozila"})

    response_code = response.status_code
    print("*************************************")
    if(response_code != 200):
        print("Error occured")

    else:
        html_content = response.content
        # Create a DOM model for HTML data obtained
        dom = BeautifulSoup(html_content, 'html.parser')
        all_repo = dom.select("ul.repo-list li div.d-flex div a")
        # INSTALL beautifulsoup4

        for each_repo in all_repo:
            name = each_repo.attrs["href"][1:]
            href_link = "https://github.com/{}".format(name)
            nameList.append(href_link)
    # print(nameList)
    return nameList


for i in range(number):
    i = i + 1
    url = "https://github.com/search?p={}&q=girlswhocode&type=Repositories".format(
        i)
    print(getUserInfo(url))
