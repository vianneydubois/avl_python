# AVL-Python
An interface between AVL and Python

My initial objective is to run multiple AVL calculations to optimize flight control surfaces (FCS) dimensions. For that, I need to control AVL with Python.

I use the `subprocess` module to run AVL, and `openmdao` tools to generate and read the input geometry file and the stability output file.
