
# 🌌 Solar System Planet Data Explorer

This Python project lets you explore and compare key physical and orbital properties of the planets in our Solar System. It’s a simple, interactive script that uses a clean dataset along with `pandas` and `matplotlib` to display information in both table and chart form. It’s great for anyone curious about planetary science or just looking to practice data handling and visualization in Python.

---

## 📁 Dataset Overview

The dataset includes scientific data on the 8 main planets, with fields like:

- Planet Name  
- Color Description  
- Mass (10²⁴ kg)  
- Diameter (km)  
- Gravity (m/s²)  
- Escape Velocity (km/s)  
- Mean Temperature (°C)  
- Density (kg/m³)  
- Number of Moons  
- Orbital Period and more  

The data has been cleaned and formatted to work with the script.

---

## 🧪 What the Script Does

This script allows you to:

- Select a planetary feature (e.g. mass, gravity, temperature)
- Choose one, multiple, or all planets for comparison
- View a neat, pandas-based table of the results
- Automatically generate a bar chart to visualize differences

The interaction is entirely menu-driven, so you don’t need to modify any code — just run the script and follow the prompts.

---

## ▶️ How to Run the Project

1. Make sure the following files are in the same folder:
   - `planets.csv`
   - `planets.py`

2. Open your terminal and run:

```bash
python planets.py
```

## 📁 Dataset Overview

This project uses a curated dataset containing scientific data on the **8 major planets**, including:

- 🌍 Planet Name  
- 🎨 Color Description  
- ⚖️ Mass (10²⁴ kg)  
- 📏 Diameter (km)  
- 🧲 Surface Gravity (m/s²)  
- 🚀 Escape Velocity (km/s)  
- 🌡 Mean Temperature (°C)  
- 🧪 Density (kg/m³)  
- 🌙 Number of Moons  
- 🔁 Orbital Period and more...


## 🧪 Features

This script enables users to:

- 🔘 Select planetary features via a simple menu  
- 🪐 Choose one, multiple, or all planets  
- 📊 View clean data tables  
- 📈 Visualize results with color-coded bar charts  

---

## ▶️ How to Run

1. Make sure the following files are in the same directory:
   - `planets.csv`
   - `planets.py`

2. Open a terminal and run:

```bash
python planets.py
````

3. Follow the interactive prompts to:

   * Pick a data feature (e.g., mass, temperature)
   * Select planets (or type `all`)
   * View the resulting table and chart

---

## 📦 Requirements

* Python 3.x
* `pandas`
* `matplotlib`

Install dependencies using:

```bash
pip install pandas matplotlib
```

---

## 🧾 Sample Interaction

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

➡️ A bar chart will also appear comparing the gravity values across the selected planets.


