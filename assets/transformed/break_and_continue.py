def transformed_break_and_continue(x: int, y: int) -> int:
    __scfg_iterator_1__ = iter(range(2))
    i = None
    __scfg_loop_cont__ = True
    while __scfg_loop_cont__:
        __scfg_iter_last_1__ = i
        i = next(__scfg_iterator_1__, '__scfg_sentinel__')
        if i != '__scfg_sentinel__':
            if i == x:
                __scfg_exit_var_0__ = 1
                __scfg_backedge_var_0__ = 1
            elif i == y:
                __scfg_exit_var_0__ = 2
                __scfg_backedge_var_0__ = 1
            else:
                __scfg_backedge_var_0__ = 0
                __scfg_exit_var_0__ = -1
        else:
            __scfg_exit_var_0__ = 0
            __scfg_backedge_var_0__ = 1
        __scfg_loop_cont__ = not __scfg_backedge_var_0__
    if __scfg_exit_var_0__ in (0,):
        i = __scfg_iter_last_1__
        __scfg_control_var_0__ = 0
    elif __scfg_exit_var_0__ in (1,):
        i = 3
        __scfg_return_value__ = i + 100
        __scfg_control_var_0__ = 1
    else:
        i = 4
        __scfg_control_var_0__ = 2
    if __scfg_control_var_0__ in (0, 2):
        __scfg_return_value__ = i
    else:
        pass
    return __scfg_return_value__
