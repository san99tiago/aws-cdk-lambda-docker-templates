# Built-in imports
import re

# External imports
import requests
from bs4 import BeautifulSoup


def get_github_information_from_user(github_user):
    """
    Simple function to get GitHub user's profile information from username.
    :param github_user: string of GitHub username.
    """
    r = requests.get("https://github.com/{}".format(github_user))
    soup = BeautifulSoup(r.text, "html.parser")

    class_to_validate_div = "user-profile-bio"
    try:
        bio = soup.find_all("div", class_=class_to_validate_div)
        response = bio[0].text.replace("\n", " ")
    except Exception as e:
        print("Error: {}".format(e))
        response = "Did not find any GitHub user/bio with given username. {}".format(e)

    return(response)


## ONLY FOR LOCAL TESTS! (OWN VALIDATIONS)
if __name__ == "__main__":
    github_user = "san99tiago"
    print(get_github_information_from_user(github_user))
