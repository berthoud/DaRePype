.. DaRePype documentation master file, created by
   sphinx-quickstart on Sat Apr 11 13:21:49 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   Run with 'make html' from doc folder may have to 
   export PATH=$PATH:/opt/local/Library/Frameworks/Python.framework/Versions/3.6/bin

########
DarePype
########

**Table of Contents**

.. toctree::
   :maxdepth: 4
   
   index

************
Introduction
************

DarePype is a framework to build data reduction pipelines. It helps organize and run pipeline parts as steps which can be run individually or as part of a larger pipeline. DarePype includes sample steps but other projects have steps which can be used. DarePype can be used by itself, as part of a batch job, interactively or to run individual pipeline steps. 
 
*********************
DarePype Architecture
*********************

The object structure and a simple data processing sequence are shown in the figure below:

.. image:: images/core_basic_all.png
   :alt: Pipeline architecture
   :width: 600
   
The diagram above on the left shows the object structure of the software: The flow of data through pipe steps is managed by the *Pipe Line* object. This object creates and calls *Pipe Step* objects, each responsible for a data reduction step. The sequence of pipe steps depends on the *Pipe Mode* which can either be set manually or is determined by matching input data header keywords. Data is stored and exchanged in *Pipe Data* objects, each containing data (images and/or tables) and header information. All pipeline components use a common *Configuration* object which contains description for all pipe modes, parameters for pipe steps and settings for pipe data behavior and pipeline operations. This object is loaded upon pipeline initialization. Messages are sent to common loggers by all pipeline objects. All log messages are usually sent to a log file but can be sent to standard output as well.

The diagram above on the on the right illustrates the flow of data through a two-step pipeline: Raw data is loaded into a pipe data object. Such objects are passed to the the pipe steps which return intermediate (or final) pipe data objects. Any pipe data object can be saved to file. Some steps (Multi-Input or MI) ingest several data objects, some steps (Multi-Output or MO) also return several data objects. The Pipe Line object stored intermediate results to rerun such steps when new data is added.

***************
Getting Started
***************

**Requirements:** You need the following to install and run DarePype:
 - Python with configobj and astropy installed (those should install autimatically if you use pip). Depending on the pipe steps you're running additional packages might be required.
 
 
**Installation:** Use PIP to install darepype.

.. code-block:: bash

    pip install darepype
    
If you are using **conda**, you might want to install the conda packages first before you install darepype and other packages with pip.

**Getting Pipe Steps:** To see example pipesteps download the Stoneedge Pipeline on github at `github.com/yerkesobservatory/pipeline <https://github.com/yerkesobservatory/pipeline>`_.
 
**************
Using DarePype
**************

Configuration
=============

The pipeline will also not run without a valid configuration file. These configuration files are written in plain text and are divided into sections (specified by [brackets] ), each section contains keywords. A DarePype configuration file contains the following sections:
 - General information such as the list of python packages to use for pipe steps (steppacks).
 - Data information such as which part of the filename indicates the file step identifier and which data objects to load.
 - Information for each pipe mode, such as the sequence of pipe steps. The mode_chop shown in the example below runs the steps LoadHAWC, Demod, Flat and NodBeams. The results from Demod and NodBeams are saved. The mode applies to files where the INSTCFG keyword is “POLARIZATION” and where the CMDFILE keyword is “ChopNod.txt”.
 - A section for each pipe step. In the example for StepFlat below, the step two parameters: flatfile, a string, and datalist, a list of strings.
 - Information about data handling such as instructions to substitute primary header keywords or combining multiple files.
 
 Config file example:

.. code-block:: ini

    [general]
        # list of packages to look for pipe step modules (order matters)
        steppacks = darepype.drp
        
    [data]
        # Regexp for part of the filename before the file step identifier
        # - default is '\A.+\.' for all filename before the last '.' including the '.'
        filenamebegin = '\A.+\.'
        # Regexp for part of the filename after the file step identifier
        # - default is '\.[A-Za-z0-9]+\Z' for alphanum characters after last '.'
        filenameend = '\.fits(\.gz)?\Z' # For fits files
        # list of data objects to consider when loading data
        dataobjects = DataFits

    [mode_chop]
        # list of steps
        stepslist = StepLoadHAWC, StepDemod, save, StepFlat, StepNodBeams, save
        # List of keyword=values required in file header to select this pipeline mode
        #   Format is: Keyword=Value|Keyword=Value|Keyword=Value
        datakeys = "INSTCFG = POLARIZATION|CMTFILE = ChopNod.txt"

    [flat]
        # filename for flat file
        flatfile = flatfiles/hawc_flat.fits
        # list of input file datasets to flatten
        datalist = R array, T array

Python based reduction
======================

Simple data reduction
---------------------

You can use the python interpreter to reduce a list of files you need to create a pipe object, assign a config file and run it with the file list. The necessary commands are:

