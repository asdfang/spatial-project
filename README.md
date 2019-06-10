# spatial-project

## To scrape:
In `niche.py`, replace line 10 with the list of zip codes that Niche grades are needed for, and uncomment line 10 and 11. Then, in the `nichescrape` directory, run `scrapy crawl niche -o [filename].csv -t csv`.
