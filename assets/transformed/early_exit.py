def transformed_early_exit(a: int) -> int:
    c = 0
    __scfg_loop_cont__ = True
    while __scfg_loop_cont__:
        if c < 10:
            c += 3
            if c > a:
                __scfg_exit_var_0__ = 1
                __scfg_backedge_var_0__ = 1
            else:
                __scfg_backedge_var_0__ = 0
                __scfg_exit_var_0__ = -1
        else:
            __scfg_exit_var_0__ = 0
            __scfg_backedge_var_0__ = 1
        __scfg_loop_cont__ = not __scfg_backedge_var_0__
    if __scfg_exit_var_0__ in (0,):
        __scfg_return_value__ = c
    else:
        __scfg_return_value__ = c + 1
    return __scfg_return_value__
