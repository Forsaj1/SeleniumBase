from seleniumbase import BaseCase
import csv
from datetime import date

class MyTestClass(BaseCase):

    def test_basic(self):
        with open('adsupply.csv', 'r') as reader:
            redirects = reader.readlines()
            domains = []
            with open('redirected_urls.csv', 'a') as f:
                writer = csv.writer(f, delimiter=',')
                for redirect in redirects:
                    self.open(redirect)
                    self.ad_block()
                    self.remove_elements('iframe')
                    self.wait_for_element_present('title', timeout=1)

                    ad_url = self.get_current_url()
                    split_url = ad_url.split('/')
                    domains.append(split_url[2])  # here can domain check happen
                    writer.writerow('\n'+[redirect]+['>>']+[ad_url]+['>>']+[split_url])
            temp = set(domains)
            result = {}
            for i in temp:
                result[i] = domains.count(i)
            with open('redirected_urls.csv', 'a') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow('\n'+[str(date.today())]+'Domains:'+[result])
