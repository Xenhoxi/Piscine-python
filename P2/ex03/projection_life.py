from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        data = load("../data_csv/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        data = load("../data_csv/population_total.csv")
        data.set_index('country', inplace=True)
        population_1900 = data.loc[:, '1900']
        print(population_1900)
        # plt.title("Population Projections")
        # plt.xlabel("Year")
        # plt.ylabel("Population")
        # plt.legend()
        plt.show()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()