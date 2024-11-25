# Weighted Average Calculator

This project implements a Python class `WeightedAverage` to calculate the weighted average of a signal using a list of predefined weights.

## How It Works

1. **Initialization**:

   - The class is initialized with a list of weights. The number of weights determines how many signal values can be stored and processed.

2. **Signal Storage**:

   - Incoming signal values are stored in a list.
   - If the number of signal values exceeds the number of weights, the oldest value is removed to maintain a fixed size.

3. **Weighted Average Calculation**:
   - Each stored signal value is multiplied by its corresponding weight.
   - The sum of the weighted values is divided by the total number of weights to compute the average.

## Usage

### Creating an Instance

To use the `WeightedAverage` class, initialize it with a list of weights.

# Example

## Example Weights and Signal

```python
w = [5, 4, 3, 2, 1]  # Weights for the weighted average
signal = [1, 2, 3, 4, 5]  # Signal values
```

## Initialize the WeightedAverage class with the weights

```python
w_ave = WeightedAverage(w)
```

## Add new signal values and calculate the weighted average

```python
print(w_ave.process(signal[0]))  # Output after processing 1
print(w_ave.process(signal[1]))  # Output after processing 2
print(w_ave.process(signal[2]))  # Output after processing 3
print(w_ave.process(signal[3]))  # Output after processing 4
print(w_ave.process(signal[4]))  # Output after processing 5
```

outputs:

```python
1.0
2.6
4.4
6.0
7.0
```
