#https://resend.com/onboarding
#resend - free tier available

import os
import resend
from dotenv import load_dotenv

load_dotenv()  # Loads the .env file

resend.api_key = os.environ["RESEND_API_KEY"]

params: resend.Emails.SendParams = {
    "from": "ai <onboarding@resend.dev>",
    "to": [os.environ["MY_GMAIL_ADDRESS"]],
    "subject": "hi there from resend python sdk ",
    "html": "<strong>it works!</strong>",
}

email = resend.Emails.send(params)
print(email)

### Did you receive the test email

#If you get a 202, then you're good to go!

#### Certificate error

#If you get an error SSL: CERTIFICATE_VERIFY_FAILED then students Chris S and Oleksandr K have suggestions:  
#First run this: `!uv pip install --upgrade certifi`  
#Next, run this:
#```python
#import certifi
#import os
#os.environ['SSL_CERT_FILE'] = certifi.where()
#```

#### Other errors or no email
#
#If there are other problems, you'll need to check your API key and your verified sender email address in the SendGrid dashboard

#Or use the alternative implementation using "Resend Email" in community_contributions/2_lab2_with_resend_email

