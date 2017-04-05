# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_projekt'),
    ]

    operations = [
        migrations.AddField(
            model_name='projekt',
            name='image_url',
            field=models.ImageField(upload_to='images', default=None),
        ),
    ]
