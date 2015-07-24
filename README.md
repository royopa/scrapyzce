# scrapyzce

Generating news URL to use in crawler
-------------------------------------

To generate new urls to use in crawler, use the command below:

```bash
$ python generate_urls_crawler.py
```

That will generate an urls_to_check.txt file containing all urls for use in
crawler.

Storing the scraped data
-------------------------

The simplest way to store the scraped data is by using Feed exports,
with the following command:

```bash
$ scrapy crawl zce_spider -o items.json
```

Or

```bash
$ scrapy crawl zce_spider -o items.csv -t csv
```

That will generate an items.json or items.csv file containing all scraped items.
