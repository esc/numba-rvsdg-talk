import ast
import os
import sys

from numba_rvsdg.core.datastructures.ast_transforms import (
    AST2SCFGTransformer,
    SCFG2ASTTransformer,
    unparse_code,
)
from numba_rvsdg.rendering.rendering import SCFGRenderer

sys.path.append("./source")

names = ("function",
         "branch",
         "multi_return",
         "while_loop",
         "early_exit",
         "for_loop")


def exec_import(name):
    gl, lo = {}, {}
    exec(f"from {name} import {name}", gl, lo)
    return lo[name]


def process_example(name, func):
    print(f"Processing: '{name}'...")
    scfg = AST2SCFGTransformer(func).transform_to_SCFG()
    g = SCFGRenderer(scfg).g
    g.render(outfile=f"images/{name}-cfg.pdf")
    os.remove(f"images/{name}-cfg.gv")
    scfg.restructure()
    g = SCFGRenderer(scfg).g
    g.render(outfile=f"images/{name}-scfg.pdf")
    os.remove(f"images/{name}-scfg.gv")
    original_ast = unparse_code(func)[0]
    transformed_ast = SCFG2ASTTransformer().transform(
        original=original_ast, scfg=scfg)
    transformed_source = ast.unparse(transformed_ast)
    with open(f"transformed/{name}.py", "w") as f:
        f.write(transformed_source)
        f.write("\n")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        name = sys.argv[1]
        process_example(name, exec_import(name))
    else:
        for n in names:
            process_example(n, exec_import(n))
