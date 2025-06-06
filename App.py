import os
import fitz  # PyMuPDF
import cohere
import streamlit as st

# === CONFIGURATION ===
COHERE_API_KEY = "7WgKL5QpJ2b2dh9OrbYRKmNSRPbyEpRlPoTMxAvD"  # Use your real key here
COHERE_MODEL = "command-r"
PDF_FOLDER = "pdf_data"

client = cohere.Client(COHERE_API_KEY)

# === EXTRACT TEXT FROM PDFs ===
def extract_text_from_pdf_fileobj(file_obj):
    """Extract text from a PDF file-like object (uploaded file)."""
    try:
        doc = fitz.open(stream=file_obj.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        file_obj.seek(0)  # reset stream pointer after reading
        return text
    except Exception as e:
        return f"[Error reading PDF: {e}]"

def extract_text_from_pdf_path(file_path):
    """Extract text from PDF file path."""
    text = ""
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        return f"[Error reading {file_path}: {e}]"
    return text

def extract_all_pdfs(folder_path):
    all_text = ""
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            all_text += extract_text_from_pdf_path(file_path) + "\n\n"
    return all_text

# === QUERY COHERE CHAT MODEL ===
def query_cohere(prompt):
    response = client.chat(
        model=COHERE_MODEL,
        message=prompt,
        temperature=0.5,
        max_tokens=1000
    )
    return response.text.strip()

# === COMBINE CONTEXT AND ASK AI ===
def ask_ai(user_request, context):
    final_prompt = f"""
Using the following VEX documents (notebook, game manual, criteria), write a detailed and coherent response to this request:

--- DOCUMENT CONTEXT START ---
{context}
--- DOCUMENT CONTEXT END ---

Request: {user_request}
"""
    return query_cohere(final_prompt)

# === STREAMLIT UI ===
def main():
    st.set_page_config(page_title="VEX Notebook AI Assistant", page_icon="🔺", layout="centered")
    col1, col2 = st.columns(2)

    with col1:
        with col1.container():
            st.write("\n" * 10)  # Push image downward to simulate vertical centering
            st.image("https://viterbiundergrad.usc.edu/wp-content/uploads/2023/09/VEX.png", width=180)

    with col2:
        with col2.container():
            st.write("\n" * 10)
            st.image("https://i.imgur.com/Z4yRwct.png", width=160)
    
    st.title("VEX Notebook AI Assistant")
    st.markdown("""Upload your VEX engineering notebook (PDF) below.
                This AI is trained by the VEX Game Manual, Notebook Criteria, and Judge's Guide!""")

    # 1) Load existing PDFs from folder
    if not os.path.exists(PDF_FOLDER):
        st.error(f"Folder '{PDF_FOLDER}' not found. Please create it and add PDF files.")
        return

    with st.spinner("Loading PDFs from folder..."):
        context_from_folder = extract_all_pdfs(PDF_FOLDER)

    # 2) Upload extra notebook PDF
    uploaded_file = st.file_uploader("Upload your engineering notebook (PDF)", type=["pdf"])
    context_uploaded = ""
    if uploaded_file is not None:
        with st.spinner("Reading your uploaded PDF..."):
            context_uploaded = extract_text_from_pdf_fileobj(uploaded_file)

    # 3) Combine contexts
    combined_context = context_from_folder + "\n\n" + context_uploaded

    if not combined_context.strip():
        st.warning("No PDF content found in folder or uploaded file.")
        return

    # 4) User input to ask AI
    user_question = st.text_input("What do you want to analyze about your VEX Notebook? (Ex. Does it follow VEX Guidelines?):")

    if st.button("Ask AI") and user_question.strip() != "":
        with st.spinner("Querying AI..."):
            answer = ask_ai(user_question, combined_context)
        st.markdown("### 🤖 AI Response:")
        st.write(answer)

if __name__ == "__main__":
    main()
