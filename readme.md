# Pikio articles scraper
Script downloads the content of articles posted on pikio.pl webpage.

## Getting started
All files needed to run the program are located in the folder. Start by installing prerequisites included in **requirements.txt**.
```
pip install requirements.txt
```

## Usage
usage: m<span>ain.py</span> [-h] -u URL [--first-task] [--second-task] [--third-task]

optional arguments:
  -h, --help         show this help message and exit
  -u URL, --url URL  Url to scrape - required field
  --first-task       Call to run first task
  --second-task      Call to run second task
  --third-task       Call to run third task

## Example
```
python3 main.py -u https://pikio.pl/psy-1312192-pp-niecenzuralne-slowa/ --first-task
```
Result of this call:
>Article content: Psy są niezwykle ważne dla pani Żanety. Gdy tyko zobaczyła ranne zwierzę, natychmiast zadzwoniła do ratownika. To, co usłyszała, zwala z nóg. Psy bardzo często są uzależnione od pomocy ludzi. Zdarza się, że ranne zwierzęta są zdane same na siebie, jeśli nikt nie zwróci na nie uwagi. Pani Żaneta nie chciała być obojętna na krzywdę czworono...

