from langchain_community.llms import HuggingFacePipeline
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document


DB_FAISS_PATH = "vectorstore/db_faiss"

print("Loading model...")
pipe = pipeline("text2text-generation", model="google/flan-t5-base", device=-1)
llm = HuggingFacePipeline(pipeline=pipe)

print("Loading FAISS DB...")
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever()

qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

def generate_financial_report(query):
    return qa.run(query)

def generate_from_text(text):
    doc = Document(page_content=text)
    prompt = "Generate a financial summary report based on the provided document."
    return qa.combine_documents_chain.run(input_documents=[doc], question=prompt)
