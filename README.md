# 🧠 AI Data Analyst Agent

A Streamlit-based web application that enables users to upload CSV, Excel, PDF, Word, text, or image files and interactively query the contents using the **LLaMA-4 Maverick 17B model** from Together.ai. Supports conversational Q\&A, summarization, and even code-based data visualizations!

## 🚀 Features

* 📄 **Multi-format File Upload**: Supports `.csv`, `.xlsx`, `.pdf`, `.docx`, `.txt`, `.jpg`, `.jpeg`, `.png`.
* 🤖 **AI-Powered Q\&A**: Asks questions and receives insights using the LLaMA-4 model.
* 📊 **Smart Data Preview**: Automatically displays a preview of the uploaded tabular data.
* 🧾 **Document Summarization**: Summarize long reports, proposals, and scanned documents.
* 🖼️ **OCR Support**: Extract and analyze text from scanned images using Tesseract.
* 🧠 **Conversational Memory**: Maintains interaction history for a seamless experience.
* 📈 **Visualization Support**: Generates Python code for charts using `matplotlib` and `seaborn`.

## 🛠️ Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **Backend**: [Together.ai](https://www.together.ai/) for LLaMA-4 inference
* **Data Processing**: `pandas`
* **PDF Parsing**: `PyMuPDF (fitz)`
* **OCR**: `pytesseract`, `Pillow`
* **Docx Reading**: `python-docx`
* **Visualization**: `matplotlib`, `seaborn`


## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/ai-data-analyst-agent.git
   cd ai-data-analyst-agent
   ```

2. **Install the dependencies**

   ```bash
   pip install streamlit pandas together PyMuPDF matplotlib seaborn openpyxl python-docx pytesseract pillow
   ```

3. **Set your Together.ai API Key**

   Open `app.py` and replace:

   ```python
   together.api_key = "your_api_key"
   ```

   with your actual API key from [Together.ai](https://www.together.ai/).


## ▶️ Usage

Run the app with:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`.

## 💡 Example Use Cases

| File Type       | Example Query                                  |
| --------------- | ---------------------------------------------- |
| `sales.csv`     | “What are the top 3 performing products?”      |
| `report.pdf`    | “Summarize the key insights from this report.” |
| `scan.jpg`      | “Extract any contact or price information.”    |
| `proposal.docx` | “Summarize the business proposal.”             |


## 📌 Notes

* The AI can suggest matplotlib/seaborn code for visualizations, but rendering depends on whether the generated code is executable.
* OCR accuracy depends on image quality and Tesseract configuration.


## 📁 File Structure

```
├── app.py               # Streamlit application code
├── README.md            # This file
```


## 📄 License

MIT License. See [LICENSE](LICENSE) for more information.

## 🙌 Acknowledgements

* [Together.ai](https://together.ai/) for access to the LLaMA-4 model
* [Streamlit](https://streamlit.io/) for the frontend framework
* [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for image text recognition
