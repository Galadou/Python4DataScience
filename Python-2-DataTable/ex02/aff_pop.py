from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def transpose_txt_to_nb(value: str) -> float:
    """
    Transpose a string to a float.
    M = * 1 000 000.
    K = * 1 000.
    Args:
        value (str): The string you want to transpose.
    Returns:
        float: The value transposed to a float.
    """
    if isinstance(value, str):
        value = value.upper()
        if 'M' in value:
            return (float(value.replace('M', '')) * float(1000000))
        elif 'K' in value:
            return (float(value.replace('K', '')) * float(1000))
    return float(value)


def main():
    """
    Load population_total.csv, and create a plot with it,
    comparing 'France' and 'Belgium'.
    """
    try:
        data = load("population_total.csv")
        if data is None:
            return
        france_data = pd.DataFrame
        belgium_data = pd.DataFrame

        france_data = data.query("country == 'France'")
        fr_values = france_data.iloc[0, 1:252].apply(transpose_txt_to_nb)
        fr_years = france_data.columns[1:252]
        plt.plot(fr_years, fr_values, label="France", color="green")

        belgium_data = data.query("country == 'Belgium'")
        bg_values = belgium_data.iloc[0, 1:252].apply(transpose_txt_to_nb)
        bg_years = belgium_data.columns[1:252]
        plt.plot(bg_years, bg_values, label="Belgium", color="#2E80B9")

        plt.title("Population Projections")
        plt.xticks(fr_years[::40])
        plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend()
        plt.show()

    except KeyboardInterrupt as error:
        print(f"{type(error)} : Interrupted.")
    except Exception as error:
        print(f"{type(error)} : {error}")


if __name__ == "__main__":
    main()
