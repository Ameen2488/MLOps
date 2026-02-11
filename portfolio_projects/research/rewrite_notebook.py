import json
import os

notebook_path = r"c:/Users/asidd/Desktop/Data_science_projects/MLOps/portfolio_projects/research/01_data_ingestion.ipynb"

# Define the cells content
source_imports = [
    "import os\n",
    "from dataclasses import dataclass\n",
    "from pathlib import Path\n",
    "from portfolio_projects.constants import *\n",
    "from portfolio_projects.utils.common import read_yaml, create_directories\n",
    "import zipfile\n",
    "import gdown\n",
    "from portfolio_projects import logger\n"
]

source_config = [
    "@dataclass(frozen=True)\n",
    "class DataIngestionConfig:\n",
    "    root_dir: Path\n",
    "    source_URL: str\n",
    "    local_data_file: Path\n",
    "    unzip_dir: Path\n"
]

source_manager = [
    "class ConfigurationManager:\n",
    "    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):\n",
    "        self.config = read_yaml(config_file_path)\n",
    "        self.params = read_yaml(params_file_path)\n",
    "\n",
    "        create_directories([self.config.artifacts_root])\n",
    "\n",
    "    def get_data_ingestion_config(self) -> DataIngestionConfig:\n",
    "        config = self.config.data_ingestion\n",
    "        create_directories([config.root_dir])\n",
    "\n",
    "        data_ingestion_config = DataIngestionConfig(\n",
    "            root_dir=config.root_dir,\n",
    "            source_URL=config.source_URL,\n",
    "            local_data_file=config.local_data_file,\n",
    "            unzip_dir=config.unzip_dir,\n",
    "        )\n",
    "\n",
    "        return data_ingestion_config\n"
]

source_implementation = [
    "class DataIngestion:\n",
    "    def __init__(self, config: DataIngestionConfig):\n",
    "        self.config = config\n",
    "\n",
    "    def download_file(self)-> str:\n",
    "        '''\n",
    "        Fetch data from the url\n",
    "        '''\n",
    "\n",
    "        try:\n",
    "            dataset_url = self.config.source_URL\n",
    "            zip_download_dir = self.config.local_data_file\n",
    "            os.makedirs(\"artifacts/data_ingestion\", exist_ok=True)\n",
    "            logger.info(f\"Downloading data from {dataset_url} into file {zip_download_dir}\")\n",
    "            file_id = dataset_url.split(\"/\")[-2]\n",
    "            prefix = 'https://drive.google.com/uc?export=download&id='\n",
    "            gdown.download(prefix+file_id, str(zip_download_dir))\n",
    "            logger.info(f\"Downloaded data from {dataset_url} into file {zip_download_dir}\")\n",
    "        except Exception as e:\n",
    "            raise e\n",
    "\n",
    "\n",
    "    def extract_zip_file(self):\n",
    "\n",
    "        unzip_path = self.config.unzip_dir\n",
    "        os.makedirs(unzip_path, exist_ok = True)\n",
    "        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:\n",
    "            zip_ref.extractall(unzip_path)     \n"
]

source_execution = [
    "try:\n",
    "    config = ConfigurationManager()\n",
    "    data_ingestion_config = config.get_data_ingestion_config()\n",
    "    data_ingestion = DataIngestion(config=data_ingestion_config)\n",
    "    data_ingestion.download_file()\n",
    "    data_ingestion.extract_zip_file()\n",
    "except Exception as e:\n",
    "    raise e    \n"
]

# Create new cells list
new_cells = [
    {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source_imports},
    {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source_config},
    {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source_manager},
    {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source_implementation},
    {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source_execution}
]

# Load original to keep metadata if possible, else create fresh
if os.path.exists(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    print("Loaded existing notebook metadata.")
else:
    nb = {
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

nb["cells"] = new_cells

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print("Notebook rewritten successfully with clean structure.")
