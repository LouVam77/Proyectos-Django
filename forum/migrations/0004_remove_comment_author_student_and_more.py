# Generated by Django 4.2.7 on 2023-12-03 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_remove_comment_student_comment_author_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author_student',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author_teacher',
        ),
        migrations.CreateModel(
            name='Commenters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.student')),
                ('author_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='forum.commenters'),
        ),
    ]
