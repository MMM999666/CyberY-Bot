# CyberY-Bot 🤖

Lokale X (Twitter) bot die cybersecurity-tips post (met kerst-sfeer).

## Installatie (lokaal)

1. Clone de repo:
   ```bash
   git clone https://github.com/MMM999666/CyberY-Bot.git
   cd CyberY-Bot
   ```

2. Installeer dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Kopieer `.env.example` naar `.env` en vul je X API keys in:
   ```bash
   cp .env.example .env
   ```

4. Start de bot:
   ```bash
   python bot.py
   ```

## Netlify
Deze bot draait lokaal. Je kunt eventueel een simpele status-pagina op Netlify zetten, of de bot later via een serverless function laten draaien (maar dat is complexer met API keys).

## Let op
- Deel je API keys nooit publiek.
- De bot post elke 6 uur een willekeurige tip.
- Pas de `tips` lijst aan in `bot.py` naar wens.
