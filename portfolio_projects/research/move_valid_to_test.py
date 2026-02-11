
import os
import shutil
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

data_dir = r"c:\Users\asidd\Desktop\Data_science_projects\MLOps\portfolio_projects\chest_cancer_image_classification\data"
valid_dir = os.path.join(data_dir, "valid")
test_dir = os.path.join(data_dir, "test")

if not os.path.exists(valid_dir):
    logging.error(f"Validation directory not found: {valid_dir}")
    exit(1)

if not os.path.exists(test_dir):
    logging.error(f"Test directory not found: {test_dir}")
    exit(1)

# Get all classes in valid dir
classes = os.listdir(valid_dir)

moved_count = 0

for cls in classes:
    src_cls_dir = os.path.join(valid_dir, cls)
    dst_cls_dir = os.path.join(test_dir, cls)
    
    if not os.path.isdir(src_cls_dir):
        continue
        
    # Create destination class dir if it doesn't exist
    os.makedirs(dst_cls_dir, exist_ok=True)
    
    files = os.listdir(src_cls_dir)
    for f in files:
        src_file = os.path.join(src_cls_dir, f)
        dst_file = os.path.join(dst_cls_dir, f)
        
        # Handle duplicate filenames if any
        if os.path.exists(dst_file):
            base, ext = os.path.splitext(f)
            dst_file = os.path.join(dst_cls_dir, f"{base}_valid{ext}")
            
        shutil.move(src_file, dst_file)
        moved_count += 1

logging.info(f"Successfully moved {moved_count} images from valid to test.")

# Optional: Remove empty valid directories
shutil.rmtree(valid_dir)
logging.info(f"Removed empty validation directory: {valid_dir}")
