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

The csv must not have a header.
