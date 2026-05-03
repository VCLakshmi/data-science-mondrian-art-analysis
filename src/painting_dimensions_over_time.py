import pandas as pd
import matplotlib.pyplot as plt


features = pd.read_csv("data/raw/mondrian-painting-features.csv")
print("\nMondrian Painting features: ")
print(features)

info = pd.read_csv("data/raw/mondrian-painting-info.csv")
print(info)

# compute area of each painting over the years
info["area"] = info["width"] * info["height"]
print("\nMondrian Painting info: ")
print(info)

# visualize how Mondrian painting area evolved over the years
plt.scatter(info["year"], info["area"])

plt.xlabel("year")
plt.xticks(range(min(info["year"]), max(info["year"])+1, 2))
plt.ylabel("area")
plt.title("Mondrian painting area over the years")
plt.savefig("outputs/figures/mondrian-painting-area-over-the-years.png")

plt.show()


# indentify the features where blue color is being used.
blue_feature_painting = features.query("color == 'blue'")

# Calculate the area of these blue features
blue_feature_painting["area"] = blue_feature_painting["width"] * blue_feature_painting["height"]

# Group the blue feature areas by `painting_id` and sum them.
blue_feature_painting = blue_feature_painting.groupby('painting_id')
blue_feature_painting = blue_feature_painting["area"].sum().reset_index(name="blue_area")

# Merge this data with `painting_info`
blue_area = info.merge(blue_feature_painting, how="left", on="painting_id")
blue_area["blue_area"] = blue_area["blue_area"].fillna(0)

# find percentage of blue area
blue_area["percentage_blue_area"] = (blue_area["blue_area"]/blue_area["area"]) * 100
print("\nMondorian painting ids where blue color is used and it's area: ")
print(blue_area)

# save under processed data
blue_area.to_csv("data/processed/percentage-of-blue-used-in-mondorian-painting.csv")

# Plot the percentage of blue in each painting over time.
plt.plot(blue_area["year"], blue_area["percentage_blue_area"], marker='o')

plt.xlabel("year")
plt.ylabel("percentage of blue area")
plt.title("Percentage of blue color per painting over the years")

plt.savefig("outputs/figures/blue_area_in_each_painting_over_years.png")
plt.show()
