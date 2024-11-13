from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        data = load("../data_csv/life_expectancy_years.csv")
        if data is None:
            return
        data.set_index('country', inplace=True)
        data.loc['France'].plot()
        plt.title("France Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
