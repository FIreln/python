from selenium import webdriver

brow = webdriver.Chrome()
brow.get('http://localhost:8000')
assert 'Dijango' in brow.title