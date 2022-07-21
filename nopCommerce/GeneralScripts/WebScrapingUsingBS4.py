from bs4 import BeautifulSoup
import requests
import pandas as pd

mainURI = 'https://news.google.com'
r = requests.get(mainURI)
s = BeautifulSoup(r.content, 'lxml')
# print(s.prettify())
print(s.title)

# ss = s.find('div', {'jscontroller': 'MRcHif'}).find_all('a')
ss = s.find_all('div', {'jscontroller': 'MRcHif'})
# print(ss)
URLs = []
URL_Texts = []
for i in ss:
    a = i.find_all('a', {'class': 'DY5T1d RZIKme'})


# .find_all('a')
# ss1 = ss.find('div', {'jscontroller': 'MRcHif'}).find_all('a')
# print(len(a))
for i in range(0, len(a)):
    SP = a[i].get('href')
    # print(a[i].text)
    URL_Texts.append(a[i].text)
    if SP != None:
        URLs.append(SP.replace('.', mainURI))

dict1={"URL_Text": [], "URL": []}
# a.setdefault("URL_Text",[])
for i in range(0, len(URL_Texts)):
    dict1["URL_Text"].append(URL_Texts[i])
    dict1["URL"].append(URLs[i])
# print(dict1)
# new_dict = {URL_Texts[i]: URLs[i] for i in range(len(URL_Texts))}
# print ("Created dictionary:", new_dict)
new_pandasTable = pd.DataFrame(dict1)
print(new_pandasTable)

new_pandasTable.to_csv('./saved_data.csv',
        header=['News HeadLine','URL'],
        sep=',',index=True)
