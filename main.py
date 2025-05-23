import getpass
import os
import pickle
import time

import langchain
import langchain_community
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain     
from langchain.vectorstores import FAISS
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()  # take environment variables from .env file


st.title("News Research Tool")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

"st.session_state object:", st.session_state

main_placeholder = st.empty()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.9,
    max_tokens=500,
)

print("dzsfxgdxcg")
if process_url_clicked:
    print(f"{process_url_clicked=}")
    print(f"{urls=}")
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data loading started .........")
    data = loader.load()
    print(data)

    # splitting into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "], chunk_size=1000, chunk_overlap=200
    )
    main_placeholder.text("text Splitter started .........")
    docs = text_splitter.split_documents(data)
    print(len(docs))

    # embedding the docs
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    if len(docs) > 0:
        if "vectore_index_store" not in st.session_state:
            st.session_state["vector_index_store"] = FAISS.from_documents(
                docs, embeddings
            )
    main_placeholder.text("Embedding started .........")
    time.sleep(2)


query = main_placeholder.text_input("Question : ")
if query:
    print(f"{query=}")
    st.header("Answer")
    vectorStore = st.session_state["vector_index_store"]
    chain = RetrievalQAWithSourcesChain.from_llm(
        llm=llm, retriever=vectorStore.as_retriever()
    )
    result = chain({"question": query}, return_only_outputs=True)
    st.write(result["answer"])

    sources = result.get("sources", "")
    if sources:
        st.subheader("Sources:")
        sources_list = sources.split("\n")  # Split the sources by newline
        for source in sources_list:
            st.write(source)
