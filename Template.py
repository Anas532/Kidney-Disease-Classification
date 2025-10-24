{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "76492442-3fe5-448b-acbc-47f89d31c059",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from pathlib import Path\n",
    "import logging"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "21ebc29b-8c35-4449-8415-48d11cb786e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Logging string\n",
    "logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "53731bc8-f162-4240-87ca-91f2ad6e7177",
   "metadata": {},
   "outputs": [],
   "source": [
    "project_name = 'cnnClassifier'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "03394cdf-4c2f-4165-8326-fc7bbfe6b873",
   "metadata": {},
   "outputs": [],
   "source": [
    "list_of_files = [\n",
    "    \".github/workflows/.gitkeep\",\n",
    "    f\"src/{project_name}/__init__.py\",\n",
    "    f\"src/{project_name}/components/__init__.py\",\n",
    "    f\"src/{project_name}/utils/__init__.py\",\n",
    "    f\"src/{project_name}/config/__init__.py\",\n",
    "    f\"src/{project_name}/config/configuration.py\",\n",
    "    f\"src/{project_name}/pipeline/__init__.py\",\n",
    "    f\"src/{project_name}/entity/__init__.py\",\n",
    "    f\"src/{project_name}/constants/__init__.py\",\n",
    "    \"config/config.yaml\",\n",
    "    \"dvc.yaml\",\n",
    "    \"params.yaml\",\n",
    "    \"requirements.txt\",\n",
    "    \"setup.py\",\n",
    "    \"research/trials.ipynb\",\n",
    "    \"templates/index.html\",\n",
    "    \"test.py\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ac74c6a8-96b7-4156-aab0-e436ff4941f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[2025-10-24 08:44:22,144]: Creating directory; .github/workflows for the file: .gitkeep:\n",
      "[2025-10-24 08:44:22,160]: Creating empty file: .github/workflows/.gitkeep:\n",
      "[2025-10-24 08:44:22,161]: Creating directory; src/cnnClassifier for the file: __init__.py:\n",
      "[2025-10-24 08:44:22,163]: Creating empty file: src/cnnClassifier/__init__.py:\n",
      "[2025-10-24 08:44:22,164]: Creating directory; src/cnnClassifier/components for the file: __init__.py:\n",
      "[2025-10-24 08:44:22,166]: Creating empty file: src/cnnClassifier/components/__init__.py:\n",
      "[2025-10-24 08:44:22,167]: Creating directory; src/cnnClassifier/utils for the file: __init__.py:\n",
      "[2025-10-24 08:44:22,167]: Creating empty file: src/cnnClassifier/utils/__init__.py:\n",
      "[2025-10-24 08:44:22,168]: Creating directory; src/cnnClassifier/config for the file: __init__.py:\n",
      "[2025-10-24 08:44:22,168]: Creating empty file: src/cnnClassifier/config/__init__.py:\n",
      "[2025-10-24 08:44:22,169]: Creating directory; src/cnnClassifier/config for the file: configuration.py:\n",
      "[2025-10-24 08:44:22,169]: Creating empty file: src/cnnClassifier/config/configuration.py:\n",
      "[2025-10-24 08:44:22,169]: Creating directory; src/cnnClassifier/pipeline for the file: __init__.py:\n",
      "[2025-10-24 08:44:22,170]: Creating empty file: src/cnnClassifier/pipeline/__init__.py:\n",
      "[2025-10-24 08:44:22,170]: Creating directory; src/cnnClassifier/entity for the file: __init__.py:\n",
      "[2025-10-24 08:44:22,171]: Creating empty file: src/cnnClassifier/entity/__init__.py:\n",
      "[2025-10-24 08:44:22,171]: Creating directory; src/cnnClassifier/constants for the file: __init__.py:\n",
      "[2025-10-24 08:44:22,172]: Creating empty file: src/cnnClassifier/constants/__init__.py:\n",
      "[2025-10-24 08:44:22,172]: Creating directory; config for the file: config.yaml:\n",
      "[2025-10-24 08:44:22,173]: Creating empty file: config/config.yaml:\n",
      "[2025-10-24 08:44:22,173]: Creating empty file: dvc.yaml:\n",
      "[2025-10-24 08:44:22,174]: Creating empty file: params.yaml:\n",
      "[2025-10-24 08:44:22,174]: Creating empty file: requirements.txt:\n",
      "[2025-10-24 08:44:22,175]: Creating empty file: setup.py:\n",
      "[2025-10-24 08:44:22,175]: Creating directory; research for the file: trials.ipynb:\n",
      "[2025-10-24 08:44:22,176]: Creating empty file: research/trials.ipynb:\n",
      "[2025-10-24 08:44:22,176]: Creating directory; templates for the file: index.html:\n",
      "[2025-10-24 08:44:22,177]: Creating empty file: templates/index.html:\n",
      "[2025-10-24 08:44:22,177]: Creating empty file: test.py:\n"
     ]
    }
   ],
   "source": [
    "for filepath in list_of_files:\n",
    "    filepath = Path(filepath)\n",
    "    filedir, filename = os.path.split(filepath)\n",
    "\n",
    "\n",
    "    if filedir !=\"\":\n",
    "        os.makedirs(filedir, exist_ok=True)\n",
    "        logging.info(f\"Creating directory; {filedir} for the file: {filename}\")\n",
    "\n",
    "    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):\n",
    "        with open(filepath, \"w\") as f:\n",
    "            pass\n",
    "            logging.info(f\"Creating empty file: {filepath}\")\n",
    "\n",
    "\n",
    "    else:\n",
    "        logging.info(f\"{filename} is already exists\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe955647-3a1b-4782-86a2-9b8345ac27ca",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
