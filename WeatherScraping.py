#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created Mon Dec  7 13:53:09 2020 by jordan_ehler"""

import bs4, requests, pandas as pd, pprint


url = "https://weather.gc.ca/city/pages/ns-19_metric_e.html"
page = requests.get(url)

soup = bs4.BeautifulSoup(page.text, "html.parser")

#info = soup.select("dl", {'class':'attributes dl-horizontal'})

info = soup.select("dd", class_ = "mrgn-bttm-0 wxo-metric-hide")


pprint.pprint(info[8])

#comp_info = pd.DataFrame()
#cleaned_id_text = []
#for i in info[0].find_all('dt'):
#    cleaned_id_text.append(i.text)
#cleaned_id__attrb_text = []
#for i in info[0].find_all('dd'):
#    cleaned_id__attrb_text.append(i.text)
#
#comp_info['Id'] = cleaned_id_text
#comp_info['Attribute'] = cleaned_id__attrb_text
#comp_info