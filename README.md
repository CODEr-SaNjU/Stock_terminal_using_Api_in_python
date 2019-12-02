# StockTerminalApp

Weekend Assignments for Python-Full Stack

---
### Description
* We will be building a terminal stock trader game.
* The files have been made, notice there is one called `wrapper.py`
* Our game is going to give users a starting amount of money - maybe $100,000? and let them buy and sell stocks based on the current market info we get from the Markit API. 
* It should update their earnings whenever they login. There should be an admin who can log in and get an up to date leaderboard.

### Objectives

##### Part 1 - Building the Markit API Wrapper

* We'll be using the [Markit on Demand API](http://dev.markitondemand.com/MODApis/Api/v2/doc) 
* We will be pulling data from this API in JSON format
* Examples of the endpoint
```
http://dev.markitondemand.com/Api/v2/Lookup/json?input=Netflix
http://dev.markitondemand.com/Api/v2/Quote/json?symbol=AAPL
http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol=MSFT
```
* Take a look at the `wrapper.py` file. We have wrapped the calls to our api in a class. Now you must fill out what goes in each method. We will be utilizing these methods in our MVC application later
* company_search: takes a company's name and returns some basic data. 
    * company's formal name
    * the exchange that company is on
    * the company's ticker symbol
    * how can you standardize the input? maybe use the uppercase method?
* get_quote: takes a ticker symbol and receives up to the minute quote data.

##### Part 2 - Set up your database
* Your database should have two tables: Users and Stocks.
* Design a schema. What kind of relationship will these tables have? 
* What data goes into each table and relationship between 2 tables?
    
##### Part 3 - Game Functionality
* Users should be able to
    * search companies and get the exact stock ticker symbol
    * retrieve market data for a stock before they purchase it
    * log in with a username and password
    * buy and sell stock
        * buying should subtract from their funds, they cannot spend more money than what they have
        * selling will add to their funds, they cannot sell more stocks then what they have
        * users should be buying and selling at the current rate of the stock
    * view their "portfolio"
        * what are their total worth of stocks plus the money in the wallet
        * view their list of stocks

##### Part 4 - Admin
* Create a superuser who can see a leaderboard that displays the top ten users by portfolio earnings. 

