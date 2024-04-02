from setuptools import find_packages, setup

setup(

    name = "mcqgen",
    version = "0.0.1", 
    author = "Katia Oussar", 
    author_email = "basketkaty8000@gmail.com",
    install_requires = ["openai","langchain", "streamlit","python-dotenv ","PyPDF2"],
    packages = find_packages()
)