# Generated by Django 2.2.16 on 2022-08-30 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20220830_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientquantity',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_quantity', to='recipes.Recipe', verbose_name='Рецепт'),
        ),
    ]
