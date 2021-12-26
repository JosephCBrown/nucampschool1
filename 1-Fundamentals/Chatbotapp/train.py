import json
from nltk_utils import tokenize, stem, list_of_words
import numpy as np

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from model import NeuralNetwork

with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['?', '!', '.', ',']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

# ---Test that tags is working dont need--- print(tags)

X_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    bag = list_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)  # CrossEntropyLoss Dont need 1 hot endcodding here

X_train = np.array(X_train)
y_train = np.array(y_train)


class ChatDatset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    # allows you to access dataset[idx]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples


# Hyperparameters
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(X_train[0])
""" ----Test that Nueral Network is working---- 
print(input_size, len(all_words))
print(output_size,tags) """
dataset = ChatDatset()
train_loader = DataLoader(
    dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=2)  # if trouble set num_workers to 0

model = NeuralNetwork(input_size, hidden_size, output_size)
