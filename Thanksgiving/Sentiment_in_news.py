# Robert Bayer
# First Thanksgiving Assignment (Problem C)
# Takes a news article or website and analyzes the sentiment of each article.

#DEPENDING ON THE VERSION YOU WANT TO USE, DELETE THE TRIPLE QUOTES AROUND THE ONE YOU WANT TO USE


import requests
from bs4 import BeautifulSoup as bs
from pip._vendor.distlib.compat import raw_input
from textblob import TextBlob as tb

choice = ""

cybertruck = ["www.cnet.com/roadshow/news/tesla-cybertruck-aerodynamics/", "cleantechnica.com/2019/11/28/who-is-actually-going-to-buy-a-tesla-cybertruck/", "www.digitaltrends.com/cars/teslas-elon-musk-says-yes-to-fords-f-150-cybertruck-challeng"]
choices = [1,2]
while choice not in choices:
    choice = input("""Do you want to input a url or see the program demonstrated with articles for Tesla's Cybertruck
1. My URL
2. Cybertruck
Enter your choice: """)
    if choice.isdigit():
        choice = int(choice)

if choice == choices[0]:
    try:
        url = raw_input("Please enter a URL: http://")
        url = "https://" + url
        response = requests.get(url)
        soup = bs(response.content, 'html5lib')
        text = soup.get_text(strip=True)

        blob = tb(text)
        result = blob.sentiment


        print(f'The site "{url}" gives the following sentiment results: {result}')

    except Exception as e:
        print("Sorry, we've run in to an issue...")
        print(e)


elif choice == choices[1]:
    for site in cybertruck:
        try:
            url = "https://" + site
            response = requests.get(url)
            soup = bs(response.content, 'html5lib')
            text = soup.get_text(strip=True)

            blob = tb(text)
            result = blob.sentiment

            print(f'The site "{url}" gives the following sentiment results: {result}')

        except Exception as e:
            print("Sorry, we've run into an issue...")
            print(e)

else:
    input("Sorry, somthing has happened. Try again later...")