# DummyDock

Dummy project to practice API development, model serving, and dockerization.


### Prerequisites

1. **Install Conda**: Ensure Conda is installed on your system. Download it from [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. **Install Docker**: Install Docker from [Docker Desktop](https://www.docker.com/products/docker-desktop).

---

### Clone the Repository

```bash
git clone <repository-url>
cd "Docker Project"
```

---

### Setup the Environment

#### Using Conda

1. **Create the Conda environment**:
   ```bash
   conda env create -p <environment-name> python==3.11
   ```
2. **Activate the environment**:
   ```bash
   conda activate <environment-name>
   ```
3. **Install dependencies** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   Start the Flask app:
    ```bash
    python app.py
    ```
   Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

#### Using Docker

1. **Build the Docker image**:
   ```bash
   docker build -t dummydock .
   ```
2. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 dummydock
   ```
3. **Access the app** at [http://127.0.0.1:5000](http://127.0.0.1:5000).
