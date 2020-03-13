""" Test_Piping

    Unittest for running pipesteps and the entire pipeline.
"""

import unittest
import logging
import numpy as np
logging.basicConfig(level=logging.DEBUG)
import os
TESTDATA_FOLDER = os.path.join(os.path.dirname(__file__), 'testdata')
CONFFILE = os.path.join(TESTDATA_FOLDER, 'testconf.txt')
FITSFILE = os.path.join(TESTDATA_FOLDER, 'testfit.fits')
from darepype.drp import DataParent

class TestSingleSteps(unittest.TestCase):
    
    def test_siso(self):
        """ Test siso step. Runs the step and makes sure
            that the data is the same but that the header
            has changed.
        """
        dp = DataParent(config = CONFFILE)
        df = dp.load(FITSFILE)
        step = dp.getobject('StepParent')
        head = df.header.copy()
        img = df.image.copy()
        do = step(df)
        self.assertEqual(np.sum(img-do.image), 0)
        self.assertNotEqual(head, do.header)
        
    def test_miso(self):
        """ Test a miso step. Runs the step and makes sure
            that the output data is as expected.
        """
        dp = DataParent(config = CONFFILE)
        df1 = dp.load(FITSFILE)
        df2 = dp.load(FITSFILE)
        step = dp.getobject('StepMIParent')
        head = df1.header.copy()
        img = df1.image.copy()
        do = step([df1, df2])
        self.assertEqual(np.sum(img-do.image), 0)
        self.assertNotEqual(head, do.header)
        
    def test_mimo(self):
        """ Test a mimo step. Runs the step and makes sure
            that the output data is as expected.
        """
        dp = DataParent(config = CONFFILE)
        df1 = dp.load(FITSFILE)
        df2 = dp.load(FITSFILE)
        step = dp.getobject('StepMOParent')
        head = df1.header.copy()
        img = df1.image.copy()
        do1, _do2 = step([df1, df2])
        self.assertEqual(np.sum(img-do1.image), 0)
        self.assertNotEqual(head, do1.header)

    def test_nimo(self):
        """ Test nimo step. Runs the step and makes sure
            that there is output data.
        """
        dp = DataParent(config = CONFFILE)
        dp.config['parentni']['filloutput'] = True
        step = dp.getobject('StepNIParent')
        step.config = dp.config
        do = step()
        self.assertIsInstance(do[0], DataParent)

class TestPipeLine(unittest.TestCase):
    
    def test_line(self):
        """ Test pipeline with all Steps
            - test with siso only
            - test with siso miso siso
            - test with mimo miso siso
            - test with nimo siso
        """
        pass