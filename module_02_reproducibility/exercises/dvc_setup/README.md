# Exercise: DVC Setup

**Objective**: Initialize a DVC project and track a large file.

## 📝 Steps

1. **Initialize**: Run `dvc init` in this folder.
2. **Create Data**: Run `python -c "import numpy as np; np.savetxt('data.csv', np.random.rand(1000,1000))"`
3. **Track**: Run `dvc add data.csv`.
4. **Git Ignore**: Check `.gitignore`. It should contain `data.csv`.
5. **Commit**: `git add data.csv.dvc .gitignore` and commit.

## ❓ Question
If you delete `data.csv`, how do you get it back?
> Answer: `dvc checkout`
