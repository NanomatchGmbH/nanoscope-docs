.. _user_guide_settings:

Settings and Options
====================


This section contains a reference of all settings available in the individual modules. Refer to the :ref:`user_guide_examples` section to learn how different settings may be applied.

MolPrep
---------
+--------------------+-------------------------------------------------------+----------------+-----------+
| Setting            | Description                                           | Standard value | Anything? |
+====================+=======================================================+================+===========+
| Molecule (Mol2)    |Input file in mol2 format. Refer to the first steps of | N/A            |           |
|                    |:ref:`getting_started_quick_start_setup` for           |                |           |
|                    |instructions how to generate input files.              |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| Molecule Identifier|A 3-letter numeric string to label the molecule        | ABC (random)   |           |
|                    |throughout the workflow in various output files        |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| Optimize Molecule  |Optimize the molecule with DFT (B3LYP, def2-TZVP)      | True           |           |
|                    |Disable to use the molecular conformation as provided  | (checked)      |           |
|                    |in the inpup file                                      |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| Compute Dihedral   |Energy profiles for dihedral rotations are computed    | True           |           |
| Forcefields        |to sample different conformations during deposition    | (checked)      |           |
+--------------------+-------------------------------------------------------+----------------+-----------+


Deposit
--------

Simulation Parameters Tab
^^^^^^^^^^^^^^^^^^^^^^^^^

* Simulation Box
    
+--------------------+-------------------------------------------------------+----------------+-----------+
| Setting            | Description                                           | Standard value | Anything? |
+====================+=======================================================+================+===========+
| Lx                 |Input file in mol2 format. Refer to the first steps of | 45.0           |           |
|                    |:ref:`getting_started_quickstart_setup` for            |                |           |
|                    |instructions how to generate input files.              |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| Ly                 |                                                       | 45.0           |           |
|                    |                                                       |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| Ly                 |                                                       | 180.0          |           |
|                    |                                                       |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| PBC enabled        |                                                       | True           |           |
|                    |                                                       | (checked)      |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| PBC cutoff         |                                                       | 20.0           |           |
|                    |                                                       |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+

* Simulation Parameters

+--------------------+-------------------------------------------------------+----------------+-----------+
| Setting            | Description                                           | Standard value | Anything? |
+====================+=======================================================+================+===========+
| Number of          |Input file in mol2 format. Refer to the first steps of | 1000-4000      |           |
| Molecules          |:ref:`getting_started_quickstart_setup` for            |                |           |
|                    |instructions how to generate input files.              |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| Initial            |                                                       | 4000.0         |           |
| Temperature [K]    |                                                       |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| Final              |                                                       | 300.0          |           |
| Temperature [K]    |                                                       |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| SA Acc Temp        |                                                       | 5.0            |           |
|                    |                                                       |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| Number of Steps    |                                                       | 130000         |           |
|                    |                                                       |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| Number of SA       |                                                       | 32             |           |
| cycles             |                                                       |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| Dihedral moves     |                                                       | True           |           |
|                    |                                                       | (checked)      |           |
+--------------------+-------------------------------------------------------+----------------+-----------+
| Postrelaxaiton     |                                                       | 100000         |           |
| Steps              |                                                       |                |           |
+--------------------+-------------------------------------------------------+----------------+-----------+


Molecules Tab
^^^^^^^^^^^^^^^^^^^^^^^^^
+--------------------+-------------------------------------------------------+----------------------------+-----------+
| Setting            | Description                                           | Standard value             | Anything? |
+====================+=======================================================+============================+===========+
| Restart from       |Input file in mol2 format. Refer to the first steps of | False                      |           |
| existing           |:ref:`getting_started_quickstart_setup` for            |                            |           |
| morphology         |instructions how to generate input files.              |                            |           |
+--------------------+-------------------------------------------------------+----------------------------+-----------+
| Restartfile        |Only visible when Restart enabled. Load file from your | restartfile.zip            |           |
|                    |hardrive or import from another Deposit run            |                            |           |
+--------------------+-------------------------------------------------------+----------------------------+-----------+
| Molecules/         |                                                       | molecule.pdb               |           |
| Molecule           |                                                       | from MolPrep               |           |
+--------------------+-------------------------------------------------------+----------------------------+-----------+
| Molecules/         |                                                       | molecule_forcefield.spf    |           |
| Forcefield         |                                                       | from MolPrep               |           |
+--------------------+-------------------------------------------------------+----------------------------+-----------+
| Molecules/         |                                                       | 1.0                        |           |
| Mixing Ratio       |                                                       |                            |           |
+--------------------+-------------------------------------------------------+----------------------------+-----------+



Postprocessing Tab
^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------------+-------------------------------------------------------+----------------------------+-----------+
| Setting            | Description                                           | Standard value             | Anything? |
+====================+=======================================================+============================+===========+
| Extend             |Input file in mol2 format. Refer to the first steps of | True                       |           |
| morphology         |:ref:`getting_started_quickstart_setup` for            | (checked)                  |           |
| (x,y)              |instructions how to generate input files.              |                            |           |
+--------------------+-------------------------------------------------------+----------------------------+-----------+
| Cut first layer by |Only visible when Restart enabled. Load file from your | 7.0                        |           |
| (A)                |hardrive or import from another Deposit run            |                            |           |
+--------------------+-------------------------------------------------------+----------------------------+-----------+


ESAnalysis
--------------





