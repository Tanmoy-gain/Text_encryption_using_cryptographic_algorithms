from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ''
    decrypted_text = ''

    if request.method == 'POST':
        # Get the action and input text from the form
        action = request.form.get('action')
        input_text = request.form.get('input_text').encode()

        if action == 'Encrypt':
            encrypted_text = cipher_suite.encrypt(input_text).decode()
        elif action == 'Decrypt':
            decrypted_text = cipher_suite.decrypt(input_text).decode()

    return render_template('index.html', encrypted_text=encrypted_text, decrypted_text=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
