### Project Setup

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd <project-folder>
```

#### 2. Create a Virtual Environment
```bash
conda create -p env python=3.10 -y
```

#### 3. Activate the Virtual Environment
```bash
conda activate env/
```

#### 4. Install Project Requirements
```bash
pip install -r requirements.txt
```

#### 5. Environment Variables
Create a .env file and add the required key-value pairs:
```bash
OPENAI_API_KEY = your_api_key
```

#### 6. How to Run the Project
```bash
streamlit run app.py
```