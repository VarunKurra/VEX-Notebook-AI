# 🧠 VEX Notebook AI – Analyze, Score, and Improve VEX Robotics Notebooks with AI

<img src="Icon.png" alt="VEX Notebook AI Icon" width="150"/>

Welcome to **VEX-Notebook-AI**, a Streamlit-based app that helps students and teams analyze their engineering notebook PDFs using official VEX judging rubrics and generate high-quality essay-style feedback with the power of large language models.

---

## 🚀 Features

- 📤 Upload your VEX Notebook as a PDF
- 📚 Automatically integrates official VEX judging rubrics, engineering design documents, and examples for contextual understanding
- 🧠 Uses AI (via Cohere API) to generate:
  - A detailed evaluation of your notebook’s strengths and weaknesses
  - A professional essay reflecting official judging language
  - Suggestions for improvement and competition preparedness
- 💻 Streamlit-based UI that runs locally on your machine
- 🔐 Cohere API integration for high-quality, low-latency language generation
- 📁 Modular, extensible architecture for future model upgrades and rubric changes

---

## ⚙️ Installation Instructions

Follow these steps to run the app locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/VEX-Notebook-AI.git
cd VEX-Notebook-AI
```

### 2. Prepare the PDF Data Folder

Download and place the following official VEX PDFs into a folder named `pdf_data/` in the root directory:

- [Judge Guide](https://www.roboticseducation.org/documents/2024/05/judge-guide-2023-24.pdf/)
- [Engineering Notebook Rubric](https://www.roboticseducation.org/documents/2024/05/vrc-judging-rubrics-2023-24.pdf/)
- [Engineering Design Process Documents or Examples](https://example.com/your-pdfs)

Make sure all filenames are clean and readable (e.g., `judge_guide.pdf`, `rubric.pdf`, etc.).

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 4. Install Python Dependencies

Paste the following contents into a file named `requirements.txt`:

```txt
streamlit
PyPDF2
openai
cohere
python-dotenv
```

Then install them:

```bash
pip install -r requirements.txt
```

### 5. Add Your Cohere API Key

Open the `App.py` file and locate the following line:

```python
co = cohere.Client("YOUR_API_KEY_HERE")
```

Replace `"YOUR_API_KEY_HERE"` with your actual Cohere API key. You can get one by signing up at [cohere.com](https://cohere.com).

---

## ▶️ Running the App

From the root directory:

```bash
streamlit run App.py
```

Then open the local URL that appears (typically `http://localhost:8501`) in your browser.

---

## 🧬 How It Works (Architecture)

1. **PDF Parsing**: The user uploads their VEX notebook in PDF format, which is parsed using `PyPDF2`.
2. **Reference Context**: The app loads key official PDFs from the `pdf_data/` folder for context (judge guides, rubrics, examples).
3. **Prompt Construction**: The app combines the uploaded notebook with the official PDFs to construct a rich prompt.
4. **AI Evaluation**: The constructed prompt is sent to Cohere's LLM, which generates a high-quality essay evaluating the notebook.
5. **Output Display**: The AI-generated evaluation is shown in a scrollable Streamlit UI, styled and easy to read.

---

## 🧠 Advanced Notes

- **Model-Driven Feedback**: The AI isn’t just summarizing the notebook; it compares it against *VEX's own judging standards* to simulate a real judge’s evaluation.
- **Secure API Handling**: For production, consider using `python-dotenv` and `.env` files to store your API key instead of hardcoding it.
- **Expandable Architecture**: You can add more PDFs, change models, or hook into other LLMs (like OpenAI or Claude) with minor tweaks.
- **Custom Scoring**: You can modify the prompt to include a rubric-style numerical scoring system if desired.
- **Offline Mode (Future Feature)**: A local model version (using LLaMA or Mistral) is under consideration for private evaluation.

---

## 📬 Contact / Support

For questions, feedback, or feature requests, open an issue or email `youremail@example.com`.

---

## 🏁 License

MIT License – See `LICENSE.md` for full terms.
