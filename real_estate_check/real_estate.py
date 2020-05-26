from seleniumbase import BaseCase
import csv
from datetime import date

class MyTestClass(BaseCase):

    def test_basic(self):
        with open('list.csv', 'a') as f:
            urls = ["Long-Beach_CA", "Redondo-Beach_CA", "Gardena_CA", "Torrance_CA", "Hawthorne_CA", "Culver-City_CA"
                    , "Playa-Vista_CA", "Playa-Del-Rey_CA" , "El-Segundo_CA", "Ladera-Heights_CA"
                    , "Fox-Hills_Culver-City_CA", "Lawndale_CA"]
            writer = csv.writer(f, delimiter=',')
            for url in urls:
                self.open("https://www.google.com/")
                self.update_text('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input'
                             , 'https://www.realtor.com/realestateandhomes-search/'+url+'\n')
                self.assert_element("#rso > div:nth-child(1) > div > div.s > div > span")
                extracted_text = self.driver.find_element_by_css_selector(
                    "#rso > div:nth-child(1) > div > div.s > div > span").text
                x = extracted_text.split()
                writer.writerow([str(date.today())]+[url]+[str(x[1])])
