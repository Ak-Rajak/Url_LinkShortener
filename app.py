from flask import Flask, render_template, request, redirect, url_for, flash
import pyshorteners
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Required for flash messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

# Database model to store URLs
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form.get('url')
        
        try:
            # Generate short URL
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(long_url)
            
            # Store in database
            new_url = URL(original_url=long_url, short_url=short_url)
            db.session.add(new_url)
            db.session.commit()
            
            flash('URL shortened successfully!', 'success')
            return render_template('index.html', short_url=short_url)
            
        except Exception as e:
            flash('Error: Invalid URL or service unavailable', 'error')
            return render_template('index.html')
    
    return render_template('index.html')

@app.route('/history')
def history():
    urls = URL.query.order_by(URL.created_date.desc()).all()
    return render_template('history.html', urls=urls)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)