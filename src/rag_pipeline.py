from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are an assistant answering questions from a document.
Use only the below context to answer the question.
If unsure, say "I don't know."

Context:
{context}

Question: {question}"""
)

retriever = Chroma(persist_directory="vectordb", embedding_function=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")).as_retriever()

# Example: OpenAI GPT-3.5 (can replace with local model using TextGenerationPipeline)
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0),
    retriever=retriever,
    return_source_documents=True
)
