import pandas as pd
import matplotlib.pyplot as plt


fake_painting_df = pd.read_csv("data/raw/fp26-features.csv")
print("The Mondrian painting FP26 in the year 1926:")
print(fake_painting_df)


# Plot the fp26 painting with the original mondrian collection to detect if that falls under the mondrian collections
mondrian_painting_collections = pd.read_csv("data/processed/mondrian-painting-info-with-features-complexity.csv")
plt.scatter(mondrian_painting_collections["year"], mondrian_painting_collections["complexity"])
plt.scatter(x=1926, y=fake_painting_df.shape[0], marker="d")

plt.title("Mondrian Paintings analysis and comparison with fake paintings")
plt.xlabel("year")
plt.xticks(range(min(mondrian_painting_collections["year"]), max(mondrian_painting_collections["year"])+1, 2))
plt.ylabel("complexity")
plt.show()

plt.savefig("outputs/figures/mondrian-painting-analysis-with-fake-painting.png")
