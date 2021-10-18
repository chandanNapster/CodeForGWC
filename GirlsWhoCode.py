import requests as rq
import json as js
from bs4 import BeautifulSoup
from time import sleep
from random import randint


# GIT_HUB_SEARCH_STRING = "girlswhocode"
GIT_HUB_SEARCH_STRING = "womenwhocode"
nameListMain = []
FIRST_PAGE = 1
MIN_WAIT_TIME = 4
MAX_WAIT_TIME = 12
URL = "https://github.com/search?p={0}&q={1}&type=Repositories"


def getRequestToGithub(url):
    response = rq.get(url, headers={'User-agent': "Mozila"})
    response_code = response.status_code
    print("*************************************")
    if(response_code != 200):
        print("Error occured")
    else:
        return BeautifulSoup(response.content, 'html.parser')


def fetchGithubMainPage():
    url = URL.format(FIRST_PAGE, GIT_HUB_SEARCH_STRING)
    # Create DOM model
    dom = getRequestToGithub(url)
    getAllUserData(int(getTotalPages(dom.select("em"))))
    nameListMain = displayList()
    print(nameListMain)


def getUserInfo(url):
    nameList = []
    # Create a DOM model for HTML data obtained
    dom = getRequestToGithub(url)
    all_repo = dom.select("ul.repo-list li div.d-flex div a")
    for each_repo in all_repo:
        name = each_repo.attrs["href"][1:]
        href_link = "https://github.com/{}".format(name)
        nameList.append(href_link)
    return nameList


def getAllUserData(total_pages):
    print(total_pages)
    for i in range(0, total_pages):
        i = i + 1
        url = URL.format(i, GIT_HUB_SEARCH_STRING)
        print(url)
        nList = getUserInfo(url)
        nameListMain.append(nList)
        sleep(randint(MIN_WAIT_TIME, MAX_WAIT_TIME))
    return nameListMain


def displayList():
    nameLst = []
    for nl in nameListMain:
        for names in nl:
            nameLst.append(names)
    return nameLst


def getTotalPages(pages):
    for page in pages:
        tp = page.attrs
        if(not(bool(tp))):
            continue
        else:
            total_pages = tp.get("data-total-pages")
    return total_pages


fetchGithubMainPage()
