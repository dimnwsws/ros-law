from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('admin', 'Админ'),
        ('curator', 'Куратор'),
        ('moderator', 'Модератор'),
        ('specialist', 'Специалист'),
        ('volunteer', 'Волонтер'),
        ('blocked', 'Заблокированный'),
    )
    
    SEX_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='specialist')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birth_date = models.DateField(null=True, blank=True)  # Making this optional for easier initial setup
    region = models.CharField(max_length=100, default='')
    address = models.TextField(default='')
    organization = models.CharField(max_length=200, default='')
    position = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=20, default='')
    
    registration_date = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
    def get_full_name(self):
        if self.patronymic:
            return f"{self.last_name} {self.first_name} {self.patronymic}"
        return f"{self.last_name} {self.first_name}"

# These are minimal implementations of the core models
# Add more fields as your implementation progresses

class Chapter(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='authored_chapters')
    written_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='draft')
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    number = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.number}. {self.title}"

class Section(models.Model):
    title = models.CharField(max_length=50)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='sections')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='authored_sections')
    written_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='draft')
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    number = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.chapter.number}.{self.number}. {self.title}"

class Subsection(models.Model):
    title = models.CharField(max_length=50)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='subsections')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='authored_subsections')
    written_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='draft')
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    number = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.section.chapter.number}.{self.section.number}.{self.number}. {self.title}"

class QA(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='authored_qas')
    written_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='draft')
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    max_links = models.PositiveSmallIntegerField(default=3)
    
    def __str__(self):
        return self.question

class QA_Subsection(models.Model):
    qa = models.ForeignKey(QA, on_delete=models.CASCADE, related_name='subsection_links')
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE, related_name='qas')
    copy_number = models.PositiveSmallIntegerField(default=1)
    number = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.qa.question} in {self.subsection.title}"

class QA_Reference(models.Model):
    qa = models.ForeignKey(QA, on_delete=models.CASCADE, related_name='references')
    url = models.URLField()
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.description

class RevisionHistory(models.Model):
    MATERIAL_TYPE_CHOICES = (
        ('chapter', 'Глава'),
        ('section', 'Раздел'),
        ('subsection', 'Подраздел'),
        ('qa', 'Вопрос-ответ'),
    )
    
    material_type = models.CharField(max_length=20, choices=MATERIAL_TYPE_CHOICES)
    material_id = models.PositiveIntegerField()
    editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='revisions')
    written_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(null=True, blank=True)
    changes = models.JSONField(default=dict)
    material_title = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='pending')
    
    def __str__(self):
        return f"Revision of {self.material_type} {self.material_id} by {self.editor}"

class Log(models.Model):
    ACTION_CHOICES = (
        ('login', 'Вход в систему'),
        ('logout', 'Выход из системы'),
        ('create_material', 'Создание материала'),
        ('edit_material', 'Редактирование материала'),
        ('delete_material', 'Удаление материала'),
        ('review_material', 'Проверка материала'),
        ('create_user', 'Создание пользователя'),
        ('edit_user', 'Редактирование пользователя'),
        ('block_user', 'Блокировка пользователя'),
        ('change_role', 'Изменение роли'),
        ('restore_material', 'Восстановление материала'),
    )
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='logs')
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES)
    action_details = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.get_action_type_display()} at {self.created_at}"