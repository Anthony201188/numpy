import numpy as np

""" You have been given a 2D NumPy array representing temperature data across different days and cities. 
Each row corresponds to a city, and each column corresponds to a day. 
Perform the following tasks:

- Slice and print the temperatures for the first 3 cities and the first 5 days.
- Calculate and print the average temperature for each city.
- Find and print the city with the highest average temperature. """

temperature_data = np.array([[28, 30, 32, 29, 27, 26, 28],
                             [31, 33, 30, 29, 28, 25, 26],
                             [24, 26, 25, 28, 30, 29, 27],
                             [22, 23, 26, 21, 20, 24, 26],
                             [29, 31, 33, 32, 30, 28, 27]])


#slice and print
print(temperature_data[:5,:3])

#avg temp each city
count = 0
averages = []
for city in temperature_data:
    avg = sum(city) / len(city)
    averages.append(avg)
    count += 1
    print(f"city{count} average:{avg}")

#avg max
max_avg = np.argmax(averages) #argmax returns the index of the largest value, second arg is which axis= which is optional i.e which line of data to fine the max for 
print("index position:",max_avg,"average temp:",averages[max_avg])

#VERSION 2
average_temperatures = np.mean(temperature_data, axis=1) #  similair to arg max apart from using mean.
print("\nAverage Temperatures for Each City:")
print(average_temperatures)