Writing documentation using Sphinx and ReadtheDocs
===============================================================

Starting with Sphinx
----------------------------

To get started, run:

.. code-block:: text

  sphinx-quickstart
  
and choose its default options. 
It will create basis of your documentation. You can run 

.. code-block:: bash

  $ make html
  
and check your first documentation in the browser by opening *index.html*! (Don't forget to compile your documentation after every change, otherwise no changes will be visible on your local machine.)

Automatic source code documentation
------------------------------------

Now, to document your source code with comments written using Python documentation strings (or docstrings) run:

.. code-block:: text

  sphinx-apidoc -f -o <outputdir> <sourcedir>

Then modify *index.rst* as follows:

.. code-block:: text

  .. toctree::
    :maxdepth: 2
    :caption: Contents:

    modules
   
   
Done! 


Readthedocs import Problem
----------------------------

You created your documentation, run *sphinx-apidoc*, you can see nice source code documentation on your local machine, but no code documentation appears on the remote webpage? Check carefully the output of the recent build on ReadtheDocs. To do so log into https://readthedocs.org/ and follow the path: 

 Settings -> Profile -> <your_project_name> -> Build
 
Check output of each command. Probably, somewhere you have an error like

.. code-block:: text

  ImportError: No module named numpy
  
We need to tell ReadtheDocs (https://readthedocs.org/) to install module dependencies via pip in a the Python virtual environment. To do so, create requirements.txt file in a root directory of your project:

.. code-block:: text

  # Install numpy
  numpy


Log into https://readthedocs.org/ and follow the path: 

 Settings -> Profile -> <your_project_name> -> Admin -> Advanced Settings
 
Tick the box ‘Install your project inside a virtualenv using setup.py install’.
Below the box ‘Requirements file:’ it says *a pip requirements file needed to build your documentation. Path from the root of your project.* Thus fill in this box with (for example) *requirements.txt* and click ‘Submit’.

Now, when ReadtheDocs will compile your documentation, it will first create a virtual environment with installed numpy inside and then there run Sphinx autodoc.




Documentation examples
--------------------------

Here you can see examples of documentations created using Sphinx and ReadtheDocs:

http://docs-python2readthedocs.readthedocs.io/en/master/index.html
