from scipy import signal
import numpy as np
from SignalPreProcessor import normalize
 

def spectrogram(_signal, fs, window='hamming', nperseg=250, noverlap=10, nfft=250):
  f, t, Sxx = signal.spectrogram(normalize(_signal), fs, window=window, nperseg=nperseg, 
                                 noverlap=noverlap, nfft=nfft)
  return f, t, Sxx
