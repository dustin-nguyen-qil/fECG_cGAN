
import numpy as np

def normalize(signal):
  return 2 * (signal - np.min(signal)) / (np.max(signal) - np.min(signal)) - 1
    
    