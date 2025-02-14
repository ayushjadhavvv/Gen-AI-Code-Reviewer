📌 AI Code Reviewer (Powered by Google Gemini)
🔍 A Smart AI-Based Code Review Tool

🔹 AI Code Reviewer is an intelligent tool that reviews Python code, detects potential bugs, optimizations, and best practices, and provides feedback using Google Gemini AI.

🚀 Live Demo: https://gen-ai-code-reviewer-oxcbwhptfzmgdfmdasmkzu.streamlit.app/

🛠 Features
✅ AI-Powered Code Review – Analyzes Python code using Google Gemini AI.
✅ Bugs & Optimization Suggestions – Highlights potential issues and provides fixes.
✅ Live AI Analysis – Get real-time feedback while typing your code.
✅ Downloadable Reports – Save AI feedback as a .txt file for future reference.
✅ Dark Mode Toggle – Switch between light and dark themes.
✅ Review History – View past code submissions and AI feedback.

🚀 Tech Stack
Frontend: Streamlit
AI Model: Google Gemini AI
Backend: Python
Deployment: Streamlit Cloud

📂 Project Structure
graphql
Copy
Edit
📂 AI-Code-Reviewer
├── 📄 app.py                # Main application file (Streamlit)
├── 📄 requirements.txt      # Dependencies
├── 📄 .env                  # Stores API Key 
└── 📄 README.md             # Documentation

⚡ Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR_GITHUB_USERNAME/AI-Code-Reviewer.git
cd AI-Code-Reviewer

2️⃣ Create a Virtual Environment (Optional)
bash
Copy
Edit
python -m venv venv
# Activate virtual environment
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Your API Key
Create a .env file in the project folder and add:

ini
Copy
Edit
GEMINI_API_KEY = "your_google_gemini_api_key_here"

5️⃣ Run the Application
bash
Copy
Edit
streamlit run app.py
Now, open http://localhost:8501/ in your browser! 🎉

🌍 Deployment
1️⃣ Deploy on Streamlit Cloud (Easiest)
Push your code to GitHub.
Go to Streamlit Cloud and connect your GitHub repo.
Add your GEMINI_API_KEY under Settings > Secrets:
toml
Copy
Edit
GEMINI_API_KEY = "your_google_gemini_api_key_here"
Click Deploy and get your live app URL! 🚀

📜 License
This project is licensed under the MIT License.

🤝 Contribution
Want to contribute? 🚀

Open an issue for bug fixes or new feature requests.
Submit a pull request to enhance the AI review capabilities.
