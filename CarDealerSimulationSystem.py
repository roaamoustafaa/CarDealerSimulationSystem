import numpy as np
import matplotlib.pyplot as plt

# Constants
MAX_CARS = 5
PROFIT_PER_CAR = 10000
HOLDING_COST = 1000
ORDER_COST = 20000

# Demand probabilities and values
demands = np.array([0, 1, 2, 3])
demand_probabilities = np.array([0.2, 0.34, 0.36, 0.1])

# Lead time probabilities and values
lead_times = np.array([1, 2, 3])
lead_time_probabilities = np.array([0.4, 0.35, 0.25])

# Function to simulate one run of 10 days
def simulate_ten_days(REVIEW_PERIOD_N):
    inventory = 3  # Starting inventory
    showroom = 4   # Starting showroom
    cars_ordered = 0
    total_profit = 0
    shortage_days = 0
    days_until_order_arrives = 0

    daily_demand = []
    daily_lead_time = []

    for day in range(10):
        # Simulate demand
        demand = np.random.choice(demands, p=demand_probabilities)
        daily_demand.append(demand)

        # Sell cars based on demand
        if demand <= showroom + inventory:
            sold_cars = demand
        else:
            sold_cars = showroom + inventory
            shortage_days += 1

        # Update showroom and inventory
        showroom -= sold_cars
        if showroom < 0:
            inventory += showroom
            showroom = 0

        # Check if we need to order more cars
        if inventory <= REVIEW_PERIOD_N and days_until_order_arrives <= 0:
            lead_time = np.random.choice(lead_times, p=lead_time_probabilities)
            daily_lead_time.append(lead_time)
            days_until_order_arrives = lead_time
            cars_ordered = MAX_CARS - (showroom + inventory)

        # Order arrives
        if days_until_order_arrives > 0:
            days_until_order_arrives -= 1
        if days_until_order_arrives == 0 and cars_ordered > 0:
            inventory += cars_ordered
            showroom = MAX_CARS - inventory
            cars_ordered = 0

        # Calculate daily profit
        daily_profit = sold_cars * PROFIT_PER_CAR - HOLDING_COST * inventory
        if showroom + inventory == 0:
            daily_profit -= ORDER_COST
        total_profit += daily_profit

    average_demand = np.mean(daily_demand)
    average_lead_time = np.mean(daily_lead_time) if daily_lead_time else 0
    ending_showroom_inventory = showroom + inventory

    return {
        'average_demand': average_demand,
        'average_lead_time': average_lead_time,
        'ending_showroom_inventory': ending_showroom_inventory,
        'shortage_days': shortage_days,
        'total_profit': total_profit
    }

# Function to simulate with varying review period N and return average net profit
def simulate_with_varying_review_period(N_values, num_simulation_runs=10, days_per_run=10):
    results = []
    for N in N_values:
        simulation_runs = [simulate_ten_days(N) for _ in range(num_simulation_runs)]
        average_net_profit = np.mean([run['total_profit'] for run in simulation_runs])
        results.append((N, average_net_profit))
    return results

# Run the original 10-day simulation 10 times with the default N and calculate averages
default_review_period_N = 3
simulation_runs = [simulate_ten_days(default_review_period_N) for _ in range(10)]

# Calculate experimental averages
experimental_avg_demand = np.mean([run['average_demand'] for run in simulation_runs])
experimental_avg_lead_time = np.mean([run['average_lead_time'] for run in simulation_runs])
avg_ending_inventory = np.mean([run['ending_showroom_inventory'] for run in simulation_runs])
total_shortage_days = np.sum([run['shortage_days'] for run in simulation_runs])
average_net_profit = np.mean([run['total_profit'] for run in simulation_runs])

print("Results for default review period (N = 3):")
print(f"Average Ending Units: {avg_ending_inventory}")
print(f"Average Net Profit: {average_net_profit} LE")
print(f"Number of Shortage Days: {total_shortage_days}")
print(f"Average Demand: {experimental_avg_demand}")
print(f"Average Lead Time: {experimental_avg_lead_time}")

# Plotting the results for default N
# Extracting data for plotting
demands_over_simulation = [run['average_demand'] for run in simulation_runs]
lead_times_over_simulation = [run['average_lead_time'] for run in simulation_runs if run['average_lead_time'] > 0]
profits_over_simulation = [run['total_profit'] for run in simulation_runs]

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Demand distribution plot
axs[0].bar(range(10), demands_over_simulation, color='blue', alpha=0.7)
axs[0].axhline(y=1.36, color='r', linestyle='--')
axs[0].set_title('Demand Distribution over Simulation Runs')
axs[0].set_xlabel('Simulation Run')
axs[0].set_ylabel('Average Demand')
axs[0].legend(['Theoretical Average Demand', 'Experimental Demand'])

# Lead time distribution plot
axs[1].bar(range(len(lead_times_over_simulation)), lead_times_over_simulation, color='green', alpha=0.7)
axs[1].axhline(y=1.85, color='r', linestyle='--')
axs[1].set_title('Lead Time Distribution over Simulation Runs')
axs[1].set_xlabel('Simulation Run')
axs[1].set_ylabel('Average Lead Time')
axs[1].legend(['Theoretical Average Lead Time', 'Experimental Lead Time'])

# Net profit plot
axs[2].plot(range(10), profits_over_simulation, marker='o', color='purple', alpha=0.7)
axs[2].set_title('Net Profit over Simulation Runs')
axs[2].set_xlabel('Simulation Run')
axs[2].set_ylabel('Net Profit (LE)')
axs[2].grid(True)

plt.tight_layout()
plt.show()


# Simulate with varying N values and plot the results
N_values_to_test = range(1, 6)
varying_N_results = simulate_with_varying_review_period(N_values_to_test)

# Plotting the results for varying N
plt.figure(figsize=(10, 5))
N_values, profits = zip(*varying_N_results)
plt.plot(N_values, profits, marker='o', linestyle='-', color='orange')
plt.title('Average Net Profit for Different Review Periods (N)')
plt.xlabel('Review Period N')
plt.ylabel('Average Net Profit (LE)')
plt.xticks(N_values)
plt.grid(True)
plt.show()

# Print the results for varying N values
print("\nResults for varying review period (N):")
for N, profit in varying_N_results:
    print(f"Review Period N = {N}: Average Net Profit = {profit} LE")
