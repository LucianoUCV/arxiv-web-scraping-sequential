import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time

# Automatically creates the output folder which will store the papers in a PDF format
def create_output_folder(folder_name = "pdfs"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name


# Sanitizes the title
def clean_filename(text):
    return re.sub(r'[\\/*?:"<>|]', "", text)


# Returns the URL with 2 added parameters ( query - the topic and page )
def get_search_url(query, page):
    return f"https://arxiv.org/search/?query={query}&searchtype=all&abstracts=show&order=-announced_date_first&size=50&start={page*50}"


# Scraping function ( using bp4 )
def scrape_arxiv(query, amount):
    articles = []
    page = 0

    while len(articles) < amount:
        url = get_search_url(query, page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        results = soup.find_all("li", attrs = {"class": "arxiv-result"})
        if not results:
            break

        for result in results:
            if len(articles) > amount:
                break
            title = result.find("p", attrs={"class": "title"}).text.strip()
            authors = [a.text.strip() for a in result.find("p", {"class": "authors"}).find_all("a")]
            abstract = result.find("span", attrs={"class": "abstract-full"}).text.strip().replace("\n", "")[
                       :-7].strip()
            pdfUrl = result.div.p.span.a['href']

            articles.append({
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "pdfUrl": pdfUrl
            })

        page += 1
    return articles


# Saving metadata in a JSON file and the papers pdfs in the output folder
def save_and_download(articles, folder = "pdfs", metadata_file="articles.json"):
    create_output_folder("pdfs")
    jsonArticles = []

    for article in articles:
        # Add article information to the list ( for the JSON file )
        jsonArticles.append({
            "title": article["title"],
            "authors": article["authors"],
            "abstract": article["abstract"],
            "pdfUrl": article["pdfUrl"]
        })

        # Download pdfs
        if article["pdfUrl"]:
            try:
                pdf_data = requests.get(article["pdfUrl"]).content
                safe_title = clean_filename(article["title"])[:100]
                filename = os.path.join(folder, f"{safe_title}.pdf")
                with open(filename, "wb") as pdf_file:
                    pdf_file.write(pdf_data)
            except Exception as e:
                print(f"Error downloading PDF: {e}")

    # Write data in JSON file
    with open("articles.json", "w", encoding="utf-8") as jsonFile:
        json.dump(jsonArticles, jsonFile, ensure_ascii=False, indent = 4) # type: ignore

    print(f"\033[35mData saved to \"{metadata_file}\" and PDFs stored in \"{folder}\"\033[0m")


def main():
    start_time = time.time()

    query = input("What subject sparks your interest?:\n")
    amount = int(input(f"How many papers matching \"{query}\" would you like?:\n"))
    articles = scrape_arxiv(query, amount)
    save_and_download(articles)

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time: {total_time}")

if __name__ == "__main__":
    main()
