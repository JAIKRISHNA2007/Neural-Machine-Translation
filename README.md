# Neural Machine Translation using MarianMT

A Streamlit-based **Neural Machine Translation (NMT)** application that translates English text into French using the pre-trained **Helsinki-NLP/opus-mt-en-fr** MarianMT model from Hugging Face Transformers. This project demonstrates how state-of-the-art Natural Language Processing (NLP) models can be deployed through an interactive and user-friendly web interface.

---

## 🌐 Quick Links

- **🚀 Live Demo:** https://neural-machine-translation-version1.streamlit.app/
- **💻 GitHub Repository:** https://github.com/JAIKRISHNA2007/Neural-Machine-Translation
- **🎥 Demo Video:** https://drive.google.com/drive/folders/1DK89HskWys5jNu7a_qcL8tAws8uo8aAw?usp=drive_link

---

## ✨ Features

- 🌍 English to French Neural Machine Translation
- 🤖 Powered by MarianMT (Helsinki-NLP/opus-mt-en-fr)
- ⚡ Fast model loading using Streamlit caching
- 🎨 Interactive and responsive Streamlit web interface
- 📝 Clean and modern user interface
- ✅ Error handling for invalid inputs
- 🚀 Uses pre-trained models without additional training

---

## 🛠️ Technologies Used

- Python 3.11
- Streamlit
- PyTorch
- Hugging Face Transformers
- MarianMT
- SentencePiece

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/JAIKRISHNA2007/Neural-Machine-Translation.git
cd Neural-Machine-Translation
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
Neural-Machine-Translation/
│
├── app.py
├── translator.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── images/
    ├── home.png
    └── result.png
```

---

## 💡 Example

Enter English text and click **Translate to French**.

### Input

```text
Hi, nice to meet you.
```

### Output

```text
Bonjour, ravi de vous rencontrer.
```

---

## 📸 Screenshots

### 🏠 Home Page

![Home Page](images/home.png)

### 🌍 Translation Result

![Translation Result](images/result.png)

---

## 🎥 Demo Video

Watch the complete project demonstration here:

**Google Drive:**  
https://drive.google.com/drive/folders/1DK89HskWys5jNu7a_qcL8tAws8uo8aAw?usp=drive_link

---

## 🌱 Future Improvements

- 🌐 Support multiple language pairs
- 🎤 Voice-to-text translation
- 📄 Document translation (PDF, DOCX, TXT)
- 📜 Translation history
- ☁️ FastAPI backend deployment
- 🔊 Text-to-Speech output
- 📱 Mobile-friendly interface

---

## 💼 Internship Information

This project was developed as part of the **AI Internship** at **Codtech IT Solutions Private Limited**.

- **Intern ID:** CTTS162
- **Intern:** JAI KRISHNA S

---

## 👨‍💻 Author

**JAI KRISHNA S**

GitHub: https://github.com/JAIKRISHNA2007

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more information.