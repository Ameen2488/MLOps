FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libgomp1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY data/ data/ 
# In production, we wouldn't copy data, we'd mount volumes or pull from S3. 
# But for this standalone demo, we need the parquet file for the "Mock DB".

# We also trigger training during build (Bad practice usually, but good for self-contained demo)
# Or we assume user runs training locally before docker build.
# Let's run it:
RUN python src/models/train.py

EXPOSE 8000

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
