# Generated by Django 5.0.3 on 2024-05-17 19:17

import django.db.models.deletion
import grocery_store_app.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_datatime', models.DateTimeField(blank=True, default=grocery_store_app.models.get_datetime, null=True, validators=[grocery_store_app.models.check_created_datatime], verbose_name='created_datatime')),
                ('modified_datatime', models.DateTimeField(blank=True, default=grocery_store_app.models.get_datetime, null=True, validators=[grocery_store_app.models.check_modified_datatime], verbose_name='modified_datatime')),
                ('title', models.TextField(max_length=100, verbose_name='title')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': '"grocery_store"."categories"',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_datatime', models.DateTimeField(blank=True, default=grocery_store_app.models.get_datetime, null=True, validators=[grocery_store_app.models.check_created_datatime], verbose_name='created_datatime')),
                ('modified_datatime', models.DateTimeField(blank=True, default=grocery_store_app.models.get_datetime, null=True, validators=[grocery_store_app.models.check_modified_datatime], verbose_name='modified_datatime')),
                ('money', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, validators=[grocery_store_app.models.check_positive], verbose_name='money')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
                'db_table': '"grocery_store"."client"',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_datatime', models.DateTimeField(blank=True, default=grocery_store_app.models.get_datetime, null=True, validators=[grocery_store_app.models.check_created_datatime], verbose_name='created_datatime')),
                ('modified_datatime', models.DateTimeField(blank=True, default=grocery_store_app.models.get_datetime, null=True, validators=[grocery_store_app.models.check_modified_datatime], verbose_name='modified_datatime')),
                ('title', models.TextField(max_length=200, verbose_name='title')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7, validators=[grocery_store_app.models.check_positive], verbose_name='price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery_store_app.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': '"grocery_store"."products"',
                'ordering': ['category', 'title', 'price'],
            },
        ),
        migrations.CreateModel(
            name='ProductToPromotion',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_datatime', models.DateTimeField(blank=True, default=grocery_store_app.models.get_datetime, null=True, validators=[grocery_store_app.models.check_created_datatime], verbose_name='created_datatime')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery_store_app.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Relationship product to promotion',
                'verbose_name_plural': 'Relationships product to promotion',
                'db_table': '"grocery_store"."product_to_promotion"',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_datatime', models.DateTimeField(blank=True, default=grocery_store_app.models.get_datetime, null=True, validators=[grocery_store_app.models.check_created_datatime], verbose_name='created_datatime')),
                ('modified_datatime', models.DateTimeField(blank=True, default=grocery_store_app.models.get_datetime, null=True, validators=[grocery_store_app.models.check_modified_datatime], verbose_name='modified_datatime')),
                ('title', models.TextField(max_length=200, verbose_name='title')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='description')),
                ('discount_amount', models.PositiveSmallIntegerField(default=0, validators=[grocery_store_app.models.check_max_discount_amount], verbose_name='discount amount')),
                ('start_date', models.DateField(validators=[grocery_store_app.models.check_start_date], verbose_name='start date')),
                ('end_date', models.DateField(blank=True, null=True, validators=[grocery_store_app.models.check_end_date], verbose_name='end date')),
                ('products', models.ManyToManyField(through='grocery_store_app.ProductToPromotion', to='grocery_store_app.product', verbose_name='products')),
            ],
            options={
                'verbose_name': 'promotion',
                'verbose_name_plural': 'promotions',
                'db_table': '"grocery_store"."promotions"',
                'ordering': ['discount_amount'],
            },
        ),
        migrations.AddField(
            model_name='producttopromotion',
            name='promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery_store_app.promotion', verbose_name='promotion'),
        ),
        migrations.AddField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(through='grocery_store_app.ProductToPromotion', to='grocery_store_app.promotion', verbose_name='promotions'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_datatime', models.DateTimeField(blank=True, default=grocery_store_app.models.get_datetime, null=True, validators=[grocery_store_app.models.check_created_datatime], verbose_name='created_datatime')),
                ('modified_datatime', models.DateTimeField(blank=True, default=grocery_store_app.models.get_datetime, null=True, validators=[grocery_store_app.models.check_modified_datatime], verbose_name='modified_datatime')),
                ('text', models.TextField(max_length=1000, verbose_name='text')),
                ('rating', models.PositiveSmallIntegerField(blank=True, default=5, null=True, validators=[grocery_store_app.models.check_max_rating], verbose_name='rating')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery_store_app.client', verbose_name='client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery_store_app.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
                'db_table': '"grocery_store"."reviews"',
                'ordering': ['rating'],
            },
        ),
        migrations.CreateModel(
            name='CategoryToCategory',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_datatime', models.DateTimeField(blank=True, default=grocery_store_app.models.get_datetime, null=True, validators=[grocery_store_app.models.check_created_datatime], verbose_name='created_datatime')),
                ('child_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_categories', to='grocery_store_app.category', verbose_name='child_category')),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_categories', to='grocery_store_app.category', verbose_name='parent_category')),
            ],
            options={
                'verbose_name': 'Relationship category to category',
                'verbose_name_plural': 'Relationships category to category',
                'db_table': '"grocery_store"."category_to_category"',
                'unique_together': {('parent_category', 'child_category')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='producttopromotion',
            unique_together={('product', 'promotion')},
        ),
    ]
