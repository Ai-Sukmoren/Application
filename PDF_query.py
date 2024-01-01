from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from typing_extensions import Concatenate
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os


#pdf file path

pdf = "C:\\Users\\Ai Sukmoren\\Desktop\\spinningup-openai-com-en-latest.pdf"

# provide the path to the pdf file
pdfreader = PdfReader(pdf)

# read text from PDF
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content

# split the text using charazter Text Split such that it should not increse token
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len  # corrected typo here
)

# Split the text
texts = text_splitter.split_text(raw_text)

#embedded api key inside the enironment
openai_api_key = os.getenv("OPENAI_API_KEY")

# Dowload embeddings from OpenAI
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Create a searchable  index and configure a question-answering chain that can be used to process queries
document_search = FAISS.from_texts(texts, embeddings)
chain = load_qa_chain(OpenAI(openai_api_key=openai_api_key), chain_type="stuff")

# Ask the user to input their question
query = " "

# Search for documents based on the input query
docs = document_search.similarity_search(query)
 
# Run the chain with the input documents and the user's question
chain.run(input_documents=docs, question=query)