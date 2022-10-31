from bs4 import BeautifulSoup

file = open("B:\DS290822B\DS290822B\_22_xml_file_handling\sample_xml.xml")

soup = BeautifulSoup(file,'html.parser')

# # it will convert your soup object into list
data = soup.find_all("students")
# print(data)

# find is used to fetch the data on the bases of tag_name
name = soup.find("name")
print(name.text)

rno = soup.find("rno")
print(rno.text)

name = soup.find("name",{"name":"three"})
print(name.text)

