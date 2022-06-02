# Different ways to create a dictionary
data = {
    "beer_data": 'beers',
    "brewery_data": 'breweries'
    }

# Using keyword arguments
data2 = dict(beer_data='beers', brewery_data='breweries')

# Using a list of tuples
tuple_list = [("brewery_data", 'breweries'), ("beer_data", 'beers')]
data3 = dict(tuple_list)


print(data == data2 == data3)       # True

data2.clear()
print(data2)

del data3
print(data3)        # Error name
