from math import log, sqrt

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

# Simple return of an investment is preferred when making calculations about multiple assets over the same time period
def calculate_simple_return(start_price, end_price, dividend=0):
  result = (end_price - start_price + dividend) / start_price
  return result

simple_return = calculate_simple_return(200, 250, 20)
print('The simple rate of return is ' + display_as_percentage(simple_return))


# Logarithmic rate of return, where the earnings are to be reinvested over the time period.
# It is is preferred when making calculations about a single asset over time
def calculate_log_return(start_price, end_price):
  result = log(end_price/start_price)
  return result

log_return = calculate_log_return(200, 250)
print('The log rate of return is ' + display_as_percentage(log_return))


# In case we have a list of returns over a time and want to convert them into specific time period
def convert_returns(log_returns, t):
  return (sum(log_returns) / len(log_returns)) * t


# To calculate correlation between two instruments x and y
def calculate_correlation(set_x, set_y):
  sum_x = sum(set_x)
  sum_y = sum(set_y)

  sum_x2 = sum([x ** 2 for x in set_x])
  sum_y2 = sum([y ** 2 for y in set_y])

  sum_xy = sum([x * y for x, y in zip(set_x, set_y)])

  n = len(set_x)

  numerator = n * sum_xy - sum_x * sum_y
  denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

  return numerator / denominator
