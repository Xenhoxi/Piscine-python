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


def ft_mean(*args):
    print("ft_mean", sum(list(args)))


def ft_median(*args):
    print("ft_median", args)


def ft_quartile(*args):
    print("ft_quartile", args)


def ft_std(*args):
    print("ft_std", args)


def ft_var(*args):
    print("ft_var", args)
