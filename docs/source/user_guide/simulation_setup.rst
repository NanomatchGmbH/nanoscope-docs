.. _user_guide_simulation_setup:

Simulation Setup
================

Generate Input for Molecules
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

    `<your_input_format>` can be any format accepted by openbabel, such as `mol2`, `pdb`, `xyz`, or simply a smiles-code or InChI, with `<your_input_molecule>` being the filename of the input file or simply the string for smiles or InChI. Refer to the `Open Babel User Guide <http://openbabel.org/docs/index.html>`_ for reference.


    .. note:: Even if your original input is a mol2-file, we recommend to follow this 2-step procedure to make sure it is properly formatted.

    .. note:: If you generated an initial 3D-structure from smiles or InChI, double check that the initial conformation is reasonable, e. g. by visualization with `jmol <https://jmol.sourceforge.net/>`_.

Simulation of a pristine layer
-------------------------------


Simulation of a guest-host system
----------------------------------


Simulation of a multi-layer films and interfaces
--------------------------------------------------