# Fetal ECG Extraction on Time-Frequency Domain using Pix2Pix GAN

This repository contains code and data for implementing a method to extract fetal electrocardiogram (ECG) signals from a maternal ECG signal on the time-frequency domain using Pix2Pix GAN.

## 1 Background

Fetal ECG extraction from maternal ECG signals is important in clinical settings, as it can provide crucial information about fetal health. However, fetal ECG signals are typically much weaker than maternal ECG signals, making it challenging to extract them directly from the raw signal. One approach is to first convert the signal into the time-frequency domain using a spectrogram, and then use image processing techniques to extract the fetal ECG signal from the spectrogram.

## 2 Method

In this repository, we present a method for fetal ECG extraction on the time-frequency domain using Pix2Pix GAN. We train Pix2Pix to learn the mapping between maternal ECG spectrograms and corresponding fetal ECG spectrograms. During testing, we apply the trained Pix2Pix to a maternal ECG spectrogram to obtain the corresponding fetal ECG spectrogram, and then use image processing techniques to extract the fetal ECG signal from the spectrogram.

## 3 Running instructions

### 3.1 Getting started

#### Create virtual environment

First, create a virtual environment for the repository
```bash
$ conda create -n p2p python=3.8
```
then activate the environment 
```bash
$ conda activate p2p
```
...


#### Clone the repository

Download or clone the repository:

```bash
$ git clone https://github.com/dustin-nguyen-qil/fECG_cGAN.git
```

### 3.2 Data Preparation

#### Dataset download
- Download the Abdominal and Direct dataset from [here](https://physionet.org/content/adfecgdb/1.0.0/)
- Unzip the data, put into folder `data`

#### Generating spectrograms
Run the following command line to generate spectrograms 
```bash
$ python data/preprocessing/main.py
```
Then move the generated spectrograms to folder A and B for training Pix2Pix by running 
```bash
$ python data/prepare.py
```
Pix2Pix requires to align the data to each pair of images 
```bash
$ python datasets/combine_A_and_B.py --fold_A /path/to/data/A --fold_B /path/to/data/B --fold_AB /path/to/data
```

### 3.3 Training Pix2Pix

Run the following command for training

```bash
$ python train.py --dataroot ./datasets/adbecg --name fecg_p2p --model pix2pix --direction AtoB
```

Training results will be saved in `checkpoints`. To see more intermediate results, check out `./checkpoints/facades_pix2pix/web/index.html`

### 3.3 Testing Pix2Pix

Run the following command for testing

```bash
$ python test.py --dataroot ./datasets/adbecg --name fecg_p2p --model pix2pix --direction AtoB
```

The test results will be saved to a html file here: `./results/facades_pix2pix/test_latest/index.html`.



## Acknowledgement

This repository was based on the following repository: [Pix2PixGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). We would like to thank you the authors for a contributing work.

