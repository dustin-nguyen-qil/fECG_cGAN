import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from utils.DataUtils import DataUtils
from Processing import spectrogram
import os
import json
from SignalPreProcessor import normalize

from typing import List

# def segment_signal(_signal: np.ndarray, segment_size: int, overlap_size: int) -> List[np.ndarray]:
#     segments = []
#     step = segment_size - overlap_size * 2
#     for i in range(0, len(_signal) - segment_size + 1, step):
#         segment = _signal[i:i+segment_size]
#         segments.append(segment.tolist())
#     return segments

def segment_signal(signal, segment_size, overlap_size):
    """
    Segments a given signal into non-overlapping segments of size `segment_size`, with
    overlap of size `overlap_size` between consecutive segments.
    
    Args:
        signal (ndarray): the signal to be segmented
        segment_size (int): the size of each segment
        overlap_size (int): the size of the overlap between consecutive segments
        
    Returns:
        list: a list of the segmented signal, where each element is a numpy array
        representing a segment of the signal.
    """
    signal_length = signal.shape[0]
    segments = []
    start_idx = 0
    end_idx = segment_size
    while end_idx <= signal_length:
        segment = signal[start_idx:end_idx]
        segments.append(segment.tolist())
        start_idx += segment_size - overlap_size
        end_idx = start_idx + segment_size
    return segments

def main():
    data = ['adbecg', 'nifecg', 'synt_ecg']
    data_utils = DataUtils()
     # # # NIFECG
    # nifecg = data_utils.get_data(dataset='nifecg')
    # # SYNT_ECG
    # synt_ecg = data_utils.get_data(dataset='synt_ecg')
 
    # # ADBECG
    adbecg = data_utils.get_data(dataset='adbecg')

    fs = 1000  # 1000Hz sampling frequency
    
    segment_size = int(0.27 * fs)  # 250ms segment size
    overlap_size = int(0.01 * fs)  # 10ms overlap size
    window = signal.get_window('hamming', segment_size)  # Hamming window
    time_axis = np.arange(0, segment_size) / fs

    data = {} 

    for record in adbecg:
        record_id = (record.split('/')[-1][1:3])
        data[record_id] = []
        print(f"Reading record {record_id}")
        record_signal = data_utils.open_record(record)

        for chn in range(0, len(record_signal.getSampleFrequencies())):

            channel_name = record_signal.getSignalLabels()[chn]

            print('Reading channel: {}'.format(record_signal.getSignalLabels()[chn]))
            _signal = normalize(record_signal.readSignal(chn))
            segments = segment_signal(_signal, segment_size, overlap_size)
            
            data[record_id].append({'channel': channel_name, 'segments': segments})

    file_path = "data/preprocessing/segments.json"

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
  main()