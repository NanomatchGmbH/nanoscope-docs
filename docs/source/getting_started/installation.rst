.. _getting_started_installation:

Installation
============

Software structure
-------------------

Nanoscope is designed to run on scalable computational resources. To define simulation workflows and then execute on remote computational resources we use the `SimStack workflow platform <https://simstack.readthedocs.io/>`_ that consists of a SimStack Client to be installed locally (on the `Client`, e.g. your laptop) and a SimStack Server component on your computational resource. In total the Nanoscope consists of four parts:

=============================== =======================
Module                          Installed on...
=============================== =======================
Nanoscope Simulation Software   Computational resource
SimStack Server                 Computational resource
SimStack Client                 Client (e.g. laptop)
WaNos                           Client (e.g. laptop)
=============================== =======================

`WaNos` - short for `Workflow Active Nodes` are the graphical representation of the Nanoscope modules on the Client to combine into simulation workflows. The setup is summarized in the figure below.

.. figure:: installation/SoftwareStructure.png
   :alt: Software Structure
   :width: 80%
   :align: center

   Overview of the Nanoscope Software Structure

.. ToDo: Align font type in pic with readthedocs


Technical requirements
-----------------------
Computational resource
^^^^^^^^^^^^^^^^^^^^^^^^
The Nanoscope modules are best executed on 32 cores or more. Especially the `ES Analysis` scales very well with the number of cores. The modules `MolPrep` and `Deposit` scale well up to 64 and 32 cores respectively. 

=============================== ======================= =======================
Feature                         Recommendation          Minimal requirement
=============================== ======================= =======================
Operating system                Linux                   Linux
Number of cores                 120 or more             16
Memory                          3 GB / core             1.5 GB / core
=============================== ======================= =======================

Client / Local PC
^^^^^^^^^^^^^^^^^
There are no special requirements for the local resource where the SimStack Client and the WaNos are installed. The SimStack Client is available for Linux, Windows and MacOS.



Installation step-by-step
----------------------------




SimStack Configuration
-------------------------