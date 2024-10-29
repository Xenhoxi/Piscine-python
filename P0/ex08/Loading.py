def ft_tqdm(lst: range) -> None:
    for i in lst:
        pourcentage = int(i * 100 / len(lst) + 1)
        max_char = 53
        bar_lenght = int(max_char * (pourcentage / 100))
        str = ''
        for char in range(0, max_char):
            if char + 1 == bar_lenght:
                str += '>'
            elif char < bar_lenght:
                str += '='
            else:
                str += ' '
        yield print(f"{pourcentage}%|[{str}]| {i + 1}/333", end='\r')
