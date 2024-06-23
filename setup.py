from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Huzair Amjad',
    author_email='mhuzairbusdev123',
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)