# scrapyzce

Storing the scraped data
-------------------------

The simplest way to store the scraped data is by using Feed exports, 
with the following command:

```bash
$ scrapy crawl zce_spider -o items.json
```

That will generate an items.json file containing all scraped items, serialized 
in JSON.
