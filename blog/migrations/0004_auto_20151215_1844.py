# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_projekt_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projekt',
            name='image_url',
            field=models.ImageField(default='images/no-img.jpg', upload_to='images'),
        ),
    ]
