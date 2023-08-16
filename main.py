import requests
from twilio.rest import Client

#Choose a stock 

STOCK_NAME = "PGR"
COMPANY_NAME = "The Progressive Company"

STOCK_ENDPOINT = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey=UO4YUGW7OL53IRBC"
NEWS_ENDPOINT = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey=7c9a821fc6f94dd580f330eb7a5d0fd5"

stock_response = requests.get(STOCK_ENDPOINT)
stock_response.raise_for_status()
stock_data = stock_response.json()

closing_prices = [float(entry["4. close"]) for date, entry in stock_data["Time Series (Daily)"].items()]
percent_difference_abs = abs(((closing_prices[0] - closing_prices[1]) / closing_prices[1]) / 100)
percent_difference = ((closing_prices[0] - closing_prices[1]) / closing_prices[1]) / 100

news_response = requests.get(NEWS_ENDPOINT)
news_response.raise_for_status()
news_data = news_response.json()

#sign up for a Twilio acct and input your account sid and token

account_sid = "__________"
auth_token = "_______________"

if percent_difference_abs > 0:
    articles = news_data["articles"][:3]
    shortened_news =[f"Headline: {article['title']}\nBrief: {article['description']}" for article in articles]

    client = Client(account_sid, auth_token)
#input your virtual twilio number and the real phone number you used to verify your twilio account
    if percent_difference > 0:
        message_percent_change = client.messages \
            .create(
            body=f"{STOCK_NAME}: 🔺{percent_difference}%",
            from_= TWILIO_NUMBER,
            to=REAL_NUMBER
        )
    if percent_difference < 0:
        message_percent_change = client.messages \
            .create(
            body=f"{STOCK_NAME}: 🔻{percent_difference}%",
            from_= TWILIO_NUMBER,
            to=REAL_NUMBER
        )
    for article in shortened_news:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=REAL_NUMBER
        )
