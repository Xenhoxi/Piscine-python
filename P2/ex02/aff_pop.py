from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


def to_integers(x):
    """Transform abbreviated numerals to integers"""
    if x.endswith('k'):
        x = float(x[:-1]) * 1_000
    elif x.endswith('M'):
        x = float(x[:-1]) * 1_000_000
    elif x.endswith('B'):
        x = float(x[:-1]) * 1_000_000_000
    else:
        x = x
    return x


def main():
    try:
        data = load("../data_csv/population_total.csv")
        data.set_index('country', inplace=True)
        Yemen = data.loc['Yemen'][:-50]
        Yemen = Yemen.apply(to_integers).plot(label='Yemen')
        France = data.loc['France'][:-50]
        France = France.apply(to_integers).plot(label='France')
        Yemen.yaxis.set_major_formatter(EngFormatter())
        France.yaxis.set_major_formatter(EngFormatter())
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend()
        plt.show()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
