import argparse
from scraper import PikioScraper


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="XBerry recrutation task - Igor Czyrski")
    parser.add_argument('-u', '--url', help="Url to scrape - required field", required=True)
    parser.add_argument('--first-task', help='Call to run first task', action='store_true')
    parser.add_argument('--second-task', help='Call to run second task', action='store_true')
    parser.add_argument('--third-task', help='Call to run third task', action='store_true')

    args = parser.parse_args()

    if sum([args.first_task, args.second_task, args.third_task]) == 0:
        print("No task selected")
        exit(0)

    pikio_scraper = PikioScraper(args.url)
    if not pikio_scraper.response_create_validate():
        print("Request error")
        exit(0)

    if args.first_task:
        print(pikio_scraper.get_article_content())

    if args.second_task:
        print(pikio_scraper.get_article_title())
        print(pikio_scraper.get_article_date())

    if args.third_task:
        pikio_scraper.get_article_photos()
        print("Images from article saved in /downloaded_photos")