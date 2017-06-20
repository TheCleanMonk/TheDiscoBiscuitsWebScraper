from bs4 import BeautifulSoup
import requests,re
from collections import Counter
from operator import itemgetter


r  = requests.get("http://discobiscuits.net/setlists.php?year=2016")

data = r.text



soup = BeautifulSoup(data,"html.parser")
# text = soup.find_all("div",{"class":"setlist"})
# dates = soup.find_all("div",{"class":"setlist-dateline"})

# for date in soup.find_all("a",{"href": ()}): # Finds all dates and venue
#     print(date.get_text())

# for set in soup.find_all("div",{"class": "set"}): # Finds all dates and venue
#     print(set.get_text())

set = soup.findAll("div",{"class": "set"}) # Finds all dates and venue
i = 1; count = 0; iter = []
for div in set:
    string = div.text.replace("Set 1:","").replace("Set 2:","").replace("E:  ","  ").replace(u'\xa0', u'').replace(" ","").replace(",",">").replace("Set:",">")
    string = re.sub("\d", "", string)
    row1 = string.split(">")
    for entry in row1:
        iter.append(entry)
        # if entry == 'ComingHome':
        #     count = count + 1
    if i == 1:
        set1 = row1
        # print("Set 1 \n" + str(set1))
    elif i == 2:
        set2 = row1
        # print("Set 2 \n" + str(set2))
    elif i == 3:
        set3 = row1
        # print("Encore \n" + str(set3))
        i = 0
    i = i + 1
# print(*iter,sep='\n')

count_country = Counter(iter)
output_list= []


for i in count_country:
    output_list.append([i,count_country[i]])

output_list.sort(key=itemgetter(1),reverse=True)
print(*output_list,sep='\n')
