import os
import random
import schedule
import time
from dotenv import load_dotenv
import tweepy

load_dotenv()

# X API credentials (van het aparte account waarmee je wilt posten)
client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

tips = [
    "🔒 Tip: Gebruik een wachtwoordmanager. Unieke wachtwoorden per site = veel veiliger. @Melialset #CyberY #CyberSecurity",
    "🎄 Kerst-tip: Let op phishing-mails over cadeaus of leveringen. Klik niet zomaar op links! @Melialset #CyberY",
    "🛡️ Update je software altijd. Veel aanvallen gebruiken oude kwetsbaarheden. @Melialset #CyberSecurity #CyberY",
    "📱 Schakel 2FA in overal waar het kan. Dit stopt de meeste account-overnames. @Melialset #CyberY",
    "🎁 Veilige feestdagen gewenst! Deel geen persoonlijke info op social media over waar je bent. @Melialset #CyberY"
]

def post_tip():
    tip = random.choice(tips)
    try:
        client.create_tweet(text=tip)
        print(f"Post geplaatst: {tip}")
    except Exception as e:
        print(f"Fout: {e}")

# Post elke 6 uur een tip
schedule.every(6).hours.do(post_tip)

print("CyberY Bot gestart! Druk Ctrl+C om te stoppen.")
post_tip()  # Direct een post bij start

while True:
    schedule.run_pending()
    time.sleep(60)
