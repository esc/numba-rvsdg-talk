================
Numba-RVSDG Talk
================

Title: Regularizing Python using Structured Control Flow.

Abstract
========

In this talk we will present applied research and working code to regularize
Python programs using a Structured Control Flow Graph (SCFG). This is a novel
approach to rewriting programs at the source level such that the resulting
(regularized) program is potentially more amenable to compiler optimizations,
for example when using Numba[1] to compile Python.  The SCFG representation of
a program is simpler to analyze and thus significantly easier to optimize
because the higher order semantic information regarding the program structure
is explicitly included. This can be of great benefit to many scientific
applications such as High Performance Computing (HPC), a discipline that relies
heavily on compiler optimizations to turn user source code into highly
performant executables. Additionally the SCFG format is a first step to
representing Python programs as Regionalized Value State Dependence Graphs
(RVSDGs). This is another recently proposed program representation which is
expected to unlock even more advanced compiler optimizations at the
Intermediary Representation (IR) level. The talk will cover an introduction to
the theory of SCFGs and RVSDG and demonstrate how programs are transformed. We
will start with simple Python programs containing control-flow constructs and
then show both the SCFG representation and the resulting regularized result to
illustrate the transformations.

Description
===========

The Control Flow Graph (CFG) is a well known and established concept in
computer science and used as part of the compilation or interpretation step of
all modern programming languages. Unfortunately, CFGs are not always the ideal
representation for compilers to work with because they often result in
arbitrarily structured graphs (“spaghetti”). This in turn can lead to compiler
optimization steps not being leveraged and as a result a compiler may be unable
to generate an optimal low-level representation of the program. A recent
enhancement is the concept of the Structured Control Flow Graph (SCFG). In this
extension to CFGs all blocks are part of special regions within the SCFG. The
three possible region shapes are: linear, branch and loop. A linear region is
simply a linear sequence of instructions. A Branch region is a shape where the
control flow is split symmetrically and joined again. Finally, a loop region is
a subgraph with a single backedge from the region's exiting latch. These shapes
effectively describe all possible control flow patterns of a computer program
and resulting structure offers significantly more chances for a compiler to
apply transformations and optimizations, which in turn may lead to significant
performance improvements.

The Python package being presented is capable of constructing a CFG from Python
source code input in the form of an Abstract Syntax Tree (AST). Furthermore the
package can then apply two algorithmic steps known as Loop Restructuring (LR)
and Branch Restructuring (BR) (as described in [2]) which convert the
constructed CFG into an SCFG. Lastly, the package is able to synthesize a
regularized Python program from the SCFG representation which is behaviourally
equivalent to the original but is potentially easier for a compiler to work
with. Essentially the package implements a program transformation at the source
code level, where both input and output are runnable Python programs.

Going beyond SCFGs, a novel Intermediate Representation (IR), the
Regionalized Value State Dependence Graph (RVSDG), has been proposed [3].
Compared to CFGs and SCFGs, which are control-flow centric IRs, RVSDGs are
data-flow centric IRs.  This means that a number of common compiler transforms
can be performed when the program has been converted to the RVSDG
representation without having to reconstruct invariant properties post
transformation. Also, this representation unlocks a number of compiler
transforms, as data-flow through the program is explicitly available. Transforms
will be algorithmically simpler, more elegant and computationally less
expensive. Importantly, the construction of the SCFG representation for the
input program is a necessary first step to constructing the full
RVSDG and has significant merit in its own right.

Sources on GitHub as: https://github.com/numba/numba-rvsdg
Package on PyPi as: https://pypi.org/project/numba-rvsdg/

References:

[1] Siu Kwan Lam, Antoine Pitrou and Stanly Seibert. Numba: A LLVM-based Python
JIT Compiler. Proc. Second Workshop on the LLVM Compiler Infrastructure in HPC,
pp. 1-6, ACM. 2015

[2] Helge Bahmann, Nico Reissmann, Magnus Jahre, and Jan Christian Meyer.
Perfect reconstructability of control flow from demand dependence graphs. ACM
Transactions on Architecture and Code Optimization, 11(4):66:1–66:25, 2015.

[3] Nico Reissmann, Jan Christian Meyer, Helge Bahmann, and Magnus Själander.
RVSDG: An Intermediate Representation for Optimizing Compilers. Association for
Computing Machinery (ACM) 19(6):1-28, 2020 

Speaker-Bio
===========

Valentin 'esc' Haenel is a long-time "Python for Data" user and developer who
still remembers hearing Travis Oliphant's NumPy keynote at the EuroScipy 2008.
This was during a time where he first became aware of the nascent scientific
Python stack. He started using Python for simple modeling of spiking neurons
and evaluation of data from perception experiments during his Masters degree in
computational neuroscience.  Since then he has been active as a contributor
across more than 100 open source projects. For example, within the Blosc
ecosystem where he has contributed to Bcolz, Python-Blosc and Bloscpack.
Furthermore, he has acquired significant experience as a Git trainer and
consultant and had published the first German language book about the topic in
2011.  In 2014 and 2015 he helped kickstart the PyData Berlin community
alongside a few other volunteers and co-organized the first two editions of the
PyData Berlin Conference. Since 2019 he works for Anaconda as a senior software
engineer on the Numba project. His areas of contribution for the project so far
have been social architecture, release management, mutable datastructures and
recently, the compiler frontend.

Past Events
===========

* EuroScipy24

Dependencies
============

The talk is made with:

* `wiki2beamer <http://wiki2beamer.sourceforge.net/>`_ (included in repository)
* `LaTeX Beamer <https://bitbucket.org/rivanvx/beamer/wiki/Home>`_
* `Pygments <http://pygments.org/>`_
* `Minted <http://code.google.com/p/minted/>`_ (included in repository)
* `ccBeamer <http://blog.hartwork.org/?p=52>`_ (included in repository)

Licensing
=========

Content
-------

All Content is...

* Copyright 2024 Valentin Haenel <valentin@haenel.co>
* Licensed under the terms of `Attribution-ShareAlike 3.0 Unported  (CC BY-SA 3.0)  <http://creativecommons.org/licenses/by-sa/3.0/>`_

Included Dependencies
---------------------

The following dependencies are shipped with the sources:

* Wiki2beamer (file: ``wiki2beamer``) is licensed under Gnu Public Licence v2
* Minted (file: ``minted.sty``) is licensed under LaTeX Project Public License  version 1.3
* ccBeamer (directory: ``creative_commons/``) is licensed under Creative Commons Attribution-ShareAlike 3.0
