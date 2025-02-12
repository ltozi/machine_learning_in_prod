import tarfile
# # Extract the compressed models (Not needed in the Coursera environment)
compressed_models = ['imbalanced_model.tar.gz', 'balanced_model.tar.gz', 'augmented_model.tar.gz']

for compressed_model in compressed_models:
    with tarfile.open(f'{MODEL_DIR}/{compressed_model}', 'r') as my_tar:
      my_tar.extractall(MODEL_DIR)
