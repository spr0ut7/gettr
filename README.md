# 'Gettr' - Article Scraper

A Python script to scrape articles from URLs and save them as text files.

## Features
- Extracts article title and content using the `newspaper3k` library
- Organizes articles into folders by domain
- Cleans text by removing advertisements and excessive empty lines
- Saves articles with metadata (title, source URL)

## Requirements
- Python 3.x
- `newspaper3k` library (`pip install newspaper3k`)

## Usage
Run the script from the command line:
```bash
python gettr.py <URL>
```
Example:
```bash
python gettr.py https://example.com/article
```

## Output
- Articles are saved in `articles/<domain>/<title>.txt`
- Each file contains the article title, cleaned content, and source URL

## License
MIT
