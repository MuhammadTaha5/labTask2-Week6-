import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient



base_url = "https://papers.nips.cc"
page_url = "https://papers.nips.cc/paper_files/paper/2024"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(page_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

papers = []

for li in soup.select("ul.paper-list li.conference"):
    title_tag = li.find("a")
    authors_tag = li.find("i")

    title = title_tag.text.strip()
    link = base_url + title_tag["href"]


    authors = [a.strip() for a in authors_tag.text.split(",")]

    papers.append({
        "title": title,
        "link": link,
        "authors": authors
    })

print("Scraped:", len(papers), "papers")


client = MongoClient("mongodb://localhost:27017/")

db = client["nips2024"]
collection = db["papers"]


collection.delete_many({})


collection.insert_many(papers)

print("Data saved to local MongoDB successfully!")
