"""
Text Preprocessing Module for cleaning and preparing text for TTS
"""

import re

# NLTK import wrapped in try-except for compatibility
try:
    import nltk
    from nltk.tokenize import sent_tokenize
    from nltk.corpus import stopwords
    
    # Download required NLTK data
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')
    
    HAS_NLTK = True
except (ImportError, AttributeError):
    HAS_NLTK = False
    sent_tokenize = None


def preprocess_text(text):
    """
    Preprocess text by:
    - Removing extra whitespace
    - Converting to lowercase for consistency
    - Removing special characters (except punctuation useful for TTS)
    - Normalizing contractions
    - Adding proper spacing
    
    Args:
        text (str): Raw input text
    
    Returns:
        str: Preprocessed text
    """
    if not text:
        return ""
    
    # Remove extra whitespace and normalize line breaks
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Fix common spacing issues around punctuation
    text = re.sub(r'\s+([?.!,;:])', r'\1', text)
    text = re.sub(r'([?.!,;:])\s*', r'\1 ', text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^a-zA-Z0-9\s\.\,\?\!;:\'\"\-]', '', text)
    
    # Remove multiple spaces again
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Normalize contractions (e.g., "don't" stays as is, but "dont" becomes "do not")
    contractions_dict = {
        "dont": "do not",
        "wont": "will not",
        "cant": "cannot",
        "shouldnt": "should not",
        "wouldnt": "would not",
        "hasnt": "has not",
        "havent": "have not",
        "isnt": "is not",
        "arent": "are not",
        "wasnt": "was not",
        "werent": "were not",
    }
    
    for contraction, expansion in contractions_dict.items():
        text = re.sub(r'\b' + contraction + r'\b', expansion, text, flags=re.IGNORECASE)
    
    return text


def clean_text(text):
    """
    Light cleaning without heavy NLP processing
    """
    if not text:
        return ""
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    return text


def tokenize_sentences(text):
    """
    Split text into sentences for better TTS processing
    
    Args:
        text (str): Input text
    
    Returns:
        list: List of sentences
    """
    try:
        if HAS_NLTK and sent_tokenize:
            sentences = sent_tokenize(text)
            return sentences
    except:
        pass
    
    # Fallback to simple regex splitting
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip()]
