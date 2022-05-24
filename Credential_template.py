# Programme : Credential_template
# Description : This class is the template of the Crendential class
# Date : 23/05/2022
# Author : Christophe Lagaillarde
# Version : 1.0

class Credential:
    def __init__(self) -> None:
        self.email = ""     # Add your github login email here
        self.password = ""  # Add your github login password here

    def get_email(self) -> str:
        return self.email

    def get_password(self) -> str:
        return self.password