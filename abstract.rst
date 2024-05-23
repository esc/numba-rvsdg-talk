Regularizing Python using Structured Control Flow
=================================================

Abstract
--------

In this talk I will present original research and working code to regularize
Python programs using a Structured Control Flow Graph (SCFG). This is a novel
approach to rewriting Python programs at the source level such that the
resulting (regularized) program is potentially more amenable to LLVM compiler
optimizations when compiled to low-level machine code with Numba. Additionally,
this is a first step to representing Python programs as Regionalized Value
State Dependence Graphs (RVSDGs) which is expected to unlock even more advanced
compiler optimizations at the Intermediary Representation (IR) level. The talk
will cover an introduction to the theory  SCFGs and RVSDG and demonstrate how
programs can be transformed with hands-on examples.


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
extension to CFGs all blocks are part of special Regions within the SCFG. The
three possible region shapes are: linear, branch and loop. A linear region is
simply a linear sequence of instructions. A Branch region is a shape where the
control flow is split symmetrically and joined again. And lastly, a loop region
is a subgraph with a single backedge from the regions exiting latch. These
shapes effectively describe all possible control flow patterns in a program and
offer significantly more chances for a compiler to apply transformations and
optimizations.

The Python package being presented is capable of constructing a CFG from Python
source code input in the form of an Abstract Syntax Tree (AST). Furthermore the
package can then apply two algorithmic steps known as Loop Restructuring (LR)
and Branch Restructuring (BR) which convert the constructed CFG into an SCFG.
Lastly, the package is able to re-synthesize a regularized Python program from
the SCFG representation which is behaviourally equivalent to the original but
is potentially easier for a compiler to work with. Essentially the package
implements a type of regularization at the source code level where both input
and output are runnable Python programs.

Going beyond SCFGs, a novel Intermediary Representation called Regionalized
Value State Dependence Graphs (RVSDG) have been proposed []. Compared to CFGs
and SCFGs which are control-flow centric IRs, RVSDGs are data-flow centric IRs.
This means that a number of common compiler transforms can be performed when
the program has been converted to the RVSDGs representation w/o having to
reconstruct invariant properties post transformation. Also, this
representation unlocks a number of novel compiler transforms as data-flow
through the program is explicitly available. Transforms will be algorithmically
simpler, more elegant and computationally less expensive. Importantly the
construction of the SCFG representation for the input program correctly is a
necessary first step to constructing the full RVSDG and has significant merit
in it's own right.

This package available on PyPi as: https://pypi.org/project/numba-rvsdg/

References:

[]
