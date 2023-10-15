import pandas as pd
import sys
import matplotlib.pyplot as plt

def main():
    column_names = ["date", "open", "high", "low", "close", "volume"]
    data = pd.read_csv(f"csv/{sys.argv[1]}", names=column_names)

    best_parameters, best_net_points, results = find_best_parameters(data)

    print_best_parameters(best_parameters)
    print("Best Net Points:", best_net_points)

    plot_results(results, sys.argv[1])

def find_best_parameters(data):
    best_net_points = -float('inf')
    best_parameters = None
    results = {}

    for x in range(0, 100):
        for multiple in range(1, 31):
            gained_points = simulate_trading(data, x, multiple)
            results[(x, multiple)] = gained_points

            if gained_points > best_net_points:
                best_net_points = gained_points
                best_parameters = (x, multiple)

    return best_parameters, best_net_points, results

def simulate_trading(data, x, multiple):
    atr = calculate_atr(data)
    gained_points = 0
    open_positions = []

    i = 1

    while i < len(data):
        price_range = data["high"][i] - data["low"][i]
        body = abs(data['open'][i] - data['close'][i])
        # The rest of your trading simulation logic goes here
        # ...

def calculate_atr(data, period=14):
    data['true_range'] = data.apply(
        lambda row: max(
            row['high'] - row['low'],
            abs(row['high'] - row['close']),
            abs(row['low'] - row['close'])
        ),
        axis=1
    )

    data['atr'] = data['true_range'].rolling(window=period).mean()

    return data['atr']

def plot_results(results, input_filename):
    x_values, y_values = zip(*results.items())
    x, y = zip(*x_values)
    plt.scatter(x, y, c=y_values, cmap='viridis')
    plt.title(f"Points Earned for Different Body-to-Range Ratio for {input_filename}")
    plt.xlabel("Percentage of body-to-range ratio (x)")
    plt.ylabel("Multiple")
    plt.colorbar(label="Points Earned")
    plt.savefig(f"chart/{input_filename}.png")

def print_best_parameters(parameters):
    best_perc, best_multiple = parameters
    print(f"Best Percentage: {best_perc} to {best_perc + 1}")
    print(f"Best Multiple: {best_multiple}")

if __name__ == "__main__":
    main()
