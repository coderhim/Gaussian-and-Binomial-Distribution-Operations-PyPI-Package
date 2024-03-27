import numpy as np

def linear_schedule(current_step, total_steps):
    """Linear schedule for adjusting noise level."""
    return 1 - current_step / total_steps

def cosine_schedule(current_step, total_steps):
    """Cosine schedule for adjusting noise level."""
    return 0.5 * (1 + np.cos(current_step * np.pi / total_steps))
