import requests
from bs4 import BeautifulSoup as bs
import re
# res = requests.get("https://www.expertzlab.com/contact")
# print(res)
# # print(res.text)

# # Specify the parser explicitly
# val = bs(res.text, "html.parser")
# # print(val)

# result=val.findAll('div',attrs={'class':'contact-info'})
# # print(result)#print div with class contact-info as a list
# print(len(result))#show number of div tag with class contact-info
# # for i in result:
# #     print(i)#print div tags with class contact-info
# print(result[2].text)

# val=re.findall(r'[0-9]{10}',(result[2].text))
# print(val)

result=requests.get('https://www.expertzlab.com/courses/')
# print(result.text)

val=bs(result.text,"html.parser")
result=val.findAll('div',attrs={'style':'padding:50px;'})
print(result[0].text)