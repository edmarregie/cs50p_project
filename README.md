# Doji Trading Strategy Evaluation

This Python script is designed to evaluate a trading strategy based on the concept of doji candlestick patterns. The script analyzes historical price data to identify and trade doji candlestick patterns, aiming to determine the best parameters for maximizing trading gains.

## Introduction

A "doji" is a candlestick pattern commonly used in technical analysis. It occurs when the opening and closing prices of a security are nearly equal, resulting in a small or nonexistent body. This pattern suggests indecision in the market and can be a potential trading signal.

The script performs the following tasks:
- Loads historical price data from a CSV file.
- Iterates through a range of parameters (x and multiple) to find the best combination for trading doji patterns.
- Simulates trading based on the selected parameters and calculates the net trading points gained.
- Plots a chart showing the points earned for different body-to-range ratio percentages.

## Video Demo

To watch a how this works, [click here](https://youtu.be/txnx_Y_dvOg)

## Prerequisites

Before using this script, you need to have the following software and packages installed:

- Python 3.x
- pandas
- matplotlib

You can install these packages using pip:

```bash
pip install pandas matplotlib
```

## Usage

To use this script, follow these steps:

1. Prepare a CSV file containing historical price data. Ensure that the file contains columns for "date," "open," "high," "low," "close," and "volume."

2. Run the script, providing the CSV file as a command-line argument:

```bash
python project.py data_file.csv
```

Replace `data_file.csv` with the historical price data file in the csv folder.

3. The script will analyze the data and display the best parameter values and the corresponding net points earned. It will also generate a chart showing the points earned for different body-to-range ratio percentages and save it as a PNG file.

## Results

The script will output the following results:

- Best Percentage: This represents the optimal percentage range for the body-to-range ratio in doji patterns.
- Best Multiple: This represents the optimal multiple used in trading simulations.
- Best Net Points: This is the net trading points gained with the best parameter combination.

The script will also create a chart that visually represents the points earned for different parameter combinations.
Spoiler Alert: Doji does not result in increased earnings according to the program.

## Methodology

The script simulates trading by identifying doji patterns in the historical price data and using the Average True Range (ATR) to set stop-loss and take-profit levels. It calculates trading points gained or lost for each trade and iterates through different parameter combinations to find the best trading strategy.

## License

This script is provided under an open-source license. You are free to modify and distribute it as needed, but use it responsibly and at your own risk.

---

**Disclaimer:** This script is for educational and research purposes only and should not be considered as financial advice. Trading carries risks, and it is essential to conduct thorough research and consider your financial situation before engaging in any trading activities.
