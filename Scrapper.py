import requests
from bs4 import BeautifulSoup
import urllib

def scrape_images(url, num_images):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    img_tags = soup.find_all("img")

   
    image_urls = [img["src"] for img in img_tags]


    for i, url in enumerate(reversed(image_urls)):
        if i >= num_images:
            break
        try:
            urllib.request.urlretrieve(url, f"image{i+1}.jpg")
            print(f"Downloaded image{i+1}.jpg")
        except:
            print(f"Error downloading image{i+1}.jpg")


url = "https://www.airbnb.co.uk/s/Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=filter_change&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-07-01&monthly_length=3&price_filter_input_type=2&price_filter_num_nights=5&channel=EXPLORE&place_id=ChIJA9KNRIL-1BIRb15jJFz1LOI&date_picker_type=calendar&checkin=2023-06-16&checkout=2023-06-30"
num_images = 10

scrape_images(url, num_images)
