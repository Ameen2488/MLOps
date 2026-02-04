from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
import onnxruntime as ort
import numpy as np
import cv2
import io
from PIL import Image

app = FastAPI(
    title="YOLOv8 Object Detection API",
    description="Serve ONNX model with FastAPI",
    version="1.0.0"
)

# Global variables for model
ORIT_SESSION = None
CLASS_NAMES = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 5: 'bus', 7: 'truck'} # Partial list for COCO128

@app.on_event("startup")
def load_model():
    """Load ONNX model on startup to avoid loading it for every request"""
    global ORT_SESSION
    # Check for INT8 model first, then standard ONNX, then fall back
    model_path = "../notebooks/yolov8n_int8.onnx" 
    
    # For demo purposes, we might need to adjust path depending on where uvicorn runs
    # Assuming running from root `cv_mlops_project/`
    import os
    if not os.path.exists(model_path):
        model_path = "../notebooks/yolov8n.onnx"
    
    try:
        ORT_SESSION = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
        print(f"✅ Loaded model from {model_path}")
    except Exception as e:
        print(f"❌ Failed to load model: {e}")

def preprocess_image(image_bytes: bytes, target_size=(640, 640)):
    """Convert bytes to numpy array, resize, and normalize"""
    # Decode
    image = Image.open(io.BytesIO(image_bytes))
    image = np.array(image)
    
    # Resize
    image = cv2.resize(image, target_size)
    
    # Normalize (0-255 -> 0.0-1.0)
    image = image.astype(np.float32) / 255.0
    
    # Transpose (H, W, C) -> (C, H, W)
    image = image.transpose(2, 0, 1)
    
    # Add Batch Dimension (1, C, H, W)
    image = np.expand_dims(image, axis=0)
    return image

@app.get("/")
def home():
    return {"status": "running", "model": "yolov8n-onnx"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Upload an image and get bounding boxes.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    # Read Bytes
    content = await file.read()
    
    # Preprocess
    input_tensor = preprocess_image(content)
    
    # Inference
    input_name = ORT_SESSION.get_inputs()[0].name
    outputs = ORT_SESSION.run(None, {input_name: input_tensor})
    
    # Post-process (Simplification for YOLOv8 output)
    # YOLOv8 output shape is (1, 84, 8400) -> 84 rows (4 box + 80 classes), 8400 anchors
    # We need to perform NMS (Non-Max Suppression) here ideally.
    # For this simple demo, we just return raw shape to prove it works.
    
    raw_output = outputs[0]
    return {
        "filename": file.filename,
        "output_shape": str(raw_output.shape),
        "message": "Model ran successfully! (NMS required for final boxes)"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
