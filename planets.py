import pandas as pd
import matplotlib.pyplot as plt

# get data
df = pd.read_csv("planets.csv")
df["Planet"] = df["Planet"].str.strip().str.lower()  # lowercase for easier matching

# data options
options = {
    "1": "Mass",
    "2": "Diameter",
    "3": "Gravity",
    "4": "Mean Temperature (C)",
    "5": "Density",
    "6": "Number of Moons",
    "7": "Escape Velocity "
}


# ask user for wanted information
def show_menu():
    print("\nWhat data do you want to see?")
    for key, val in options.items():
        print(f"{key}. {val}")
    print("0. Exit")

# ask user which planets they want 
def get_planet_filter():
    print("\nEnter the planets you want (like: earth mars), or type 'all' to show everything.")
    choice = input("Your choice: ").strip().lower()

    if choice == "all":
        return df
    else:
        selected = [p.strip().lower() for p in choice.split()]
        filtered = df[df["Planet"].isin(selected)]
        if filtered.empty:
            print("No matching planets.Try again")
            return get_planet_filter()
        return filtered

# main loop
while True:
    show_menu()
    choice = input("Enter a number (0–7): ")

    if choice == "0":
        print("Done. Goodbye.")
        break

    if choice not in options:
        print("not a valid option.")
        continue

    feature = options[choice]
    selected_df = get_planet_filter()

    # capitalize planet names for display
    selected_df["Planet"] = selected_df["Planet"].str.title() 
    

    # show table
    print(f"\nShowing: {feature}\n")
    print(selected_df[["Planet", feature]].to_string(index=False))

    # Show bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(selected_df["Planet"], selected_df[feature], color="blue")
    plt.title(f"{feature} of Selected Planets")
    plt.ylabel(feature)
    plt.xlabel("Planet")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

