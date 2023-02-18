from bs4 import BeautifulSoup as bs
import requests

github_user = input("\nInput Github User: ")
url = 'https://github.com/' + github_user
reqs = requests.get(url)
soup = bs(reqs.content, 'html.parser')

def main():
    def menu():
        print("\n\n")
        print("-" * 20, "MAIN MENU", "-" * 20)
        print("What would you like to view?\n")
        print("[a] Followers")
        print("[b] Following")
        print("[c] Repositories")
        print("[d] Exit Program")
    menu()
    menu = str(input("\nChoose an option: ").lower())

    if menu in ("a", "b", "c", "d"):
        if menu == "a":
            print()
        elif menu == "b":
            print()
        elif menu == "c":
            def repository():
                repoList = soup.find_all("li", class_='mb-3 d-flex flex-content-stretch col-12 col-md-6 col-lg-6')

                print("\n\nLIST OF REPOSITORIES\n")
                for repos in repoList:    
                    repoName = repos.find('span', class_='repo')
                    repoDescription = repos.find('p', class_='pinned-item-desc color-fg-muted text-small d-block mt-2 mb-3')
                    try:
                        print('Repository     :   ', repoName.text.strip())
                        print('Description    :   ', repoDescription.text.strip(), '\n')
                    except AttributeError:
                        continue

                repeat = input("\nWould you like to view other things, [y/n]: ").lower()
                if repeat.lower() == "y":
                    main()
                elif repeat.lower() == "n":
                    print("\nThank you for using this program!")
                    print("Have a nice day :)")
                    exit()
                else:
                    print("\nInvalid input! Please try again!")
                    main()
            repository()
        elif menu == "d":
            def exitProgram():
                exitOption = input("\nAre you sure you want to close this program, [y/n]: ").lower()
                if exitOption == "y":
                    print("\nThank you for using this program!")
                    print("Have a nice day :)")
                    exit()
                elif exitOption == "n":
                    main()
                else:
                    print("\nInvalid Input! Please try again!")
                    main()
            exitProgram()
        else:
            print("\nInvalid Input! Please try again!")
            menu()

    else:
        print("\nInvalid Input! Please try again!")
        main()
main()