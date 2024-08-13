import ast
import os
import sys

from numba_rvsdg.core.datastructures.ast_transforms import AST2SCFGTransformer, SCFG2ASTTransformer, unparse_code
from numba_rvsdg.rendering.rendering import SCFGRenderer

sys.path.append('./source')

from function import function

scfg = AST2SCFGTransformer(function).transform_to_SCFG()
g = SCFGRenderer(scfg).g
g.render(outfile='images/function-cfg.pdf')
os.remove('images/function-cfg.gv')

from branch import branch

scfg = AST2SCFGTransformer(branch).transform_to_SCFG()
g = SCFGRenderer(scfg).g
g.render(outfile='images/branch-cfg.pdf')
os.remove('images/branch-cfg.gv')
scfg.restructure()
g = SCFGRenderer(scfg).g
g.render(outfile='images/branch-scfg.pdf')
os.remove('images/branch-scfg.gv')

from multi_return import multi_return

scfg = AST2SCFGTransformer(multi_return).transform_to_SCFG()
g = SCFGRenderer(scfg).g
g.render(outfile='images/multi_return-cfg.pdf')
os.remove('images/multi_return-cfg.gv')
scfg.restructure()
g = SCFGRenderer(scfg).g
g.render(outfile='images/multi_return-scfg.pdf')
os.remove('images/multi_return-scfg.gv')
original_ast = unparse_code(multi_return)[0]
transformed_ast = SCFG2ASTTransformer().transform(original=original_ast, scfg=scfg)
transformed_source = ast.unparse(transformed_ast)
with open('transformed/multi_return.py', 'w') as f:
    f.write(transformed_source)
    f.write("\n")
