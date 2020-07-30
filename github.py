""" Quick Script for Github search on subdomains """


import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SubGitter:
    """ Run Github Search on Subdomains headless or opening actual browser """

    def __init__(self, file):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        self.browser = webdriver.Chrome(options=options)
        self.file = file

    def github_search(self):
        """ Perform Github Search """

        email = "<your-email@mail.com>"
        password = "<password>"
        self.browser.get("https://github.com/login")
        element = self.browser.find_element_by_id("login_field")
        element.send_keys(email)
        element1 = self.browser.find_element_by_id("password")
        element1.send_keys(password)
        self.browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()
        f = open("subdomains.txt", "r")
        for i in f:
            url = "https://github.com/search?q=%%22%s%%22&type=Code" %(i.split()[0])
            self.browser.get(url)
            time.sleep(2)
            try:
                res = (self.browser.find_element_by_xpath\
                      ('//*[@id="js-pjax-container"]/div/div[2]/nav[1]/a[2]/span')\
                      .text.split('\n')[0])
                if res != 0:
                    print("%s for %s" %(res, i), end='')
            except:
                time.sleep(10)
        f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=\
             'Quick script to find github code searches for each subdomain')
    parser.add_argument('-f', '--file', required=True, help='the file consisting of subdomains')
    args = parser.parse_args()
    SubGitter(args.file).github_search()
