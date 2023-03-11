.. ltb documentation master file, created by
   sphinx-quickstart on Tue Feb 28 09:37:51 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

LTB Documentation
===============================

**Useful Links**: `Source Repository`_ | `Report Issues`_
| `Q&A`_ | `Try in Jupyter Notebooks`_

.. _`Source Repository`: https://github.com/CURENT/ltb
.. _`Report Issues`: https://github.com/CURENT/ltb/issues
.. _`Q&A`: https://github.com/CURENT/ltb/discussions

The CURENT Large-scale Testbed (LTB) is a state-of-the-art research facility designed
for rapid prototyping of power systems. It is a tightly integrated, closed-loop system
consisting of four major independent sub-packages: ANDES for dynamic simulation,
AMS (under development) for market simulation,DiME for distributed messaging environment,
and AGVis for grid visualization. These LTB packages can be used individually or in a federated
manner, making it a versatile tool for power system research and development.

.. panels::
    :card: + intro-card text-center
    :column: col-lg-6 col-md-6 col-sm-6 col-xs-12 d-flex

    ---

    Getting started
    ^^^^^^^^^^^^^^^

    New to ANDES? Check out the getting started guides. They contain tutorials
    to the ANDES command-line interface, scripting usages, as well as guides to
    configure ANDES and work with case files.

    +++

    .. link-button:: getting-started
            :type: ref
            :text: To the getting started guides
            :classes: btn-block btn-secondary stretched-link

    ---

    Examples
    ^^^^^^^^

    The examples provide in-depth usage of ANDES in a Python scripting
    environment. Advanced usage and and power system studies are shown with
    explanation.

    +++

    .. link-button:: scripting_examples
            :type: ref
            :text: To the examples
            :classes: btn-block btn-secondary stretched-link

    ---

    Model development guide
    ^^^^^^^^^^^^^^^^^^^^^^^

    Looking to implement new models, algorithms and functionalities in ANDES?
    The development guide provides in-depth information on the design
    philosophy, data structure, and implementation of the hybrid
    symbolic-numeric framework.

    +++

    .. link-button:: development
            :type: ref
            :text: To the development guide
            :classes: btn-block btn-secondary stretched-link
    ---

    API reference
    ^^^^^^^^^^^^^

    The API reference contains a detailed description of the ANDES package. The
    reference describes how the methods work and which parameters can be used.
    It assumes that you have an understanding of the key concepts.

    +++

    .. link-button:: api_reference
            :type: ref
            :text: To the API reference
            :classes: btn-block btn-secondary stretched-link

    ---
    :column: col-12 p-3

    Using LTB for Research?
    ^^^^^^^^^^^^^^^^^^^^^^^^^
    Please cite our paper [Li2020]_[Cui2021]_[Cui2021]_ if LTB is used in your research for
    publication.

.. [Li2020] F. Li, K. Tomsovic and H. Cui, "A Large-Scale Testbed as a Virtual Power
      Grid: For Closed-Loop Controls in Research and Testing," in IEEE Power and
      Energy Magazine, vol. 18, no. 2, pp. 60-68, March-April 2020, doi:
      10.1109/MPE.2019.2959054.
.. [Cui2021] H. Cui, F. Li and K. Tomsovic, "Hybrid Symbolic-Numeric Framework
       for Power System Modeling and Analysis," in IEEE Transactions on Power
       Systems, vol. 36, no. 2, pp. 1373-1384, March 2021, doi:
       10.1109/TPWRS.2020.3017019.
.. [Parsly2022] N. Parsly, J. Wang, N. West, Q. Zhang, H. Cui and F. Li,
      "DiME and AGVIS: A Distributed Messaging Environment and Geographical Visualizer
      for Large-scale Power System Simulation," in arXiv, Nov. 2022, doi:
      arXiv.2211.11990.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

.. toctree::
   :caption: LTB Documentation
   :maxdepth: 3
   :hidden:

   getting_started/index
   demos/index
   release-notes
