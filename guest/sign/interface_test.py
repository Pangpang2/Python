import requests
import unittest

class GetEventListTest(unittest.TestCase):

	def setUp(self):
		self.url = "http://127.0.0.1:8000/api/get_event_list/"

	def test_get_event_null(self):
		r = requests.get(self.url, params = {'eid':''})
		result = r.json()
		print(result)
		self.assertEqual(result['status'],10021)
		self.assertEqual(result['message'],'parameter error')

	def test_get_event_success(self): 
		'''发布会id为1，查询成功''' 
		r = requests.get(self.url, params={'eid':'1'}) 
		result = r.json() 
		print(result) 
		self.assertEqual(result['status'],200) 
		self.assertEqual(result['message'], "success") 
		self.assertEqual(result['data']['name'], "小米5发布会") 
		self.assertEqual(result['data']['address'], "软件园广场") 
		self.assertEqual(result['data']['start_time'], "2017-07-05T18:00:00Z")

if __name__ == '__main__':
	unittest.main()