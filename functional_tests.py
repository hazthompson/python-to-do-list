from selenium import webdriver

browser = webdriver.Firefox()

# navit
browser.get('http://localhost:8080')

assert 'Django' in browser.title
