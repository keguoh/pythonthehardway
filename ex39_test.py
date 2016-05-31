import ex39_hashmap as hm

# create a mapping of state to abbreviation
states = hm.new()
hm.set(states, 'Oregon', 'OR')
hm.set(states, 'Florida', 'FL')
hm.set(states, 'California', 'CA')
hm.set(states, 'New York', 'NY')
hm.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = hm.new()
hm.set(cities, 'CA', 'San Francisco')
hm.set(cities, 'MI', 'Detroit')
hm.set(cities, 'FL', 'Jacksonville')

# add some more cities
hm.set(cities, 'NY', 'New York')
hm.set(cities, 'OR', 'Portland')


# print out some cities
print '-' * 10
print "NY State has: %s" % hm.get(cities, 'NY')
print "OR State has: %s" % hm.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % hm.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hm.get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
hm.list(states)

# print every city in state
print '-' * 10
hm.list(cities)

print '-' * 10
state = hm.get(states, 'Texas')

if not state:
	print "Sorry, no Texas."

# default values using ||= with the nil result
# can you do this on one line?
city = hm.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city