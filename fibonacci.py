def fibonacci_seq(nth_term=10):
    fib_list = [0,1]
    
    # Get the nth term of the fibonacci sequence
    for k in range(nth_term-1):
        new_fib = fib_list[k] + fib_list[k+1]
        fib_list.append(new_fib)

    return fib_list[-1]
