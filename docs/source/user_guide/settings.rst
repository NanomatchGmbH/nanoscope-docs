.. _user_guide_settings:

Settings and Options
====================


This section contains a reference of all settings available in the individual modules. Refer to the :ref:`user_guide_examples` section to learn how different settings may be applied.

MolPrep
---------

+--------------------+-------------------------------------------------------+----------------+
| Setting            | Description                                           | Standard value |
+====================+=======================================================+================+
| Molecule (Mol2)    |Input file in mol2 format. Refer to the first steps of | N/A            |
|                    |:ref:`getting_started_quick_start_setup` for           |                |
|                    |instructions how to generate input files.              |                |
+--------------------+-------------------------------------------------------+----------------+
| Molecule Identifier|A 3-letter numeric string to label the molecule        | ABC (random)   |
|                    |throughout the workflow in various output files        |                |
+--------------------+-------------------------------------------------------+----------------+
| Optimize Molecule  |Optimize the molecule with DFT (B3LYP, def2-TZVP)      | True           |
|                    |Disable to use the molecular conformation as provided  | (checked)      |
|                    |in the inpup file                                      |                |
+--------------------+-------------------------------------------------------+----------------+
| Compute Dihedral   |Energy profiles for dihedral rotations are computed    | True           |
| Forcefield         |to sample different conformations during deposition    | (checked)      |
+--------------------+-------------------------------------------------------+----------------+


Deposit
--------

Simulation Parameters Tab
^^^^^^^^^^^^^^^^^^^^^^^^^

* Simulation Box
    
+--------------------+-------------------------------------------------------+----------------+
| Setting            | Description                                           | Standard value |
+====================+=======================================================+================+
| Lx                 |Half the box size in x direction in A. Box extends     | 45.0           |
|                    |from -Lx to Lx.                                        |                |
+--------------------+-------------------------------------------------------+----------------+
| Ly                 |Half the box size in y direction in A. Box extends     | 45.0           |
|                    |from -Ly to Ly. Recommended: Lx=Ly                     |                |
+--------------------+-------------------------------------------------------+----------------+
| Ly                 |Box size in z direction (deposition axis) in A. For    | 180.0          |
|                    |180A is sufficient for 2000 standard molecules with    |                |
|                    |60-100 atoms. Increase for morphologies containing     |                |
|                    |more or larger molecules                               |                |
+--------------------+-------------------------------------------------------+----------------+
| PBC enabled        |If enabled, periodic boundary conditions in x and y    | True           |
|                    |direction are applied, and the final morphology is     | (checked)      |
|                    |expanded in x and y direction (file `structurePBC.cml`)|                |
+--------------------+-------------------------------------------------------+----------------+
| PBC cutoff         |Cutoff in A applied in the computation of forcefield   | 20.0           |
|                    |contributions of periodic copies.                      |                |
+--------------------+-------------------------------------------------------+----------------+

* Simulation Parameters

.. note:: Most of the simulation parameters are calibrated to generate good morphologies. We recommend to modify parameters only as indicated.

