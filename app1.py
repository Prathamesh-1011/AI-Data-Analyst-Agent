import streamlit as st
import pandas as pd
import together
import matplotlib.pyplot as plt
import seaborn as sns
import fitz
from io import StringIO
from PIL import Image
import pytesseract
import docx

# Set your Together API key
together.api_key = "your_api_key"  # Replace with your actual API key

# Function: query_llama
def query_llama(prompt):
    response = together.Complete.create(
        model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        prompt=prompt,
        max_tokens=512,
        temperature=0.7,
        top_p=0.9,
        stop=["</s>"]
    )
    return response["choices"][0]["text"]

# Function: extract_text_from_pdf
def extract_text_from_pdf(uploaded_pdf):
    text = ""
    with fitz.open(stream=uploaded_pdf.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

# Function: extract_text_from_docx (Word files)
def extract_text_from_docx(uploaded_file):
    doc = docx.Document(uploaded_file)
    return '\n'.join([p.text for p in doc.paragraphs])

# Function: extract_text_from_image (OCR)
def extract_text_from_image(uploaded_file):
    image = Image.open(uploaded_file)
    return pytesseract.image_to_string(image)

# Session State: Store Conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = []

st.title("🧠 AI Data Analyst Agent")

uploaded_file = st.file_uploader("Upload your dataset or document", type=["csv", "xlsx", "txt", "pdf", "docx", "png", "jpg", "jpeg"])

file_text = None
df = None
answer = None

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1].lower()

    try:
        if file_type == "csv":
            df = pd.read_csv(uploaded_file)
            file_text = df.head(10).to_markdown()

        elif file_type == "xlsx":
            df = pd.read_excel(uploaded_file)
            file_text = df.head(10).to_markdown()

        elif file_type == "txt":
            file_text = uploaded_file.read().decode("utf-8")

        elif file_type == "pdf":
            file_text = extract_text_from_pdf(uploaded_file)

        elif file_type == "docx":
            file_text = extract_text_from_docx(uploaded_file)

        elif file_type in ["png", "jpg", "jpeg"]:
            file_text = extract_text_from_image(uploaded_file)

        else:
            st.warning("Unsupported file type")

        if df is not None:
            st.write("### 📄 Data Preview", df.head())

        st.write("### 💬 Ask a Question")
        user_question = st.text_input("Enter your question:", key="user_input")

        if st.button("Submit Question"):
            if user_question and file_text:
                prompt = f"Document content:\n{file_text}\n\nUser Question: {user_question}"
                with st.spinner("🤖 Thinking..."):
                    answer = query_llama(prompt)

                st.session_state.conversation.append(("You", user_question))
                st.session_state.conversation.append(("Analyst", answer))

        # Show conversation history
        if st.session_state.conversation:
            st.write("### 🗨️ Conversation History")
            for speaker, text in st.session_state.conversation:
                st.markdown(f"**{speaker}:** {text}")

        # Try to plot if LLaMA returns matplotlib code
        if answer and ("plt." in answer or "sns." in answer):
            try:
                exec(answer, globals())
                st.pyplot()
            except Exception as e:
                st.error(f"⚠️ Failed to render plot: {e}")

        if st.button("🔄 Clear Chat"):
            st.session_state.conversation = []

    except Exception as e:
        st.error(f"Error reading file: {e}")

else:
    st.info("📂 Please upload a file to begin.")

