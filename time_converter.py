# Seconds Program
#Jeremy Bargy
#Jan. 31, 2020 
# 
# time converter for seconds

# Get a number of seconds from the user.
total_seconds = float(input('Enter a number of seconds: '))

# Calculate the number of hours.
hours = total_seconds // 3600

# Calculate the number of remaining seconds.
minutes = (total_seconds // 60) % 60

# Calclate the number of remaining seconds.
seconds = total_seconds % 60

# Display the results.
print('Here is the time in hours, minutes, and seconds:')
print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', seconds)
