# Code to create visualizations
import numpy as np
import matplotlib.pyplot as plt

def plot_cumulative_gain(y_test, y_scores, model_name, ax):
    # Ensure y_test and y_scores are numpy arrays
    y_test_array = np.array(y_test)
    y_scores_array = np.array(y_scores)

    # Total number of positives
    total_positives = np.sum(y_test_array)

    # Get the indices that would sort the scores
    sorted_indices = np.argsort(y_scores_array)[::-1]

    # Sort the actual values based on the indices
    sorted_y_test = y_test_array[sorted_indices]

    # Calculate cumulative sum of the true positives
    cum_true_positives = np.cumsum(sorted_y_test)

    # Calculate cumulative gain
    cumulative_gain = cum_true_positives / total_positives

    # Normalize cumulative gain for the y-axis
    cumulative_gain *= 100

    # Calculate the percentage of samples reviewed
    percent_sampled = np.linspace(0.01, 100, len(cumulative_gain))

    # Plotting
    ax.plot(percent_sampled, cumulative_gain, label=f'{model_name}')

    return cumulative_gain, percent_sampled


def plot_lift_curve(y_test, y_scores, model_name, ax, cumulative_gain, percent_sampled):
    baseline = np.maximum(percent_sampled, 0.1)  # Avoid division by zero or very low values
    cumulative_gain = np.maximum(cumulative_gain, 0.1)
    lift = cumulative_gain / baseline
    ax.plot(percent_sampled, lift, label=f'{model_name} Lift')
    ax.set_xlabel('Percentage of Population targeted')
    ax.set_ylabel('Lift')
    ax.set_title('Lift Curve')
    ax.legend()
    ax.grid(True)
