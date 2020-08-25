from django.test import TestCase
from sign.models import Event, Guest
from django.test import Client
from django.contrib.auth.models import User
from datetime import datetime

# Create your tests here.

class ModelTest(TestCase):

	def setUp(self):
		Event.objects.create(name='oneplus 3 event', 
							 status = True,
							 limit = 200,
							 address ='shenzhen',
							 start_time = '2016-08-31 02:18:22')

		Guest.objects.create(event_id = 5,  
							 realname= 'david',
							 phone='13711001101',
							 email='david@mail.com',
							 sign = False)

	def test_event_modules(self):
		result = Event.objects.get(name = 'oneplus 3 event')
		self.assertEqual(result.address, 'shenzhen')
		self.assertTrue(result.status)

class IndexPageTest(TestCase):

	def test_index_page_renders_index_template(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')

class LoginActionTest(TestCase):

	def setUp(self):
		User.objects.create_user('admin', 'admin@mail.com','admin123456')
		self.c = Client()

	def test_login_action_username_password_null(self):
		test_data = {'username': '','password':''}
		response = self.c.post('/login_action/', data = test_data)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b"username or password error!", response.content)

	def test_login_action_username_password_error(self):
		test_data = {'username':'abc','password':'123'}
		response = self.c.post('/login_action/', data = test_data)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b"username or password error!", response.content)

	def test_login_action_success(self):
		test_data = {'username':'admin','password':'admin123456'}
		response = self.c.post('/login_action/', data = test_data)
		self.assertEqual(response.status_code, 302)

class EventManageTest(TestCase):
	def setUp(self):
		Event.objects.create(id=2, name='xiaomi5', limit = 2000,status = True,address='beijing',start_time=datetime(2016,8,10,14,0,0))
		self.c = Client()

	def test_event_manage_success(self):
		response = self.c.post('/event_manage/')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'xiaomi5', response.content)
		self.assertIn(b'beijing', response.content)

	def test_event_manage_search_success(self):
		response = self.c.post('/search_name/',{'name':'xiaomi5'})
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'xiaomi5', response.content)
		self.assertIn(b'beijing', response.content)