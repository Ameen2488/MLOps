
import os
import pandas as pd
from PIL import Image

data_dir = r"c:\Users\asidd\Desktop\Data_science_projects\MLOps\portfolio_projects\chest_cancer_image_classification\data"
splits = ["train", "test", "valid"]
classes = ["adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib", 
           "large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa", 
           "normal", 
           "squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa"]

report = []

for split in splits:
    split_dir = os.path.join(data_dir, split)
    if not os.path.exists(split_dir):
        print(f"Skipping {split}, not found")
        continue
        
    for cls in classes:
        cls_dir = os.path.join(split_dir, cls)
        if os.path.isdir(cls_dir):
            files = os.listdir(cls_dir)
            
            # Analyze image dimensions for the first few images
            widths = []
            heights = []
            valid_extensions = 0
            
            for f in files:
                ext = f.split('.')[-1].lower()
                if ext in ['png', 'jpg', 'jpeg']:
                    valid_extensions += 1
                    try:
                        with Image.open(os.path.join(cls_dir, f)) as img:
                            w, h = img.size
                            widths.append(w)
                            heights.append(h)
                    except:
                        pass
            
            avg_width = sum(widths)/len(widths) if widths else 0
            avg_height = sum(heights)/len(heights) if heights else 0
            
            report.append({
                "Split": split,
                "Class": cls,
                "Count": len(files),
                "Valid Images": valid_extensions,
                "Avg Width": avg_width,
                "Avg Height": avg_height
            })

df = pd.DataFrame(report)
print(df.to_markdown(index=False))
