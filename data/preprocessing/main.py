import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from utils.DataUtils import DataUtils
from Processing import spectrogram
import os
import json
from SignalPreProcessor import normalize

def main():
    data = ['adbecg', 'nifecg', 'synt_ecg']
    data_utils = DataUtils()

    # # ADBECG
    adbecg = data_utils.get_data(dataset='adbecg')
    # # # NIFECG
    # nifecg = data_utils.get_data(dataset='nifecg')
    # # SYNT_ECG
    # synt_ecg = data_utils.get_data(dataset='synt_ecg')
    
    fs = 1000  # 1000Hz sampling frequency
    
    segment_size = int(0.25 * fs)  # 250ms segment size
    overlap_size = int(0.01 * fs)  # 10ms overlap size
    window = signal.get_window('hamming', segment_size)  # Hamming window
    time_axis = np.arange(0, segment_size) / fs

    # data = {} # create an empty dictionary to store the segments for each record
    # metadata = [] # create an empty list to store the metadata for each record

    for record in adbecg:
        if record.endswith('r01.edf') or record.endswith('r04.edf'):
            continue
        record_id = (record.split('/')[-1][1:3])
        print(f"Reading record {record_id}")
        record_signal = data_utils.open_record(record)
        # record_segments = {record_id: {'abdominal': {}, 'fetal': {}}}

        for chn in range(0, len(record_signal.getSampleFrequencies())):
            if record.endswith('r07.edf'):
                if chn == 0:
                    continue
            channel_name = record_signal.getSignalLabels()[chn]
            print('Reading channel: {}'.format(record_signal.getSignalLabels()[chn]))
            _signal = normalize(record_signal.readSignal(chn))
            # _signal = np.interp(_signal, (_signal.min(), _signal.max()), (-1, 1))
            
            segments = []
            segments_index = 0
            for i in range(0, len(_signal) - segment_size, segment_size - overlap_size):
                segment = _signal[i:i+segment_size] * window
                # segments.append(segment)
                # segments.append(_signal[i:i+segment_size] * window)
                # spectrogram_path = os.path.join('/home/dustin/Documents/Research/FetalECG/Code/fECG_cGAN/data/adbecg', 'spectrograms', record_id, f"{channel_name}_{segments_index}.png")
                plt.specgram(segment, Fs=1000, window=window, noverlap=overlap_size, NFFT=250)
                # os.makedirs(os.path.dirname(spectrogram_path), exist_ok=True) # create the directory for the spectrogram
                # plt.savefig(spectrogram_path) # Save the spectrogram  # 250ms segment size
                plt.savefig(f"{record}_{record_signal.getSignalLabels()[chn]}_{segments_index}.png")
                segments_index += 1

    #             if chn == 0: # store the fetal spectrogram path for the current segment
    #                 record_segments[record_id]['fetal'][f"segment{segments_index}"] = spectrogram_path
    #             else: # store the abdominal spectrogram path for the current segment and add to metadata
    #                 record_segments[record_id]['abdominal'][channel_name] = spectrogram_path

    #                 if chn == len(record_signal.getSampleFrequencies()) - 1: # create the metadata entry for the current record
    #                     metadata.append({'record_id': record_id,
    #                                       'data_a': record_segments[record_id]['abdominal'],
    #                                       'data_b': record_segments[record_id]['fetal']})

    #             segments_index += 1
            
    #     data.update(record_segments) # add the record segments to the data dictionary

    # # save the metadata to a JSON file
    # with open('/home/dustin/Documents/Research/FetalECG/Code/fECG_cGAN/data/adbecg/metadata.js', 'w') as f:
    #     json.dump(metadata, f, indent=2)

if __name__ == '__main__':
  main()