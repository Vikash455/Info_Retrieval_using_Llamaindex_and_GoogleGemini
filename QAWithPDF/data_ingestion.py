from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging

def load_data(data):
    """
    Load PDF documents from the specified directory.
    
    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """

    try:
        logging.info("Data loading started...")
        loader = SimpleDirectoryReader("Data")
        documents = loader.load_data()
        logging.info("Data loading completed...")
        return documents
    except Exception as e:
        logging.info("exception occured in load_data_method of data_ingestion.py")
        raise customexception(e, sys)
