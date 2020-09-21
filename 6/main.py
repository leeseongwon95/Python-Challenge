import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")


def get_superbrand():
    URL = "http://www.alba.co.kr"
    LIST = []

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    super_brands = soup.select("#MainSuperBrand > ul.goodsBox > li")

    for super_brand in super_brands:
        name_link = {}
        name = super_brand.select("img")
        if name != None and len(name) > 0 and name[0] and name[0]['alt']:
            name_link['name'] = name[0]['alt']
        else:
            name_link['name'] = ""
        link = super_brand.select("a.goodsBox-info")
        if link != None and len(link) > 0:
            name_link['link'] = link[0]['href']
        else:
            link = super_brand.select("a.brandHover")
            if link != None and len(link) > 0:
                name_link['link'] = link[0]['href']
            else:
                name_link['link'] = ""

        LIST.append(name_link)

    return LIST


def save_csv(filename, data_tabe):
    with open(f"{filename}.csv", mode='w') as file:
        writer = csv.writer(file)
        for data_row in data_tabe:
            writer.writerow(data_row)
    print(f"Create {filename}.csv")


def extract_alba(LIST):
    for superbrand_name_link in LIST:
        brand_name = superbrand_name_link['name']
        brand_link = superbrand_name_link['link']
        if brand_name == None or brand_link == None:
            continue
        print(brand_name, brand_link)
        brand_request = requests.get(superbrand_name_link['link'])
        brand_soup = BeautifulSoup(brand_request.text, "html.parser")
        nomal_jobs_num = brand_soup.select('#NormalInfo > p.jobCount > strong')
        if len(nomal_jobs_num) > 0:
            nomal_jobs_num = nomal_jobs_num[0].text
        else:
            nomal_jobs_num = brand_soup.select(
                '#NormalInfo > p.listCount > strong')[0].text
        print(nomal_jobs_num, '건')
        if nomal_jobs_num == '0':
            print()
            print()
            continue

        nomal_jobs = brand_soup.select("#NormalInfo > table > tbody > tr")

        nomal_job_list = []
        nomal_job_list.append(["place", "title", "time", "pay", "date"])
        for nomal_job in nomal_jobs:
            if len(nomal_job['class']) > 0 and nomal_job['class'][0] == 'summaryView':
                continue

            place = nomal_job.select('td.local')
            if len(place) > 0:
                place = place[0].text
            title = nomal_job.select('td.title span.company')
            if len(title) > 0:
                title = title[0].text
            time = nomal_job.select('td.data span.time')
            if len(time) > 0:
                time = time[0].text
            pay = nomal_job.select('td.pay span.number')
            if len(pay) > 0:
                pay = pay[0].text
            date = nomal_job.select('td.regDate')
            if len(date) > 0:
                date = date[0].text

            nomal_job_list.append([place, title, time, pay, date])
        for nomal_job in nomal_job_list:
            print(nomal_job)

        save_csv(brand_name, nomal_job_list)
        print()
        print()


LIST = get_superbrand()
print(LIST)
print()
print()
extract_alba(LIST)
print()
print()
print("extract end!")
