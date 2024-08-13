def transformed_for_loop() -> int:
    c = 0
    __scfg_iterator_1__ = iter(range(10))
    i = None
    __scfg_loop_cont__ = True
    while __scfg_loop_cont__:
        __scfg_iter_last_1__ = i
        i = next(__scfg_iterator_1__, '__scfg_sentinel__')
        if i != '__scfg_sentinel__':
            c += i
            __scfg_backedge_var_0__ = 0
        else:
            __scfg_backedge_var_0__ = 1
        __scfg_loop_cont__ = not __scfg_backedge_var_0__
    i = __scfg_iter_last_1__
    return c
