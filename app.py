from flask import Flask, render_template, request, url_for
import qrcode
import os
from datetime import datetime

# Flask app setup
app = Flask(__name__)

# ✅ Path to the static folder Flask serves
QR_FOLDER = os.path.join(app.static_folder, 'qr_codes')
os.makedirs(QR_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form["url"].strip()
        filename = f"qr_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"

        file_path = os.path.join(QR_FOLDER, filename)

        # Generate QR code
        qr = qrcode.QRCode()
        qr.add_data(url)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_path)

        # Pass only the filename to the template
        return render_template("result.html", qr_filename=filename)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
