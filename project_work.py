# -*- coding: utf-8 -*-
"""Project_work.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u2KtgJvNYHvnqZvG748iaso_s7HjR4wm

## **PART 1** - **Data Preparation and EDA**

**Extracting S&P 500 Companies by sector**
"""

from google.colab import drive
drive.mount('/content/drive')



import pandas as pd

# Load dataset
file_path =  '/content/drive/MyDrive/Updated_Health_Sleep_Statistics.csv' # Change this to your actual file path
df = pd.read_csv(file_path)

# Define function to categorize age into 20 divisions
def categorize_age(age):
    lower_bound = (age // 5) * 5  # Find the lower bound of the range (multiples of 5)
    upper_bound = lower_bound + 4  # Upper bound of the range
    return f"{lower_bound}-{upper_bound} years"

# Apply function to create Age_Group column
df["Age_Group"] = df["Age"].apply(categorize_age)

# Save updated dataset
output_file = "Updated_Age_Groups.csv"
df.to_csv(output_file, index=False)

print(f"Updated dataset saved as {output_file}")

# If you are using Google Colab, you can use the following code to download the file
from google.colab import files

# Download the file
files.download('Updated_Age_Groups.csv')

"""**Description:**

We begin by importing the pandas library to help work with data. Next, we set up the link to a Wikipedia page that lists all S&P 500 companies and use pandas to pull the table from that page. The first table contains the data we need, so we save it in a variable called sptable.And then specified the sectors we’re interested in—“Utilities,” “Financials,” and “Materials”—and filter the table to include only companies in those sectors. Finally, we collect the stock symbols (tickers) of these companies and print them out for reference.

**Organizing tickers by Sectors**
"""

# Create dictionaries to store tickers by sector
utilities_tickers = []
financials_tickers = []
materials_tickers = []

# Segregate tickers by sector
for ticker in tickers_list:

    # Find the row in sptable matching this ticker
    row = sptable[sptable['Symbol'] == ticker]
    if not row.empty:
        sector = row['GICS Sector'].values[0]

        # Append ticker to the appropriate sector list
        if sector == 'Utilities':
            utilities_tickers.append(ticker)
        elif sector == 'Financials':
            financials_tickers.append(ticker)
        elif sector == 'Materials':
            materials_tickers.append(ticker)

# Print the results
print("Utilities Sector Tickers:", utilities_tickers)
print("Financials Sector Tickers:", financials_tickers)
print("Materials Sector Tickers:", materials_tickers)

"""**Description:**

In this code, we start by creating three empty lists to store tickers for each of the sectors: Utilities, Financials, and Materials. Then, we use a loop to go through each ticker symbol in our previously filtered list. For each ticker, we find its corresponding row in the sptable data. If the ticker's row exists, we check its sector and add the ticker to the appropriate list based on whether it belongs to Utilities, Financials, or Materials. Finally, we print out the tickers organized by sector for easy reference.

**Retrieving and Storing Historical Stock Price Data for Selected Tickers**
"""

!pip install yahoo_fin
import yahoo_fin.stock_info as si
from datetime import datetime

# Define start and end dates for your data retrieval
start_date = '01/01/2017'
end_date = '12/31/2022'

# Dictionary to store price data
sector_prices = {}

# Loop through tickers to retrieve data, handling errors
for ticker in tickers_list:
    try:
        # Retrieve data for each ticker
        data = si.get_data(ticker, start_date=start_date, end_date=end_date, interval='1d')
        sector_prices[ticker] = data
        print(f"Data retrieved successfully for {ticker}")
    except AssertionError as e:
        print(f"Error retrieving data for {ticker}: {e}")

"""**Description:**

In this part, we start by installing and importing yahoo_fin, a library used to get stock data, and set the date range for data retrieval from January 1, 2017 to December 31, 2022. Next, we create an empty dictionary, sector_prices, to store stock price data for each ticker. Using a loop, we attempt to retrieve daily price data for each ticker in our list within the specified date range. If data retrieval is successful, we store it in sector_prices and print a success message; if there’s an error, it displays an error message for that ticker.

**Printing Historical Stock price data for the tickers**
"""

# Loop through all tickers and display the full dataset for each
for ticker, data in sector_prices.items():
    print(f"\nData for {ticker}:\n", data)

"""**Description :**

In this code section, we loop through all the tickers stored in sector_prices and display the complete dataset for each one. For each ticker, we print its name, followed by the full data table containing its daily stock prices within the specified date range. This helps us visually verify that data has been collected correctly for each stock.

**Cleaning and Filtering Stock price data**
"""

# Set the expected number of rows
expected_rows = 1510

# Dictionary to store the cleaned data
clean_data = {}

# Loop through each ticker's data and store only those with complete data
for ticker, data in sector_prices.items():
    # Check if the data has the expected number of rows and no missing values
    if len(data) == expected_rows and data.isnull().sum().sum() == 0:
        clean_data[ticker] = data
    else:
        print(f"Excluding {ticker}: Row count = {len(data)}, Missing values = {data.isnull().sum().sum()}")

# Display the tickers that are included in the cleaned data
print("Tickers with complete data:")
print(list(clean_data.keys()))

"""**Decription :**

In this code block, we first define the expected number of rows (1510) for each ticker’s dataset, covering the daily data from January 1, 2017, to December 31, 2022. We create an empty dictionary called clean_data to store only the tickers with complete datasets. For each ticker, we check if its dataset has the expected number of rows and no missing values. If both conditions are met, the ticker’s data is added to clean_data; otherwise, we print a message indicating the ticker is excluded, showing the actual row count and number of missing values. Finally, we print the list of tickers that have complete data.

**Organising the obtained data by sector**
"""

# Create a dictionary to store data by sector
sector_data = {sector: {} for sector in our_sectors}

# Loop through each ticker in clean_data and match it with its sector
for ticker, data in clean_data.items():
    # Find the sector for the ticker in sector_companies
    sector = sector_companies.loc[sector_companies['Symbol'] == ticker, 'GICS Sector'].values
    if sector.size > 0:  # Ensure the sector was found
        sector_name = sector[0]
        # Add the ticker's data to the respective sector dictionary
        sector_data[sector_name][ticker] = data

# Display the tickers segregated by sector
for sector_name, tickers in sector_data.items():
    print(f"\nTickers in the {sector_name} sector:")
    print(list(tickers.keys()))

"""**Description :**

In this code, we start by creating a dictionary, sector_data, to store stock data organized by each sector (Utilities, Financials, and Materials). For each ticker in clean_data, we identify its sector by looking it up in sector_companies. If the sector is found, we add the ticker’s data to the corresponding sector in sector_data. Finally, we print out the tickers grouped by sector to confirm they’re correctly organized. This setup ensures that each sector has its relevant tickers and data stored neatly for further analysis.

**Calculating Cumulative Returns for Each Ticker Over a Period**
"""

# Function to calculate cumulative return over the period
def calculate_cumulative_return(data):
    return (data['adjclose'][-1] / data['adjclose'][0]) - 1

# Dictionary to store cumulative returns
cumulative_returns = {}

for ticker, data in clean_data.items():
    cumulative_returns[ticker] = calculate_cumulative_return(data)

"""**Description :**

In this section, we define a function called calculate_cumulative_return to compute the cumulative return for each stock over the entire period. The function calculates this by dividing the last closing price by the first closing price and subtracting one to express it as a percentage change. We then create a dictionary, cumulative_returns, to store the calculated cumulative return for each ticker in clean_data. Using a loop, we apply the function to each ticker’s data and save the result in cumulative_returns.

**Identifying Top 3 Performing Stocks in each Sector Based on Cumulative Returns**
"""

# Dynamically separate tickers by sector using clean data
sector_tickers = {
    sector: [ticker for ticker in clean_data.keys() if sector_companies.loc[sector_companies['Symbol'] == ticker, 'GICS Sector'].values[0] == sector]
    for sector in our_sectors
}
top_stocks = {}

for sector, tickers in sector_tickers.items():
    # Filter cumulative returns for tickers in this sector
    sector_returns = {ticker: cumulative_returns[ticker] for ticker in tickers if ticker in cumulative_returns}

    # Select top 3 based on returns and store ticker with its cumulative return
    top_stocks[sector] = {ticker: sector_returns[ticker] for ticker in sorted(sector_returns, key=sector_returns.get, reverse=True)[:3]}

print("Top stocks per sector based on cumulative returns:")
for sector, stocks in top_stocks.items():
    print(f"\nSector: {sector}")
    for ticker, cumulative_return in stocks.items():
        print(f"{ticker}: {cumulative_return:.2f}")

"""**Decription :**

In this code, we start by defining the tickers for each sector (Utilities, Financials, and Materials) in the sector_tickers dictionary. We then initialize top_stocks, which will store the top 3 stocks by cumulative return for each sector. For each sector, we filter cumulative_returns to get only the tickers belonging to that sector. We then sort these tickers by cumulative return in descending order and select the top 3, storing each ticker along with its cumulative return in top_stocks. Finally, we print the top-performing stocks in each sector, displaying their tickers and cumulative returns.
"""

# Function to get top 3 stocks for each sector
def get_top_stocks_by_sector(top_stocks):
    top_stocks_by_sector = {}
    for sector, stocks in top_stocks.items():
        sorted_stocks = sorted(stocks.items(), key=lambda item: item[1], reverse=True)[:3]
        top_stocks_by_sector[sector] = sorted_stocks
    return top_stocks_by_sector

# Get the top 3 stocks for each sector
top_3_stocks_by_sector = get_top_stocks_by_sector(top_stocks)

print(top_stocks)

"""**Visualizing Cumulative Returns Ratio for Top Stocks by sector**"""

import matplotlib.pyplot as plt

# Plot cumulative return ratios
for sector, tickers in top_stocks.items():
    plt.figure(figsize=(10, 6))

    for ticker in tickers:
        data = clean_data[ticker].copy()

        # Calculate return ratio
        data['Return Ratio'] = data['adjclose'] / data['adjclose'].iloc[0]

        # Plot return ratio
        plt.plot(data.index, data['Return Ratio'], label=ticker)

    plt.title(f'Cumulative Return Ratios for {sector} Sector')
    plt.xlabel('Date')
    plt.ylabel('Return Ratio')
    plt.legend()
    plt.grid(True)
    plt.show()

"""**Description :**

In this code, we use matplotlib to create plots showing cumulative return ratios for the top 3 stocks in each sector. For each sector, we initialize a new plot and loop through its top-performing tickers. For each ticker, we calculate the return ratio by dividing each day's closing price by the initial closing price, giving a normalized view of how the stock has grown over time. We then plot the return ratio over the date range, labeling each stock by its ticker. Each plot is titled according to the sector and includes axis labels and a legend to differentiate the stocks. Finally, we display the plot for each sector.

1. In this Utilities sector plot, each line shows the cumulative return ratio for NEE, NRG, and AES, reflecting their price growth from January 1, 2017, NRG (orange line) stands out with the highest return ratio, reaching approximately 2.0, which corresponds to a 100% increase. NEE (blue line) follows a steady upward trend, achieving a return ratio of around 1.7, or 70% growth. AES (green line) shows more modest growth, with a return ratio close to 1.4, translating to a 40% increase. This plot highlights NRG’s strong performance within this range, followed by NEE's consistent growth, while AES displays a more moderate rise.

2. In this Financials sector plot, each line represents the cumulative return ratio for MSCI, PGR, and AJG, illustrating their price growth relative to the starting value on January 1, 2017, MSCI (blue line) shows the strongest performance, reaching a return ratio of around 2.5, equivalent to a 150% increase, with noticeable fluctuations, especially after 2019. PGR (orange line) demonstrates a steady growth, with a return ratio of approximately 1.8, reflecting an 80% increase. AJG (green line) also maintains a stable growth trajectory, achieving a return ratio close to 1.6, or a 60% rise. This visualization highlights MSCI’s robust but volatile growth compared to the more moderate, consistent increases seen with PGR and AJG.

3. In this plot for the Materials sector, the cumulative return ratios for LIN, FCX, and STLD illustrate the growth of each stock’s price relative to its starting value on January 1, 2017, FCX (orange line) shows the most significant rise, with a return ratio nearing 2.0, which translates to a 100% gain by late 2022. LIN (blue line) follows with a return ratio around 1.7, indicating a 70% increase. STLD (green line) exhibits more modest growth, with a return ratio close to 1.5, or a 50% gain. This plot highlights FCX's stronger performance within this range, with LIN and STLD showing steady but lower gains over the period.

# PART 2

**Extracting Selected Stocks for Optimization Across Sectors**
"""

# Collect the selected stocks from the top companies in each sector
selected_stocks = []
for sector in top_stocks:
    selected_stocks.extend(top_stocks[sector].keys())

print("Selected Stocks for Optimization Model:", selected_stocks)

print(selected_stocks)

import yfinance as yf
prices_df = yf.download(selected_stocks, start="2017-01-01", end="2022-12-31")['Adj Close']
prices_df.head()

returns_df = prices_df.pct_change().dropna()
returns_df.head()

returns_df.describe()

import matplotlib.pyplot as plt
prices_df.plot(figsize=(10, 6))
plt.title('Daily Returns of Selected Stocks')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.show()

import matplotlib.pyplot as plt
returns_df.plot(figsize=(10, 6))
plt.title('Daily Returns of Selected Stocks')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.show()

# Calculate mean daily returns for each stock
mean_returns = returns_df.mean()
# Calculate standard deviation for each stock
std_dev = returns_df.std()
# Print the results
print("Mean Daily Returns:")
print(mean_returns)
print("\nStandard Deviation:")
print(std_dev)

summary = pd.DataFrame({'Mean Return': mean_returns, 'Standard Deviation': std_dev})
print(summary)

# Calculate the covariance matrix of daily returns
cov_matrix = returns_df.cov()
print("\nCovariance Matrix:")
print(cov_matrix)

# Calculation of Correlation matrix of daily returns
corr_matrix = returns_df.corr()
print("\nCorrelation Matrix:")
print(corr_matrix)

print(cov_matrix)
print('\n')
print(mean_returns)

min_cov = cov_matrix.min().min()
max_cov = cov_matrix.max().max()
print("Minimum Covariance:", min_cov)
print("Maximum Covariance:", max_cov)

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# import sys
# import os
# 
# # Installing necessary libraries and extensions
# if 'google.colab' in sys.modules:
#    !pip install idaes-pse --pre     # Install IDAES-PSE for optimization
#    !idaes get-extensions --to ./bin  # Get extensions for BonMin solver
#    os.environ['PATH'] += ':bin'   # Add the extensions path to system PATH
# 
# # Import required modules for optimization and plotting
# %matplotlib inline
# from pylab import *  # Importing Pyomo for optimization modeling
# 
# import shutil
# import sys
# import os.path
# from pyomo.environ import *
# 
# # Specify the executable path for the BonMin solver
# executable = '/content/bin/bonmin' # THIS IS NEW! We are using the IPOPT Solver.
#

from pyomo.environ import *

# Initialize the optimization model
m = ConcreteModel()

# Define continuous and binary variables dynamically
m.continuous_vars = Var(selected_stocks, within=NonNegativeReals,bounds=(0, 1))  # Allocation variables
m.binary_vars = Var(selected_stocks, within=Binary)  # Binary decision variables

# Defining objective function
# Maximize portfolio return based on the mean return of selected stocks
m.objective = Objective(expr=sum(m.continuous_vars[stock] * m.binary_vars[stock] * mean_returns[stock] for stock in selected_stocks),sense=maximize)

#Constraints
m.limit=Constraint(expr=sum(m.continuous_vars[stock]*m.binary_vars[stock]for stock in selected_stocks)==1)

m.pprint() #verifying that my constraints are declared

# Constraint 1: Sum of all proportions must equal 1
if 'sum_proportions' in m.component_map(Constraint):
    m.del_component(m.sum_proportions)
m.sum_proportions = Constraint(expr=sum(m.continuous_vars[stock] for stock in selected_stocks) == 1)

# Constraint 2: Minimum allocation of 2% for each stock, or allocation must be zero if not selected
m.allocation = ConstraintList()
for stock in selected_stocks:
  m.allocation.add(m.continuous_vars[stock] >= 0.02 * m.binary_vars[stock])
  m.allocation.add(m.continuous_vars[stock] <= m.binary_vars[stock])



# Additional Technical Constraint: Ensure all allocations are non-negative (Optional)
if 'total_risk' in m.component_map(Constraint):
    m.del_component(m.total_risk)
m.total_risk = Constraint(expr=sum(m.continuous_vars[stock] for stock in selected_stocks) >= 0.0)

# Risk constraint (ensures portfolio risk is considered)
m.total_risk=Constraint(expr=sum(m.continuous_vars[stock]*m.binary_vars[stock]for stock in selected_stocks)>=0)

# Activate all constraints in the model
for con in m.component_objects(Constraint, active=None):
    con.activate()

# Verify that all constraints are active
print("All constraints have been activated.")

m.pprint() #verifying that my constraints are declared

# Function to calculate portfolio risk
def calc_risk(m):
    risk_exp = sum(
        m.continuous_vars[i] * cov_matrix.at[i, j] * m.continuous_vars[j]
        for i in selected_stocks for j in selected_stocks
    )
    return risk_exp

# Compute the risk expression
expr_risk = calc_risk(m)

# Print the calculated risk expression
print("Calculated Risk Expression:", expr_risk)

# Use a nonlinear solver
solver = SolverFactory('ipopt')
solver.solve(m)

# Extract results
print("\nOptimal Portfolio Allocation:")
for stock in selected_stocks:
    print(f"{stock}: {m.continuous_vars[stock].value}")

print("\nPortfolio Risk:")
print(expr_risk())

import numpy as np

# Maximum allowable risk
max_risk = 0.0005  # Adjust this value based on your project's requirements

# Generate a sequence of risk levels (at least 100 distinct levels)
risk_limits = np.linspace(0.00001, max_risk, 100)  # Linearly spaced risk ceilings

# Displaying the total count of distinct risk ceiling values used
print("Total number of risk ceilings used:", len(risk_limits))

# Display the first few and last few risk limits for verification
print("Sample Risk Ceilings:")
print("First 5:", risk_limits[:5])
print("Last 5:", risk_limits[-5:])

from pyomo.opt import TerminationCondition
import os

# Initialize dictionaries to store results
parameter_analysis = {}  # key = risk, value = stock allocations
returns = {}  # key = risk, value = return
infeasible_risks = []  # store infeasible risk values

# Solver setup for Bonmin (ensure Bonmin is correctly installed)
bonmin_executable = '/content/bin/bonmin'

for r in risk_limits:
    # Remove and recalculate the risk constraint for each iteration
    if "total_risk" in m.component_map(Constraint):
        m.del_component(m.total_risk)

    # Add updated risk constraint with the current risk limit
    m.total_risk = Constraint(expr=expr_risk <= r)

    # Solve the model using the Bonmin solver
    result = SolverFactory('bonmin', executable=bonmin_executable).solve(m, tee=True)

    # If the result is infeasible, store the risk value and skip to the next iteration
    if result.solver.termination_condition == TerminationCondition.infeasible:
        infeasible_risks.append(r)
        continue

    # Store stock allocations for this risk limit
    parameter_analysis[r] = [m.continuous_vars[stock].value for stock in selected_stocks]

    # Calculate and store the portfolio return for this risk level
    returns[r] = sum(
        m.continuous_vars[stock].value * mean_returns[stock] for stock in selected_stocks
    )

# After running the loop, check for at least one discarded risk level
if not infeasible_risks:
    raise ValueError("At least one risk level should lead to an infeasible problem.")

# Print infeasible risks
print("Infeasible Risks:", infeasible_risks)

# Convert results to a DataFrame for analysis
import pandas as pd

results_df = pd.DataFrame({
    "Risk Limit": list(parameter_analysis.keys()),
    "Allocations": list(parameter_analysis.values()),
    "Returns": list(returns.values())
})

# Display the first few rows of results
print(results_df.head())

# Save results to a CSV file (optional)
results_df.to_csv("risk_analysis_results.csv", index=False)

print("Infeasible Risk Values:", infeasible_risks)
len(infeasible_risks)

print(parameter_analysis)

# Risk limits and step sizes
max_risk = cov_matrix.abs().max().max()  # Maximum covariance
min_risk = cov_matrix.abs().min().min()  # Minimum covariance
step = (max_risk - min_risk) / 100  # Step size
risk_limits = np.arange(min_risk, max_risk, step)  # Sequence of risk levels
print("Risk Limits: ",risk_limits)

from pyomo.opt import TerminationCondition
import os

# Initialize dictionaries to store results
parameter_analysis = {}  # key = risk, value = stock allocations
returns = {}  # key = risk, value = return
infeasible_risks = []  # store infeasible risk values

# Solver setup for Bonmin (ensure Bonmin is correctly installed)
bonmin_executable = '/content/bin/bonmin'

for r in risk_limits:
    # Remove previous total_risk constraint to avoid errors
    if hasattr(m, 'total_risk'):
        m.del_component(m.total_risk)

    # Add updated risk constraint with the current risk limit
    m.total_risk = Constraint(expr=expr_risk <= r)

    # Solve the model using the Bonmin solver
    result = SolverFactory('bonmin', executable=bonmin_executable).solve(m, tee=True)

    # If the result is infeasible, store the risk value and skip to the next iteration
    if result.solver.termination_condition == TerminationCondition.infeasible:
        infeasible_risks.append(r)
        continue

    # Skip if the solution is not optimal
    if result.solver.termination_condition != TerminationCondition.optimal:
        continue

    # Store allocations for this risk level
    parameter_analysis[r] = {stock: m.continuous_vars[stock].value for stock in selected_stocks}

    # Calculate and store the portfolio return for this risk level
    returns[r] = sum(m.continuous_vars[stock].value * mean_returns[stock] for stock in selected_stocks)

# Final results
print("Parameter Analysis (Allocations):", parameter_analysis)
print("Returns for Each Risk Level:", returns)

# Creating a DataFrame to store portfolio allocations for each risk level
param_analysis = pd.DataFrame.from_dict(parameter_analysis, orient='index')

# Renaming columns to match ticker names for better clarity
param_analysis.columns = [selected_stocks[i] for i in range(len(selected_stocks))]

# Identifying the minimum risk level
least_risk = min(param_analysis.index)

# Plotting the allocation proportions for each risk level
param_analysis.plot(figsize=(10, 10))  # Generate a plot with defined figure size

# Adding labels and title for clarity
plt.xlabel('Risk Level')  # X-axis label
plt.ylabel('Proportion of allocation')  # Y-axis label
plt.title('Optimal Stock Allocation for Different Risk Levels')  # Plot title

# Display the plot
plt.show()

# Extracting the list of risk levels from the keys of the returns dictionary
risk_list = list(returns.keys())

# Extracting the corresponding return values from the returns dictionary
return_list = list(returns.values())

from pylab import *

# Plotting risk levels against returns to visualize the efficient frontier
plt.figure(figsize=(10, 10))
plot(risk_list, return_list)  # Creating the efficient frontier curve
plt.title('Efficient Frontiers')
plt.xlabel('Risk Level')  # X-axis represents risk levels
plt.ylabel('Return')  # Y-axis represents portfolio returns
plt.show()

"""# **Part 5**

# **Insights:**

*   **Understanding Market Dynamics**: The analysis highlighted diverse performance
trends across sectors, emphasizing the need to analyze market data to uncover unique behaviors and identify top-performing stocks.

* **Data Quality and Validation**: Addressing issues like missing data and delisted stocks ensured a clean dataset, establishing a solid foundation for accurate analysis and decision-making.



*  **Market Adaptability**: The analysis underscored the importance of adaptability in response to frequent market changes, emphasizing the need for flexible strategies to preserve returns and mitigate risk.

* **Correlations Between Assets**: EDA revealed key correlations between stocks across different sectors, helping inform better diversification strategies and reduce overall risk.

*  **Long-Term Stability**: Structured investment strategies demonstrated their ability to maintain portfolio alignment over time, ensuring steady growth even amidst market fluctuations.

*  **Balancing Risk and Reward**: MPT emphasized the need to balance potential risks with expected returns, reinforcing the importance of calculated investment decisions.
*   **Efficient Frontier Observations**: The efficient frontier analysis illustrated the balance between risk and return, helping identify the optimal risk-return trade-off for investment decisions.


*  **Validation Through Repetition**: Increasing the number of Monte Carlo simulations added reliability to the projections, ensuring robust and actionable insights for portfolio decision-making.


*  **Optimized Allocation Benefits**: Optimized strategies demonstrated their effectiveness in sustaining long-term performance, showcasing the benefits of thoughtful asset allocation.


* **Strategic Diversification**: Distributing investments across various assets proved valuable in minimizing risks while maintaining returns. MPT reinforced the importance of optimal allocation spread across sectors.



*  **Hands-On Learning**: Through the project, we gained practical experience in financial modeling, equipping us with essential skills for future portfolio management and risk analysis.

