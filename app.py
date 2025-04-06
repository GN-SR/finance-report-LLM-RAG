
import streamlit as st
from backend import load_and_split_pdf, create_vector_store, load_vector_store, generate_financial_report
import os

st.title("📊 Finance Report Generator with LLM & RAG")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with open(os.path.join("data", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")

    if st.button("Generate Report"):
        with st.spinner("Processing..."):
            docs = load_and_split_pdf(os.path.join("data", uploaded_file.name))
            vs = create_vector_store(docs)
            report = generate_financial_report(vs)
        st.subheader("Generated Report")
        st.write(report)
