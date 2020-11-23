# django-text-search

A proof of concept for different strategies on text searching with Django.

**This was not meant to production!**

- [ ] Full Text search
- [ ] Apache Solr
- [ ] Elasticsearch

## Importing data

You can import a csv containing a `url` and its `content` to make your own tests
by running:

```
docker-compose run --rm backend python manage.py import_csv files.csv
```

You can find a sample file in `data/`. The content of this dataset is in Brazilian portuguese.

## About the data

* 4740 files
* two columns: `url` and `content`
* about `content`: smallest have X characters (XX words) and biggest have Y characters (YY words)

## Testing


```
docker-compose run --rm backend python manage.py shell_plus --print-sql

File.objects.filter(content__search="merenda")

File.objects.filter(content_search_vector=SearchQuery(term, config='portuguese'))
```
