# -*- coding: utf-8 -*-
#写好TestCase，然后由TestLoader加载TestCase到TestSuite，
#然后由TextTestRunner来运行TestSuite，
#运行的结果保存在TextTestResult中，整个过程集成在unittest.main模块中

import random
import unittest
import sys

class TestSequenceFunctions(unittest.TestCase):

	def setUp(self):  #setUpClass setUpModule
		self.seq = list(range(10))

	def tearDown(self):
		pass

	def test_shuffle(self):
		  # make sure the shuffled sequence does not lose any elements
		random.shuffle(self.seq)
		self.seq.sort()
		self.assertEqual(self.seq, list(range(10)))
		#self.assertNotEqual(a,b)
		#self.assertListEqual(a,b) #Dict Set Tuple
		#self.assertTrue(x)
		#self.assertFalse(x)
		#slef.assertIs(a,b)
		#self.assertIsNot(a,b)
		#slef.assertIsNone(x)
		#self.assertIsNotNone(x)
		#self.assertIn(a,b)
		#self.assertNotIn(a,b)
		#self.assertRaise() should raise an exception for an immutable sequence

	def test_choice(self):
		element = random.choice(self.seq)
		self.assertTrue(element in self.seq)
		self.fail('Error raised by May')
		print(self.failureException)

	#@unittest.skip("demonstrating skipping")
	#@unittest.skipIf(sys.platform.startswutg('mac'), "requires Windows")
	@unittest.skipUnless(sys.platform.startswith('mac'),"requires Mac")
	def test_sample(self):
		for element in random.sample(self.seq, 5):
			self.assertTrue(element in self.seq)

	@unittest.expectedFailure
	def test_fail(self):
		self.assertEqual(1,0,"broken")

def suite():
	#1.
	# suite = unittest.TestSuite()
	# suite.addTest(TestSequenceFunctions('test_shuffle'))
	# unittest.TextTestRunner(verbosity=2).run(suite)
	#2.
	suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)  #TestLoader load cases from testcase to suite
	#suite = unittest.TestLoader().loadTestsFromModule(unittest_module)
	test_result = unittest.TextTestRunner(verbosity=2).run(suite)
	#suite.debug()
	#suite.run()
	print(unittest.TestCase.failureException)
	print(suite.countTestCases())
	print(test_result.errors)
	print(test_result.failures)
	print(test_result.skipped)
	print(test_result.expectedFailure)

if __name__ =='__main__':
	#unittest.main()
	suite()



    #cmd
    #python -m unittest -v unittestmodule[ test_module2]
    #python -m unittest unittestmodule.TestSequenceFunctions
    #python -m unittest unittestmodule.TestSequenceFunctions.test_upper
    #python -m unittest discover
