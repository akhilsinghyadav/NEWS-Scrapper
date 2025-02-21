# NEWS-Scrapper
Simple News Scrapper (based on Flask API )

This is a simple web application that scrapes and displays the latest news headlines from *The Hindu* and *Indian Express*. The backend is built using Flask, and the frontend is a static HTML page that fetches data from the API.

## Features

- Scrapes the latest news from *The Hindu* and *Indian Express*.
- Displays news headlines side by side in a clean, responsive layout.
- Fetches data dynamically using JavaScript.
- Option to include news images (if available).
- Uses Flask as the backend API.

## Technologies Used

- **Backend**: Python, Flask, BeautifulSoup (for web scraping)
- **Frontend**: HTML, CSS, JavaScript
- **Others**: Flask-CORS (for handling cross-origin requests)

## Installation and Setup

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/news-scraper.git
cd news-scraper

```

### 2. Create a Virtual Environment 
```sh
python -m venv scrape
source scrape/bin/activate  # On Windows use `scrape\Scripts\activate`
```
### 3. Install Dependencies
```sh
pip install -r requirements.txt

```
### 4. Run the Backend Server
```sh
python backend.py
```
### 5. Frontends
PREFER  ----> test.html   (supports BOTH)

Note: frontend.html has single functionality i.e. The Hindu   .   


![Img1](https://github.com/akhilsinghyadav/NEWS-Scrapper/blob/main/Screenshot1.jpg)
![Img2](https://github.com/akhilsinghyadav/NEWS-Scrapper/blob/main/Screenshot2.jpg)
## API ENDPOINTS
-GET /headlines_ie → Fetches news from Indian Express.
-GET /headlines_th → Fetches news from The Hindu.

![Img3](https://github.com/akhilsinghyadav/NEWS-Scrapper/blob/main/Screenshot3.jpg)
![Img4](https://github.com/akhilsinghyadav/NEWS-Scrapper/blob/main/Screenshot4.jpg)


## Project Structure 
```sh
news-scraper/
│── backend.py          # Flask backend
│── thehindu.py         # Scraper for The Hindu
│── indianexpress.py    # Scraper for Indian Express
│── frontend.html       # Frontend UI
│── requirements.txt    # Python dependencies
│── .gitignore          # Git ignore file
│── README.md           # Project documentation

```


