.. _user_guide_simulation_setup:

Simulation Setup
================

Prerequesits
-------------
* **Nanoscope Installation**: Ensure that Nanoscope is installed on your system. If not, follow the  :ref:`getting_started_installation` to set it up.
* **Open Babel**: Install `Open Babel <http://openbabel.org/docs/index.html>`_ for molecule file conversion tasks.


Input for Molecules
------------------------------
1. Drawing Molecules From Scratch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    If you don't have any input for your molecule(s) yet, a good starting point are drawing tools such as MolView. In the following we use MolView as an example, but other tools work in a similar way.

    a. Open `MolView <https://www.nanomatch.de/nanomatch-files/molview/>`_  in your web browser.
    b. Design a molecule of your choice, e.g. a biphenyl molecule.
    c. Use the ``clean`` and the ``2D to 3D`` buttons to generate a 3D structure of the molecule.

        .. figure:: simulation_setup/quick_start_0.png
           :alt: Design a molecule with MolView
           :width: 100%
           :align: center
        
           Design a molecule with MolView

    d. In MolView, download the 3D molecule file with ``Tools -> MOL file`` and proceed with step 2 below.

2. Formatting existing input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Existing files as well as newly generated input files need to be converted into proper mol2 format to use it as input for Nanoscope. The safest way to do so is a 2-step conversion via xyz using openbabel:

        .. code-block:: bash

           obabel -i<your_input_format> -I<your_input_molecule> -oxyz -OMyMol.xyz
           obabel MyMol.xyz -omol2 -OMyMol.mol2

    `<your_input_format>` can be any format accepted by openbabel, such as `mol2`, `pdb`, `xyz`, or simply a smiles-code or InChI, with `<your_input_molecule>` being the filename of the input file or simply the string for smiles or InChI. Check the `Open Babel User Guide <http://openbabel.org/docs/index.html>`_ for reference.


    .. note:: Even if your original input is a mol2-file, we recommend to follow this 2-step procedure to make sure it is properly formatted.

    .. note:: If you generated an initial 3D-structure from smiles or InChI, double check that the initial conformation is reasonable, e. g. by visualization with `jmol <https://jmol.sourceforge.net/>`_.



Workflow setup and submission
--------------------------------

.. note:: If you are unfamiliar with the setup of workflows, the :ref:`getting_started_quick_start` may be a good starting point.

1. SimStack
^^^^^^^^^^^^

Open SimStack on your local PC using

    .. code-block:: bash

       micromamba activate simstack
       simstack

2. Design your workflow
^^^^^^^^^^^^^^^^^^^^^^^^
**Drag&Drop** the modules `MolPrep`, `Deposit` and `ESAnalysis` from the top left panel into the middle workflow panel into a linear workflow and arrange as depicted below. Double click on each module to adapt settings and allocate resources for each simulation step.

    .. figure:: simulation_setup/quick_start_1.png
       :alt: Construct the workflow with drag&drop
       :width: 100%
       :align: center

a. Simulation of a pristine layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To simulate a pristine layer we construct a linear worklfow in SimStack comprising `MolPrep`, `Deposit3` and `ESAnalysis`, as depicted in the above figure.

* **MolPrep**: 

    Load an input mol2-file from your hard drive using the button right next to the input field `Molecule (Mol2)`. 

* **Deposit**:

    1. Adjust settings in the `Simulation Parameters Tab` as described in :ref:`user_guide_settings`.
    2. Switch to the `Molecules` Tab. Use the rightmost buttons next to the `Molecule` and `Forcefield` input fields to load `MolPrep/outputs/molecule.pdb` and `MolPrep/outputs/molecule_forcefield.spf`, respectively.

* **ESAnalysis**:

    1. Use the rightmost button next to the `Morphology` input field to load `Deposit3/outputs/structurePBC.cml`.
    2. Depending on the required output, adjust the `Compute X` options in the General Settings panel
    3. Depending on the settings of 2., adapt `Core Shell` definition and `Shell for Disorder and Couplings`
    4. Switch to the Engines Tab and set `Memory per CPU (MB)`.

b. Simulation of a guest-host system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To simulate a guest-host systems, we need to combine two molecules in a single deposition:

1. Use a `Parallel` control from the `Controls panel` (bottom left) and click `Add additional parallel pane`.
2. Add one `MolPrep` module to each of the panes. 
3. Add `Deposit3` and `ESAnalysis` after the `Parallel` control.

Your workflow should look like this:

    .. figure:: simulation_setup/simulation_setup_guest_host.png
       :alt: Construct the workflow with drag&drop
       :width: 100%
       :align: center


* **MolPrep**: 
    
    Load the input (mol2) for the two molecules you would like to combine in the thin film into the two `MolPrep` modules.

* **Deposit**:

    1. Adjust settings in the `Simulation Parameters Tab` as described in :ref:`user_guide_settings`.
    2. Switch to the `Molecules` Tab. 
    
        a. Press the `+` button to add the input for a second molecule.
        b. First molecule: use the rightmost buttons next to the `Molecule` and `Forcefield` input fields to load `Parallel/0/MolPrep/outputs/molecule.pdb` and `Parallel/0/MolPrep/outputs/molecule_forcefield.spf`, respectively.
        c. Second molecule: use the rightmost buttons next to the `Molecule` and `Forcefield` input fields to load `Parallel/1/MolPrep/outputs/molecule.pdb` and `Parallel/1/MolPrep/outputs/molecule_forcefield.spf`, respectively. **Note the `1` in contrast to `0` in step b**.
        d. Adjust concentrations for your purpose.

* **ESAnalysis**:

    1. Use the rightmost button next to the `Morphology` input field to load `Deposit3/outputs/structurePBC.cml`.
    2. Depending on the required output, adjust the `Compute X` options in the General Settings panel
    3. Depending on the settings of 2., adapt the following: 

        `Core Shell`: 

            To compute absolute IP and EA in a mixed morphology for all species with sufficient accuracy, we recommend to set

            * `Shell size defined by`: `Number of Molecules of each Type`
            * `Number of molecules`: >= 2


            Alternatively, if you are interested in the IP or EA of a few specific guest molecules in a host matrix, you can provide the list of molecule IDs. Note that for this purpose, you need to design the workflow up to Deposit, identify the respecitve IDs in the resulting `structurePBC.cml` and subsequently run ESAnalysis in a separate workflow with `structurePBC.cml` loaded from the hard drive.

        `Shell for Disorder and Couplings`: 

            Accuracy of computed disorder depends heavily on the sample size. Keep in mind that for low concentrations, a large total number of molecules may be required in the disorder shell.

    4. Switch to the Engines Tab and set `Memory per CPU (MB)`.



c. Simulation of a multi-layer films and interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For an interface, we use the `Parallel` control to compute input for all molecules, but use multiple Deposit modules in sequence to deposit materials layer by layer:

1. Use a `Parallel` control from the `Controls panel` (bottom left) and click `Add additional parallel pane`. Add as many materials as you need in your multi-layer stack.
2. Add one `MolPrep` module to each of the panes. 
3. Add multiple `Deposit3` modules after the `Parallel` control in linear sequence.
4. Add `ESAnalysis` after the last `Deposit3` module.

Your workflow should look like this:

    .. figure:: simulation_setup/simulation_setup_interface.png
       :alt: Construct the workflow with drag&drop
       :width: 100%
       :align: center

* **MolPrep**: 

    Load the input (mol2) for the two molecules you would like to combine in the thin film into the two `MolPrep` modules.

* **Deposit modules**:

    1. Adjust settings in the `Simulation Parameters Tab` as described in :ref:`user_guide_settings`.

        .. note:: All Deposit modules must have the same box settings!

    2. Switch to the `Molecules` Tab. Use the rightmost buttons next to the `Molecule` and `Forcefield` input fields to load `Parallel/X/MolPrep/outputs/molecule.pdb` and `Parallel/X/MolPrep/outputs/molecule_forcefield.spf`, respectively. Adjust `X` depending on which material you would like to have in your layer.
    3. For all Deposit modules **except the first**: 
    
        a. Enable `Restart from existing morphology`.
        b. Use the button rightmost of the `Restartfile` input field to load the restartfile from the preceeding Deposit module, e. g. `Deposit3/outputs/restartfile.zip`. See the above figure for reference.

* **ESAnalysis**:

    1. Use the rightmost button next to the `Morphology` input field to load `Deposit3_1/outputs/structurePBC.cml`. If you have more than two layers, substitute `Deposit3_1` with the last Deposit3 module in line.
    2. Depending on the required output, adjust the `Compute X` options in the General Settings panel
    3. Depending on the settings of 2., adapt the following: 

        `Core Shell`: 

            To compute absolute IP and EA in a mixed morphology for all species with sufficient accuracy, we recommend to set

            * `Shell size defined by`: `Number of Molecules of each Type`
            * `Number of molecules`: >= 2


            Alternatively, if you are interested in the IP or EA of a few specific molecules, e.g. near an interface, you can provide the list of molecule IDs. Note that for this purpose, you need to design the workflow up to Deposit, identify the respecitve IDs in the resulting `structurePBC.cml` and subsequently run ESAnalysis in a separate workflow with `structurePBC.cml` loaded from the hard drive.

        `Shell for Disorder and Couplings`: 

            The disorder shell is defined as N molecules closest to the center of the morphology. Depending on your layer setup, not all species may be well represented. We recommend to compute disorder in separate morphologies layer by layer.

    4. Switch to the Engines Tab and set `Memory per CPU (MB)`


3. Save and submit the workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    1. Save the workflow with ``Ctrl+S`` or by clicking ``File -> Save`` or ``File -> Save As...``
    2. Connect to your resource using the `Connect` button in the top right of SimStack. Wait for the button to become green.
    3. Submit the workflow wiht ``Ctrl+R`` or by clicking ``Run -> Run``.


Monitor progress and view results
------------------------------------

    You can monitor the progress of your workflow with the ``Jobs & Workflows`` tab in the right panel of SimStack:

    1. Navigate to the ``Jobs & Workflows`` tab on the right panel.

    2. Expand **Workflows** (double click) and locate your submitted workflow (identified by timestamp if necessary).

    3. Monitor the status of the workflow and the contained modules:

       - **Green**: Completed successfully
       - **Yellow**: Currently running
       - **Red**: Encountered an error

    4. Double-click on a module to view logs, output files, and detailed status.

    .. note :: Modules are only listed in this view once they have been started, i.e. when the predecessing module was finished successfully.

    .. figure:: simulation_setup/quick_start_monitor.png
       :alt: progress_monitoring
       :width: 60%
       :align: center

    Once modules have completed successfully, you can download and view results by double-clicking on the modules and then the respective files in the ``Jobs & Workflows`` tab. Refer to :ref:`user_guide_computed_properties` for reference.

