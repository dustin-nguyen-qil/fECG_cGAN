# Fetal ECG Extraction on Time-Frequency Domain using Pix2Pix GAN

### The presentation of the project can be watched [here](https://youtu.be/UaDcA1xhbZI)

This repository contains code and data for implementing a method to extract fetal electrocardiogram (ECG) signals from a maternal ECG signal on the time-frequency domain using Pix2Pix GAN.

## 1 Background

Fetal ECG extraction from maternal ECG signals is important in clinical settings, as it can provide crucial information about fetal health. However, fetal ECG signals are typically much weaker than maternal ECG signals, making it challenging to extract them directly from the raw signal. 

## 2 Method

In this repository, we present a method for fetal ECG extraction on the time-frequency domain using Pix2Pix GAN. We train Pix2Pix to learn the mapping between maternal ECG spectrograms (domain A) and corresponding fetal ECG spectrograms (domain B). During testing, we apply the trained Pix2Pix to a maternal ECG spectrogram to obtain the corresponding fetal ECG spectrogram.

## 3 Running instructions

### 3.1 Getting started

#### Create virtual environment

First, create a virtual environment for the repository
```bash
$ conda create -n fecg python=3.8
```
then activate the environment 
```bash
$ conda activate fecg
```


#### Clone the repository

Download or clone the repository:

```bash
$ git clone https://github.com/dustin-nguyen-qil/fECG_cGAN.git
```
Next, install the dependencies by running
...
```bash
$ pip install -r requirements.txt
```

### 3.2 Data Preparation

#### Dataset 
- Download the spectrograms generated from Abdominal and Direct dataset from [here](https://uofh-my.sharepoint.com/:u:/g/personal/dnguy222_cougarnet_uh_edu/EftKBDNDgtlCmx4PClYJcogB42zOuQZOmCdeH9F2rOd_Ug?e=wgu81y)
- Unzip the data, put into folder `data` as following
```
data
---> adbecg
---> ...
```

Pix2Pix requires to align the data for pairs of training images 
```bash
$ python datasets/combine_A_and_B.py --fold_A data/adbecg/spectrogram/A --fold_B data/adbecg/spectrogram/A --fold_AB datasets/adbecg
```

### 3.3 Training Pix2Pix

Run the following command for training

```bash
$ python train.py --dataroot ./datasets/adbecg --name fecg_p2p --model pix2pix --direction AtoB
```

Training results will be saved in `checkpoints`. To see more intermediate results, check out `./checkpoints/fecg_p2p/web/index.html`

### 3.3 Testing Pix2Pix

Run the following command for testing

```bash
$ python test.py --dataroot ./datasets/adbecg --name fecg_p2p --model pix2pix --direction AtoB
```

The test results will be saved to a html file here: `./results/fecg_p2p/test_latest/index.html`.

To see comparison results with Conventional Method, refer to `evaluate.ipynb` to directly see the results.
If you want to run the code cells again, download the fECG spectrograms produced by conventional method from [here](https://uofh-my.sharepoint.com/:u:/g/personal/dnguy222_cougarnet_uh_edu/EQ2o2injDp9BjFag7zLFeoMB76fMKRBU3bFRsY85vkhi-Q?e=2A3MeZ). Then unzip and put the data into

```
results
---> fecg_p2p
    ---> spectrogram_conventional
    ---> test_latest
```

## Acknowledgement

This repository was based on the following repository: [Pix2PixGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). We would like to thank the authors for a contributing work.

