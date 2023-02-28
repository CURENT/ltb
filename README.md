![alt text](images/logo/CURENT_Logo_FullOnWhite.png)

![alt text](images/logo/LTB.svg)

![alt text](images/logo/LTB_ANDES_horizontal.svg)
![alt text](images/logo/LTB_AMS_horizontal.svg)
![alt text](images/logo/LTB_AGVis_horizontal.svg)
![alt text](images/logo/LTB_DiME_horizontal.svg)

# CURENT Large-scale Testbed

The Large-scale Testbed (LTB) is a tightly integrated, closed-loop platform for rapid prototyping of power systems. **[ANDES](https://docs.andes.app/en/stable/index.html)**, **[AMS](https://github.com/jinningwang/ams)** (under development), **[DiME](https://ltbdime.readthedocs.io/en/latest/)**, and **[AGVis](https://agvis.readthedocs.io/en/latest/#what-is-agvis)** are four major independent sub packages of LTB that serve as a dynamic simulator, market simulator, distributed messaging environment, and grid visualizer, respectively. Towards a one-stop solution, these LTB packages can serve for both individual and federated use.

# Why LTB

LTB platform enables power system *dynamic simualiton*, *market simulation*, *geographical visualization*, *real-time simualtion*, and ***dispatch-dynamic co-simulaiton***.

*Getting trouble with dispatch in a dynamic simulation?* The interoperability of ANDES for scheduling supports secured dispatch in a dynamic simulation.

*Getting lost in the APIs of simulators?* Easy-to-use ANDES and AMS can be your last stop to prototype new algorithms and models.

*Looking for a geographical visualization?* AGVis allows geographical visualization with multiple options.

*Interested in a real-time closed-loop simulation?* LTB has integrated simulators and communication environments.

Video list:

- [Using ANDES for Damping Control Allocation using Wind Generation](https://www.youtube.com/watch?v=OtCFRHMtdo8)
- Using AMS for LMP-based cyber attack detection
- Using ANDES and AMS for **dispatch-dynamic co-simulaiton**
- [Webnair: Large-scale Testbed as a Virtual Power Grid](https://www.youtube.com/watch?v=QBt72ww-Xk4&t=2161s)

LTB is currently under active development. Welcome to join the [Discussion](https://github.com/CURENT/ltb2/discussions) of LTB.

# Citing LTB

If you use LTB packages for research or consulting, we kindly request you to cite the following papers in your publication that uses LTB

> F. Li, K. Tomsovic and H. Cui, "A Large-Scale Testbed as a Virtual Power Grid: For Closed-Loop Controls in Research and Testing," in IEEE Power and Energy Magazine, vol. 18, no. 2, pp. 60-68, March-April 2020, doi: 10.1109/MPE.2019.2959054.

> H. Cui, F. Li and K. Tomsovic, "Hybrid Symbolic-Numeric Framework for Power System Modeling and Analysis," in IEEE Transactions on Power Systems, vol. 36, no. 2, pp. 1373-1384, March 2021, doi: 10.1109/TPWRS.2020.3017019.

> Parsly, N., Wang, J., West, N., Zhang, Q., Cui, H., & Li, F. (2022). "DiME and AGVIS A Distributed Messaging Environment and Geographical Visualizer for Large-scale Power System Simulation". arXiv. https://doi.org/https://arxiv.org/abs/2211.11990v1

# Publications using LTB

## Journal

> H. Cui et al., "Disturbance Propagation in Power Grids With High Converter Penetration," in Proceedings of the IEEE, doi: 10.1109/JPROC.2022.3173813.

> W. Wang, X. Fang, H. Cui, F. Li, Y. Liu and T. J. Overbye, "Transmission-and-Distribution Dynamic Co-Simulation Framework for Distributed Energy Resource Frequency Response," in IEEE Transactions on Smart Grid, vol. 13, no. 1, pp. 482-495, Jan. 2022. doi: 10.1109/TSG.2021.3118292.

> Y. Zhang et al., "Encoding Frequency Constraints in Preventive Unit Commitment Using Deep Learning With Region-of-Interest Active Sampling," in IEEE Transactions on Power Systems, vol. 37, no. 3, pp. 1942-1955, May 2022. doi: 10.1109/TPWRS.2021.3110881.

> H. Cui, F. Li and X. Fang, "Effective Parallelism for Equation and Jacobian Evaluation in Large-Scale Power Flow Calculation," in IEEE Transactions on Power Systems, vol. 36, no. 5, pp. 4872-4875, Sept. 2021. doi: 10.1109/TPWRS.2021.3073591.

> C. Lackner, D. Osipov, H. Cui and J. H. Chow, "A Privacy-Preserving Distributed Wide-Area Automatic Generation Control Scheme," in IEEE Access, vol. 8, pp. 212699-212708, 2020. doi: 10.1109/ACCESS.2020.3040883

## Conference

> H. Cui and Y. Zhang, "Andes_gym: A Versatile Environment for Deep Reinforcement Learning in Power Systems," 2022 IEEE Power & Energy Society General Meeting (PESGM), Denver, CO, USA, 2022, pp. 01-05. doi: 10.1109/PESGM48719.2022.9916967.

> Y. Liu et al., "Transmission-Distribution Dynamic Co-simulation of Electric Vehicles Providing Grid Frequency Response," 2022 IEEE Power & Energy Society General Meeting (PESGM), Denver, CO, USA, 2022, pp. 1-5. doi: 10.1109/PESGM48719.2022.9917027.

> J. Wang, F. Li, H. Cui and Q. Zhang, "Impacts of VSG Control on Frequency Response in Power Systems with High-Penetration Renewables," 2021 IEEE 5th Conference on Energy Internet and Energy System Integration (EI2), Taiyuan, China, 2021, pp. 171-176. doi: 10.1109/EI252483.2021.9712880.

# Who is using LTB

![Natinoal Science Foundation](https://raw.githubusercontent.com/cuihantao/andes/master/docs/source/images/sponsors/nsf.jpg)
![US Department of Energy](https://raw.githubusercontent.com/cuihantao/andes/master/docs/source/images/sponsors/doe.png)
![CURENT ERC](https://raw.githubusercontent.com/cuihantao/andes/master/docs/source/images/sponsors/curent.jpg)
![Oklahoma State University](https://omni.okstate.edu/_resources_global/pattern-lab-v1/images/logo-vertical.svg)
<img src="https://engage.nrel.gov/static/images/nrel_logo_full.jpg" width=30% height=30%>
![Lawrence Livermore National Laboratory](https://raw.githubusercontent.com/cuihantao/andes/master/docs/source/images/sponsors/llnl.jpg)
![Idaho National Laboratory](https://raw.githubusercontent.com/cuihantao/andes/master/docs/source/images/sponsors/inl.jpg)

# Sponsors and developers

This work was supported in part by the Engineering Research Center Program of the National Science Foundation and the Department of Energy under NSF Award Number EEC-1041877 and the CURENT Industry Partnership Program.

ANDES is authored by [Hantao Cui](https://github.com/cuihantao), DiME and AGVis are developed and maintained by [Nicholas West](https://github.com/TheHashTableSlasher) and [Nicholas Parsly](https://github.com/nparsly).

AMS is under development, stay tuned!

# License

LTB is licensed under the [GPL v3 License](./LICENSE).
