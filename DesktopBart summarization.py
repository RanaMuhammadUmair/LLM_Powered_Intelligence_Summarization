import torch
from transformers import BartForConditionalGeneration, BartTokenizer
import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def summarize_text(text, model, tokenizer, max_length=500, min_length=100):
    """Summarizes the given text using the BART model."""
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        min_length=min_length,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Load BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Example usage
pdf_path =r"C:\Thesis\LLM_Powered_Intelligence_Summarization\sample_intelligence_report.pdf"
text = extract_text_from_pdf(pdf_path)
summary = summarize_text(text, model, tokenizer)

print("\n--- Summary ---\n")
print(summary)
