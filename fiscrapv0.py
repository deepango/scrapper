from lxml import etree
import requests

s = "https://www.franchiseindia.com/business-opportunities/all/all?page=1"
page = requests.get(s)
tree = etree.HTML(page.text)
element = tree.xpath('/html[1]/body[1]/div[11]/div[1]/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]')
content = etree.tostring(element[0])
print(content)
