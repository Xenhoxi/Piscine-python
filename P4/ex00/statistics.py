def ft_statistics(*args: any, **kwargs: any) -> None:
    func_list = [ft_mean, ft_median, ft_quartile, ft_std, ft_var]
    word_list = ["mean", "median", "quartile", "std", "var"]
    for kwarg in kwargs.values():
        for i in range(len(word_list)):
            if kwarg == word_list[i]:
                if len(args) > 0:
                    func_list[i](args)
                else:
                    print("ERROR")


def ft_mean(args):
    print("ft_mean", sum(args) / len(args))


def ft_median(args):
    nbs = list(args)
    nbs.sort()
    if len(args) % 2 == 0 and len(args) > 2:
        mid = round(len(args) / 2)
        med = (nbs[mid] + nbs[mid - 1]) / 2
    else:
        med = nbs[round(len(nbs) / 2)]
    print("ft_median", med)


def ft_quartile(args):
    nbs = list(args)
    nbs.sort()
    i1 = round((len(nbs) + 3) / 4)
    Q1 = nbs[i1 - 1]
    i3 = round((3 * len(nbs) + 1) / 4)
    Q3 = nbs[i3 - 1]
    print("ft_quartile", [Q1 / 1, Q3 / 1])


def ft_std(args):
    print(args)


def ft_var(args):
    mean = sum(args) / len(args)
    res = 0
    for i in args:
        res += (mean - i) ** 2
    print("var :", res / (len(args)))
