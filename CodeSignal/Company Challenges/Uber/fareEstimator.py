def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    arr = []
    for i in range(len(cost_per_minute)):
        arr.append((cost_per_minute[i] * ride_time) + (cost_per_mile[i] * ride_distance))
    return arr