from bs4 import BeautifulSoup
import requests

github_user = input("Input Github User: ")
url = "https://github.com/" + github_user
request = requests.get(url).text
soup = BeautifulSoup(request, "lxml")
repoList = soup.find_all("ol", class_="d-flex flex-wrap list-style-none gutter-condensed mb-4")

for repos in repoList:
    repositoryName = repos.find("span", class_='repo')
    repositoryDescription = repos.find("p", class_="pinned-item-desc color-fg-muted text-small d-block mt-2 mb-3")
    progLang = repos.find("span", itemprop="programmingLanguage")

    print("Repository:             ", repositoryName.text)
    print("Description:", repositoryDescription.text.replace("\n",""))
    print("Programming Language:   ", progLang.text)
