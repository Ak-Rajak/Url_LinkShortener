# URL Shortener App

## Overview

The **URL Shortener App** is a web-based application that allows users to shorten long URLs using a simple interface. It is built using **Python 3**, **Flask**, and **SQLite**.

This project showcases full-stack development skills, including:

- **Backend Development** (Flask, SQLite, Python)
- **Frontend Design** (HTML, CSS, Bootstrap)
- **Database Management** (SQLAlchemy with SQLite)

🔗 **Live Demo:** [URL Shortener](https://url-linkshortener.onrender.com/)

## Features

- 🔗 **Shorten Long URLs** using the TinyURL API
- 📜 **View URL History** (Saved URLs with timestamps)
- 📋 **Copy Shortened URLs** with a single click
- 🌐 **Web Version** with Flask & SQLite
- 🎨 **Modern UI** with Bootstrap for web

## Technologies Used

- **Python 3**
- **Flask** (for backend)
- **SQLite** (for database storage)
- **PyShorteners** (TinyURL API integration)
- **Flask-SQLAlchemy** (ORM for database management)
- **Bootstrap 5** (for responsive UI)
- **HTML & CSS** (for frontend design)

## How It Works

### Web Application

1. **Enter a long URL** in the input box.
2. Click **Generate Short URL** to shorten it.
3. The **shortened URL** is displayed and saved in history.
4. Users can **view the history** of shortened URLs.

## Installation & Setup

### Web Application

#### Prerequisites:

- Python 3 installed
- Flask and dependencies installed

#### Steps:

```sh
# Clone the repository
$ git clone https://github.com/Ak-Rajak/Url_LinkShortener.git
$ cd url-shortener

# Install dependencies
$ pip install -r requirements.txt

# Run the application
$ python app.py
```

The application will be available at: `http://127.0.0.1:5000/`

## File Structure

```
📂 url-shortener/
│── app.py           # Flask backend
│── templates/
│   ├── index.html   # Homepage (URL shortener form)
│   ├── history.html # URL history page
│── static/
│── requirements.txt # Python dependencies
```

## Future Enhancements

🚀 **Custom Short URLs** - Allow users to create their own short links. 🔒 **User Authentication** - Secure URL history with login/signup. 📊 **Analytics** - Track click counts on shortened URLs.

---

🎯 **Why This Project?** This project demonstrates full-stack development skills and practical experience in **Python, Flask, databases, and API integration**. It is an excellent addition to your portfolio to showcase your ability to build functional and user-friendly applications!

---
