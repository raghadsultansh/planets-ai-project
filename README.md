
#🌌 Solar System Planet Data Explorer

This Python script allows you to interactively explore and visualize various physical and orbital features of the planets in our solar system using a clean dataset and the pandas and matplotlib libraries.

##📁 Dataset Overview

The dataset includes scientific data on the 8 planets in the Solar System, with attributes such as:

- Planet Name
- Color Description
- Mass (10^24 kg)
- Diameter (km)
- Surface Gravity (m/s²)
- Escape Velocity (km/s)
- Mean Temperature (°C)
- Density (kg/m³)
- Number of Moons
- And more...

##🧪 Script Features

This script is interactive and provides:

- **Menu-based User Input**: Select which planet features you want to explore.
- **Flexible Planet Selection**: Choose one, many, or all planets.
- **Clean Data Table Output**: Shows selected values for each planet.
- **Bar Chart Visualization**: Displays comparison using simple visual charts.

##🗞 How to Run

1. Make sure the following files are in the same folder:
   - `planets.csv`
   - `planets.py`

2. Run the script using:

```bash
python planets.py
````

3. Follow the prompts in the terminal to:

* Pick a planetary feature (like mass or temperature)
* Choose which planets to show
* View the table and chart

🧠 Requirements

* Python 3.x
* pandas
* matplotlib

If not already installed, you can install the libraries using:

```bash
pip install pandas matplotlib
```

📊 Sample Output

```
What data do you want to see?
1. Mass
2. Diameter
3. Gravity
...

Enter a number (0–7): 3

Enter the planets you want (like: earth mars), or type 'all' to show everything.
Your choice: mars earth

Showing: Gravity

 Planet  Gravity
  Earth      9.8
   Mars      3.7
```

A bar chart will also be shown comparing the values across selected planets.


