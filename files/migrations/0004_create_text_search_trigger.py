from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_auto_20201122_2200'),
    ]

    migration = '''
        CREATE TRIGGER content_search_update BEFORE INSERT OR UPDATE
        ON files_file FOR EACH ROW EXECUTE FUNCTION
        tsvector_update_trigger(content_search_vector, 'pg_catalog.portuguese', content);

        -- Force triggers to run and populate the text_search column.
        UPDATE files_file set ID = ID;
    '''

    reverse_migration = '''
        DROP TRIGGER content_search_vector ON files_file;
    '''

    operations = [
        migrations.RunSQL(migration, reverse_migration)
    ]
