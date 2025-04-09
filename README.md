# arXiv Web Scraper ( Sequential )
This is a Python project that allows you to scrape research papers from arXiv.org. You can search for papers based on a query and retrieve their metadata (such as authors, abstract, and PDF links) as well as download the corresponding PDFs.

## Features
* Search for research papers based on specific keywords on arXiv.

* Scrape metadata such as title, authors, abstract ( summary ), and PDF URL.

* Download the PDFs of the papers into an automatically created output folder.

* Save metadata in a JSON file for future reference.

## Project Requirements
* **Algorithm**: Web scraping in a sequential manner using BeautifulSoup to extract data from arXiv.org.

* **Programming Language**: Python 3.

* **External libraries**: `requests`, `bs4` (BeautifulSoup), `os`, `json`, `re`, `time`


## Project Structure
* `main.py`: Main Python script for scraping data.
* `README.MD`: Project info and user guide.


## How to use
1. Clone the repository to your local machine: <br>
```bash
git clone https://github.com/LucianoUCV/arxiv-web-scraping-sequential.git
```
2. Navigate to the project directory: <br>
```bash
cd arxiv-web-scraper
```

3. Run the script:<br>
```bash
python main.py
```
4. Enter a search query and the number of papers you want to scrape.

## Expected Output
* A "pdfs" folder containing the downloaded PDF files of the scraped papers.
* An "articles.json" file containing metadata about the papers ( title, authors, abstract, and PDF URL )

---

### The [Google Doc](https://docs.google.com/document/d/1NvsXqRVfJSIbVowtc2CUaf6xblmApB0sx64_y3_wFlk/edit?usp=sharing) includes more useful information:

