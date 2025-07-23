from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)
app.secret_key = "email_sender_secret"

EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_app_password"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        names = request.form.getlist('name')
        emails = request.form.getlist('email')

        message_body = request.form.get('message')

        try:
            for name, email in zip(names, emails):
                msg = EmailMessage()
                msg['Subject'] = 'Scholarship Notification from CGIT Student Section'
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = email

                # Personalize message
                body = message_body.replace("[Name]", name)
                msg.set_content(body)

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg)

            flash("Emails sent successfully!", "success")
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")

        return redirect('/')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
