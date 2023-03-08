import pyedflib
import numpy as np
from scipy import signal
from scipy.signal import butter, filtfilt
from sklearn.decomposition import FastICA
from sklearn.preprocessing import scale
import padasip as pa

class DataUtils:

    def __init__(self) -> None:
        self.dataset = ["adbecg/", "nifecg/", "synt_ecg/"]
        self.record = '/RECORDS' # each dataset has a RECORDs file which contains file names
    """
    Read data from edf files. 3 Datasets contains:
    - Abdominal and Direct ECG: 5 signal files, each file contains:
        - referenced fetal signals
        - 4 channels of abdominal signals

    - Non-Invasive Fetal ECG: each recording contains:
        - 2 thoracic signals
        - 3 or 4 abdominal signals

    - Synthesized dataset: to be updated
    """
    def readData(self, dataset, path='data/'):
        dataset_path = path + dataset
        # if dataset == 'adbecg':
        fileNames = dataset_path + self.record 
        with open(fileNames, 'rb') as f:
            files = f.readlines()
        for file in files:
            signal_path = dataset_path + file[:-1]
            f = pyedflib.EdfReader(file_name)
            n = f.signals_in_file
    
            adbECG = np.zeros((n-1, f.getNSamples()[0]))
            fetalECG = np.zeros((1, f.getNSamples()[0]))
            fetalECG[0, :] = f.readSignal(0)
            fetalECG[0, :] = scale(self.butter_bandpass_filter(fetalECG, 1, 100, 1000), axis=1)
            for i in np.arange(1, n):
                adbECG[i - 1, :] = f.readSignal(i)
    
            adbECG = scale(self.butter_bandpass_filter(adbECG, 1, 100, 1000), axis=1)
            adbECG = signal.resample(adbECG, int(adbECG.shape[1] / 5), axis=1)
            fetalECG = signal.resample(fetalECG, int(fetalECG.shape[1] / 5), axis=1)
            return adbECG, fetalECG
            
    def windowingSig(self, sig1, sig2, windowSize = 15):
        signalLen = sig2.shape[1]
        signalWindow1 = [sig1[:, int(i):int(i+windowSize)].transpose() for i in range(0, signalLen - windowSize, windowSize)]
        signalWindow2 = [sig2[:, int(i):int(i+windowSize)].transpose() for i in range(0, signalLen - windowSize, windowSize)]
        return signalWindow1, signalWindow2

    def adaptFilter(self, src, ref):
        f = pa.filters.FilterNLMS(n=3, mu=0.1, w='random')
        for index, sig in enumerate(src):
            try:
                y, e, w = f.run(ref[index][:, 0], sig)
                ref[index][:, 0] = e
            except:
                pass
        return ref
    
    def calICA(self, sdSig, component=7):
        ica = FastICA(n_components=component, max_iter=1000)
        icaRes = []
        for index, sig in enumerate(sdSig):
            try:
                icaSignal = np.array(ica.fit_transform(sig))
                icaSignal = np.append(icaSignal, sig[:, range(2, 4)], axis=1)
                icaRes.append(icaSignal)
            except:
                pass
        return np.array(icaRes)

    def createDelayRepetition(self, signal, numberDelay=4, delay=10):
        signal = np.repeat(signal, numberDelay, axis=0)
        for row in range(1, signal.shape[0]):
            signal[row, :] = np.roll(signal[row, :], shift=delay*row)
        return signal

    def __butter_bandpass(self, lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a
    
    def butter_bandpass_filter(self, data, lowcut, highcut, fs, order=3, axis=1):
        b, a = self.__butter_bandpass(lowcut, highcut, fs, order=order)
        y = filtfilt(b, a, data, axis=axis)
        return y

