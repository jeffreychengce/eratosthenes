import time

def time_rng(fun, nrange, verbose=False):
    """
    Time a function over a range of parameters.

    Returns the list of run times.

    The function should be callable with a single argument: it will be
    called with each entry from nrange in turn.

    If verbose is true, at each step the value of nrange and time for the
    call is printed.
    """

    # BEGIN SOLUTION
    times = []
    for n in nrange:
        start = time.perf_counter()
        _ = fun(n)
        stop = time.perf_counter()
        timer = stop - start
        times.append(timer)
        if verbose:
            print('n: ', n, ', time: ', timer)

    # END SOLUTION
    return nrange, times

