from flask import Flask, request
from flask_cors import CORS
import sendgrid
from sendgrid.helpers.mail import Mail
import os

app = Flask(__name__)
CORS(app)

sg = sendgrid.SendGridAPIClient(
    api_key=os.environ.get("SENDGRID_API_KEY")
)

def send_email(mood):
    label = mood.get("label", "unknown mood")

    message = Mail(
        from_email="neeraj2111bla@gmail.com",
        to_emails="neerajnilujha@gmail.com",
        subject="Simu just shared her mood 💌",
        plain_text_content=f"Hey, Simu just tapped a mood on your app. mood:{label}"
    )

    response = sg.send(message)
    print(response.status_code)

@app.route("/mood", methods=["POST"])
def mood():
    data = request.json
    mood = data.get("mood")

    print("Mood received:", mood)

    send_email(mood)

    return {"status": "ok"}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
