import requests as rq
import json as js
from bs4 import BeautifulSoup
from time import sleep
from random import randint


number = 1
nameListMain = []
total_pages = 0


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
        tp = dom.select("em")
        # INSTALL beautifulsoup4
        total_pages = getTotalPages(tp)
        print(total_pages)
        for each_repo in all_repo:
            name = each_repo.attrs["href"][1:]
            href_link = "https://github.com/{}".format(name)
            nameList.append(href_link)
    return nameList


def getTotalPages(ttl_pages):
    pages = 0
    for pages in ttl_pages:
        tp = pages.attrs
        if(not(bool(tp))):
            continue
        else:
            pages = tp.get("data-total-pages")
    return pages


def queryGithub():
    for i in range(number):
        i = i + 1
        url = "https://github.com/search?p={}&q=girlswhocode&type=Repositories".format(
            i)
        nList = getUserInfo(url)
        nameListMain.append(nList)
        sleep(randint(2, 8))
    return nameListMain


def displayList():
    nameLst = []
    listA = queryGithub()
    for nl in listA:
        for names in nl:
            nameLst.append(names)
    return nameLst


print(displayList())
