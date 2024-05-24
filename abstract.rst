Regularizing Python using Structured Control Flow
=================================================

Abstract
--------

In this talk I will present original research and working code to regularize
Python programs using a Structured Control Flow Graph (SCFG). This is a novel
approach to rewriting programs at the source level such that the resulting
(regularized) program is potentially more amenable to compiler optimizations
when compiled to low-level machine code, for example when using Numba[1] to
compile Python.  Effectively the SCFG representation of a program is simpler to
analyze and thus significantly easier to optimize because it is more detailed
as the higher order semantic information regarding the program structure is
explicitly included. This can be of great benefit to many scientific
applications such as High Performance Computing (HPC) Additionally the SCFG
format is a first step to representing Python programs as Regionalized Value
State Dependence Graphs (RVSDGs). The is another novel program representation
which is expected to unlock even more advanced compiler optimizations at the
Intermediary Representation (IR) level. The talk will cover an introduction to
the theory of SCFGs and RVSDG and demonstrate how programs are transformed with
hands-on Python examples.


Description
-----------

The Control Flow Graph (CFG) is a well known and established concept in
computer science and used as part of the compilation or interpretation step of
all modern programming languages. Unfortunately, CFGs are not always the ideal
representation for compilers to work with because they often result in -- for
lack of a better term -- "spaghetti". This in turn, leads to compiler
optimization steps not being leveraged and as a result a compiler may be unable
to generate an optimal low-level representation of the program. A recent
enhancement is the concept of the Structured Control Flow Graph (SCFG). In this
extension to CFGs all blocks are part of special regions within the SCFG. The
three possible region shapes are: linear, branch and loop. A linear region is
simply a linear sequence of instructions. A Branch region is a shape where the
control flow is split symmetrically and joined again. And lastly, a loop region
is a subgraph with a single backedge from the regions exiting latch. These
shapes effectively describe all possible control flow patterns of a computer
program and the existing structure offers significantly more chances for a
compiler to apply transformations and optimizations, which in turn may lead to
significant performance improvements.

The Python package being presented is capable of constructing a CFG from Python
source code input in the form of an Abstract Syntax Tree (AST). Furthermore the
package can then apply two algorithmic steps known as Loop Restructuring (LR)
and Branch Restructuring (BR) (as described in [2]) which convert the
constructed CFG into an SCFG. Lastly, the package is able to re-synthesize a
regularized Python program from the SCFG representation which is behaviourally
equivalent to the original but is potentially easier for a compiler to work
with. Essentially the package implements a type of regularization at the source
code level where both input and output are runnable Python programs.

Going beyond SCFGs, a novel Intermediary Representation (IR) called
Regionalized Value State Dependence Graphs (RVSDG) have been proposed [3].
Compared to CFGs and SCFGs which are control-flow centric IRs, RVSDGs are
data-flow centric IRs.  This means that a number of common compiler transforms
can be performed when the program has been converted to the RVSDGs
representation without having to reconstruct invariant properties post
transformation. Also, this representation unlocks a number of novel compiler
transforms as data-flow through the program is explicitly available. Transforms
will be algorithmically simpler, more elegant and computationally less
expensive. Importantly, the construction of the SCFG representation for the
input program correctly is a necessary first step to constructing the full
RVSDG and has significant merit in it's own right.

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
