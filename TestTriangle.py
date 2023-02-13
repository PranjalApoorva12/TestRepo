# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
#my_brand("HW02a-Testing a legacy program and reporting on testing results")
class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testValidInputsA(self): 
        self.assertEqual(classifyTriangle(0,0,0),"InvalidInput","(0,0,0) should be Invalid")
    def testValidInputsB(self): 
        self.assertEqual(classifyTriangle(-10,1.30,-3.40),"InvalidInput","(-10,1.30,-3.40) should be Invalid")

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(9.235,10.3,13.833),'Right',"(9.235,10.3,13.833) is a Right triangle")
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(10.3,10.3,10.3),'Equilateral','10.3,10.3,10.3 should be equilateral')

    def test_Isosceles_01(self):
        self.assertEqual(classifyTriangle(2.55,3.65,3.65),"Isosceles","(2,3,3) should be Isosceles")
    def test_Isosceles_02(self):
        self.assertEqual(classifyTriangle(29,30,29),"Isosceles","(29,30,29) should be Isosceles")

    def test_Scalene_01(self):
        self.assertEqual(classifyTriangle(12.5,13.6,14.7),"Scalene","(12,13,14) should be Scalene")
    def test_Scalene_02(self):
        self.assertEqual(classifyTriangle(20,30,40),"Scalene","(20,30,40) should be Scalene")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
    
#my_brand("HW02a-Testing a legacy program and reporting on testing results")