.. code-block:: python

    from darepype.drp import PipeLine # Import the pipeline object
    pipe = PipeLine(config = 'path/file/name/of/pipeconfig.txt') # Create the pipe object and set configuration
    result = pipe(['data1.raw.fits', 'data2.raw.fits']) # Run the pipeline
    result.save('output_filename.fits') # Save the result

To see log messages from the pipeline you might want to set up logging:

.. code-block:: python

    import logging # Import the logging library
    logging.basicConfig(level = logging.INFO) # Configure logging to print messages of level info and higher
    
Step-by-step data reduction
---------------------------

To run individual pipeline steps you need to load the data into a pipedata object, then run the pipe step on it. Finally save the result. Assuming you have set the logging and the path the code would look like this:

.. code-block:: python

    # Import objects
    from darepype.drp import DataParent # Import pipedata object
    from mysteplib.stepmystep import StepMyStep # Import reduction step
    # Make a data object
    inputdata = DataParent(config = 'path/file/name/of/pipeconfig.txt')
    # Load the data with the parent object, the result is a data child object
    # of type given by the file format.
    inputdata = inputdata.load('path/file/name/of/input/data/file.fits')
    # Make a pipe step object and run it on the data
    mystep = StepMyStep()
    outputdata = mystep(inputdata)
    # Store the result
    outputdata.save('path/file/name/of/output/data/file.fits')

Command line based reduction
============================

The pipeline can be run from the (unix/windows) command line. For that the PYTHONPATH environment variable has to be set to access the darepype and step packages (see above). The pipeline can reduce multiple files and it uses the keywords from the file header to select the appropriate pipe mode and configuration. The pipeline is called as follows:

.. code-block:: bash

    python pipeline.py [-h] [-t] [--loglevel {DEBUG,INFO,WARN,ERROR,CRITICAL}]
                       [--logfile LOGFILE] [--pipemode PIPEMODE]
                       [config] [inputfiles [inputfiles ...]]


    Pipe Line
    positional arguments:
      config                pipeline configuration file (default = pipeconf.txt)
      inputfiles            input files pathname
    optional arguments:
      -h, --help            show this help message and exit
      -t, --test            runs the selftest of the pipeline
      --loglevel {DEBUG,INFO,WARN,ERROR,CRITICAL}
                            log level (default = INFO)
      --logfile LOGFILE     logging file (default = none)
      --pipemode PIPEMODE   pipeline mode (default = none)

A pipeline configuration file is required to run the pipeline.

It is also possible to run individual pipe steps directly from the command line:

.. code-block:: bash

    python stepfile.py [-h] [-t] [--loglevel {DEBUG,INFO,WARN,ERROR,CRITICAL}]
                       [--logfile LOGFILE] [--config CONFIG]
                       [--Pipe Step specific arguments]
                       [inputfiles [inputfiles ...]]
 
    Pipeline Step
    Positional arguments:
      inputfiles            input files pathname
    Optional arguments:
      -h, --help            show this help message and exit
      -t, --test            runs the selftest of this pipe step
      --loglevel={DEBUG,INFO,WARN,ERROR,CRITICAL}
                            requested log level (default = INFO)
      --logfile LOGFILE     log file pathname (default = none)
      --config=pipeconf.txt pipeline configuration file pathname (default = none)
      --Pipe Step specific arguments

The Pipe Step specific arguments depend on the parameter requirements for the particular pipe step. They are the same parameters as are specified for that pipe step in the configuration file. The config file is optional, as the steps have default parameters.

The following list of command illustrates the simplest way to fully reduce HAWC files:

.. code-block:: bash

    python pipeline.py pipeconf.txt file1.raw.fits file2.raw.fits

This process only stores the final result, unless save steps are specified under stepslist in the configuration file.

The following commands illustrate how to reduce the data using the pipe steps directly:

.. code-block:: bash

    python stepprepare.py file1.raw.fits file2.raw.fits
    python stepdemod.py file1.pre.fits file2.pre.fits
    python stepflat.py file1.dmd.fits file2.dmd.fits
    python stepnodbeams.py file1.fla.fits file2.fla.fits
    python stepnodmerge.py file1.bmc.fits file2.bmc.fits

Each program saves the files that are used as input for the next step. StepNodMerge is a multi-input single-output (MISO) step so it will only write one file, file2.mrg.fits. Each of these single step programs can have additional command line arguments as described above.

In real life several you might need several paths in your command so your command may look like this:

.. code-block:: bash

    python /home/myself/reduce/pipeline/src/drp/pipeline.py /home/myself/reduce/pipeline/config/pipeconf_myself.txt /home/myself/data/file1_RAW.fits /home/myself/data/file1_RAW.fits

******************
Indices and tables
******************

Please consult these pages for more details on using DaRePype:

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
