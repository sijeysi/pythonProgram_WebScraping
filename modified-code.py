from bs4 import BeautifulSoup as bs
import requests


github_user = input("\nInput Github User: ")
url = 'https://github.com/' + github_user
reqs = requests.get(url)
soup = bs(reqs.content, 'html.parser')

# For the overview of the profile 
print("\n\nPROFILE OVERVIEW\n")
info = soup.find_all("div", class_='js-profile-editable-replace')

for infos in info:    
    fullName = infos.find('span', class_='p-name vcard-fullname d-block overflow-hidden')
    username = infos.find('span', class_='p-nickname vcard-username d-block')
    try:
        print('Full Name   :   ', fullName.text.strip())
        print('Username    :   ', username.text.strip(), '\n')
    except AttributeError:
        continue


# For the list of repositories
repoList = soup.find_all("li", class_='mb-3 d-flex flex-content-stretch col-12 col-md-6 col-lg-6')

print("\nLIST OF REPOSITORIES\n")
for repos in repoList:    
    repoName = repos.find('span', class_='repo')
    repoDescription = repos.find('p', class_='pinned-item-desc color-fg-muted text-small d-block mt-2 mb-3')
    try:
        print('Repository     :   ', repoName.text.strip())
        print('Description    :   ', repoDescription.text.strip(), '\n')
        
    except AttributeError:
        continue


# Summary using dictionaries
info_summary= {}

fullName1 = fullName.text.replace('\n',"").strip()
username1 = username.text.replace('\n',"").strip()

info_summary["Full Name"] = fullName1
info_summary["Username"] = username1
print("Dictionaries:", info_summary)

repoName1 = repoName.text.strip()
info = [fullName1, username1, repoName1]
print("List:", info)



age = int(input("\nEnter your age: "))
school = input("Enter your school: ")

info_summary["Age"] = age
info_summary["School"] = school

print(info_summary)










