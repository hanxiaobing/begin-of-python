cars = 100
spaces_in_a_car = 4 #在python3.2 中4.0与4结果一致
drivers = 30
passengers = 90
cars_not_driven =cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * spaces_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print ("There are only",drivers,"drivers available.")
print ("There will be ", cars_not_driven,"empty cars today.")
print ("We can transport",carpool_capacity,"people today.")
print ("We have",passengers,"to carpool today.")
print ("We need to put about",average_passengers_per_car,"in each car.")