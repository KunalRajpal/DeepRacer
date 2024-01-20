import math


def reward_function(params):
    # Reward weights
    speed_weight = 100
    heading_weight = 100
    steering_weight = 50
    progress_weight = 1  # Adjust this weight as needed

    # Speed reward
    max_speed = 10
    min_speed = 3.33
    speed = params["speed"]
    speed_reward = (speed - min_speed) / (max_speed - min_speed) * speed_weight

    # Penalty for going off track
    if not params["all_wheels_on_track"]:
        return 1e-3

    # Calculate track direction
    next_point = params["waypoints"][params["closest_waypoints"][1]]
    prev_point = params["waypoints"][params["closest_waypoints"][0]]
    track_direction = math.atan2(
        next_point[1] - prev_point[1], next_point[0] - prev_point[0]
    )
    track_direction = math.degrees(track_direction)

    # Calculate heading difference
    direction_diff = abs(track_direction - params["heading"])
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Heading reward
    heading_reward = (180 - direction_diff) / 180.0 * heading_weight

    # Steering reward
    steering_diff = abs(params["steering_angle"] - direction_diff)
    steering_reward = (180 - steering_diff) / 180.0 * steering_weight

    # Progress reward
    progress_reward = params["progress"] * progress_weight

    # Total reward
    total_reward = speed_reward + heading_reward + steering_reward + progress_reward

    return total_reward
