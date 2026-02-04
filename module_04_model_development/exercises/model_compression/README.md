# Exercise: Model Compression

**Objective**: Prune a PyTorch layer.

## 📝 Steps

1. Import `torch.nn.utils.prune`.
2. Define a linear layer.
3. Apply L1 Unstructured pruning to remove 30% of connections.
4. Check `layer.weight` to see zeros.
5. Make the pruning permanent.

```python
import torch
import torch.nn as nn
import torch.nn.utils.prune as prune

layer = nn.Linear(5, 5)
print("Original Weights:", layer.weight)

# TODO: Prune 30%
# prune.l1_unstructured...

# TODO: Remove mask
# prune.remove...
```
