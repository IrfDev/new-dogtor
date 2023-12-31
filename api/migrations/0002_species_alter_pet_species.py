# Generated by Django 4.2.7 on 2023-11-09 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Species",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name="pet",
            name="species",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="api.species"
            ),
        ),
    ]
