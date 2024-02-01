import matplotlib.pyplot as plt

# Data
data_sizes = [10, 100, 1000, 10000, 100000, 1000000]
brute_force_times = [.002, .003, .023, 5.064, 11.213, 24.112]  # Replace time1, time2, ... with actual times
binary_search_times = [.002, .003, .003, .032, .035, 1.051]  # Replace time1, time2, ... with actual times

# Plot
plt.plot(data_sizes, brute_force_times, label='Brute Force')
plt.plot(data_sizes, binary_search_times, label='Binary Search')

# Add labels and title
plt.xlabel('Data Size')
plt.ylabel('Running Time (seconds)')
plt.title('Brute Force vs. Binary Search')
plt.legend()

# Scale plot to fit x-axis
plt.xticks(data_sizes)
plt.xscale('log')

# Show plot
plt.show()
