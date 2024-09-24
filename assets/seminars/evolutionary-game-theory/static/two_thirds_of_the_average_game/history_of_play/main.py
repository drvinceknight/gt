import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data.csv")


plt.figure()

two_thirds_mean_first_guess = 2 * df["Guess 1"].mean() / 3
two_thirds_mean_second_guess = 2 * df["Guess 2"].mean() / 3

plt.hist(
    df["Guess 1"], 
    bins=20, 
    alpha=.6, 
    label=f"Guess 1: $2/3\\bar x = {two_thirds_mean_first_guess:.02f}$", 
    color="blue",
)
plt.axvline(two_thirds_mean_first_guess, color="blue")

plt.hist(
    df["Guess 2"], 
    bins=20, 
    alpha=.3, 
    label=f"Guess 2: $2/3\\bar x = {two_thirds_mean_second_guess:.02f}$", 
    color="red",
)
plt.axvline(two_thirds_mean_second_guess, color="red")
plt.legend()

plt.title(f"Total guesses: {len(df.index)}")
plt.xlabel("Choices")
plt.ylabel("Frequency")

plt.savefig("main.pdf")
