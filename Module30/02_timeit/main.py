import timeit


if __name__ == '__main__':
    res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(res)


    # TODO, пожалуйста, обратите внимание, первый параметр функции timeit должен быть текс.
    #  Как в первом и последнем вызове функции timeit.
    res_map: float = timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
    print(res_map)

    res_lc: float = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
    print(res_lc)
