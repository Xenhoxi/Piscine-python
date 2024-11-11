from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
import numpy as np


def main():
    try:
        income = load("../data_csv/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        population = load("../data_csv/life_expectancy_years.csv")
        if income is None or population is None:
            return
        income.set_index('country', inplace=True)
        population.set_index('country', inplace=True)
        pop_1900 = population.loc[:, '1900']
        life_1900 = income.loc[:, '1900']
        plt.scatter(life_1900, pop_1900)
        plt.title("1900")
        plt.xscale('log')
        plt.xlim(left=300)
        plt.xticks([300, 1000, 10000])
        plt.xlabel("Gross domestic product")
        plt.gca().xaxis.set_major_formatter(EngFormatter())
        plt.ylabel("Life expectancy")
        plt.show()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
