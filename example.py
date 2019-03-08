import requests
from bs4 import BeautifulSoup as bSoup


class persamaankata(object):
 	"""docstring for persamaankata
 	Created by Ahmad Suryani 2019
 	"""
 	def __init__(self):
 		self.req = requests
 		self.url = "https://www.persamaankata.com/search.php"

 	def search(self,kata):
 		params = {'q':kata}
 		r = self.req.post(self.url,data=params)
 		data = bSoup(r.content,'html5lib')
 		temp = data.find('div',{'class':'thesaurus_group'})
 		result = []
 		for i in temp.findAll("a"):
 			teks = i.text
 			result.append(teks)
 		return result

if __name__ == '__main__':
	pk = persamaankata()
	hasil = pk.search("belajar")
	print(hasil)