+--------------------+-------------------------------------------------------+----------------+
| Setting            | Description                                           | Standard value |
+====================+=======================================================+================+
| Number of          |Number of molecules in the morphology. Number required | 1000-4000      |
| Molecules          |for ESAnalysis depends on the molecule size.           |                |
|                    |For NPB, 2000 molecules are sufficient.                |                |
|                    |For small molecules such as BPhen, increase to 3000    |                |
+--------------------+-------------------------------------------------------+----------------+
| Initial            |Initial temperature of the simulated annealing cycles. | 4000.0         |
| Temperature [K]    |*Leave as is*.                                         |                |
+--------------------+-------------------------------------------------------+----------------+
| Final              |Initial temperature of the simulated annealing cycles. | 300.0          |
| Temperature [K]    |*Leave as is*.                                         |                |
+--------------------+-------------------------------------------------------+----------------+
| SA Acc Temp        |Acceptance temperature of the simulated annealing      | 5.0            |
|                    |cycles. *Leave as is*.                                 |                |
+--------------------+-------------------------------------------------------+----------------+
| Number of Steps    |Number of Monte Carlo steps per SA cycle.              | 130000         |
|                    |*Leave as is*.                                         |                |
+--------------------+-------------------------------------------------------+----------------+
| Number of SA       |Number of simulated annealing (SA) cycles per          | 32             |
| cycles             |deposition. SA cycles are executed in parallel.        |                |
|                    |Optimal performance of deposit is achieved in case of  |                |
|                    |`Number of SA cycles` = `cpus_per_node`                |                |
|                    |We recommend to use no fewer than 20 SA cycles.        |                |
+--------------------+-------------------------------------------------------+----------------+
| Dihedral moves     |Allow for intramolecular dihedral rotations for        | True           |
|                    |flexible molecules. Moves are only executed if         | (checked)      |
|                    |`compute Dihedral Forcefield` was enabled in MolPrep.  |                |
+--------------------+-------------------------------------------------------+----------------+
| Postrelaxaiton     |Number of low-temperature Monte Carlo steps at the     | 100000         |
| Steps              |end of each SA cycle. *Leave as is*.                   |                |
+--------------------+-------------------------------------------------------+----------------+


Molecules Tab
^^^^^^^^^^^^^^^^^^^^^^^^^
+--------------------+-------------------------------------------------------+----------------------------+
| Setting            | Description                                           | Standard value             |
+====================+=======================================================+============================+
| Restart from       |Enable to deposit on top of an existing morphology.    | False                      |
| existing           |Note that box parameters need to be identical in both  |                            |
| morphology         |Deposit runs.                                          |                            |
+--------------------+-------------------------------------------------------+----------------------------+
| Restartfile        |Only visible when Restart enabled. Load file from your | restartfile.zip            |
|                    |hardrive or import from another Deposit run to continue|                            |
|                    |Deposition on the existing morphology                  |                            |
+--------------------+-------------------------------------------------------+----------------------------+
| Molecules/         |Input molecule file from MolPrep                       | molecule.pdb               |
| Molecule           |                                                       |                            |
+--------------------+-------------------------------------------------------+----------------------------+
| Molecules/         |Input focefield file from MolPrep                      | molecule_forcefield.spf    |
| Forcefield         |                                                       |                            |
+--------------------+-------------------------------------------------------+----------------------------+
| Molecules/         |In case multiple molecular inputs are supplied via the | 1.0                        |
| Mixing Ratio       |`+` button, adapt this number to define the mixing     |                            |
|                    |ratio.                                                 |                            |
+--------------------+-------------------------------------------------------+----------------------------+



Postprocessing Tab
^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------------+-------------------------------------------------------+----------------------------+
| Setting            | Description                                           | Standard value             |
+====================+=======================================================+============================+
| Extend             |If PBC was enabled, the morphology can be expanded in  | True                       |
| morphology         |x and y direction. If checked the final morphology is  | (checked)                  |
|                    |expanded and provided in the file `structurePBC.cml`.  |                            |
|                    |**The expanded file is required for ESAnalysis**       |                            |
+--------------------+-------------------------------------------------------+----------------------------+
| Cut first layer by |The bottom layer may contain artefacts and is          | 7.0                        |
| (A)                |cut during expansion. Increase for larger molecules.   |                            |
+--------------------+-------------------------------------------------------+----------------------------+


ESAnalysis
--------------

General Tab
^^^^^^^^^^^^^^^^^^^^^^^^^
* General Settings

+--------------------+-------------------------------------------------------+----------------------------+
| Setting            | Description                                           | Standard value             |
+====================+=======================================================+============================+
| Morphology         |Morphology file from Deposit. Load from your hard drive| structurePBC.cml           |
|                    |or import from the Deposit module in the same workflow.|                            |
|                    |For sufficient environment, use the periodically       |                            |
|                    |expanded morphology in `structurePBC.cml`              |                            |
+--------------------+-------------------------------------------------------+----------------------------+
| Compute absolute   |Computes absolute values for ionization potential and  | True                       |
| levels of IP/EA    |electron affinity for molecules in the core shell.     | (checked)                  |
|                    |Computationally more expensive than disorder.          |                            |
|                    |Not required e.g. for mobility of pristine materials.  |                            |
+--------------------+-------------------------------------------------------+----------------------------+
| Compute disorder   |Compute distributions of HOMO and LUMO energies on a   | True                       |
|                    |larger set of molecules.                               | (checked)                  |
|                    |                                                       |                            |
+--------------------+-------------------------------------------------------+----------------------------+
| Compute couplings  |Compute electronic couplings for molecules in the      | True                       |
|                    |Disorder shell. Computationally insignificant in       | (checked)                  |
|                    |comparison to disorder computation                     |                            |
+--------------------+-------------------------------------------------------+----------------------------+


