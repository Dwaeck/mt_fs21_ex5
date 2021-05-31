# mt_fs21_ex5

This repo is just a collection of scripts showing how to install [JoeyNMT](https://github.com/joeynmt/joeynmt), download
data and train & evaluate models.

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

# Steps

Clone this repository in the desired place:

    git clone https://github.com/lucasseiler/mt_fs21_ex5

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Download and install required software:

    ./scripts/download_install_packages.sh
    
Download data:

    ./download_iwslt_2017_data.sh

Sub-sample the training data. Do this for both source and target language.

    python translation.py ./data/file > ./data/file_with_100k_sentence_pairs

Preprocess training, developing and testing files of both source and target language in order to learn a BPE model.

Use the following command to great a joint vocabulary for training a BPE model

    python tools/joeynmt/scripts/build_vocab.py preprocessed_data_of_source_language preprossed_data_of_target_language --output_path ./data/joint_vocabulary

Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Evaluate a trained model with

    ./scripts/evaluate.sh
