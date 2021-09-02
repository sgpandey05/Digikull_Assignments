import unittest
import sys
sys.path.insert(0, 'script_4')


# import py_file
from script_4 import *
sys.path.insert(0, 'script_5')
from script_5 import *

class MyTest(unittest.TestCase):
    def test_script_4_1(self):
        self.assertEqual(bmi_script_4(30,0.8,65), 'The BMI is 101.6')

    def test_script_4_2(self):
        self.assertEqual(bmi_script_4(31,1.8,100), 'The BMI is 30.9')
    
    def test_script_4_3(self):
        self.assertEqual(bmi_script_4(13,1.6,50), 'The BMI is 19.5')
    
    def test_script_5_1(self):
        self.assertEqual(bmi_script_5(1.52,59), 'Your BMI is 25.5 which means you are overweight.')
    
    def test_script_5_2(self):
        self.assertEqual(bmi_script_5(2,59), 'Your BMI is 14.8 which means you are underweight.')
    
    def test_script_5_3(self):
        self.assertEqual(bmi_script_5(1.6,50), 'Your BMI is 19.5 which means you are normal.')
    def test_script_5_4(self):
        self.assertEqual(bmi_script_5(1.8,90), 'Your BMI is 27.8 which means you are overweight.')
    def test_script_5_5(self):
        self.assertEqual(bmi_script_5(0.8,65), 'Your BMI is 101.6 which means you are obese.')

if __name__ == '__main__':
    unittest.main()