import requests
from bs4 import BeautifulSoup
import json

def scrape_arxiv(query):
    response = requests.get(f"https://arxiv.org/search/?query={query}&searchtype=all&abstracts=show&order=-announced_date_first&size=50")

    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("li", attrs = {"class": "arxiv-result"})

    jsonArticles = []
    for article in articles:
        title = article.find("p", attrs = {"class": "title"}).text.strip()
        authors = [a.text.strip() for a in article.find("p", {"class": "authors"}).find_all("a")]
        abstract = article.find("span", attrs = {"class": "abstract-full"}).text.strip().replace("\n","")[:-7].strip()
        pdfUrl = article.div.p.span.a['href']

        arxivArticle = {
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "pdfUrl": pdfUrl
        }

        jsonArticles.append(arxivArticle)

    with open("articles.json", "w", encoding="utf-8") as jsonFile:
        json.dump(jsonArticles, jsonFile, ensure_ascii=False, indent = 4)


def main():
    query = input("What subject sparks your interest?:\n")
    scrape_arxiv(query)

if __name__ == "__main__":
    main()
