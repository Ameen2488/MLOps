import json

notebook_path = r"c:/Users/asidd/Desktop/Data_science_projects/MLOps/portfolio_projects/research/01_data_ingestion.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")
for i, cell in enumerate(nb["cells"]):
    source = "".join(cell["source"])
    first_line = source.strip().split('\n')[0] if source.strip() else "[EMPTY]"
    print(f"Cell {i}: {first_line}")
