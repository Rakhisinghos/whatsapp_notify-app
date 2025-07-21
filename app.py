from flask import Flask, render_template, request, redirect
import urllib.parse
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        names = request.form.getlist('name')
        phones = request.form.getlist('phone')

        # Create WhatsApp URLs for each contact
        links = []
        for name, phone in zip(names, phones):
            phone = phone.strip().replace(" ", "")
            if not phone.startswith('91'):
                phone = '91' + phone  # India code

            message = f"""Dear {name},
Your scholarship has arrived. Please report to the Student Section as soon as possible and pay your remaining fees. 
Otherwise, a penalty will be levied.

From:
Student Section
Chhattisgarh Institute of Technology (CGIT), Jagdalpur"""
            
            encoded_msg = urllib.parse.quote(message)
            whatsapp_url = f"https://wa.me/{phone}?text={encoded_msg}"
            links.append(whatsapp_url)

        # Optional: redirect to first URL or show all links
        return render_template('results.html', links=links)

    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
