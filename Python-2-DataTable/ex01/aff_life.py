from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """
    Load life_expectancy_years.csv, and create a plot with it, using 'France'.
    """
    try:
        data = load("life_expectancy_years.csv")
        if data is None:
            return
        france_data = pd.DataFrame
        france_data = data.query("country == 'France'")
        values = france_data.iloc[0, 1:]
        years = france_data.columns[1:]
        plt.plot(years, values)
        plt.title("France Life expectancy Projections")
        # xticks is used to change the legend of the x-axis.
        # start : stop : step
        plt.xticks(years[::40])
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()

    except KeyboardInterrupt as error:
        print(f"{type(error)} : Interrupted.")
    except Exception as error:
        print(f"{type(error)} : {error}")


if __name__ == "__main__":
    main()
