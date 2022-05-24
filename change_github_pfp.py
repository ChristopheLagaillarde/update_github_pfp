# Programme : change_github_pfp
# Description : this method change the github profile picture
#               with the pic of a cat from "thiscatdoesnotexist.com"
# Date : 23/05/2022
# Author : Christophe Lagaillarde
# Version : 1.0

from time import sleep

from selenium import webdriver

from Credential import Credential
from selenium_tools.id_exist import id_exist


def change_github_pfp(driver: webdriver) -> None:
    path_to_pic = 'C://Users/Lagaillarde/PycharmProject/automatically_change_pfp/temporary/cat.png'
    driver.get("https://thiscatdoesnotexist.com/")
    with open(path_to_pic, 'wb') as file:
        file.write(driver.find_element_by_xpath("// img[ @ src = 'https://thiscatdoesnotexist.com/']")
                   .screenshot_as_png)
    driver.get("https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsettings%2Fprofile")

    while not id_exist("login_field", driver):
        sleep(1)
    my_login = Credential()
    driver.find_element_by_id('login_field').send_keys(my_login.get_email())
    driver.find_element_by_id('password').send_keys(my_login.get_password())
    driver.find_element_by_name('commit').click()
    del my_login

    while not id_exist("avatar_upload", driver):
        sleep(1)
    driver.find_element_by_id("avatar_upload").send_keys(path_to_pic)

    sleep(40)
    driver.find_element_by_xpath("/html/body/details[2]/details-dialog/form/div[2]/button").click()