* Shell setup


+---------------------+--------------------------------------------------------------------------------------------+----------------------------+
| Setting             | Description                                                                                | Standard value             |
+=====================+============================================================================================+============================+
| Core Shell /        |Specify how to chose molecules for computation of IP                                        | Number of Molecules        |
| Shell size defined  |and EA.                                                                                     |                            |
| by                  |Number of molecules: Compute IP and EA on the N innermost molecules in the morphology:      |                            |
|                     |Number of molecules of each type: Compute IP and EA on the N innermost molecules of each    |                            |
|                     |type in the morphology;                                                                     |                            |
|                     |List of Molecule IDs: Provide a specific list of molecule IDs.                              |                            |
+---------------------+--------------------------------------------------------------------------------------------+----------------------------+
| Core Shell /        |Number of molecules or molecules of each type on which to compute IP and EA. Reasonable     | 8                          |
| Number of molecules |values are between 2 and 8, depending on available resources and required statistics.       |                            |
+---------------------+--------------------------------------------------------------------------------------------+----------------------------+
| Core Shell /        |Specific list of molecule IDs. IDs can be separated by                                      | 43; 57; 79-100             |
| List of molecule IDs|semicolon, applied as a range using a hyphen, or a combination of both.                     |                            |
|                     |                                                                                            |                            |
+---------------------+--------------------------------------------------------------------------------------------+----------------------------+
| Disorder Shell /    |Number of molecules on which to compute HOMO and LUMO disorder. Depending on the available  | 200                        |
| Number of molecules |resources, 200-400 molecules are recommended for sufficient statistics.                     |                            |
+---------------------+--------------------------------------------------------------------------------------------+----------------------------+


Enginges Tab
^^^^^^^^^^^^^^^^^^^^^^^^^
+--------------------+-------------------------------------------------------+----------------------------+
| Setting            | Description                                           | Standard value             |
+====================+=======================================================+============================+
| Memory per CPU (MB)|Set to the total memory of your node / resource,       | 2000                       |
|                    |divided by the number of processors.                   |                            |
|                    |                                                       |                            |
+--------------------+-------------------------------------------------------+----------------------------+
| GW Engine          |The GW step during IP/EA computation can be performed  | PySCF                      |
|                    |with Turbomole or PySCF. PySCF is integrated in the    |                            |
|                    |Nanoscope, Turbomole requires separate installation and|                            |
|                    |license.                                               |                            |
+--------------------+-------------------------------------------------------+----------------------------+
| Functional GW      |Functional for the GW step. For PySCF, this step is    | PBE0                       |
|                    |only calibrated for PBE0. For Turbomole, TMHF is       |                            |
|                    |slightly more accurate than PBE0.                      |                            |
+--------------------+-------------------------------------------------------+----------------------------+


Storage Tab
^^^^^^^^^^^^^^^^^^^^^^^^^
+--------------------+-------------------------------------------------------+----------------------------+
| Setting            | Description                                           | Standard value             |
+====================+=======================================================+============================+
| Storage            |ESAnalysis typically runs in a scratch directory       | Workdir                    |
| location           |defined during installation. At the end of the run,    |                            |
|                    |a certain set of runtime files are copied back to the  |                            |
|                    |work directory where the job was submitted. In the     |                            |
|                    |case of limited space in the Workdir, set to `Scratch` |                            |
|                    |to keep runtime files in scratch and only copy main    |                            |
|                    |output files back to the work directory.               |                            |
+--------------------+-------------------------------------------------------+----------------------------+