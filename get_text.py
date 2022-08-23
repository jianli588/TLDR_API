from bs4 import BeautifulSoup
from bs4.element import Comment
import requests


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False

    return True


def text_from_html(new_url):
    body = requests.get(new_url)
    website_data = body.text
    soup = BeautifulSoup(website_data, 'html.parser')

    text = ""
    # this gets text from CNN
    if "cnn" in new_url:
        for EachPart in soup.find_all("p", {"class": "zn-body__paragraph speakable"}):
            text = text + EachPart.get_text() + " "
        for EachPart in soup.find_all("div", {"class": "zn-body__paragraph"}):
            text = text + EachPart.get_text() + " "

    else:
        for EachPart in soup.find_all('a'):
            text = text + EachPart.get_text() + " "

    return text


# def get_file():
#     new_url = input("please enter an URL from CNN")
#     return text_from_html(new_url)
