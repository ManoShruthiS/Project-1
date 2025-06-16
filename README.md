# 🧙 AI Dungeon Story Generator

An interactive story generator using GPT-2 that crafts fantasy, mystery, and sci-fi stories based on user prompts. Built with Python and Streamlit, the project allows users to explore generative storytelling with selectable genres and multiple outputs.

## 🔧 Tools & Technologies
- Python
- Streamlit
- Hugging Face Transformers
- GPT-2 (can be extended to GPT-Neo, GPT-J)
- Torch (PyTorch)

## 🚀 Features
- Prompt-based interactive storytelling
- Genre selection (Fantasy, Mystery, Sci-Fi, Adventure)
- Multiple AI-generated story continuations
- Save story to text file
- Streamlit web UI

## 📦 Setup Instructions

### 1. Clone or Extract Repository
Extract the ZIP or clone this repo using:
```bash
git clone <repo_url>
cd AI_Dungeon_Story_Generator
```

### 2. Create Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate   # Windows
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

## 📁 Project Structure
```
AI_Dungeon_Story_Generator/
├── app.py
├── requirements.txt
├── README.md
├── report.pdf
├── modules/
│   ├── model_loader.py
│   └── story_generator.py
└── outputs/
    └── example_story.txt
```

## ✍️ Sample Prompt
```
Prompt: A young girl discovers an ancient book in her attic.

Genre: Fantasy
```

## ✅ Output
Generates 3 different storylines for the input prompt under selected genre.

## 📄 License
This is a free project under the MIT License for educational purposes.
