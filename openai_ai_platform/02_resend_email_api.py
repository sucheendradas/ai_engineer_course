#https://resend.com/onboarding
#resend - free tier available

import os
import resend
from dotenv import load_dotenv

load_dotenv()  # Loads the .env file

resend.api_key = os.environ["RESEND_API_KEY"]

params: resend.Emails.SendParams = {
    "from": "Acme <onboarding@resend.dev>",
    "to": ["your email here"],
    "subject": "hi there from resend python sdk ",
    "html": "<strong>it works!</strong>",
}

email = resend.Emails.send(params)
print(email)
