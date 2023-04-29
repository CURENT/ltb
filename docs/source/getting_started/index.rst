
.. raw:: html

   <embed>
   <h1 style="font-size: 3em; margin: 0;">
   CURENT LTB <span style="color: #00746F;"></span></h1>
   <p style="font-size: 1.2em; font-weight: bold; margin: 1em 0;">
   Center for Ultra-Wide-Area Resilient Electric Energy Transmission Networks
   Large-scale Testbed
   </embed>

.. _getting-started:

===============
Getting started
===============

.. toctree::
    :maxdepth: 3
    :hidden:

    overview
    install
    tutorial
    copyright

Quick install
=============

Before LTB comes to conda and pip, you can install it from source.

Step 1: Get LTB source code, with all submodules

.. code-block:: bash

    git clone https://github.com/CURENT/ltb.git --recursive

.. note::
    When you clone LTB from the Git repository with suffix ``--recursive``, the submodules
    are cloned as well.

    Replace the URL with yours to use your fork. With ``git``, you can later easily
    update the source code and perform version control.

Step 2: Install dependencies

In the Mambaforge environment, use ``cd`` to change directory to the LTB root folder.
The folder should contain the ``setup.py`` file.

Install dependencies with ``pip``:

.. code:: bash

    pip install -r requirements.txt
    pip install -r requirements-extra.txt

Step 4: Install LTB in the development mode using

.. code:: bash

      python3 -m pip install -e .

Note the dot at the end. Pip will take care of the rest.

.. note::
    The versions of each submodule that LTB uses are specified in the
    ``requirements.txt`` file. If you require a different version of a submodule,
    you can manually install a specified version using ``pip install``.

    Alternatively, if you want to use the latest version of each submodule,
    you can install it manually using
    ``pip install git+https://github.com/CURENT/andes.git@develop``
    or other package source.