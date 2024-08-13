def transformed_while_loop() -> int:
    c = 0
    __scfg_loop_cont__ = True
    while __scfg_loop_cont__:
        if c < 10:
            c += 3
            __scfg_backedge_var_0__ = 0
        else:
            __scfg_backedge_var_0__ = 1
        __scfg_loop_cont__ = not __scfg_backedge_var_0__
    return c
