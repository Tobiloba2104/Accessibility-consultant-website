from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')

    

    
    honeypot = request.form.get('website', '')
    if honeypot:
        return render_template('contact.html', success=True)

    
    full_name = request.form.get('full_name', '').strip()
    email = request.form.get('email', '').strip()
    subject = request.form.get('subject', '').strip()
    message = request.form.get('message', '').strip()


    errors = {}
    if not full_name:
        errors['full_name'] = 'Please enter your name.'
    if not email or '@' not in email:
        errors['email'] = 'Please enter a valid email address.'
    if not subject:
        errors['subject'] = 'Please select a subject.'
    if not message:
        errors['message'] = 'Please enter a message.'

    if errors:
        return render_template('contact.html', errors=errors)

    
    try:
        send_email(full_name, email, subject, message)
        return render_template('contact.html', success=True)
    except Exception as e:
        return render_template('contact.html',
                                error='Something went wrong sending your message. Please try again or email Victor directly.')


def send_email(full_name, sender_email, subject, message):
    msg = EmailMessage()
    msg['Subject'] = f'New Contact Form Message: {subject}'
    msg['From'] = os.environ.get('MAIL_USERNAME')
    msg['To'] = 'victor@luponetconsults.com'
    msg['Reply-To'] = sender_email
    msg.set_content(f'From: {full_name} ({sender_email})\n\n{message}')

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(os.environ.get('MAIL_USERNAME'), os.environ.get('MAIL_PASSWORD'))
        smtp.send_message(msg)


if __name__ == '__main__':
    app.run(debug=True)