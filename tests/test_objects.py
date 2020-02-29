""" Test_Objects

    Unittest for darepype objects. Creates an instance of every object.
"""

import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

class TestDataParent(unittest.TestCase):
    def test_init(self):
        """ Test make an object
        """
        from darepype.drp import dataparent
        dp = dataparent.DataParent()
        self.assertIsInstance(dp, dataparent.DataParent)
        from darepype.drp import DataParent
        dp = DataParent()
        self.assertIsInstance(dp, DataParent)

class TestDataFits(unittest.TestCase):
    def test_init(self):
        """ Test make an object
        """
        from darepype.drp import datafits
        dp = datafits.DataFits()
        self.assertIsInstance(dp,datafits.DataFits)

class TestStepParent(unittest.TestCase):
    def test_init(self):
        """ Test make an object
        """
        from darepype.drp import stepparent
        sp = stepparent.StepParent()
        self.assertIsInstance(sp,stepparent.StepParent)
        
class TestPipeLine(unittest.TestCase):
    def test_init(self):
        """ Test make an object
        """
        from darepype.drp import pipeline
        pl = pipeline.PipeLine()
        self.assertIsInstance(pl,pipeline.PipeLine)
        
class TestStepMIParent(unittest.TestCase):
    def test_init(self):
        """ Test make an object
        """
        from darepype.drp import stepmiparent
        sp = stepmiparent.StepMIParent()
        self.assertIsInstance(sp,stepmiparent.StepMIParent)
        
class TestStepMOParent(unittest.TestCase):
    def test_init(self):
        """ Test make an object
        """
        from darepype.drp import stepmiparent
        sp = stepmiparent.StepMIParent()
        self.assertIsInstance(sp,stepmiparent.StepMIParent)
        
class TestStepNIParent(unittest.TestCase):
    def test_init(self):
        """ Test make an object
        """
        from darepype.drp import stepniparent
        sp = stepniparent.StepNIParent()
        self.assertIsInstance(sp,stepniparent.StepNIParent)
