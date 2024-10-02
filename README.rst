Nanoscope Documentation
=======================

Purpose
-------
This repository contains the public documentation of the Nanoscope tool from Nanomatch, including description, user guide, scientific information and support.

The documentation is hosted on Read the Docs: `Nanoscope <https://nanoscope.readthedocs.io/en/latest/>`_

Restructured Text (rst)
-----------------------
The documentation is written in reStructuredText. Check out the cheat sheet of reStructuredText: `Cheat Sheet <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_; another available here: `Quick Reference <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_

Local Build (Testing)
---------------------
To locally build the documentation, navigate into the ``docs`` folder and run:

.. code-block:: sh

    make html

Note that you need to have Sphinx installed for this:

.. code-block:: sh

    pip install sphinx
    pip install sphinx-rtd-theme

Commits and Pull Requests (PRs)
-------------------------------
Please work in a separate branch, not in ``main``.

1. Create and checkout a new branch.
2. If you want your changes to go online, log in to the GitHub repository and create a pull request (PR).
3. The admins will review the PR and merge it into ``main``; the changes will then go online automatically.
4. Please create a seperate PR for any releasable increment.


Conventions
-----------

Follow the instructions below if you need to show images in your `.rst` files or provide links to download files.

Images
~~~~~~

Create a folder named after your `.rst` file and place images there.

Example::

    source/
    └── path/
        └── to/
            ├── my_name.rst
            └── my_name/
                ├── my_image_1.png
                └── my_image_2.png


Files
~~~~~

Place in the `_static` folder, mimicking the path structure of your `.rst` file.

Example::


    source/
    ├── _static/
    │   └── path/
    │       └── to/
    │           └── my_name/
    │               └── my_text_file.txt
    └── path/
        └── to/
            └── my_name.rst
