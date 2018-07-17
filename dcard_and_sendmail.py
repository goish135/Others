# dcard and send mail


import requests #引入函式庫
from bs4 import BeautifulSoup
import re


url = 'https://www.dcard.tw/f'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
dcard_title = soup.find_all('h3', re.compile('PostEntry_title_'))

title_list = []
#print('Dcard 熱門前十文章標題和連結：')
for index, item in enumerate(dcard_title[:10]):
	#print("{0:2d}. {1}".format(index + 1, item.text.strip()))
	title_list+=["{0:2d}. {1}".format(index + 1, item.text.strip())]
	
dcard_link = soup.find_all('a',{'class':'PostEntry_root_V6g0r'})
prefix = 'https://www.dcard.tw'
#counter = 1
counter = 0
context_list = []
for h in dcard_link:
	#print('第幾篇: ',counter)
	#print(title_list[counter])
	#print(prefix+h['href'])
	context_list += [prefix+h['href']]
	if(counter==9):
		break
	counter = counter + 1

context =''
for item in range(10):
	context+=(title_list[item]+'\n')
	context+=(context_list[item]+'\n')

#print(context)

import smtplib
from email.mime.text import MIMEText
user = "acs104135@gm.ntcu.edu.tw"
pwd  = "secret"
msg = MIMEText(context)
msg['Subject'] = 'Dcard 熱門前十文章標題和連結'
msg['From'] = user
msg['To'] = 'goish13579@gmail.com'

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.ehlo()
server.login(user,pwd)
server.send_message(msg)
server.quit()

print('Email sent!')