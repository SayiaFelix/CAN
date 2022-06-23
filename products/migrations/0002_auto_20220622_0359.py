# Generated by Django 3.2.10 on 2022-06-22 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='admin',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='fullname',
            new_name='contact',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='contacts',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_pic',
            field=models.ImageField(null=True, upload_to='product_pic'),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='profiles/'),
        ),
        migrations.AlterField(
            model_name='business',
            name='business_pic',
            field=models.ImageField(null=True, upload_to='business_pic'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, default=1, max_length=200),
            preserve_default=False,
        ),
    ]