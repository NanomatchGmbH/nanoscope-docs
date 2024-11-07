.. _getting_started_quick_start:

Quick Start Guide
==================

Introduction
-------------
This guide provides step-by-step instructions for depositing a simple thin-film morphology and performing electronic structure analysis on it using Nanoscope. It is designed to help you quickly get started with the basic functionalities of Nanoscope. For more complex use cases, please refer to the **User Guide** section.

Prerequesits
-------------
* **Nanoscope Installation**: Ensure that Nanoscope is installed on your system. If not, follow the  :ref:`getting_started_installation` to set it up.

.. _getting_started_quick_start_setup:

Simulation Setup
-----------------

a. Design and Download the Molecule.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    1. Open `MolView <https://www.nanomatch.de/nanomatch-files/molview/>`_  in your web browser.
    2. Design a molecule of your choice, e.g. a biphenyl molecule.
    3. Use the ``clean`` and the ``2D to 3D`` buttons to generate a 3D structure of the molecule.
    4. Download the 3D molecule file with ``Tools -> MOL file``.

        .. figure:: quick_start/quick_start_0.png
           :alt: Design a molecule with MolView
           :width: 100%
           :align: center

           Design a molecule with MolView


    .. note:: We use biphenyl as a simple example as it allows for quick computation. It is not meant as a physical case study.

    .. note:: Feel free to try a different molecule. Keep in mind that the basic usage of Nanoscope covers molecules with up to 40 atoms.



c. Launch SimStack.
^^^^^^^^^^^^^^^^^^^
    On your local PC do the following:

    .. code-block:: bash

       micromamba activate simstack
       simstack

    This will activate SimStack environment and launch SimStack.

d. Set Up the Basic Nanoscope Workflow.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    **Drag&Drop** the modules `MolPrep`, `Deposit` and `ESAnalysis` from the top left panel into the middle workflow panel into a linear workflow and arrange as depicted below. Double click on each module to adapt settings and allocate resources for each simulation step.
    
        .. figure:: quick_start/quick_start_1.png
           :alt: Construct the workflow with drag&drop
           :width: 100%
           :align: center
        

e. Set Up Individual Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. ToDo: all this tips for test settings is ugly. Make extra page for test settings, refer to it.

    .. Tip:: All settings indicated in the following workflow and corresponding figures indicate settings for :ref:`production runs <getting_started_production_setup>`. Settings suitable for quick :ref:`technical tests <getting_started_test_setup>` that achieve quick, but meaningless results are indicated as tips below.

    In the central panel, double-click on the module to set it up.

    1. **MolPrep**.

        * Set the `Input Molecule File`: select the molecule you created above.
        * Adjust other settings as shown below.

        .. figure:: quick_start/quick_start_molprep.png
           :alt: MolPrep settings
           :width: 60%
           :align: center


    .. Tip:: For technical testing, use a small molecule and disable `Optimize Molecule` and `Compute Dihedral Forcefield`.


    2. **Desposit**

        * Adjust the ``Simulation Parameters`` tab:

        .. figure:: quick_start/quick_start_deposit_box.png
           :alt: deposit_box_settings
           :width: 60%
           :align: center

        This will generate a sufficiently large sample for the electronic structure analysis.

        .. Tip:: For technical testing especially on your laptop, adapt the settings as follows:

                * Lx, Ly = 10.0, Lz = 30.0
                * Number of Molecules: 10
                * Number of Steps: 30000
                * Number of SA cycles: 4 (or as many cpus as you have available)
                * Postrelaxation steps: 0


        * In the ``Molecules`` tab:

           Click on the rightmost buttons next to the input fields to load molecule and forcefield file from `MolPrep`:

             * `Molecule` input: `MolPPrep/outputs/molecule.pdb`
             * `Forcefield` input: `MolPPrep/outputs/molecule_forcefield.spf`

            .. note :: The `*.pdb`/`*.spf` files above do not yet exist; you specify the file paths where `MolProp` module will generate them.


        .. figure:: quick_start/quick_start_Deposit_mols.png
           :alt: deposit_molecules_input
           :width: 100%
           :align: center




    3. **ESAnalysis**

        .. Tip:: `ESAnalysis` is likely to crash for small morphologies that were generated with the test settings described in the green Tip box above. We therefore recommend to limit technical tests to the generation of morphologies, i.e. `MolPrep` and `Deposit`. If you insist to run `ESAnalysis` in a :ref:`test setup <getting_started_test_setup>` as well, disable `Compute absolute values of IP/EA` and set `Number of Molecules` for the Disorder Shell to 4. Note that you need a morphology (`structurePBC.cml`) with at least a few hundred molecules.

        .. list-table::
           :widths: 50 50
           :header-rows: 0

           * - .. figure:: quick_start/quick_start_ESA_general.png
                  :alt: ESAnalysis general tab
                  :width: 100%
                  :align: center

                  ESAnalysis general tab´
             - .. figure:: quick_start/quick_start_ESA_engines.png
                   :alt: ESAnalysis engines tab
                   :width: 100%
                   :align: center
            
                   ESAnalysis engines tab

        * In the ``General`` tab of the ESAnalysis module, adapt the following:

            * `Morphology`: `Deposit3/outputs/structurePBC.cml` (again using the rightmost button)
            * `Core Shell/Number of molecules`: For a quick test, reduce this number, minimal value 2.
            * `Shell for Disorder and Couplings/Number of molecules`: For a quick test, reduce this number to 100, increase to 400 for significant statistics.

        * In the ``Engines`` tab, set `Memory per CPU` to the total memory of your compute node divided by the number of processors.

