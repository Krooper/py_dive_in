_initial_prices = {}


def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    global _initial_prices
    result = 0
    _initial_prices = prices
    for stock, value in stocks.items():
        result += value * prices[stock]
    return result


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return (current_value - initial_value) * 100 / initial_value


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    global _initial_prices
    stocks_return = {}
    for stock, value in stocks.items():
        stocks_return[stock] = (prices[stock] - _initial_prices[stock]) * value

    max_profit_stock = ''
    tmp = 0
    for stock, profit in stocks_return.items():
        if stocks_return[stock] > tmp:
            max_profit_stock = stock
            tmp = stocks_return[stock]

    return max_profit_stock
