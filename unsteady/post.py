import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Path to the data file
file_path = "./postProcessing/forces/0/moment.dat"

tsr = 1.6
diameter = 0.22
radius = diameter/2
freestream_velocity = 10 # m/s
rotation_speed_rads = tsr*freestream_velocity/radius # rad/s

density_air = 1.225 # kg/m^3
radius = 0.11 # m
area_rotor = (radius**2)*np.pi # m^2
power_available = 0.5*density_air*area_rotor*(freestream_velocity**3)

# Function to update the plot
def update_plot(num):
    # Clear the previous plot
    plt.cla()

    # Lists to store the time and torque values
    time = []
    torque = []

    # Read the file and extract the relevant data
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('#') or line.startswith('\n'):
                continue
            data = line.strip().split('\t')
            time.append(float(data[0]))
            torque_value = float(data[1].split('(')[1].split()[0])
            torque.append(torque_value)

    torque_array = np.array(torque)  # Convert torque list to a NumPy array
    power_generated = -torque_array * rotation_speed_rads
    power_coefficient = power_generated / power_available

    # Plotting the torque values against time
    plt.plot(time, power_coefficient)
    plt.xlabel('Time')
    plt.ylabel('Power coefficient')
    plt.grid(True)
    plt.ylim(0, 0.5)  # Set the y-axis limit

    # Adding the horizontal dashed line
    plt.axhline(y=0.24, color='black', linestyle='--')
    plt.text(max(time) / 2, 0.25, 'Experimental measurement', color='black', fontsize=10, ha='center')

# Create the animation
ani = animation.FuncAnimation(plt.gcf(), update_plot, interval=60000)  # Update every minute (60000 milliseconds)

# Display the plot
plt.show()

