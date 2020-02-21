""" Test_Objects

    Unittest for darepype objects. Creates an instance of every object.
"""

import unittest

class TestDataParent(unittest.TestCase):
    def test_init(self):
        """ Test make an object
        """
        from darepype.drp import dataparent
        dp = dataparent.DataParent()
        self.assertObjectIsClass(dp,dataparent.DataParent)

class TestStepParent(unittest.TestCase):
    def test_init(self):
        """ Test make an object
        """
        from darepype.drp import stepparent
        sp = stepparent.StepParent()
        self.assertObjectIsClass(sp,stepparent.StepParent)
        
class TestPipeLine(unittest.TestCase):
    def test_init(self):
        """ Test make an object
        """
        from darepype.drp import pipeline
        pl = pipeline.PipeLine()
        self.assertObjectIsClass(pl,pipeline.PipeLine)
