from __future__ import absolute_import

from raven.contrib.django.raven_compat.models import client

client.context.merge({'user': {
    'email': 'nel@neil.com'
}})
client.context.merge({'tags': {
    'abc': 'nel@neil.com'
}})