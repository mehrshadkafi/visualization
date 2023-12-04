import numpy as np

def calculate_angle(x1, y1, x2, y2):
    # Calculate the differences in x and y coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the angle using arctangent (in radians)
    angle_rad = np.arctan2(dy, dx)

    # Convert angle from radians to degrees
    angle_deg = np.degrees(angle_rad)

    # Ensure the angle is between 0 and 360 degrees
    # angle_deg = (angle_deg + 360) % 360

    return angle_deg

# Example points
x1, y1 = 0, 0
x2, y2 = 1, 1

# Calculate the angle between the two points
angle = calculate_angle(x1, y1, x2, y2)
print(f"The angle between the two points is: {angle} degrees")
