# Generated by Django 5.1.7 on 2025-05-17 13:40

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("patronymic", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("admin", "Админ"),
                            ("curator", "Куратор"),
                            ("moderator", "Модератор"),
                            ("specialist", "Специалист"),
                            ("volunteer", "Волонтер"),
                            ("blocked", "Заблокированный"),
                        ],
                        default="specialist",
                        max_length=20,
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        choices=[("M", "Мужской"), ("F", "Женский")], max_length=1
                    ),
                ),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("region", models.CharField(default="", max_length=100)),
                ("address", models.TextField(default="")),
                ("organization", models.CharField(default="", max_length=200)),
                ("position", models.CharField(default="", max_length=100)),
                ("phone", models.CharField(default="", max_length=20)),
                (
                    "registration_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Chapter",
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
                ("title", models.CharField(max_length=50)),
                ("written_at", models.DateTimeField(auto_now_add=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("status", models.CharField(default="draft", max_length=20)),
                ("is_published", models.BooleanField(default=False)),
                ("is_deleted", models.BooleanField(default=False)),
                ("number", models.PositiveIntegerField(default=1)),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="authored_chapters",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Log",
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
                (
                    "action_type",
                    models.CharField(
                        choices=[
                            ("login", "Вход в систему"),
                            ("logout", "Выход из системы"),
                            ("create_material", "Создание материала"),
                            ("edit_material", "Редактирование материала"),
                            ("delete_material", "Удаление материала"),
                            ("review_material", "Проверка материала"),
                            ("create_user", "Создание пользователя"),
                            ("edit_user", "Редактирование пользователя"),
                            ("block_user", "Блокировка пользователя"),
                            ("change_role", "Изменение роли"),
                            ("restore_material", "Восстановление материала"),
                        ],
                        max_length=20,
                    ),
                ),
                ("action_details", models.JSONField(default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="logs",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QA",
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
                ("question", models.CharField(max_length=100)),
                ("answer", models.TextField(max_length=3000)),
                ("written_at", models.DateTimeField(auto_now_add=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("status", models.CharField(default="draft", max_length=20)),
                ("is_published", models.BooleanField(default=False)),
                ("is_deleted", models.BooleanField(default=False)),
                ("max_links", models.PositiveSmallIntegerField(default=3)),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="authored_qas",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QA_Reference",
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
                ("url", models.URLField()),
                ("description", models.CharField(max_length=200)),
                (
                    "qa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="references",
                        to="qa_system.qa",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RevisionHistory",
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
                (
                    "material_type",
                    models.CharField(
                        choices=[
                            ("chapter", "Глава"),
                            ("section", "Раздел"),
                            ("subsection", "Подраздел"),
                            ("qa", "Вопрос-ответ"),
                        ],
                        max_length=20,
                    ),
                ),
                ("material_id", models.PositiveIntegerField()),
                ("written_at", models.DateTimeField(auto_now_add=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("changes", models.JSONField(default=dict)),
                ("material_title", models.CharField(max_length=100)),
                ("status", models.CharField(default="pending", max_length=20)),
                (
                    "editor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="revisions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Section",
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
                ("title", models.CharField(max_length=50)),
                ("written_at", models.DateTimeField(auto_now_add=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("status", models.CharField(default="draft", max_length=20)),
                ("is_published", models.BooleanField(default=False)),
                ("is_deleted", models.BooleanField(default=False)),
                ("number", models.PositiveIntegerField(default=1)),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="authored_sections",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "chapter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sections",
                        to="qa_system.chapter",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subsection",
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
                ("title", models.CharField(max_length=50)),
                ("written_at", models.DateTimeField(auto_now_add=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("status", models.CharField(default="draft", max_length=20)),
                ("is_published", models.BooleanField(default=False)),
                ("is_deleted", models.BooleanField(default=False)),
                ("number", models.PositiveIntegerField(default=1)),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="authored_subsections",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subsections",
                        to="qa_system.section",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QA_Subsection",
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
                ("copy_number", models.PositiveSmallIntegerField(default=1)),
                ("number", models.PositiveIntegerField(default=1)),
                (
                    "qa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subsection_links",
                        to="qa_system.qa",
                    ),
                ),
                (
                    "subsection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qas",
                        to="qa_system.subsection",
                    ),
                ),
            ],
        ),
    ]
