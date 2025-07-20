from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']

        # Format phone number
        phone = phone.strip().replace(" ", "")
        if not phone.startswith('91'):
            phone = '91' + phone  # India code

        # Message content
        message = f"""Dear {name},
Your scholarship has arrived. Please report to the Student Section as soon as possible and pay your remaining fees. 
Otherwise, a penalty will be levied.

From:
Student Section
Chhattisgarh Institute of Technology (CGIT), Jagdalpur"""

        # Encode message for URL
        encoded_msg = urllib.parse.quote(message)

        # WhatsApp link
        whatsapp_url = f"https://wa.me/{phone}?text={encoded_msg}"
        return redirect(whatsapp_url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
