import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def draw_mondrian(features: pd.DataFrame, painting_id: str):
    rects = features.query('painting_id == @painting_id')
    total_width = rects.eval("x + width").max()
    total_height = rects.eval("y + height").max()
    
    fig, ax = plt.subplots(figsize=(3, 3))
    
    for (idx, row) in rects.iterrows():
        x, y, w, h, rgb = row[['x','y','width','height','rgb']]
        patch = mpatches.Rectangle((x, y), w, h, facecolor=rgb)
        ax.add_patch(patch)
    
    ax.axis([0, total_width, 0, total_height])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.text(0.5, 0.01, painting_id, ha="center", fontsize=14)
    fig.savefig(f"outputs/figures/{painting_id}-mondrian-painting.png")
    # close the figure
    plt.close(fig)


painting_features = pd.read_csv("data/raw/mondrian-painting-features.csv")
print("Mondrian Painting features in the year 1920 to 1940: ")
print(painting_features)


# Finding all features for the painting b104
painting_b104 = painting_features.query('painting_id == "b104"')
print("\nAll features for the painting b104: ")
print(painting_b104)


# Find the year in which the painting b104 was painted.
painting_year = pd.read_csv("data/raw/mondrian-painting-info.csv")
print("\nThe painting info for each Mondrian painting: ")
print(painting_year)

draw_mondrian(painting_features, "b104")
draw_mondrian(painting_features, "b294")
draw_mondrian(painting_features, "b234")


# count the number of features for the given painting id
sizes = painting_features.groupby("painting_id").size()
complexity_df = sizes.reset_index(name="complexity")
complexity_df.to_csv("outputs/mondrian-painting-features-complexity.csv", index=False)


# Show how complexity changes by year
new_df = painting_year.merge(complexity_df, how="left", on="painting_id")
print("\nData showing the complexity involved for each painting over the years: ")
print(new_df)

# save to file
new_df.to_csv("data/processed/mondrian-painting-info-with-features-complexity.csv", index=False)

plt.scatter(new_df["year"], new_df["complexity"])

plt.xlabel("Year")
plt.xticks(range(min(new_df["year"]), max(new_df["year"])+1, 2))
plt.ylabel("Complexity")

plt.title("Chart showing the complexity of images over the year")
plt.savefig("outputs/figures/complexity-over-years.png")
plt.show()
