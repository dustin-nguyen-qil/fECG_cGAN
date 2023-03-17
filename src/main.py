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
  window = signal.windows.hamming(segment_size)  # Hamming window

  for record in nifecg:
    record_signal = data_utils.open_record(record)
    for chn in range(0, len(record_signal.getSampleFrequencies())):
      print('Reading channel: {}'.format(record_signal.getSignalLabels()[chn]))
      _signal = record_signal.readSignal(chn)

      f, t, Sxx = spectrogram(_signal, fs=1000, window=window, nperseg=segment_size, noverlap=overlap_size, 
                              nfft=segment_size)
      
      plt.pcolormesh(t, f, np.log10(Sxx))

      plt.savefig(f"{record}_{record_signal.getSignalLabels()[chn]}.png")
      
if __name__ == '__main__':
  main()