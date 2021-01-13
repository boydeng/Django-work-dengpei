from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_dengpei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('sex', models.IntegerField(choices=[(1, '男'), (0, '女')])),
            ],
        ),
        migrations.CreateModel(
            name='yunpan_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit_date', models.DateField()),
                ('headline', models.CharField(max_length=200)),
                ('attach', models.FileField(upload_to='')),
                ('remark', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.student_dengpei')),
            ],
        ),
    ]
