from bs4 import BeautifulSoup
import requests

github_user = input("Input Github User: ")
url = "https://github.com/" + github_user