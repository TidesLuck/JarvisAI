import torch
import torch.nn as nn

class VisionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 64, kernel_size=3)
        self.fc = nn.Linear(64, 512)

    def forward(self, x):
        x = self.conv(x)
        return self.fc(x.flatten(1))