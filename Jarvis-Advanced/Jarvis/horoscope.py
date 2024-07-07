import requests
from bs4 import BeautifulSoup

def horoscope(zodiac, day="today"):
    zodiac_sign = {
        "Aries": 1, "Taurus": 2, "Gemini": 3, "Cancer": 4,
        "Leo": 5, "Virgo": 6, "Libra": 7, "Scorpio": 8,
        "Sagittarius": 9, "Capricorn": 10, "Aquarius": 11, "Pisces": 12
    }
    
    url = f"https://www.horoscope.com/us/horoscope/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign[zodiac]}"
    result = requests.get(url)
    soup = BeautifulSoup(result.content, "html.parser")
    data = soup.find("div", attrs={'class': "main-horoscope"})
    
    if data is not None:
        horoscope_text = data.p.text.strip()
        print(horoscope_text)
        return horoscope_text
    else:
        print("Horoscope data not found.")
        return None

horoscope("Cancer")
