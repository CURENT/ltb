.. ltb documentation master file, created by
   sphinx-quickstart on Tue Feb 28 09:37:51 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

LTB Documentation
===============================

**Useful Links**: `CURENT Website`_ | `CURENT YouTube Channel`_
| `Report Issues`_ | `Q&A`_

**Documentations**: `ANDES Doc`_ | `AMS Doc`_
| `AGVis Doc`_ | `DiME Doc`_

**Repositories**: `ANDES Repo`_ | `AMS Repo`_
| `AGVis Repo`_ | `DiME Repo`_ | `LTB Repo`_

.. _`CURENT Website`: https://ltb.curent.org/
.. _`CURENT YouTube Channel`: https://www.youtube.com/@curentltb
.. _`Report Issues`: https://github.com/CURENT/ltb/issues
.. _`Q&A`: https://github.com/CURENT/ltb/discussions
.. _`ANDES Doc`: https://docs.andes.app/en/latest/
.. _`AMS Doc`: https://ams.readthedocs.io/en/latest/
.. _`AGVis Doc`: https://agvis.readthedocs.io/en/latest/
.. _`DiME Doc`: https://ltbdime.readthedocs.io/en/latest/
.. _`LTB Repo`: https://github.com/CURENT/ltb
.. _`ANDES Repo`: https://github.com/CURENT/andes
.. _`AMS Repo`: https://github.com/CURENT/ams
.. _`AGVis Repo`: https://github.com/CURENT/agvis
.. _`DiME Repo`: https://github.com/CURENT/dime

.. image:: /images/sponsors/CURENT_Logo_NameOnTrans.png
   :alt: CURENT Logo
   :width: 300px
   :height: 74.2px

The CURENT Large-scale Testbed (LTB) is a state-of-the-art research facility designed
for rapid prototyping of power systems. It is a tightly integrated, closed-loop system
consisting of four major independent sub-packages: ANDES for dynamic simulation,
AMS (under development) for market simulation, DiME for distributed messaging environment,
and AGVis for grid visualization. These LTB packages can be used individually or in a federated
manner, making it a versatile tool for power system research and development.

.. panels::
    :card: + intro-card text-center
    :column: col-lg-6 col-md-6 col-sm-6 col-xs-12 d-flex

    ---

    Getting started
    ^^^^^^^^^^^^^^^

    New to CURENT LTB? Check out the getting started guides. They contain tutorials
    to the LTB co-simulations in Jupyter Notebook.

    +++

    .. link-button:: getting-started
            :type: ref
            :text: To the getting started guides
            :classes: btn-block btn-secondary stretched-link

    ---

    Demos
    ^^^^^^^^

    LTB has been used in many power system research to simulate complex power systems scenarios.
    These demos demonstrate the LTB's ability to rapidly and accurately model and simulate the behavior
    of modernized power systems.

    +++

    .. link-button:: demos
            :type: ref
            :text: To the demos
            :classes: btn-block btn-secondary stretched-link

    ---
    :column: col-12 p-3

    Using LTB for Research?
    ^^^^^^^^^^^^^^^^^^^^^^^^^
    Please cite our paper [Li2020]_ [Cui2021]_ [Parsly2022]_ if LTB is used in your research for
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

.. toctree::
   :caption: LTB documentation
   :maxdepth: 3
   :hidden:

   getting_started/index
   demos/index
   release-notes
   api
