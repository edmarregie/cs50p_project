import pytest
from project import find_best_parameters, simulate_trading, calculate_atr


def test_calculate_atr():
    data = pd.DataFrame({
        "date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "open": [100, 110, 120],
        "high": [120, 130, 140],
        "low": [90, 100, 110],
        "close": [110, 120, 130],
        "volume": [1000, 1100, 1200]
    })

    atr = calculate_atr(data, period=3)

    expected_atr = [20.0, 20.0, 20.0]

    assert atr.tolist() == expected_atr


def test_simulate_trading():
    data = pd.DataFrame({
        "date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "open": [100, 110, 120],
        "high": [120, 130, 140],
        "low": [90, 100, 110],
        "close": [110, 120, 130],
        "volume": [1000, 1100, 1200]
    })

    points = simulate_trading(data, x=50, multiple=2)

    # Expected trading points for the sample data
    expected_points = 0  # Replace with the expected result

    assert points == expected_points


def test_find_best_parameters():
    data = pd.DataFrame({
        "date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "open": [100, 110, 120],
        "high": [120, 130, 140],
        "low": [90, 100, 110],
        "close": [110, 120, 130],
        "volume": [1000, 1100, 1200]
    })

    best_parameters, best_net_points, _ = find_best_parameters(data)

    expected_parameters = (0, 1)

    assert best_parameters == expected_parameters

