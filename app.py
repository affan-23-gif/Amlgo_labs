import streamlit as st
from src.rag_pipeline import qa_chain

st.title("📘 RAG Chatbot with Streaming")
st.markdown("Ask questions about the document.")

query = st.text_input("Enter your question:")
if query:
    with st.spinner("Generating response..."):
        result = qa_chain(query)
        st.markdown("### 💬 Answer")
        st.write(result["result"])

        st.markdown("### 📚 Sources")
        for doc in result["source_documents"]:
            st.text(doc.metadata["source"])
