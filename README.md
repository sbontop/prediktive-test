## Market + Auction Value CHALLENGE:
--------------------

Included in this folder is the mocked API response for two sets of equipment. Spend some time visualizing and understanding the data structure.
For each year, there are two ratios, auctionRatio and MarketRatio. The cost is per set of equipment (ID).
If we want to calculate the 'value' of a set and year, we multiply the ratio for that year with the cost in saleDetails for that set.
- MarketValue = {cost} * {marketRatio}
- AuctionValue = {cost} * {auctionRatio}

Note: This challenge must be done in Python, but you can use the environment of your choice. 
You can use some freedom in how you implement it, as long as the basic conditions are met and you keep it simple.

- Task #1 
Write a function that takes the model id and year, and returns an object containing the calculated values (Market and Auction)
  
- Task #2
Adjust the function to ensure it handles incorrect input (EX: ID doesn't exist) graciously, you can do so however you prefer.
  
- Task #3
Add code to test your function, pass it the parameters below and log the result to the console.
Year 2007 ID 67352, Year 2011 ID 87964

Send us only the code of your final solution. Keep the project, you might be asked to screenshare and run it in a future interview.

# Setup
1. `pip install --user pipenv`
2. `cd team-international-python/`
3. `pipenv shell`
4. `python -m src.main` To run the project
5. `python -m unittest tests/test.py` To run the tests
