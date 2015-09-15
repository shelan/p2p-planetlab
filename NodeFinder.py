import os

__author__ = 'shelan'

import requests
import bs4

response = requests.get('http://monitor.planet-lab.eu/monitor/node')
print response.text

soup = bs4.BeautifulSoup(response.text)
data = []
table = soup.find('table',id ="nodelist")
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.rstrip() for ele in cols]
    data.append([ele for ele in cols if ele])


file = open("nodes.txt","w+")
ctr =0
num_of_nodes =30

#TODO: sort list by last seen date.

for item in data:
    if(item[3] == 'good' and ctr != num_of_nodes):
        ping_results = os.system("ping -c 1 " + item[2]);
        if(ping_results==0):
            print 'pinged ', item[2]
            print item[0], ', '.join(map(str, item[1:]))
            ctr += 1
            file.writelines(item[2] +'\n')

