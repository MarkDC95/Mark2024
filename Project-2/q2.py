import numpy as np
import matplotlib.pyplot as plt


class WeightedAverage:
    def __init__(self, w: list[float]):
        """Initialize with a list of weights."""
        self.weights = w  # Weights
        self.n = len(w)   # Number of samples (length of weights)
        self.x = []       # Store input signal values

    def process(self, x: float) -> float:
        """Calculate the weighted average of a signal."""
        # add the new value of x to the list to store the signal
        self.x.append(x)

        # If we have more than 'n' samples, remove the excess input samples
        if len(self.x) > self.n:
            self.x.pop()  # Remove the oldest sample

        # Calculate the weighted sum (using only available samples)
        WeightedSum = 0
        for index in range(len(self.x)):  # Loop only through available signal values
            WeightedSum += self.weights[index] * self.x[index]

        # Return the weighted average
        return WeightedSum / self.n


# Weights for moving average (equal weights)
weights = [1]*5

# Create an instance of WeightedAverage
weighted_avg = WeightedAverage(weights)

# Generate a # 1 Hz sine wave signal
sampling_rate = 1000  # 1000 samples per second
duration = 2  # 2 seconds
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
signal = np.sin(2 * np.pi * 1 * t)

# Process the sine wave and store the results
n_iterations = 10
for i in range(n_iterations):
    output = weighted_avg.process(signal[i])
    print(f"weighted average output = {output}")

# # Example Weights and Signal
# w = [5, 4, 3, 2, 1]  # Weights for the weighted average
# signal = [1, 2, 3, 4, 5]  # Signal values

# # Create the WeightedAverage instance with the weights
# wa = WeightedAverage(w)

# # Process the signal values and print the outputs
# for x in signal:
#     output = wa.process(x)
#     print(output)
