from bs4 import BeautifulSoup as bs
import requests

github_user = input("Input Github User: ")
url = "https://github.com/" + github_user
reqs = requests.get(url)
soup = bs(reqs.content, "html.parser")
repoList = soup.find_all("li", class_='mb-3 d-flex flex-content-stretch col-12 col-md-6 col-lg-6')

for repos in repoList:
    repoName = repos.find("span", class_='repo')
    repoDescription = repos.find("p", class_="pinned-item-desc color-fg-muted text-small d-block mt-2 mb-3")
    try:
        print("\nRepository:             ", repoName.text)
        print("Description:", repoDescription.text.replace("\n",""), '\n\n')
    except AttributeError:
        continue    