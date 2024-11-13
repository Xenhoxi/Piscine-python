def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        print(function)

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count < limit:
                count += 1
                return function()
            else:
                print("Ohoh")
        return limit_function
    return callLimiter
