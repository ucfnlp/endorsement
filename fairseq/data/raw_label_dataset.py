# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import torch

from . import FairseqDataset
import numpy as np

class RawLabelDataset(FairseqDataset):

    def __init__(self, labels):
        super().__init__()
        self.labels = labels
        self._sizes = np.array([len(ex) for ex in self.labels])

    def __getitem__(self, index):
        return self.labels[index]

    def __len__(self):
        return len(self.labels)

    def collater(self, samples):
        return torch.tensor(samples)

    @property
    def sizes(self):
        return self._sizes
