# Flight-Planner

Finished it, got rid of all the bugs

Ran Into File "/usr/lib/python3.8/tkinter/__init__.py", line 1883, in __call__ return self.func(*args) File "main.py", line 63, in search_flights max_fare = max(MaxFares.values()) AttributeError: 'list' object has no attribute 'values' Fix after Lunch

Added a way to find cheapest flight(Need to fix it displaying no flights found when it does find one)

Added a display for Indirect flights to show the cost

fixed random flights so it can take from the website instead of a premade dictionary

Added a Random Flights button

Added a Gui, Search button and find minimum fare
