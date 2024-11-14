def callLimit(limit: int):
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            # print(f"Count: {count}, Limite {limit}")
            if count < limit:
                count += 1
                return function()
            else:
                print(f"Error: {function}, call too many times")
                count += 1
        return limit_function
    return callLimiter
