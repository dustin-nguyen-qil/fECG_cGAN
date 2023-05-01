import os, shutil
import os.path as osp
<<<<<<< HEAD
import random, json
=======
import random
>>>>>>> d0f2cf758b53c7b011b716dbfe84a3a9692217ad
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

<<<<<<< HEAD
data_dir = "../adbecg/spectrogram"
=======
>>>>>>> d0f2cf758b53c7b011b716dbfe84a3a9692217ad
r01_path = "../adbecg/spectrogram/r01"
r04_path = "../adbecg/spectrogram/r04"
r07_path = "../adbecg/spectrogram/r07"
r08_path = "../adbecg/spectrogram/r08"
r10_path = "../adbecg/spectrogram/r10"

<<<<<<< HEAD
records = [r01_path, r04_path, r07_path, r08_path, r10_path]
A_path = "../adbecg/spectrogram/A"
B_path = "../adbecg/spectrogram/B"

for file in os.listdir(data_dir):
    file_path = osp.join(data_dir, file)
    if file.startswith("r01_edf_Abdomen") or file.startswith("r01_edf_Direct"):
        shutil.move(file_path, osp.join(r01_path, file))
    if file.startswith("r02_edf_A") or file.startswith("r02_edf_D"):
        shutil.move(file_path, osp.join(r04_path, file))
    if file.startswith("r03_edf_A") or file.startswith("r03_edf_D"):
        shutil.move(file_path, osp.join(r07_path, file))
    if file.startswith("r04_edf_A") or file.startswith("r04_edf_D"):
        shutil.move(file_path, osp.join(r08_path, file))
    if file.startswith("r05_edf_A") or file.startswith("r05_edf_D"):
        shutil.move(file_path, osp.join(r10_path, file))

# loop through all files in the  subfolder
for record in records:
    record_name = record.split('/')[-1]
    for filename in os.listdir(record):
        if filename.startswith(f"{record_name}_edf_Direct_1"):
=======
paths = [r01_path, r04_path, r07_path, r08_path, r10_path]
record_names = ['r01', 'r04', 'r07', 'r08', 'r10']

A_path = "../adbecg/spectrogram/A"
B_path = "../adbecg/spectrogram/B"
# loop through all files in the  subfolder
for path in paths:
    record_name = path.split('/')[-1]
    for filename in os.listdir(path):
        if filename.startswith(f"{record_name}.edf_Direct_1"):
>>>>>>> d0f2cf758b53c7b011b716dbfe84a3a9692217ad
            # create the new filenames
            filename_2 = filename.replace("Direct_1", "Direct_2")
            filename_3 = filename.replace("Direct_1", "Direct_3")
            filename_4 = filename.replace("Direct_1", "Direct_4")

            # create the full paths to the source and destination files
<<<<<<< HEAD
            src_file = os.path.join(record, filename)
            dest_file_2 = os.path.join(record, filename_2)
            dest_file_3 = os.path.join(record, filename_3)
            dest_file_4 = os.path.join(record, filename_4)
=======
            src_file = os.path.join(path, filename)
            dest_file_2 = os.path.join(path, filename_2)
            dest_file_3 = os.path.join(path, filename_3)
            dest_file_4 = os.path.join(path, filename_4)
>>>>>>> d0f2cf758b53c7b011b716dbfe84a3a9692217ad

            # create copies of the source file with the new filenames
            shutil.copy2(src_file, dest_file_2)
            shutil.copy2(src_file, dest_file_3)
            shutil.copy2(src_file, dest_file_4)

<<<<<<< HEAD
for record in records:
    record_name = record.split('/')[-1]
    for filename in os.listdir(record):
        if filename.startswith(f"{record_name}_edf_Abdomen"):
            # create the full paths to the source and destination files
            src_file = os.path.join(record, filename)
=======

for path in paths:
    record_name = path.split('/')[-1]
    for filename in os.listdir(path):
        if filename.startswith(f"{record_name}.edf_Abdomen"):
            # create the full paths to the source and destination files
            src_file = os.path.join(path, filename)
>>>>>>> d0f2cf758b53c7b011b716dbfe84a3a9692217ad
            dest_file = os.path.join(A_path, filename)

            # copy the file to folder A
            shutil.copy2(src_file, dest_file)

<<<<<<< HEAD
        if filename.startswith(f"{record_name}_edf_Direct"):
            # create the full paths to the source and destination files
            src_file = os.path.join(record, filename)
=======
        if filename.startswith(f"{record_name}.edf_Direct"):
            # create the full paths to the source and destination files
            src_file = os.path.join(path, filename)
>>>>>>> d0f2cf758b53c7b011b716dbfe84a3a9692217ad
            dest_file = os.path.join(B_path, filename)

            # copy the file to folder B
            shutil.copy2(src_file, dest_file)

