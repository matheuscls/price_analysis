from scraping import WebScraping

checkin = ['2022-11-18', '2022-11-25', '2022-12-09', '2023-01-13']
checkout = ['2022-11-20', '2022-11-27', '2022-12-11', '2023-01-15']

url = f'https://www.airbnb.com.br/s/VG-Fun-Residence-Praia-do-Futuro--Praia-do-Futuro--Praia-do-Futuro--Brazil/homes?flexible_trip_lengths%5B%5D=one_week&date_picker_type=calendar&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=user_map_move&tab_id=home_tab&price_filter_input_type=0&price_filter_num_nights=2&checkin={checkin[2]}&checkout={checkout[2]}&query=VG%20Fun%20Residence%20Praia%20do%20Futuro%2C%20Praia%20do%20Futuro%2C%20Praia%20do%20Futuro&place_id=ChIJN9dI3ltGxwcRx8ZjVelykQI&ne_lat=-3.739147300315572&ne_lng=-38.435220162730275&sw_lat=-3.759017406136136&sw_lng=-38.46313659415728&zoom=15&search_by_map=true'
#url = f'https://www.airbnb.com.br/s/Vila-Do-Porto-Resort-Av-Dos-Oceanos-285-Porto-Das-Dunas--Porto-das-Dunas--Porto-das-Dunas--Brazil/homes?flexible_trip_lengths%5B%5D=one_week&date_picker_type=calendar&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=autocomplete_click&tab_id=home_tab&query=Vila%20Do%20Porto%20Resort%20Av%20Dos%20Oceanos%20285%20Porto%20Das%20Dunas%2C%20Porto%20das%20Dunas%2C%20Porto%20das%20Dunas&price_filter_input_type=0&price_filter_num_nights=2&checkin={checkin[2]}&checkout={checkout[2]}&place_id=ChIJOTyl9lRDxwcRJC1_OpXmzzA'
next_pages = []

web_scraping = WebScraping(url)
dict_listings = web_scraping.pick_all_rooms()
try:
    next_url = web_scraping.get_session_id()
except:
    next_url = None

while next_url is not None:
    web_scraping2 = WebScraping(next_url)
    next_page = web_scraping2.pick_all_rooms()
    next_pages.append(next_page)
    try:
        next_url = web_scraping2.get_session_id()
    except:
        next_url = None

for listings in next_pages:
    for listing in listings:
        dict_listings.append(listing)