# Stock News and SMS Notification Script

This script fetches stock data and related news articles for a chosen stock from the Alpha Vantage and NewsAPI services. It then sends SMS notifications via Twilio API to alert you about the stock's percent change and provides brief news headlines and descriptions.

![download (2)](https://github.com/davidmakoyo/stock-alerts/assets/110312975/84d32f7b-e187-4d2d-83d4-dd91fb75ec39)

## Prerequisites

Before using this script, ensure you have the following:

1. **Alpha Vantage API Key**: Sign up for an API key on the [Alpha Vantage website](https://www.alphavantage.co/) and replace `UO4YUGW7OL53IRBC` with your API key in the `STOCK_ENDPOINT` URL.

2. **NewsAPI Key**: Get an API key from the [NewsAPI website](https://newsapi.org/) and replace `7c9a821fc6f94dd580f330eb7a5d0fd5` with your API key in the `NEWS_ENDPOINT` URL.

3. **Twilio Account**: Sign up for a Twilio account and get your Account SID and Auth Token. Replace `__________` and `_______________` with your actual Account SID and Auth Token.

4. **Twilio Phone Numbers**: Replace `TWILIO_NUMBER` and `REAL_NUMBER` with your virtual Twilio phone number and your real phone number, respectively.

## Usage

1. Clone or download the repository.

2. Open the `stock_news_twilio.py` file in your preferred code editor.

3. Configure the script by providing the required API keys, Twilio credentials, and phone numbers.

4. Run the script.

## Steps Performed by the Script

1. Fetches stock data for the chosen stock from Alpha Vantage's API.

2. Calculates the percent difference in closing prices between the latest two days.

3. Fetches news articles related to the chosen stock from NewsAPI.

4. Sends an SMS indicating the stock's percent change.

5. Sends three separate SMS notifications for each of the first three news articles' headlines and descriptions.

## Example

1. Run the script.

If the absolute value of percent change > 5:
  2.  Receive an SMS notification indicating whether the stock's percent change is positive or negative.

  3. Receive SMS notifications with brief news headlines and descriptions related to the chosen stock.

## Notes

- Make sure you have valid API keys for Alpha Vantage and NewsAPI, as well as a Twilio account.
- The script fetches the latest news articles related to the chosen stock.
- This script can be customized and integrated into other applications or workflows.
