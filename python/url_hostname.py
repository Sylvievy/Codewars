'''
Extract the domain name from a URL[host name]
5kyu
6 d ago

this isn't mine, i am yet to explore re library
'''
import re

def domain_name(url):
    return re.search(r"(?:https?://)?(?:www\.)?([^\.]+)", url).group(1)


