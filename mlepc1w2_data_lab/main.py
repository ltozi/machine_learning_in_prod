import os
import gc
import tarfile
import numpy as np
import pickle
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, balanced_accuracy_score
import lab_utils
import tensorflow as tf
from IPython.display import Image, display


# Filename of the downloaded dataset archive
DATASET_COMPRESSED = './cats_dogs_birds.tar.gz'

# Base directory for extracting and preparing the dataset
DATA_DIR = '/tmp/data'

# Base directory for extracting the pretrained models
MODEL_DIR = './models'

# Name of the classes to predict
ANIMALS = ['dogs', 'cats', 'birds']

# Directories for the training and dev sets
TRAIN_DIRS = ['train/dogs', 'train/cats', 'train/birds']
DEV_DIRS = ['dev/dogs', 'dev/cats', 'dev/birds']

# Imbalanced portion of images among the 3 classes
PORTIONS = [0.2, 1, 0.1]

#compressed_models = ['imbalanced_model.tar.gz', 'balanced_model.tar.gz', 'augmented_model.tar.gz']

#for compressed_model in compressed_models:
#    with tarfile.open(f'{MODEL_DIR}/{compressed_model}', 'r') as my_tar:
#      my_tar.extractall(MODEL_DIR)

# Extract the dataset
#with tarfile.open(DATASET_COMPRESSED, 'r') as my_tar:
#  my_tar.extractall(DATA_DIR)

os.listdir(DATA_DIR)

os.listdir(f'{DATA_DIR}/images')

base_dogs_dir = os.path.join(DATA_DIR, 'images/dog')
base_cats_dir = os.path.join(DATA_DIR,'images/cat')
base_birds_dir = os.path.join(DATA_DIR,'images/bird')
base_image_dirs = [base_dogs_dir, base_cats_dir, base_birds_dir]

for animal, base_image_dir in zip(ANIMALS, base_image_dirs):
    print(f"There are {len(os.listdir(base_image_dir))} images of {animal}")

print("Sample cat image:")
display(Image(filename=f"{os.path.join(base_cats_dir, os.listdir(base_cats_dir)[0])}"))
print("\nSample dog image:")
display(Image(filename=f"{os.path.join(base_dogs_dir, os.listdir(base_dogs_dir)[0])}"))
print("\nSample bird image:")
display(Image(filename=f"{os.path.join(base_birds_dir, os.listdir(base_birds_dir)[0])}"))


for dir in TRAIN_DIRS:
    os.makedirs(os.path.join(DATA_DIR, dir), exist_ok=True)
    
for dir in DEV_DIRS:
    os.makedirs(os.path.join(DATA_DIR, dir), exist_ok=True)
