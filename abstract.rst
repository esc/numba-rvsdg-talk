Regularizing Python using Structured Control Flow
=================================================

Abstract
--------

The Control Flow Graph (CFG) is a well known and established concept in
computer science and used as part of the compilation or interpretation step of
all modern programming languages. Unfortunately, CFGs are not always the ideal
represention for compilers to work with because they often result in -- for
lack of a better term -- "spaghetti". This in turn, leads to compiler
optimization steps not being leveraged and as a result a compiler may be unable
to generate an optimal low-level representation of the program. A recent
enhancement is the concept of the Structured Control Flow Graph (SCFG). In this
extension to CFGs all blocks are part of special Regions within the SCFG. The
three possible region shapes are: linear, branch and loop. A linear region is
simply a linear sequence of instructions. A Branch region is a shape where the
control flow is split symetrically and joined again. And lastly, a loop region
is a subgraph with a single backedge from the regions exiting latch. These
shapes effectively describe all possible control flow patterns in a program and
offer significantly more chances for a compiler to apply transformations and
optimizations.

In this talk I will present original research and working code in the form of a
Python package that implements a conversion of Python source code (in the form
of an Abstract Syntax Tree (AST)) to a CFG and the transforms required to
derive an SCFG. In addition the package also implements re-synthesisis of
regularized Python source code which can then be handed over to a Python
compilers such as Numba to produce optimized machine code.

This package available on PyPi as: https://pypi.org/project/numba-rvsdg/

Description
-----------
