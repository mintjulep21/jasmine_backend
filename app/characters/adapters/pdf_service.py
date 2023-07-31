# adapters/pdf_service.py

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI


class PDFService:
    def analyze_pdf(self, pdf_file):
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # split into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=2000,
            chunk_overlap=200,
            length_function=len
        )
        docs = text_splitter.create_documents([text])

        llm = ChatOpenAI()
        summarization_chain = load_summarize_chain(llm, chain_type="map_reduce")

        return summarization_chain.run(docs)
