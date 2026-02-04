# Exercise: ONNX Conversion

**Objective**: Export ResNet18 to ONNX.

## 📝 Steps

1. Import `torchvision.models`.
2. Load a pre-trained ResNet18.
3. Create a dummy input `torch.randn(1, 3, 224, 224)`.
4. Export to `resnet.onnx`.

```python
import torch
import torchvision

model = torchvision.models.resnet18(pretrained=True)
model.eval()

# TODO: Export
# torch.onnx.export(...)
```
