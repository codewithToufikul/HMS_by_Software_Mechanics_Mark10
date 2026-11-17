# Hospital Management System (HMS) - Backend
> Developed by **Software Mechanics**

A modern, scalable Hospital Management System (HMS) backend built with **Django REST Framework**, **PostgreSQL**, and **Docker**.

---

## 🛠 Tech Stack

- **Framework:** Django 5.2+ & Django REST Framework (DRF)
- **Database:** PostgreSQL 17
- **Authentication:** SimpleJWT (JWT-based auth)
- **Containerization:** Docker & Docker Compose
- **Language:** Python 3.12+

---

## 📋 Prerequisites

Before running the project, make sure you have the following installed on your machine:

1. **Git**
2. **Docker & Docker Desktop** *(Recommended for team development)*
   - [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)
3. **Python 3.12+** *(Only if running locally without Docker)*

---

## 🚀 Getting Started (Setup & Installation)

You can run this project using either **Docker** (Recommended) or **Local Python Virtual Environment**.

### Method 1: Running with Docker (Recommended)

Docker ensures that everyone on the team runs the exact same Python and PostgreSQL environment without any local dependency mismatches.

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd HMS_by_Software_Mechanics_Mark10
```

#### 2. Setup Environment Variables
Copy `.env.example` to create your `.env` file:

- **macOS / Linux:**
  ```bash
  cp .env.example .env
  ```
- **Windows (Command Prompt / PowerShell):**
  ```cmd
  copy .env.example .env
  ```

*(You can modify passwords or database credentials in `.env` if needed).*

#### 3. Build & Start Containers
Ensure **Docker Desktop** is running, then run:
```bash
docker compose up --build
```
> **Tip:** To run containers in detached (background) mode, use `docker compose up --build -d`.

#### 4. Run Database Migrations
Open a new terminal tab and run:
```bash
docker compose exec web python manage.py migrate
```

#### 5. Create an Admin / Superuser
```bash
docker compose exec web python manage.py createsuperuser
```

#### 6. Access the Application
- **Backend API Root:** `http://localhost:8000/`
- **Django Admin Panel:** `http://localhost:8000/admin/`

---

### Method 2: Running Locally without Docker

If you prefer running directly on your local system with a Python virtual environment:

#### 1. Clone & Enter Directory
```bash
git clone <repository-url>
cd HMS_by_Software_Mechanics_Mark10
```

#### 2. Create and Activate Virtual Environment

- **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- **Windows (Command Prompt):**
  ```cmd
  python -m venv .venv
  .venv\Scripts\activate
  ```
- **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

#### 3. Install Dependencies
```bash
pip install -r backend/requirments.txt
```

#### 4. Setup Environment File
Create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```
> **Note for Local DB:** If PostgreSQL is running on your host machine, change `DBHOST=db` to `DBHOST=localhost` in your `.env` file.

#### 5. Run Migrations & Start Server
```bash
cd backend
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## ⚙️ Environment Variables Reference

| Variable | Description | Default |
| :--- | :--- | :--- |
| `SECRET_KEY` | Django secret key for cryptographic signing | `your-secret-key-here` |
| `DEBUG` | Enable/Disable debug mode (`True`/`False`) | `True` |
| `DBNAME` | PostgreSQL database name | `hospitaldb` |
| `DBUSER` | PostgreSQL user | `hospitaluser` |
| `DBPASSWORD` | PostgreSQL password | `hospitalpass` |
| `DBHOST` | Database host (`db` for Docker, `localhost` for local) | `db` |
| `DB_PORT` | Database port | `5432` |

---

## 🗂 Project Directory Structure

```text
HMS_by_Software_Mechanics_Mark10/
├── .env.example            # Sample environment variables for team
├── .gitignore              # Git ignore rules
├── docker-compose.yml      # Multi-container orchestration (Web + DB)
├── dockerfile              # Docker container build specifications
├── README.md               # Project documentation & setup instructions
└── backend/
    ├── manage.py           # Django management CLI utility
    ├── requirments.txt     # Python dependencies
    └── config/             # Django project configuration
        ├── __init__.py
        ├── asgi.py
        ├── settings.py     # Base settings & environment integration
        ├── urls.py         # Main URL routes
        └── wsgi.py
```

---

## 💻 Useful Commands

### Docker Commands
- **Stop containers:**
  ```bash
  docker compose down
  ```
- **Stop containers and delete database volume (fresh start):**
  ```bash
  docker compose down -v
  ```
- **View container logs:**
  ```bash
  docker compose logs -f
  ```
- **Enter the web container shell:**
  ```bash
  docker compose exec web bash
  ```

### Django Management Commands
- **Create new app:**
  ```bash
  # Inside Docker:
  docker compose exec web python manage.py startapp <app_name>
  # Locally:
  python manage.py startapp <app_name>
  ```
- **Make migrations:**
  ```bash
  # Inside Docker:
  docker compose exec web python manage.py makemigrations
  # Locally:
  python manage.py makemigrations
  ```

---

## 👥 Contribution & Git Guidelines

1. **Pull the latest changes** from `main` before starting work:
   ```bash
   git checkout main
   git pull origin main
   ```
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes** following clear commit message conventions:
   - `feat: add patient registration API`
   - `fix: resolve JWT token expiration issue`
   - `docs: update setup instructions in README`
4. **Push and create a Pull Request (PR)** for team review.

