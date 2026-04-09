import seaborn as sns
import pandas as pd

sns.set_theme(style="whitegrid", context="talk")


def load_exercise_data(path="Exercise_Data.csv"):
    df = pd.read_csv(path)
    return df


def prepare_exercise_data(df):
    df_long = df.melt(
        id_vars=["id", "diet", "kind"],
        value_vars=["1 min", "15 min", "30 min"],
        var_name="time",
        value_name="pulse",
    )
    return df_long


def exercise_heatmap(df_long):
    heatmap_data = (
        df_long.groupby(["diet", "kind", "time"])["pulse"]
        .mean()
        .unstack("time")
    )
    heatmap_data.index = heatmap_data.index.map(lambda x: f"{x[0]} / {x[1]}")

    ax = sns.heatmap(
        heatmap_data,
        annot=True,
        fmt=".1f",
        cmap="coolwarm",
        cbar_kws={"label": "Average Pulse (BPM)"},
        linewidths=0.5,
        linecolor="white",
    )
    ax.set_title("Average Pulse by Diet, Exercise, and Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Diet / Exercise")
    return ax


def exercise_categorical_plots(df_long):
    cat_diet = sns.catplot(
        data=df_long,
        x="diet",
        y="pulse",
        kind="box",
        palette="Set2",
        height=6,
        aspect=1.2,
    )
    cat_diet.fig.suptitle("Pulse Distribution by Diet")
    cat_diet.set_axis_labels("Diet", "Pulse (BPM)")
    cat_diet.fig.tight_layout()

    cat_exercise = sns.catplot(
        data=df_long,
        x="kind",
        y="pulse",
        kind="box",
        palette="Set3",
        height=6,
        aspect=1.3,
    )
    cat_exercise.fig.suptitle("Pulse Distribution by Exercise Type")
    cat_exercise.set_axis_labels("Exercise Type", "Pulse (BPM)")
    cat_exercise.fig.tight_layout()

    return cat_diet, cat_exercise


def planets_plots():
    planets = sns.load_dataset("planets").dropna(subset=["mass", "distance", "orbital_period", "method", "year"])

    rel1 = sns.relplot(
        data=planets,
        x="distance",
        y="mass",
        hue="method",
        size="orbital_period",
        sizes=(30, 200),
        alpha=0.7,
        palette="tab10",
        height=6,
        aspect=1.3,
    )
    rel1.fig.suptitle("Planet Mass vs Distance by Discovery Method")
    rel1.set_axis_labels("Distance (AU)", "Mass (Jupiter masses)")
    rel1.fig.tight_layout()

    discovery_by_year = (
        planets.groupby("year")["distance"].mean().reset_index()
    )
    rel2 = sns.relplot(
        data=discovery_by_year,
        x="year",
        y="distance",
        kind="line",
        marker="o",
        height=5,
        aspect=1.6,
    )
    rel2.fig.suptitle("Average Discovery Distance by Year")
    rel2.set_axis_labels("Discovery Year", "Average Distance (AU)")
    rel2.fig.tight_layout()

    dist1 = sns.displot(
        data=planets,
        x="mass",
        hue="method",
        kind="hist",
        element="step",
        stat="density",
        common_norm=False,
        alpha=0.5,
        height=6,
        aspect=1.4,
    )
    dist1.fig.suptitle("Mass Distribution of Discovered Exoplanets by Method")
    dist1.set_axis_labels("Mass (Jupiter masses)", "Density")
    dist1.fig.tight_layout()

    dist2 = sns.displot(
        data=planets,
        x="orbital_period",
        kind="kde",
        fill=True,
        height=6,
        aspect=1.4,
        bw_adjust=0.8,
    )
    dist2.fig.suptitle("Orbital Period Density for Exoplanets")
    dist2.set_axis_labels("Orbital Period (days)", "Density")
    dist2.fig.tight_layout()

    cat1 = sns.catplot(
        data=planets,
        x="method",
        y="mass",
        kind="box",
        palette="pastel",
        height=6,
        aspect=1.8,
    )
    cat1.fig.suptitle("Planet Mass by Discovery Method")
    cat1.set_axis_labels("Discovery Method", "Mass (Jupiter masses)")
    cat1.fig.tight_layout()

    planets_count = planets["method"].value_counts().reset_index()
    planets_count.columns = ["method", "count"]
    cat2 = sns.catplot(
        data=planets_count,
        x="count",
        y="method",
        kind="bar",
        palette="muted",
        height=6,
        aspect=1.2,
    )
    cat2.fig.suptitle("Number of Exoplanet Discoveries by Method")
    cat2.set_axis_labels("Discovery Count", "Method")
    cat2.fig.tight_layout()

    return rel1, rel2, dist1, dist2, cat1, cat2


def main():
    exercise_df = load_exercise_data()
    exercise_long = prepare_exercise_data(exercise_df)

    print("Exercise Data Summary:")
    print("- The heatmap shows how average pulse values change across 1 min, 15 min, and 30 min for each diet and exercise combination.")
    print("- The boxplots compare pulse distributions by diet and by exercise type.")
    print("- Overall, no-fat diet participants tend to start with slightly higher pulses, and running consistently produces the highest pulse values.")

    exercise_heatmap(exercise_long)
    exercise_categorical_plots(exercise_long)

    print("\nPlanets Data Summary:")
    print("- The relational plots show how planet mass relates to distance and how average discovery distance evolves by year.")
    print("- The distribution plots show mass density by detection method and the orbital period density shape.")
    print("- The categorical plots show the wide mass ranges found by different discovery methods and which methods contributed the most discoveries.")
    print(
        "\nBest planetary visualization: the mass vs distance scatter plot really shows that more massive planets are often found farther out or by different methods, "
        "while the bar chart clearly highlights which discovery methods are most common."
    )

    planets_plots()


if __name__ == "__main__":
    main()
