# News Research Bot 📰🤖

An intelligent news analysis tool that leverages AI to extract insights from multiple news articles and answer user questions based on the content. Built with LangChain, Google Gemini AI, and Streamlit for an interactive web experience.

## 🌟 Features

- **Multi-URL Analysis**: Process up to 3 news article URLs simultaneously
- **AI-Powered Q&A**: Ask questions and get intelligent answers based on article content
- **Source Attribution**: All answers include source references for transparency
- **Real-time Processing**: Live feedback during document processing stages
- **Vector Search**: Uses FAISS for efficient similarity search and retrieval
- **Modern UI**: Clean, intuitive Streamlit interface

## 🏗️ Architecture

### Core Components

1. **Document Loading**: Uses `UnstructuredURLLoader` to extract content from news URLs
2. **Text Processing**: `RecursiveCharacterTextSplitter` breaks content into manageable chunks
3. **Embeddings**: Google Generative AI embeddings for semantic understanding
4. **Vector Store**: FAISS for efficient document retrieval
5. **LLM Integration**: Google Gemini 2.0 Flash for intelligent question answering
6. **Chain Architecture**: `RetrievalQAWithSourcesChain` for context-aware responses

### Technology Stack

- **Frontend**: Streamlit
- **LLM**: Google Gemini 2.0 Flash
- **Embeddings**: Google Generative AI Embeddings
- **Vector Database**: FAISS
- **Framework**: LangChain
- **Language**: Python 3.12+

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- Google API Key for Gemini AI
- Internet connection for URL processing

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd News-research-bot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

### Running the Application

```bash
streamlit run main.py
```

The application will open in your default browser at `http://localhost:8501`

## 📖 Usage Guide

### Step 1: Input URLs
1. Open the application in your browser
2. In the sidebar, enter up to 3 news article URLs
3. Click "Process URLs" to begin analysis

### Step 2: Processing
The system will:
- Load content from the provided URLs
- Split text into optimized chunks
- Generate embeddings for semantic search
- Create a searchable vector index

### Step 3: Ask Questions
1. Enter your question in the main input field
2. The AI will analyze the processed articles
3. Receive comprehensive answers with source citations

### Example Questions
- "What are the main points discussed in these articles?"
- "What is the impact of Tesla on Wall Street?"
- "Summarize the key financial trends mentioned"
- "What are the expert opinions on market conditions?"

## 🔧 Configuration

### Model Settings
- **Model**: Gemini 2.0 Flash
- **Temperature**: 0.9 (adjustable for creativity vs consistency)
- **Max Tokens**: 500 (response length limit)
- **Chunk Size**: 1000 characters
- **Chunk Overlap**: 200 characters

## 📁 Project Structure

```
News-research-bot/
├── main.py              # Main Streamlit application
├── app.ipynb           # Jupyter notebook for development/testing
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
├── .env               # Environment variables (create this)
└── README.md          # Project documentation
```

## 🔍 Key Dependencies

| Package | Version | Purpose |
|---------|---------|----------|
| streamlit | 1.45.1 | Web interface |
| langchain | 0.3.25 | LLM framework |
| langchain-google-genai | 2.1.4 | Google AI integration |
| faiss-cpu | 1.11.0 | Vector similarity search |
| python-dotenv | 1.1.0 | Environment management |
| unstructured | 0.17.2 | Document processing |

## 🛠️ Development

### Running in Development Mode

1. **Using Jupyter Notebook**
   ```bash
   jupyter notebook app.ipynb
   ```

2. **Debug Mode**
   Enable LangChain debugging in the notebook:
   ```python
   langchain.debug = True
   ```

### Code Structure

- **URL Processing**: Handles multiple URL inputs and validation
- **Document Processing**: Manages text extraction and chunking
- **Vector Operations**: Handles embedding generation and storage
- **Query Processing**: Manages user questions and response generation
- **Session Management**: Maintains state across Streamlit sessions

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---
