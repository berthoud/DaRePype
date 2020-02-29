""" Test_Objects

    Unittest for darepype objects. Creates an instance of every object.
    Runs specific tests for each type of object.
"""

import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
import os
TESTDATA_FOLDER = os.path.join(os.path.dirname(__file__), 'testdata')

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
        
    def test_config(self):
        """ Tests loading the configuration
        """
        from darepype.drp import DataParent
        conf = os.path.join(TESTDATA_FOLDER,'testconf.txt')
        dp = DataParent(config = conf)
        self.assertIn('general', dp.config)

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
