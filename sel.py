from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  # Replace with the appropriate driver for your browser

def open_link_in_new_tab(url):
    # Open the link in a new tab using JavaScript
    driver.execute_script("window.open('{}', '_blank');".format(url))

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])

# Example usage
links = ["https://www.otodom.pl/pl/wyniki/sprzedaz/dom/wiele-lokalizacji?distanceRadius=0&page=1&limit=36&ownerTypeSingleSelect=ALL&locations=[pomorskie/wejherowski/gmina-wiejska--wejherowo/gowino,pomorskie/kartuski/przodkowo/zaleze,pomorskie/wejherowski/szemud,pomorskie/wejherowski/szemud/donimierz,pomorskie/wejherowski/szemud/lebno,pomorskie/kartuski/zukowo,pomorskie/wejherowski/szemud/dobrzewino,pomorskie/wejherowski/szemud/bojano,pomorskie/gdansk/gdansk/gdansk,pomorskie/wejherowski/szemud/kielno,pomorskie/wejherowski/szemud/koleczkowo,pomorskie/kartuski/zukowo/chwaszczyno]&by=DEFAULT&direction=DESC&viewType=listing",
         "https://www.mobile.de/pl/kategoria/ciężarowe/vhc:truckover7500,pgn:2,pgs:50,srt:date,sro:desc,frn:2015,vcg:tippertruck,ax:3-3",
           "https://www.mobile.de/pl/kategoria/ciągniki-siodłowe/vhc:semitrailertruck,pgn:14,pgs:20,srt:date,sro:desc,frn:2015,wf:wheel_drive_4x4",
        "https://www.mobile.de/pl/kategoria/maszyny-budlowlane/vhc:constructionmachine,pgn:13,pgs:10,srt:date,sro:desc,ycn:2015,vcg:mobiledigger",
           "https://www.otomoto.pl/ciezarowe/wywrotki/od-2015?search[filter_float_wheel_axis:from]=4&search[filter_float_wheel_axis:to]=4&page=3&search[advanced_search_expanded]=true",
           "https://www.otomoto.pl/ciezarowe/uzytkowe/od-2015?search[filter_enum_features]=4x4&search[advanced_search_expanded]=true",
           "https://www.otomoto.pl/maszyny-budowlane/koparki-kolowe/sprzedaz/od-2015",
           "https://www.olx.pl/motoryzacja/ciezarowe/wywrotka/?search[filter_float_axes:from]=3&search[filter_float_axes:to]=3&search[filter_float_year:from]=2018",
           "https://finsterwalder.de/startseite/fahrzeuge"]


for link in links:
    open_link_in_new_tab(link)
    time.sleep(1)

# Keep the browser open until the user presses Enter
input("Press Enter to close the browser.")



# from selenium import webdriver
# import time

# driver = webdriver.Edge()  # Replace with the appropriate driver for your browser
# def open_link_in_browser(url):
#     driver.get(url)

# # Example usage
# links = [
#     "https://www.mobile.de/pl/kategoria/ci%C4%99%C5%BCarowe/vhc:truckover7500,frn:2006,vcg:tippertruck,ax:4-",
#     "https://www.mobile.de/pl/kategoria/ci%C4%99%C5%BCarowe/vhc:truckover7500,frn:2015,vcg:tippertruck,ax:3-3",
#     "https://www.mobile.de/pl/kategoria/ci%C4%85gniki-siod%C5%82owe/vhc:semitrailertruck,frn:2006,frx:2023,vcg:standardtractorandtrailerunit,ax:2-2,wf:wheel_drive_4x4",
#     "https://www.mobile.de/pl/kategoria/maszyny-budlowlane/vhc:constructionmachine,ycn:2006,ycx:2023,vcg:mobiledigger",
#     "https://www.otomoto.pl/ciezarowe/wywrotki/od-2006?search%5Bfilter_float_wheel_axis%3Afrom%5D=3&search%5Bfilter_float_wheel_axis%3Ato%5D=4",
#     "https://www.otomoto.pl/ciezarowe/uzytkowe/od-2006?search%5Bfilter_enum_features%5D=4x4&search%5Bfilter_float_wheel_axis%3Afrom%5D=2&search%5Bfilter_float_wheel_axis%3Ato%5D=2",
#     "https://www.otomoto.pl/maszyny-budowlane/koparki-kolowe/sprzedaz/od-2006"
# ]
# for i in links:
#     open_link_in_browser(i)
#     time.sleep(1) 




