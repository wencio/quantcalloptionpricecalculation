import QuantLib as ql  # Import the QuantLib library for quantitative finance calculations
import pandas as pd   # Import pandas for data manipulation
import numpy as np    # Import numpy for numerical operations

# Define option parameters
option_type = ql.Option.Call  # Set the option type to Call (you can also use Put)
underlying_price = 100       # Current price of the underlying asset
strike_price = 105           # Strike price of the option
time_to_maturity = 1         # Time to option expiration (in years)
volatility = 0.2            # Volatility of the underlying asset
interest_rate = 0.05        # Risk-free interest rate

# Define today's date
today = ql.Date(15, ql.May, 2023)

# Calculate the option's expiration date
expiration_date = today + ql.Period(int(time_to_maturity * 365), ql.Days)  # 365 days in a year

# Create the option object
option = ql.EuropeanOption(ql.PlainVanillaPayoff(option_type, strike_price), ql.EuropeanExercise(expiration_date))

# Create the Black-Scholes-Merton model
spot_handle = ql.QuoteHandle(ql.SimpleQuote(underlying_price))  # Handle for the underlying asset price
rate_handle = ql.YieldTermStructureHandle(ql.FlatForward(today, ql.QuoteHandle(ql.SimpleQuote(interest_rate)), ql.Actual360()))  # Handle for the risk-free interest rate curve
dividend_rate = ql.YieldTermStructureHandle(ql.FlatForward(today, ql.QuoteHandle(ql.SimpleQuote(0.0)), ql.Actual360()))  # Handle for the dividend rate (assumed to be 0)
volatility_surface = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(today, ql.NullCalendar(), ql.QuoteHandle(ql.SimpleQuote(volatility)), ql.Actual360()))  # Handle for the volatility surface

# Create the Black-Scholes-Merton process
process = ql.BlackScholesMertonProcess(spot_handle, dividend_rate, rate_handle, volatility_surface)

# Calculate the option price using the Analytic European Engine
engine = ql.AnalyticEuropeanEngine(process)
option.setPricingEngine(engine)
option_price = option.NPV()  # Net Present Value (Option Price)

# Print the calculated option price
print("Option Price:", option_price)
