import streamlit as st
import requests

# Define News API parameters
API_KEY = "YOUR_NEWS_API_KEY"
BASE_URL = "https://newsapi.org/v2/top-headlines"
DEFAULT_COUNTRY = "us"

# Function to fetch news headlines
def fetch_news(country=DEFAULT_COUNTRY):
    params = {
        "country": country,
        "apiKey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

# Create the news app
def news_app():
    st.title("News App")
    
    # Choose country
    country = st.selectbox("Select Country", ["United States", "United Kingdom", "India"])
    country_code = {"United States": "us", "United Kingdom": "gb", "India": "in"}.get(country, DEFAULT_COUNTRY)

    # Fetch news headlines
    data = fetch_news(country_code)

    # Display headlines
    if data["status"] == "ok":
        articles = data["articles"]
        st.write("### Top Headlines:")
        for article in articles:
            st.write(f"- **{article['title']}**")
            st.write(f"  Source: {article['source']['name']}")
            st.write(f"  Published at: {article['publishedAt']}")
            st.write(f"  {article['description']}")
            st.write("[Read more]({})".format(article["https://news.google.co.in/"]))
            st.write("---")
    else:
        st.error("Failed to fetch news. Please try again later.")

# Run the app
if __name__ == "__main__":
    news_app()
