import requests
from bs4 import BeautifulSoup

def get_price_amazon(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find(id="productTitle").get_text(strip=True)
    price = soup.find("span", class_="a-price-whole")
    price_text = price.get_text(strip=True) if price else "Not found"
    
    return title, price_text

# Test it
if __name__ == "__main__":
    url = "https://www.amazon.in/dp/B09G9D8KRQ"  # Example product link
    title, price = get_price_amazon(url)
    print(f"Product: {title}\nPrice: ₹{price}")
