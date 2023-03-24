import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from utils.DataUtils import DataUtils
from Processing import spectrogram

def main():
  data = ['adbecg', 'nifecg', 'synt_ecg']
  data_utils = DataUtils()

  # # ADBECG
  adbecg = data_utils.get_data(dataset='adbecg')
  # # # NIFECG
  nifecg = data_utils.get_data(dataset='nifecg')
  # # SYNT_ECG
  synt_ecg = data_utils.get_data(dataset='synt_ecg')
  
  fs = 1000  # 1000Hz sampling frequency
  segment_size = int(0.25 * fs)  # 250ms segment size
  overlap_size = int(0.01 * fs)  # 10ms overlap size
  window = signal.get_window('hamming', segment_size)  # Hamming window
  time_axis = np.arange(0, segment_size) / fs

  
  for record in adbecg:
    record_signal = data_utils.open_record(record)
    for chn in range(0, len(record_signal.getSampleFrequencies())):
      print('Reading channel: {}'.format(record_signal.getSignalLabels()[chn]))
      _signal = record_signal.readSignal(chn)
      
      segments = []
      segments_index = 0
      for i in range(0, len(_signal) - segment_size, segment_size - overlap_size):
        segments.append(_signal[i:i+segment_size] * window)
        plt.specgram(segments[0], Fs=1000, window=window, noverlap=overlap_size, NFFT=250)  # 250ms segment size
        plt.savefig(f"{record}_{record_signal.getSignalLabels()[chn]}_{segments_index}.png")
        segments_index += 1

if __name__ == '__main__':
  main()