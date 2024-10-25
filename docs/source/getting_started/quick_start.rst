.. _getting_started_quick_start:


Quick Start Guide
==================

Introduction
-------------
This section is a step-by-step instruction of the deposition and electronic structure analysis of a simple thin film morphology. For the setup of more involved use cases, refer to the sections in the User Guide.


Prerequesits
-------------
Follow the :ref:`getting_started_installation` section to setup Nanoscope. 


Simulation Setup
-----------------


1. Create an input molecule file

    1. Go to `MolView <https://www.nanomatch.de/nanomatch-files/molview/>`_ and design a molecule, e.g. a biphenyl molecule. 
    2. Use the ``clean`` and the ``2D to 3D`` buttons to generate a 3D structure of the molecule

        .. figure:: quick_start/quick_start_0.png
           :alt: Design a molecule with MolView
           :width: 100%
           :align: center
        
           Design a molecule with MolView

    3. Download the 3D molecule file with ``Tools -> MOL file``
    4. Convert the molecule to a valid mol2 input file for the MolPrep module via an xyz file
    
        .. code-block:: bash

           obabel MolView.mol -oxyz -OMyMol.xyz
           obabel MyMol.xyz -omol2 -OMyMol.mol2

    .. note:: We use biphenyl as a simple example as it allows for quick computation. It is not meant as a physical case study.

    .. note:: Feel free to try a different molecule. Keep in mind that the basic usage of Nanoscope covers molecules with up to 40 atoms.



2. Open SimStack Client on your local PC

    .. code-block:: bash

       micromamba activate simstack
       # and run simstack:
       simstack


3. Setup the basic Nanoscope workflow

    1. **Drag&Drop** the modules `MolPrep`, `Deposit` and `ESAnalysis` from the top left panel into the middle workflow panel into a linear workflow and arrange as depicted below. Double click on each module to adapt settings and allocate resources for each simulation step.
    
        .. figure:: quick_start/quick_start_1.png
           :alt: Construct the workflow with drag&drop
           :width: 100%
           :align: center
        
           Construct the standard Nanoscope workflow with drag&drop

    2. **MolPrep** settings

        .. figure:: quick_start/quick_start_molprep.png
           :alt: MolPrep settings
           :width: 60%
           :align: center
        



    3. **Desposit**

        In the ``Simulation Parameters`` panel of Deposit, adapt the settings as follows:

        .. figure:: quick_start/quick_start_deposit_box.png
           :alt: deposit_box_settings
           :width: 60%
           :align: center

        This will generate a sufficiently large sample for the electronic structure analysis. 

        Switch to the ``Molecules`` tab. Click on the rightmost buttons next to the input fields to load molecule and forcefield file from `MolPrep`:

            * `Molecule` input: `MolPPrep/outputs/molecule.pbd`
            * `Forcefield` input: `MolPPrep/outputs/molecule_forcefield.spf`

        .. figure:: quick_start/quick_start_Deposit_mols.png
           :alt: deposit_molecules_input
           :width: 100%
           :align: center




    4. **ESAnalysis**

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

        In the ``General`` tab of the ESAnalysis module, adapt the following:

            * `Morphology`: `Deposit3/outputs/structurePBC.cml` (again using the rightmost button)
            * `Core Shell/Number of molecules`: For a quick test, reduce this number, minimal value 2.
            * `Shell for Disorder and Couplings/Number of molecules`: For a quick test, reduce this number to 100, increase to 400 for significant statistics.

        In the ``Engines`` tab, set `Memory per CPU` to the total memory of your compute node divided by the number of processors.

    5. **Resources**
        
        Double click on each module and select the ``Resources`` tab to set computational resources for each module individually. 

        * **CPUs**: The following is recommended:

            =============================== =======================
            Module                          cpus_per_node
            =============================== =======================
            MolPrep                         32 or more
            Deposit                         32
            ESAnalysis                      64 or more
            =============================== =======================

            .. note :: You can run the workflow with fewer cores, if the above resources are not available. This increases runtime respectively.

        * **walltime**: Provide a walltime in seconds suitable for your resource. Typical runtimes with the above number of cpus are a couple of hours.
        * **memory**: Memory is provided in MB. For 32 cores, memory should be 64000 MB or higher. Large molecules may run into memory issues, if insufficiently memory is provided.

        Further information on resources is provided in the :ref:`user_guide_settings` section.


4. Save and submit the workflow

    1. Save the workflow with ``Ctrl+S`` or by clicking ``File -> Save`` or ``File -> Save As...``
    2. Connect to your resource using the `Connect` button in the top right of SimStack. Wait for the button to become green.
    3. Submit the workflow wiht ``Ctrl+R`` or by clicking ``Run -> Run``.
 

5. Monitor progress

    You can monitor the progress of your workflow with the `Jobs & Workflows` tab in the right panel of SimStack:

    1. Double click on `Workflows`
    2. Double click on the submitted workflow (identified by the timestamp, if multiple are listed) to expand the view and show the status of all modules. The color code for both the workflow icon and the modules is:
    
        * green: Finished successfully
        * yellow: Running
        * red: crashed
       
      Note that modules are only listed in this view once they have been started, i.e. when the predecessing module was finished successfully.

    3. Double click on each module to view and download output files.

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

The main output of the ESAnalysis module can be found in the module runtime folder in the subfolder `Analysis/DOS`. The following figure summarizes the main output, i.e. the density of states in the thin film morphology. The values in the figure are onsets of the distributions that compare to experimental values.

.. figure:: quick_start/quick_start_all_DOS_plot.png
   :alt: DOS of pristine film
   :width: 100%
   :align: center

   Density of States of a pristine morphology

Further outputs are:

.. table:: 
   :class: responsive-table

   ==================================== ========
   File                                 Content
   ==================================== ========
   DOS_Gaussian.png                     Plot visualizing the Gaussian-broadened DOS for HOMO and LUMO levels without vibrational effects.
   Vibrational_Gaussian_DOS_plot.png    Plot showing the Gaussian-broadened DOS including vibrational broadening.
   all_DOS_plot.png                     Combined plot overlaying DOS distributions with and without vibrational broadening (both are Gaussian-broadened).
   raw_data_homo_lumo.yaml              Exact HOMO and LUMO energies (in mixed morphologies for each molecule type). Includes mean, std, and all individual energy levels.
   homo_lumo_onsets.yaml                Calculated onset energies for HOMO and LUMO levels for each molecule type, can be compared with experimental onsets.
   homo_lumo_centers.yaml               Mean and standard deviation of the DOS distributions for HOMO and LUMO levels for each molecule type. Can be used as an ab-initio input for multi-scale simulation workflows.
   ==================================== ========
