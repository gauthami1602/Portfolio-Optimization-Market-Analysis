Portfolio Optimization with Modern Portfolio Theory
Project Overview
This project implements portfolio optimization strategies using Modern Portfolio Theory (MPT) on S&P 500 stocks. The analysis covers data preparation, portfolio optimization, investment strategy comparison, and Monte Carlo simulations to evaluate portfolio performance.
Table of Contents

Data Preparation and EDA

Extracted S&P 500 companies by sector (Utilities, Financials, and Materials)
Retrieved and filtered historical stock price data (2017-2022)
Calculated cumulative returns and identified top-performing stocks in each sector
Visualized cumulative return ratios for analysis

Portfolio Optimization

Implemented Modern Portfolio Theory using Pyomo optimization
Calculated mean returns, standard deviations, and covariance matrices
Created constraints for portfolio allocation (minimum 2% per selected stock)
Generated the efficient frontier by varying risk levels
Visualized optimal stock allocations at different risk levels

Investment Strategies

Implemented and compared multiple investment approaches:

Buy-and-Hold
Daily Rebalancing
Weekly Rebalancing
Monthly Rebalancing


Analyzed performance metrics for each strategy

Monte Carlo Simulation

Performed Monte Carlo simulations to project future portfolio performance
Generated density plots of portfolio returns
Calculated probability of losing money
Validated projections through multiple simulation runs

Key Insights

Market dynamics vary significantly across sectors, requiring tailored analysis
Data quality is crucial for accurate portfolio optimization
Strategic diversification helps minimize risk while maintaining returns
The efficient frontier provides a visual guide for balancing risk and reward
Optimized allocation strategies demonstrate better long-term performance
