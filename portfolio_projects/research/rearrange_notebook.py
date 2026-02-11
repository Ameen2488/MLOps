import json
import re

notebook_path = r"c:/Users/asidd/Desktop/Data_science_projects/MLOps/portfolio_projects/research/01_data_ingestion.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

cells = nb["cells"]

# Classify cells
imports = []
pwd = []
dataclass_config = []
manager_class = []
implementation_class = []
execution = []
others = []

for cell in cells:
    source = "".join(cell["source"])
    if not source.strip():
        others.append(cell) # Keep empty cells? Maybe put at end or ignore. Let's keep at end.
        continue

    # Identify by content
    if "import os" in source and "zipfile" not in source and "dataclasses" not in source:
         # Initial import os (Cell 1)
         imports.append(cell)
    elif "pwd" in source:
        pwd.append(cell)
    elif "from dataclasses import dataclass" in source:
        imports.append(cell)
    elif "@dataclass(frozen=True)" in source:
        dataclass_config.append(cell)
    elif "from portfolio_projects.constants import" in source:
        imports.append(cell)
    elif "class ConfigurationManager:" in source:
        manager_class.append(cell)
    elif "import os" in source and "zipfile" in source:
         # Cell 7 imports
         imports.append(cell)
    elif "class DataIngestion:" in source:
        implementation_class.append(cell)
    elif "try:" in source and "config: ConfigurationManager" in source:
        execution.append(cell)
    else:
        # Fallback
        print(f"Unclassified cell found: {source[:30]}...")
        others.append(cell)

# Define new order
# 1. Imports (flattened or sequential)
# 2. PWD (optional, usually near top)
# 3. DataIngestionConfig
# 4. ConfigurationManager
# 5. DataIngestion
# 6. Execution
# 7. Others

new_cells = []
new_cells.extend(imports)
new_cells.extend(pwd)
new_cells.extend(dataclass_config)
new_cells.extend(manager_class)
new_cells.extend(implementation_class)
new_cells.extend(execution)
new_cells.extend(others)

# Verify count
if len(new_cells) != len(cells):
    print(f"Warning: Cell count mismatch! Original: {len(cells)}, New: {len(new_cells)}")
    print("Aborting reorder to prevent data loss.")
else:
    nb["cells"] = new_cells
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)
    print("Notebook cells rearranged successfully.")
