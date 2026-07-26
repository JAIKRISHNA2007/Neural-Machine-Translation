import torch
from transformers import MarianMTModel, MarianTokenizer

# Global cache for tokenizer and model to ensure they are loaded only once
_tokenizer = None
_model = None
MODEL_NAME = "Helsinki-NLP/opus-mt-en-fr"

def get_translator():
    """
    Loads and caches the Marian tokenizer and model.
    """
    global _tokenizer, _model
    if _tokenizer is None or _model is None:
        _tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        _model = MarianMTModel.from_pretrained(MODEL_NAME).to(device)
    return _tokenizer, _model

def translate(text: str) -> str:
    """
    Translates English text to French using the cached MarianMT model.
    
    Args:
        text (str): The English text to translate.
        
    Returns:
        str: The translated French text.
    """
    if not text.strip():
        return ""
    
    tokenizer, model = get_translator()
    device = model.device
    
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True).to(device)
    
    # Generate the translation tokens
    with torch.no_grad():
        translated_tokens = model.generate(**inputs)
        
    # Decode the tokens back to string
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text
