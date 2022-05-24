# Programme : main
# Description : this program execute change_github_pfp without displaying anything to the user
# Date : 23/05/2022
# Author : Christophe Lagaillarde
# Version : 1.0

from selenium_tools.while_making_automation_headless import while_making_automation_headless
from change_github_pfp import change_github_pfp


def main() -> None:
    change_github_pfp(while_making_automation_headless())


if __name__ == "__main__":
    main()

