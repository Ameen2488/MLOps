# Exercise: Weights & Biases Practice

**Objective**: Visualize training curves.

## 📝 Steps

1. Login: `wandb login --relogin`
2. Run the script below.
3. Check your dashboard for the Loss Curve.

```python
import wandb
import random

wandb.init(project="exercise-wandb")

for epoch in range(10):
    loss = 1.0 / (epoch + 1) + random.random() * 0.1
    wandb.log({"loss": loss, "epoch": epoch})
    
wandb.finish()
```
