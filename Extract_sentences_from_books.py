import fitz  # PyMuPDF
import re
import pandas as pd

def pdf_to_text(pdf_path):
    # Using PyMuPDF to extract text from the PDF
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

def clean_text(text):
    # Removing unnecessary characters and extra whitespaces
    cleaned_text = re.sub(r'\s+', ' ', text).strip()
    return cleaned_text

def extract_sentences(text):
    # Splitting the text into sentences using a simple regex
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentences

def preprocess_pdf(pdf_path):
    # Convert PDF to text
    raw_text = pdf_to_text(pdf_path)
    # Clean the text
    cleaned_text = clean_text(raw_text)
    # Extract sentences
    sentences = extract_sentences(cleaned_text)
    return sentences

# Example usage:
pdf_path = 'William J. Brown, Raphael C. Malveau, Hays W. _Skip_ McCormick, Thomas J. Mowbray - Antipatterns. Refactoring Software, Archtectures and Projects in Crisis-Wiley (1998).pdf'
preprocessed_sentences = preprocess_pdf(pdf_path)

df=pd.DataFrame({'text':preprocessed_sentences})

def Preprocessing(text):
    text= re.sub("[\(\[].*?[\)\]]", "", text)                   # remove (..) [..]
    return text
df['text'] = df['text'].apply(Preprocessing)

x=[]
for i in range(len(df)):
    if len(df['text'][i].split())>3:
        x.append(df['text'][i])
    
df=pd.DataFrame({'text':x})
df.to_csv('reviewer_response.csv', index=False)
