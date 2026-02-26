from langchain_community.document_loaders import PyPDFLoader


def read_financial_document(file_path: str):

    loader = PyPDFLoader(file_path)

    docs = loader.load()

    text = ""

    for d in docs:
        text += d.page_content + "\n"

    return text