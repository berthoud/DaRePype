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
        df = datafits.DataFits()
        self.assertIsInstance(df,datafits.DataFits)
        
    def test_load(self):
        """ Test to load a fits file.
            Also tests if DataParent.load correctly finds
            data object for file
        """
        from darepype.drp import DataParent
        from darepype.drp import DataFits
        dp = DataParent(config = os.path.join(TESTDATA_FOLDER, 'testconf.txt'))
        df = dp.load(os.path.join(TESTDATA_FOLDER, 'testfit.fits'))
        self.assertIsInstance(df, DataFits)
        self.assertGreater(sum(df.image.shape), 0)
        
class TestDataText(unittest.TestCase):
    def test_init(self):
        """ Test make an object
        """
        from darepype.drp import datatext
        dt = datatext.DataText()
        self.assertIsInstance(dt, datatext.DataText)
        
    def test_load(self):
        """ Test to laod a text file.
            Also tests if DataParent.load correctly finds
            data object for file
        """
        from darepype.drp import DataParent
        from darepype.drp import DataText
        dp = DataParent(config = os.path.join(TESTDATA_FOLDER, 'testconf.txt'))
        dt = dp.load(os.path.join(TESTDATA_FOLDER, 'testtext.txt'))
        self.assertIsInstance(dt, DataText)
        self.assertGreater(len(dt.data), 0)

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
