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

Client / local PC
^^^^^^^^^^^^^^^^^
There are no special requirements for the local resource where the SimStack Client and the WaNos are installed. The SimStack Client is available for Linux, Windows and MacOS.



Installation step-by-step
----------------------------
On the computational resource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Install micromamba
    ::

        "${SHELL}" <(curl -L micro.mamba.pm/install.sh)

    For details or special installation requirements, refer to the `Micromamba documentation page <https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html>`_.

2. Install the Nanoscope software
    1. Clone the `nanomatch-release Github respository <https://github.com/NanomatchGmbH/nanomatch-release.git>`_
    ::

        git clone git@github.com:NanomatchGmbH/nanomatch-release.git
    2. Go into the repository and list all available releases:
    :: 

        cd nanomatch-release
        ./install_environment_helper.sh
    3. Copy and paste one of the printed commands to install the Nanoscope software. Use the **second topmost** command to get the latest version, e.g. 
    ::

        micromamba create --name=nmsci-2024.2 -f /home/tobias/Software/nanomatch/nanomatch-release/releases/nmsci-2024.2.2.conda-lock.yml

    .. note::

        To update the Nanoscope software, pull the repository 

        ::

            git pull

        and execute steps 2.2, and subsequently 2.3 with a new version, as indicated in the printed commands.

3. Install the SimStack **Server**
    In the list of available installs from step 2.2 above, execute the **topmost** command to install SimStack Server:

    ::

        micromamba create --name=simstack_server_v6 -f /home/tobias/Software/nanomatch/nanomatch-release/releases/simstackserver.conda-lock.yml

Details on steps 2 and 3 are provided in the `README <https://github.com/NanomatchGmbH/nanomatch-release/blob/main/README.md>`_ of the repository.

On the client / local PC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Install micromamba
    On Linux distributions: see above

    On MacOS, use the same command as for Linux (above) or use Homebrew:
    :: 

        brew install micromamba

    On Windows via powershell:
    ::

        Invoke-Expression ((Invoke-WebRequest -Uri https://micro.mamba.pm/install.ps1).Content)

    For details or special installation requirements, refer to the `Micromamba documentation page <https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html>`_.
2. Install and run the SimStack **Client**
    Installation:
    ::

        # Create a new environment for the simstack client:
        micromamba create --name=simstack simstack -c https://mamba.nanomatch-distribution.de/mamba-repo -c conda-forge

    Run the SimStack Client:
    ::

        # Activate the environment
        micromamba activate simstack
        # and run simstack:
        simstack

    Update the SimStack Client:
    ::
        
        micromamba activate simstack
        micromamba update simstack -c https://mamba.nanomatch-distribution.de/mamba-repo -c conda-forge
        # Or if you need a specific version, example 1.2.5:
        micromamba install simstack=1.2.5 -c https://mamba.nanomatch-distribution.de/mamba-repo -c conda-forge

.. TODO: Double check if this holdes for Mac and Windows

3. Download the WaNos 
    WaNos are available in a `public repository <https://github.com/NanomatchGmbH/wano.git>`_. To get the WaNos, go into a directory of your choice and run
    ::

        git clone git@github.com:NanomatchGmbH/wano.git

    Make sure to remember the directory for the SimStack configuration below.

SimStack configuration
-------------------------

.. note::

    In the following we provide a brief summary of the key steps to configure SimStack. Detailed information on SimStack, including all options for setup, are available on the `SimStack documentation page <https://simstack.readthedocs.io/>`_.


Setup of passwordless ssh
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Communication between the SimStack Client and the SimStack Server requires passwordless ssh access from your local PC to your computational resource. *On your local PC*, generate a ``ssh`` keypair and transfer the key to the ``authorized_keys`` file of your user account on the computational resource with one of the following commands:

On Linux and OSX (Arm and x64)
""""""""""""""""""""""""""""""""""""

If you don't have the ``ssh`` keys, use the steps below to generate them.

   * ``ssh`` key generation, press enter for the passphrase option.

      .. code-block:: bash

         ssh-keygen -t rsa

   * The ssh-key command generated two keys in the ``~/.ssh`` directory.
     Now, you must copy the key to your user account in one of the available HPC resources.

      .. code-block:: bash

        id_rsa
        id_rsa.pub

   * Please choose the HPC where you want to have passwordless access.

      .. code-block:: bash
         
         ssh-copy-id <username>@<computer name or IP address>

   * Test the connectivity of your passwordless ``ssh``  by running one of the commands below in the **Powershell** prompt.

      .. code-block:: bash
        
         ssh <username>@<computer name or IP address>

   * After completing the above steps, run the below commands.

      .. code-block:: bash

         cd  simstack_linux
         ./run_simstack.sh


On Windows
""""""""""""""""""""""""""""

You have two options on Windows: You can install either the native Windows version or (in an updated WSL2 environment) the Linux version.
WSL2 comes with all client tools required, so this is the recommended approach. If you want to use the Windows version, continue this tutorial.

If you don't have the ``ssh`` keys, use the steps below to generate them.

   * Ensure the `ssh` is enabled on your Windows system.

   * Check if **Powershell** is installed on your Windows system. If not, you can install it from the Microsoft Store.

   * To generate a public/private ``rsa key pair`` on Windows, open the **Powershell** prompt run the
     below command, and press enter for the passphrase option.

     .. code-block:: bash

         ssh-keygen

   * To copy the ``ssh`` key to your user account on the HPC resource, choose and run
     one of the commands below in the **Powershell** prompt. :green:`Literally copy the command changing only the` **user**.

      .. code:: bash

         type $env:USERPROFILE\.ssh\id_rsa.pub | ssh <username>@<computer name or IP address> "cat >> .ssh/authorized_keys"


   * After completing the above steps, double-click on ``run-simstack`` and be happy.

Test the connectivity
""""""""""""""""""""""""""

You can test the connectivity of your passwordless ``ssh`` in both systems by running one of the
commands below. You successfully transferred the key if you establish the ``ssh`` connectivity to
your HPC without entering your user password.

   .. code-block:: bash

        ssh <username>@<computer name or IP address>



Configuration of the SimStack Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

