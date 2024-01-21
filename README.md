# AWS Deep Racer Competition

## Reward Function

The reward function is a Python function named reward_function that takes a single argument params. 
This argument is a dictionary containing various parameters related to the vehicle's state and the track environment.

### Parameters

- **speed:**               The vehicle's current speed
- **all_wheels_on_track:** Boolean indicating if the vehicle has all wheels on the track
- **waypoints:**           List of points defining the track center. Each waypoint is a list of two coordinates [x, y]
- **closest_waypoints:**   Tuple of two integers representing the indices in waypoints of the two nearest waypoints
- **heading:**             The vehicle's heading in degrees between -180 and 180
- **steering_angle:**      The current steering angle in degrees

### Reward Calculation

- **Speed Reward:**      Encourages the vehicle to maintain a speed between a specified minimum (min_speed) and maximum (max_speed). The reward increases linearly with speed within this range
- **Off-Track Penalty:** A minimal reward is returned if all_wheels_on_track is False, penalizing the vehicle for going off-track
- **Heading Reward:**    Rewards the vehicle for aligning its heading with the direction of the track. The closer the vehicle's heading to the track direction, the higher the reward
- **Steering Reward:**   Rewards the vehicle for steering alignment with the direction difference. This encourages smoother turns
- **Progress Reward:**   Based on the progress parameter, which indicates how much of the track has been completed. This rewards the vehicle for moving forward along the track
- **Total Reward:**      The final reward is a sum of the speed, heading, steering, and progress rewards

### Reward Weights

- **speed_weight:**    Weight for the speed reward component
- **heading_weight:**  Weight for the heading reward component
- **steering_weight:** Weight for the steering reward component
- **progress_weight:** Weight for the progress reward component

### Additional Calculations

- **Track Direction Calculation:** Computes the direction of the track at the vehicle's current position.
- **Direction Difference:**        The absolute difference between the track direction and the vehicle's heading.
- **Steering Difference:**         The absolute difference between the steering angle and the direction difference.

## Action Space

![Action Space](images/action_space.png)

| Action No. #| Steering Angle (°) | Speed (m/s)|
| :---------- | :-----------:      | ----------:|
| 0           | 0.0                | 4.00       |
| 1           | 0.0                | 3.00       |
| 2           | 0.0                | 2.00       |
| 3           | 0.0                | 1.00       |
| 4           | 15.0               | 2.50       |
| 5           | -15.0              | 2.50       |
| 6           | 15.0               | 1.00       |
| 7           | -15.0              | 1.00       |
| 8           | 30.0               | 1.00       |
| 9           | -30.0              | 1.00       |

## Hyperparameter Values

| Hyperparameter                                                       | Value  |
| :----------                                                          | ------:|
| Gradient descent batch size                                          | 64     |
| Entropy                                                              | 0.01   |
| Discount factor                                                      | 0.985  |
| Loss type                                                            | Huber  |
| Learning rate                                                        | 0.0004 |
| Number of experience episodes between each policy-updating iteration | 30     |
| Number of epochs                                                     | 3      |

## Evaluation Results

| Trial |     Time    | Trial results |   Status      |    Off-track | Off-track penalty |  Crashes |  Crash penalty |
| :---- | :-----:     | :---------:   | :-----------: | :-----------:|:---------------:  |:-------: |---------------:|
| 1     | 00:10.727   |100%           |  Lap complete |  0           | --                | 0        | --             |
| 2     | 00:11.473   | 100%          |  Lap complete |  0           | --                | 0        | --             |
| 3     | 00:11.933   | 100%          |  Lap complete |  0           | --                | 0        | --             |

## Competition Details

Held at RRC Polytechnic in winnipeg, Manitoba on September 21, 2023
[click here for more information](https://winnipeg.ctvnews.ca/why-rrc-polytech-students-are-racing-miniature-cars-1.6573439)