<<<<<<< HEAD

# loop through all files in the folder
for record in records:
    record_name = record.split('/')[-1]
    for filename in os.listdir(B_path):
        if filename.startswith(f"{record_name}_edf_Direct"):
            # create the full paths to the source and destination files
            src_file = os.path.join(B_path, filename)
            dest_file = os.path.join(B_path, filename.replace(f"{record_name}_edf_Direct", f"{record_name}_edf_Abdomen"))
=======
# loop through all files in the folder
for record_name in record_names:
    for filename in os.listdir(B_path):
        if filename.startswith(f"{record_name}.edf_Direct"):
            # create the full paths to the source and destination files
            src_file = os.path.join(B_path, filename)
            dest_file = os.path.join(B_path, filename.replace(f"{record_name}.edf_Direct", f"{record_name}.edf_Abdomen"))
>>>>>>> d0f2cf758b53c7b011b716dbfe84a3a9692217ad

            # rename the file
            os.rename(src_file, dest_file)

# create sets of filenames for each folder
A_set = set(os.listdir(A_path))
B_set = set(os.listdir(B_path))

# find the common filenames
common_files = A_set.intersection(B_set)

# remove the unmatched files from folder A
for filename in A_set - common_files:
    os.remove(os.path.join(A_path, filename))
<<<<<<< HEAD
    print(f"Removed {filename} from folder A.")
=======
    # print(f"Removed {filename} from folder A.")
>>>>>>> d0f2cf758b53c7b011b716dbfe84a3a9692217ad

# remove the unmatched files from folder B
for filename in B_set - common_files:
    os.remove(os.path.join(B_path, filename))
<<<<<<< HEAD
    print(f"Removed {filename} from folder B.")

for folder in [A_path, B_path]:
    train_path = osp.join(folder,"train")
    val_path = osp.join(folder,"test")
    test_path = osp.join(folder,"val")

    # create lists to hold the filenames for each set
    all_files = os.listdir(folder)
    all_files.remove('train')
    all_files.remove('val')
    all_files.remove('test')
    num_files = len(all_files)
    train_size = int(0.8 * num_files)
    val_size = int(0.1 * num_files)
    test_size = num_files - train_size - val_size

    # random.shuffle(all_files)

    train_files = all_files[:train_size]
    val_files = all_files[train_size:train_size+val_size]
    test_files = all_files[train_size+val_size:]

    # loop through the filenames for each set and move the files to the corresponding folder
    for filename in train_files:
        src_file = os.path.join(folder, filename)
        dest_file = os.path.join(train_path, filename)
        shutil.move(src_file, dest_file)

    for filename in val_files:
        src_file = os.path.join(folder, filename)
        dest_file = os.path.join(val_path, filename)
        shutil.move(src_file, dest_file)

    for filename in test_files:
        src_file = os.path.join(folder, filename)
        dest_file = os.path.join(test_path, filename)
        shutil.move(src_file, dest_file)

print("Done moving spectrograms .")

=======
    # print(f"Removed {filename} from folder B.")

train_path = osp.join(A_path,"train")
val_path = osp.join(A_path,"test")
test_path = osp.join(A_path,"val")

# create lists to hold the filenames for each set
all_files = os.listdir(A_path)
all_files.remove('train')
all_files.remove('val')
all_files.remove('test')
num_files = len(all_files)
train_size = int(0.8 * num_files)
val_size = int(0.1 * num_files)
test_size = num_files - train_size - val_size

# random.shuffle(all_files)

train_files = all_files[:train_size]
val_files = all_files[train_size:train_size+val_size]
test_files = all_files[train_size+val_size:]

# loop through the filenames for each set and move the files to the corresponding folder
for filename in train_files:
    src_file = os.path.join(A_path, filename)
    dest_file = os.path.join(train_path, filename)
    shutil.move(src_file, dest_file)

for filename in val_files:
    src_file = os.path.join(A_path, filename)
    dest_file = os.path.join(val_path, filename)
    shutil.move(src_file, dest_file)

for filename in test_files:
    src_file = os.path.join(A_path, filename)
    dest_file = os.path.join(test_path, filename)
    shutil.move(src_file, dest_file)


# define the folder containing the images
folder_path = B_path

# traverse all subdirectories using os.walk
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # check if file is an image
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
            # open the image
            img_path = os.path.join(root, file)
            img = Image.open(img_path)

            # remove alpha channel
            if img.mode == 'RGBA':
                img = img.convert('RGB')

            # save the image with original name
            img.save(img_path)

print("Done preparing spectrograms!")
>>>>>>> d0f2cf758b53c7b011b716dbfe84a3a9692217ad
