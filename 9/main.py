"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
import os
import csv
import requests
from io import StringIO
from typing import Union
from flask import Flask, request, render_template, redirect, make_response
from bs4 import BeautifulSoup

root = os.path.abspath(os.path.dirname(__file__))

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}

job_urls = [
    "https://stackoverflow.com/jobs?r=true&q={term}",
    "https://weworkremotely.com/remote-jobs/search?term={term}",
    "https://remoteok.io/remote-dev+{term}-jobs",
]

db = {}


def get_jobs(term: str):
    for job_url in job_urls:
        url = job_url.format(term=term)
        soup = soup_page(url)
        if not soup:
            continue

        jobs = scrape_page(term, url, soup)
        if not db.get(term):
            db[term] = []

        db[term].extend(jobs)


def soup_page(url: str) -> Union[BeautifulSoup, None]:
    try:
        response = requests.get(url, headers=headers)
        if response.status_code >= 300:
            return

        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    except Exception as e:
        print(e)


def scrape_page(term: str, url: str, soup: BeautifulSoup):
    if "stackoverflow" in url:
        return scrape_so(soup)
    elif "weworkremotely" in url:
        return scrape_we(soup)
    elif "remoteok" in url:
        return scrape_ro(soup)


def scrape_so(soup: BeautifulSoup):
    jobs = []
    job_sections = soup.select("div.listResults > div")
    for job_section in job_sections:
        title_element = job_section.select_one("h2 > a")
        if title_element:
            title = title_element.text.strip()
            link = title_element.get("href")
            company = job_section.select_one("h3 > span").text.strip()

            job = {
                "title": title,
                "link": f"https://stackoverflow.com{link}",
                "company": company,
            }
            jobs.append(job)

    return jobs


def scrape_we(soup: BeautifulSoup):
    jobs = []
    job_sections = soup.select("article > ul > li")
    for job_section in job_sections:
        title_element = job_section.select_one("span.title")
        if title_element:
            title = title_element.text.strip()
            link = job_section.select_one("a").get("href")
            company = job_section.select_one("span.company").text.strip()

            job = {
                "title": title,
                "link": f"https://weworkremotely.com/{link}",
                "company": company,
            }
            jobs.append(job)
    return jobs


def scrape_ro(soup: BeautifulSoup):
    jobs = []
    job_sections = soup.select("tr.job")
    for job_section in job_sections:
        title = job_section.select_one("h2").text.strip()
        link = job_section.select_one("a").get("href")
        company = job_section.select_one("a.companyLink").text.strip()

        job = {
            "title": title,
            "link": f"https://remoteok.io/{link}",
            "company": company,
        }
        jobs.append(job)
    return jobs


app = Flask("DayThirteen", template_folder=f"{root}/templates")


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/search", methods=["GET"])
def search():
    term: str = request.args.get("term", str)
    term: str = term.lower()

    if not db.get(term):
        get_jobs(term)

    jobs = db[term]
    total_count = len(jobs)

    return render_template("search.html", term=term, total_count=total_count, jobs=jobs)


@app.route("/export", methods=["GET"])
def export():
    term: str = request.args.get("term", str)
    term: str = term.lower()

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=["title", "company", "link"])
    writer.writeheader()
    for row in db[term]:
        writer.writerow(row)

    response = make_response(output.getvalue())
    response.headers["Content-Disposition"] = f"attachment; filename={term}.csv"
    response.headers["Content-type"] = "text.csv"
    return response


app.run(host="0.0.0.0", debug=True)
