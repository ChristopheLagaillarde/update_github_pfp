# Programme : id_exist
# Description : This function check if the element with specified id exist
# Date : 23/05/2022
# Author : Christophe Lagaillarde
# Version : 1.0

from selenium.common.exceptions import NoSuchElementException


def id_exist(id_of_element, driver):
    try:
        driver.find_element_by_id(f'"{id_of_element}"')
    except NoSuchElementException:
        return False
    return True