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

# 👥 Contribution & Git Guidelines
## HMS — Software Mechanics Mark10

Welcome to the Hospital Management System development team!

To maintain clean code, avoid merge conflicts, and ensure smooth collaboration, every developer must follow the same Git and GitHub workflow.

Our project follows a **Feature Branch Workflow**.

### 1. 🌳 Git Branch Structure

We use three types of branches:

| Branch | Purpose |
|---|---|
| `main` | Stable and production-ready code |
| `develop` | Main integration branch for all developers |
| `feature/*` | Individual developer's working branch |

**Important Rules:**
- Never push code directly to `main`.
- Never push code directly to `develop`.
- Always create a feature branch before starting development.
- All feature branches must be merged into `develop` through Pull Requests.
- Only tested and approved code can be merged from `develop` into `main`.

### 2. 🚀 First-Time Project Setup

If you are joining the project for the first time, follow these steps.

**Step 1: Clone the repository**

```bash
git clone https://github.com/codewithToufikul/HMS_by_Software_Mechanics_Mark10.git
```

**Step 2: Enter the project directory**

```bash
cd HMS_by_Software_Mechanics_Mark10
```

**Step 3: Switch to the develop branch**

```bash
git checkout develop
```

**Step 4: Pull the latest code**

```bash
git pull origin develop
```

**Step 5: Create your own feature branch**

Example for the Clinic / OPD developer:

```bash
git checkout -b feature/clinic-opd
```

Now you are ready to work on your assigned module.

### 3. 🔄 Daily Development Workflow

Follow these steps every time you start working.

**Step 1: Switch to develop**

```bash
git checkout develop
```

**Step 2: Get the latest updates**

```bash
git pull origin develop
```

**Step 3: Switch to your own feature branch**

```bash
git checkout feature/your-feature-name
```

Example:

```bash
git checkout feature/clinic-opd
```

**Step 4: Write your code**

Work only on your assigned module and avoid modifying other developers' files without coordination.

**Step 5: Check your changes**

```bash
git status
```

Review the modified files before committing.

**Step 6: Stage your changes**

```bash
git add .
```

**Step 7: Commit your changes**

```bash
git commit -m "feat: add patient registration API"
```

**Step 8: Push your feature branch**

For the first push:

```bash
git push -u origin feature/your-feature-name
```

For subsequent pushes:

```bash
git push
```

### 4. 📝 Commit Message Convention

Every commit message must clearly describe what was changed.

Use these prefixes:

| Prefix | When to use | Example |
|---|---|---|
| `feat:` | New feature | `feat: add patient registration API` |
| `fix:` | Bug fixes | `fix: resolve JWT token issue` |
| `docs:` | Documentation changes | `docs: update README` |
| `refactor:` | Code restructuring | `refactor: simplify patient service` |
| `test:` | Adding or updating tests | `test: add patient API tests` |
| `chore:` | Configuration or maintenance | `chore: update Docker configuration` |

Avoid unclear commit messages such as:

- `update`
- `changes`
- `final`
- `test`
- `new code`

### 5. 🔀 Pull Request (PR) Workflow

After completing your assigned task, you must create a Pull Request.

**Step 1:** Open the project repository on GitHub.

**Step 2:** Navigate to the Pull Requests section.

**Step 3:** Click on `New Pull Request`.

**Step 4:** Select the branches:

- Base branch: `develop`
- Compare branch: `feature/your-feature-name`

Example:

```text
base: develop
compare: feature/clinic-opd
```

**Step 5:** Write a meaningful PR title and description.

Example:

**Title:**
`feat: implement patient registration module`

**Description:**

```text
## What was implemented?
- Patient registration API
- Patient profile management
- Patient validation

## Testing
- API tested successfully
- Validation tested

## Notes
- No unrelated module changes
```

**Step 6:** Create the Pull Request and wait for Team Lead review.

**Step 7:** After approval, the Team Lead or authorized reviewer will merge it into `develop`.

Do not merge your own PR unless the Team Lead explicitly authorizes it.

### 6. 🔁 Keeping Your Feature Branch Updated

While you are working, other developers may merge new changes into `develop`.

Before continuing development, update your feature branch.

```bash
git checkout develop
git pull origin develop

git checkout feature/your-feature-name
git merge develop
```

If Git reports merge conflicts, resolve them carefully, test your code, and then continue.

Do not blindly overwrite another developer's changes.

### 7. ⚠️ Important Team Rules

1. Never work directly on `main` or `develop`.
2. Never push directly to protected branches.
3. Always work on your assigned feature branch.
4. Always pull the latest `develop` before starting a new task.
5. Create meaningful commits with proper prefixes.
6. Test your changes before creating a PR.
7. Do not modify another developer's module without discussion.
8. Do not commit `.env`, passwords, API keys, or secret credentials.
9. Never delete or rewrite shared database migrations without Team Lead approval.
10. Communicate with the Team Lead if you encounter merge conflicts or blockers.

### 8. 🏷️ Feature Branch Naming Convention

Use the following branch names for your assigned modules:

| Developer | Feature Branch |
|---|---|
| Developer 01 — Core System | `feature/core-system` |
| Developer 02 — Clinic / OPD | `feature/clinic-opd` |
| Developer 03 — Diagnostic | `feature/diagnostic` |
| Developer 04 — Pharmacy | `feature/pharmacy` |
| Developer 05 — Accounting | `feature/accounting` |
| Developer 06 — Blood Bank | `feature/blood-bank` |
| Developer 07 — Emergency | `feature/emergency` |
| Developer 08 — Integration & Testing | `feature/integration-testing` |

### 9. 🧑‍💻 Example: Complete Workflow

Suppose you are Developer 02 and assigned to implement the Patient Registration API.

```bash
# Update develop
git checkout develop
git pull origin develop

# Create your feature branch
git checkout -b feature/clinic-opd

# Work on your assigned task

# Stage changes
git add .

# Commit changes
git commit -m "feat: implement patient registration API"

# Push your branch
git push -u origin feature/clinic-opd
```

Then:

1. Open GitHub.
2. Create a Pull Request.
3. Set `develop` as the base branch.
4. Set `feature/clinic-opd` as the compare branch.
5. Add a clear description.
6. Request a review.
7. Wait for approval and merge.

### 10. 🎯 Final Reminder

**Our development flow:**

`Clone → Pull develop → Create Feature Branch → Code → Test → Commit → Push → Pull Request → Review → Merge`

Every developer is responsible for maintaining code quality, communicating changes, and following the team's Git workflow.

Let's build the Hospital Management System together with clean code, proper collaboration, and professional development practices.

**Project Team:** Software Mechanics Mark10  
**Project:** Multi-Hospital Management System
