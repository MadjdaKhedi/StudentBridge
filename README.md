# StudentBridge

StudentBridge is a simple web application that connects students to scholarship agents for applying to universities in China. It provides a registration form where students submit personal details and upload supporting documents (passport, transcripts, degree certificates, personal statement).

📝 Features

Student Registration: Collects student information (name, email, phone, date of birth, nationality, intended major, level of study, preferred university).

File Upload: Securely uploads and stores documents: passport, transcripts, degree certificate, and optional personal statement.

API Backend: FastAPI backend handles form data, saves files in uploads/{email}/, and supports CORS for frontend integration.

🚀 Tech Stack

Frontend: React, Tailwind CSS, Axios

Backend: Python, FastAPI, Uvicorn, python-multipart

Storage: Local filesystem (uploads/ folder)

Version Control: Git, GitHub

🔧 Setup Instructions

Clone the repository:

git clone https://github.com/MadjdaKhedi/StudentBridge.git
cd StudentBridge

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate    # macOS/Linux
.\.venv\\Scripts\\activate # Windows

Install dependencies:

pip install -r requirements.txt

Run the backend server:

uvicorn backend_registration_api:app --reload

The API will be available at http://127.0.0.1:8000.

Swagger UI: http://127.0.0.1:8000/docs

Run the frontend (in a separate terminal):

cd frontend
npm install
npm start

The app will open at http://localhost:3000.

☁️ Deployment to Render

Push your code to GitHub (if not already).

On Render.com, create a new Web Service:

Environment: Python 3

Build Command: pip install -r requirements.txt

Start Command: uvicorn backend_registration_api:app --host 0.0.0.0 --port 10000

Port: 10000

Deploy, then update your React app’s API URL to the Render endpoint (e.g., https://<your-app>.onrender.com/register).

🎯 Usage

Students navigate to the registration page.

Fill out the form and upload required documents.

Submit to register; backend responds with success or error message.

🤝 Contributing

Contributions are welcome! Please fork the repo, create a feature branch, and open a pull request.

📄 License

This project is open-source under the MIT License.
