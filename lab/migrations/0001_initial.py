# Generated by Django 2.2 on 2019-05-23 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('generated_time', models.DateTimeField(auto_now_add=True)),
                ('generated_person', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=30)),
                ('type', models.IntegerField(choices=[(1, '谷类'), (2, '肉类'), (3, '蛋类'), (4, '奶类'), (5, '豆类'), (6, '鱼及海产'), (7, '蔬菜'), (8, '水果'), (9, '坚果及零食'), (10, '调味品'), (11, '食用油'), (12, '腌制食物'), (13, '其他')])),
                ('calorie', models.DecimalField(decimal_places=1, max_digits=4)),
                ('carbohydate', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('protein', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('fat', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('sodium', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('fiber', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('sugar', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('calcium', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('iron', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('phosphorus', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('potassium', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('zinc', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('vc', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('thiamin', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('riboflavin', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('niacin', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('va', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('ve', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('cholesterol', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(1, 'male'), (2, 'female')])),
                ('weight', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('disease', models.CharField(max_length=50)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='FoodUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_weight', models.DecimalField(decimal_places=1, max_digits=4)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Assessment')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Food')),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='foods',
            field=models.ManyToManyField(through='lab.FoodUse', to='lab.Food'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Patient'),
        ),
    ]
