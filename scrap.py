# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup


page = requests.get('https://hipertextual.com/page3')
soup = BeautifulSoup(page.content, 'html.parser')


for each_div in soup.find_all("a", class_="linkPost--extended"): 
	try:
		urlFont = each_div['href']
		page2 = requests.get(urlFont)
		soup2 = BeautifulSoup(page2.content, 'html.parser')
		title = soup2.find("title").text

		if "Las ofertas del" in title:
			continue

		subtitle = soup2.find("div", class_="headlineSingle__lead clearLeft").text
		headImg = soup2.find("div", class_="articleHead__wrapperImg")
		main = soup2.find("div", {"role": "main"})
		article_text = ""
		for element in main:
			if element.name == 'p':
				if (element.figure is None):
					article_text += '\n' + ''.join(element.findAll(text = True))
				elif element.figure['id'] == 'image-1' and element.figure.img is not None:
					article_text += '\n\n' + "[img=" + element.figure.img['src'] + "]" + '\n'
			elif element.name in ['h3','h2']:
				article_text += '\n\n' + '[size=18]' + ''.join(element.findAll(text = True)) + '[/size]' + '\n'
							
		print urlFont	
		print ""
		print title	
		print ""	
		print subtitle
		print "[img=" + headImg.picture.img['src'] + "]"
		print article_text
		print "--------------------------------------------"
		print ""	
	except Exception as e:
		print e.message
		print "--------------------------------------------"
		print ""



	#print title
	#print subtitle.p
	#print headImg.picture.img['src']
	#print main

# data to be sent to KN3 
#data = {
#'url': headImg.picture.img['src'], 	
#'position':'post-thumbnail'}
# sending post request and saving response as response object 
#r = requests.post(url = API_ENDPOINT, data = data) 


# data to be sent to api 
#data = {'title':title, 
#        'category':'info', 
#        'privacy':1, 
 #       'closed':1,
  #      'source_flag':1,
   #     'sources':urlFont,
    #    'tags': 'noticias,tecnologia,ciencia,cultura digital',
    #    'body': article_text + img,
   #     'image_1x1':
  #      'image_4x3':
 #       } 
# sending post request and saving response as response object 
#r = requests.post(url = API_ENDPOINT, data = data) 
#