import sys
from exception import customexception
from logger import logging
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.gemini import GeminiEmbedding
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model



def download_gemini_embedding(model, document):
    """
    Downloads and intializes the Gemini embedding model for vector embeddings.
    
    Returns:
    - VectorStoreIndex: An index of vector embeddings created from the document.
    """
    try:
        logging.info("")
        # Initialize the embedding model
        gemini_embed_model = GeminiEmbedding(model="models/embedding-001")
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.node_parser = SentenceSplitter(chunk_size=800, chunk_overlap=20)
        Settings.num_output=800
        Settings.context_window = 3900

        logging.info("")
        index = VectorStoreIndex.from_documents(
        document, settings = Settings
        )
        index.storage_context.persist()

        logging.info("")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e, sys)