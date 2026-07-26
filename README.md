# Neural Machine Translation using MarianMT

A professional and production-ready Neural Machine Translation (NMT) application built with Python and Streamlit, utilizing the pre-trained `Helsinki-NLP/opus-mt-en-fr` model from Hugging Face's Transformers library to translate English text into French.

## Features

- **Accurate English-to-French Translation:** Leverages MarianMT (`opus-mt-en-fr`) trained on large-scale parallel corpora.
- **Effortless Single-Load Optimization:** Caches the tokenizer and translation model to ensure fast subsequent translation responses.
- **Modern User Interface:** Sleek, custom-designed Streamlit frontend with a professional layout, sidebar instructions, and clear output presentation.
- **Error Handling:** Graceful exception catcher to manage any runtime or connection errors during translation.
- **No Training/Fine-Tuning Required:** Operates strictly using pre-trained weights for instantaneous setup.

## Technologies

- **Python 3.11**
- **Streamlit** (Web application framework)
- **Hugging Face Transformers** (MarianMT tokenization and generation)
- **PyTorch** (Deep learning backend)
- **SentencePiece & Sacremoses** (Subword tokenization and preprocessing libraries)

## Installation

Ensure you have Python 3.11 installed.

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/nmt-marian-en-fr.git
   cd nmt-marian-en-fr
