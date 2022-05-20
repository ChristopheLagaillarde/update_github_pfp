from selenium import webdriver
from time import sleep
from Credential import Credential


def check_if_element_exist_with_id(id_of_element, driver):
    try:
        driver.find_element_by_id(f'"{id_of_element}"')
    except Exception:
        return False
    return True


def check_if_element_exist_with_xpath(xpath_of_element, driver):
    try:
        driver.find_element_by_xpath(f'"{xpath_of_element}"')
    except Exception:
        return False
    return True


def change_github_pfp():
    options = webdriver.EdgeOptions()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Edge(executable_path="msedgedriver.exe", options=options)

    path_to_pic = 'C://Users/Lagaillarde/PycharmProject/automatically_change_pfp/temporary/cat.png'
    driver.get("https://thiscatdoesnotexist.com/")
    with open(path_to_pic, 'wb') as file:
        file.write(driver.find_element_by_xpath("// img[ @ src = 'https://thiscatdoesnotexist.com/']")
                   .screenshot_as_png)
    driver.get("https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsettings%2Fprofile")

    while check_if_element_exist_with_id("login_field", driver):
        sleep(1)
    my_login = Credential()
    driver.find_element_by_id('login_field').send_keys(my_login.get_email())
    driver.find_element_by_id('password').send_keys(my_login.get_password())
    driver.find_element_by_name('commit').click()
    del my_login

    while check_if_element_exist_with_id("avatar_upload", driver):
        sleep(1)
    driver.find_element_by_id("avatar_upload").send_keys(path_to_pic)

    sleep(40)
    driver.find_element_by_xpath("/html/body/details[2]/details-dialog/form/div[2]/button").click()


if __name__ == "__main__":
    change_github_pfp()


