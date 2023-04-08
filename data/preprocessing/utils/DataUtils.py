import os
from wfdb import rdrecord
from wfdb.io.convert.edf import rdedfann, read_edf
from wfdb import Record
import pyedflib
import numpy as np

class DataUtils:

		def __init__(self, cache=False):
				self.data = ['adbecg', 'nifecg', 'synt_ecg']
				self.cache = cache

		def get_data(self, data_root='/home/dustin/Documents/Research/FetalECG/Code/fECG_cGAN/data', dataset='adbecg'):
			records_file = os.path.join(data_root, dataset, 'RECORDS')
			with open(records_file, 'r') as f:
				for line in f:
					line = line.strip()
					if line:
						yield os.path.join(data_root, dataset, line)

		def open_record(self, record) -> Record:
			filename, ext = os.path.splitext(record)
			if ext == '.edf':
				print('Reading edf file: {}'.format(record))
				record_signal = pyedflib.EdfReader(record)

				return record_signal
			else:
				print('Reading MIT file: {}'.format(record))

				return rdrecord(record)

