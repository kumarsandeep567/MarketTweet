# MarketTweet Analyzer: Predicting Stock Trends via Tweets

This project, MarketTweet Analyzer, utilizes machine learning techniques to predict stock market trends, with a specific focus on analyzing Twitter data and employing Support Vector Machine (SVM) models for accurate predictions.

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Important Note Regarding Twitter Data Collection

Due to restrictions on collecting historical Twitter data, it is imperative to update certain parameters in the `DownloadTwitterData.py` file. Please follow these guidelines to ensure accurate data collection:

1. **Update Current Date:**

   In the `DownloadTwitterData.py` file, locate the line containing the initialization of the `TwitterData` object:

   ```python
   twitterData = get_twitter_data.TwitterData('DD-MM-YYYY')
   ```

   Replace `'DD-MM-YYYY'` with the current date. This ensures that the script collects Twitter corpus data for the past week from the specified date.

2. **Adjust Date Range for Yahoo Finance Data:**

   Similarly, in the same file, find the line initializing the `YahooData` object:

   ```python
   yahooData = get_yahoo_data.YahooData('DD-MM-YYYY', 'DD-MM-YYYY')
   ```

   Modify the date range parameters `'DD-MM-YYYY'` to match your desired date range for collecting historical Yahoo Finance data. This range should align with the Twitter data collection period to maintain coherence in the dataset.

## Instructions to Execute

1. **Twitter API Key:**

   Obtain your Twitter API key from [Twitter Developer Portal](https://developer.twitter.com/). This key is necessary for accessing Twitter data.

2. **Configure `config.json` File:**

   Update your Twitter API credentials in the `config.json` file as follows:

   ```json
   {
       "consumer_key": "ADD_YOUR_CONSUMER_KEY_HERE",
       "consumer_secret": "ADD_YOUR_CONSUMER_SECRET",
       "access_token": "ADD_YOUR_ACCESS_TOKEN_HERE",
       "access_token_secret": "ADD_YOUR_ACCESS_TOKEN_SECRET_HERE"
   }
   ```

3. **Run `DownloadTwitterData.py` Script:**

   Execute the `DownloadTwitterData.py` script to perform the following tasks:
   - Download Twitter data
   - Download Yahoo Finance data
   - Create feature set
   - Design feature matrix
   - Analyze and predict tweet sentiment using Naïve Bayes classification and Support Vector Machine
   
   Example Usage:
   To download data for Nvidia Corporation, run
   ```bash
   python DownloadTwitterData.py NVDA
   ```
   Replace `NVDA` with the appropriate stock symbol (e.g. MSFT for Microsoft Corporation).

4. **Run `StockPrediction.py` Script:**

   Execute the `StockPrediction.py` script, which contains the basic code for stock prediction analysis. The stock market movement is predicted using a Support Vector Machine model.

5. **Ensure Active Internet Connection:**

   Since the application predicts outcomes in real-time, ensure that you have an active internet connection throughout the execution process.