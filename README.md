# ResumeAI – Professional Resume Generator

ResumeAI is a simple web application that helps users generate professional resumes using large language models powered by the Groq API.

## ✅ Features

* Generate structured resumes based on user input
* Uses **Groq API** with the **LLaMA 3.3 70B Versatile** model
* Clean and formatted output (no preamble, no extra content)
* Built with **Streamlit** for quick web deployment

## 🌐 Hosted on Streamlit cloud

* The project is live at [ResumeGenerater](https://resumegenerater.streamlit.app/)

## 🚀 How to Set Up

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shivakumarsouta/ResumeGenerator.git
cd ResumeGenerator
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_actual_groq_api_key_here
```

### 5️⃣ Run the Application

```bash
python -m streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

#### Try this prompt : 
```
Name: Shiva Kumar Souta, Email: shivakumarsouta18@gmail.com, Phone: +919876543210, GitHub: https://github.com/shivakumarsouta, LinkedIn: https://linkedin.com/in/shivakumarsouta.  For more, my Portfolio: https://shivakumarsouta-portfolio.vercel.app  
He is an AI & ML Final year student at KGRCET, Hyderabad, with a CGPA of 8.7 and has worked on many projects related to ML, Data Science and front end.
He did not do any internships but has experience as he worked on projects.
He knows python, java, c and knows tools like Git.

```

---

## 📁 Project Structure

```
ResumeGenerator/
│
├── Notebook.ipynb        # Notebook
├── app.py                # Streamlit web app script
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables file
└── README.md             # Project README
```

---

## ✨ Technologies Used

* Python 3.11
* Streamlit
* Langchain Core
* Groq API

---

## 💡 Notes

* Ensure your Groq API key is valid and active.
* This project assumes a working internet connection for API calls.

---

## 🤝 License

MIT License.
Feel free to fork, customize, and use in your own projects.

---

## 📞 Contact

[LinkedIn](https://linkedin.com/in/shivakumarsouta) | [GitHub](https://github.com/shivakumarsouta) | [Mail me](shivakumarsouta18@gmail.com) | [Portfolio](https://shivakumarsouta-portfolio.vercel.app)
