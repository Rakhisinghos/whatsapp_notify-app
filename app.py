from flask import Flask, render_template, request
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get all names and phone numbers from form
        names = request.form.getlist('name')
        phones = request.form.getlist('phone')

        links = []
        for name, phone in zip(names, phones):
            phone = phone.strip().replace(" ", "")
            if not phone.startswith('91'):
                phone = '91' + phone  # Add Indian country code if not present

            # Message to be sent
            message = f"""Dear {name},
Your scholarship has arrived. Please report to the Student Section as soon as possible and pay your remaining fees. 
Otherwise, a penalty will be levied.

From:
Student Section
Chhattisgarh Institute of Technology (CGIT), Jagdalpur"""

            # Encode message for WhatsApp URL
            encoded_msg = urllib.parse.quote(message)
            whatsapp_url = f"https://wa.me/{phone}?text={encoded_msg}"
            links.append(whatsapp_url)

        return render_template('results.html', links=links)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
