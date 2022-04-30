from django.db import models
import uuid
from datetime import datetime
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

# Create your models here.
# To use:
# python manage.py shell
#
# from blog.models import PostModel
# p = PostModel.objects.create(title='How To Deploy An App', body='This is the body')
# p.save()
#
#


class PostModel(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    title = columns.Text(required=True)
    body = columns.Text(required=True)
    created_at = columns.DateTime(default=datetime.now)