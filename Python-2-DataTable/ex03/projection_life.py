from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Create a scatter plot comparing ppp (Purchasing Power Parity)
    and life expectancy in the 1900.
    """
    try:
        ppp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_exp_data = load("life_expectancy_years.csv")
        if ppp is None or life_exp_data is None:
            return

        ppp = ppp.set_index('country')
        life_exp_data = life_exp_data.set_index('country')

        income_1900 = ppp['1900']
        life_exp_1900 = life_exp_data['1900']
        plt.scatter(income_1900, life_exp_1900)
        plt.title("1900")
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.show()

    except KeyboardInterrupt as error:
        print(f"{type(error)} : Interrupted.")
    except Exception as error:
        print(f"{type(error)} : {error}")


if __name__ == "__main__":
    main()

    # ppp = ppp.set_index('country')
    # Currently, the indexes are now the countries. This isn't done by default!
    # ppp.loc['France'] to retrieve only the line for France.
    # ppp.iloc[192] to retrieve only the line for 192.

    # to retrieve only the line for France AND the year 1900 :
    # ppp.loc['France', '1900']
