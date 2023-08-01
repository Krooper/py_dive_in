import portfolio as pf

if __name__ == '__main__':
    stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
    print(pf.calculate_portfolio_value(stocks, prices))

    print(f'{round(pf.calculate_portfolio_return(10000, 15000))}%')

    prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
    print(pf.get_most_profitable_stock(stocks, prices))
