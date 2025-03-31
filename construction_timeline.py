def construction_timeline_estimate(project_size, avg_time_per_sqft):
    return project_size * avg_time_per_sqft

project_size = 20000  # square feet
avg_time_per_sqft = 0.02  # months per square foot
timeline = construction_timeline_estimate(project_size, avg_time_per_sqft)
print(f"Estimated Construction Timeline: {timeline:.2f} months")
