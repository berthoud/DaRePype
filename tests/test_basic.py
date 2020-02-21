#!/usr/bin/env python
""" DAREPYPE tests
    ==============
    
    Run basic tests for darepype
    
    2DO:
    * Still add asserts in here!!
    
"""

#### Setup
# Add current path in case a different version of darepype is on the system
import sys
sys.path.insert(0,'..')


#### Import tests - make sure all imports w/o PROBLEMS
# drp package
from darepype.drp import dataparent
from darepype.drp import stepparent
from darepype.drp import pipeline

#### Make object
# basic drp objects
dp = dataparent.DataParent()
sp = stepparent.StepParent()
pl = pipeline.PipeLine()

#### Final message
print("That's all folks!")