f. Set Up Resources for Every Module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   For each module, go to the ``Resources`` tab and set the computational resources:

   +------------+--------------+-------------+-----------+
   | Module     | CPUs         | Memory (MB) | Walltime  |
   +============+==============+=============+===========+
   | MolPrep    | ≥32          | ≥64000      | A few     |
   |            |              |             | hours     |
   +------------+--------------+-------------+-----------+
   | Deposit    | 32           | ≥64000      | A few     |
   |            |              |             | hours     |
   +------------+--------------+-------------+-----------+
   | ESAnalysis | ≥64          | ≥128000     | Several   |
   |            |              |             | hours     |
   +------------+--------------+-------------+-----------+

   .. note :: * You can run the workflow with fewer cores, if the above resources are not available. This increases runtime respectively.

        * Memory is provided in MB in the resources tab. Running Nanoscope with less memory than indicated in the table above is possible, but you may run into out-of-memory issues especially for larger molecules.

        * Further information on resources is provided in the :ref:`user_guide_settings` section.


g. Save and Submit the Workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    1. Save the workflow with ``Ctrl+S`` or by clicking ``File -> Save`` or ``File -> Save As...``
    2. Connect to your resource using the `Connect` button in the top right of SimStack. Wait for the button to become green.
    3. Submit the workflow wiht ``Ctrl+R`` or by clicking ``Run -> Run``.
 

h. Monitor Progress
^^^^^^^^^^^^^^^^^^^

    You can monitor the progress of your workflow with the ``Jobs & Workflows`` tab in the right panel of SimStack:

    1. Navigate to the ``Jobs & Workflows`` tab on the right panel.

    2. Expand **Workflows** (double click) and locate your submitted workflow (identified by timestamp if necessary).

    3. Monitor the status of the workflow and the contained modules:

       - **Green**: Completed successfully
       - **Yellow**: Currently running
       - **Red**: Encountered an error

    4. Double-click on a module to view logs, output files, and detailed status.

    .. note :: Modules are only listed in this view once they have been started, i.e. when the predecessing module was finished successfully.

    .. figure:: quick_start/quick_start_monitor.png
       :alt: progress_monitoring
       :width: 60%
       :align: center




Output
------

Here we present a few examples of outputs of the standard Nanoscope workflow. For a detailed description, refer to :ref:`user_guide_computed_properties` or :ref:`user_guide_examples`.

MolPrep Output
^^^^^^^^^^^^^^^

=============================== ================================================================
File                            Content
=============================== ================================================================
output_molecule.mol2            coordinates of the optimized vaccum conformation
molecule.pdb                    optimized molecular vacuum conformation, formatted for Deposit
molecule_forcefield.spf         forcefield file for Deposit
mol_data.yml                    HOMO, LUMO and static dipole
=============================== ================================================================

Deposit Output
^^^^^^^^^^^^^^^

.. table:: 
   :class: responsive-table

   =============================== ========
   File                            Content
   =============================== ========
   structure.cml                   3D coordinates of the atoms in the thin film morphology. This file can be visualized with `jmol <https://jmol.sourceforge.net/>`_
   structure.mol2                  Atom coordinates in mol2 format
   structurePBC.cml                Morphology extended periodically in x- and y-direction, lateral to the deposition axis
   summary_RDF.png                 Plot of radial distribution functions of molecular center-of-geometry (COG) positions
   visualization_2D_and_3D.png     Visualization of molecular COG positions
   output_dict.yml                 Raw data of radial distribution functions, density (in g/cm3) and simulation settings
   =============================== ========


ESAnalysis Output
^^^^^^^^^^^^^^^^^^

The primary outputs of the ESAnalysis module are located in the `Analysis/DOS` directory within the module's runtime folder.

.. figure:: quick_start/quick_start_all_DOS_plot.png
   :alt: DOS in pristine film
   :width: 100%
   :align: center

   HOMO and LUMO distribution in a pristine morphology. The values in the figure are onsets of the distributions that compare to experimental values.

Further outputs are:

.. table:: 
   :class: responsive-table

   ==================================== ========
   File                                 Content
   ==================================== ========
   DOS_Gaussian.png                     Plot visualizing the Gaussian-broadened density of HOMO and LUMO levels without vibrational effects.
   Vibrational_Gaussian_DOS_plot.png    Plot showing the Gaussian-broadened HOMO/LUMO distribution including vibrational broadening.
   all_DOS_plot.png                     Combined plot overlaying DOS distributions with and without vibrational broadening (both are Gaussian-broadened).
   raw_data_homo_lumo.yaml              Exact HOMO and LUMO energies (in mixed morphologies for each molecule type). Includes mean, std, and all individual energy levels.
   homo_lumo_onsets.yaml                Calculated onset energies for HOMO and LUMO levels distribution for each molecule type, can be compared with experimental onsets.
   homo_lumo_centers.yaml               Mean and standard deviation of the distribution of HOMO and LUMO levels for each molecule type. Can be used as an ab-initio input for multi-scale simulation workflows.
   ==================================== ========

