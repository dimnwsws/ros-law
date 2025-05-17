from django import forms
from django.forms import modelformset_factory
from .models import User, Chapter, Section, Subsection, QA, QA_Reference, PendingStatusLevel
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    """Form for user login"""
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )

class ChapterForm(forms.ModelForm):
    """Form for creating and editing chapters"""
    
    class Meta:
        model = Chapter
        fields = ['title', 'number']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}),
            'number': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'})
        }
        labels = {
            'title': 'Название главы',
            'number': 'Расположение'
        }
        help_texts = {
            'title': 'Максимум 50 символов',
            'number': 'Позиция в иерархии'
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 50:
            raise ValidationError('Название главы не должно превышать 50 символов')
        return title

class SectionForm(forms.ModelForm):
    """Form for creating and editing sections"""
    
    class Meta:
        model = Section
        fields = ['title', 'chapter', 'number']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}),
            'chapter': forms.Select(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'})
        }
        labels = {
            'title': 'Название раздела',
            'chapter': 'Глава',
            'number': 'Расположение'
        }
        help_texts = {
            'title': 'Максимум 50 символов',
            'chapter': 'Выберите главу, к которой относится раздел',
            'number': 'Позиция в иерархии'
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 50:
            raise ValidationError('Название раздела не должно превышать 50 символов')
        return title

class SubsectionForm(forms.ModelForm):
    """Form for creating and editing subsections"""
    
    class Meta:
        model = Subsection
        fields = ['title', 'section', 'number']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'})
        }
        labels = {
            'title': 'Название подраздела',
            'section': 'Раздел',
            'number': 'Расположение'
        }
        help_texts = {
            'title': 'Максимум 50 символов',
            'section': 'Выберите раздел, к которому относится подраздел',
            'number': 'Позиция в иерархии'
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 50:
            raise ValidationError('Название подраздела не должно превышать 50 символов')
        return title

class QAForm(forms.ModelForm):
    """Form for creating and editing question-answers"""
    
    class Meta:
        model = QA
        fields = ['question', 'answer']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'maxlength': '3000', 'rows': '8'})
        }
        labels = {
            'question': 'Вопрос',
            'answer': 'Ответ'
        }
        help_texts = {
            'question': 'Максимум 100 символов',
            'answer': 'Максимум 3000 символов'
        }
    
    def clean_question(self):
        question = self.cleaned_data.get('question')
        if len(question) > 100:
            raise ValidationError('Вопрос не должен превышать 100 символов')
        return question
    
    def clean_answer(self):
        answer = self.cleaned_data.get('answer')
        if len(answer) > 3000:
            raise ValidationError('Ответ не должен превышать 3000 символов')
        return answer

class QAReferenceForm(forms.ModelForm):
    """Form for QA references"""
    
    class Meta:
        model = QA_Reference
        fields = ['url', 'description']
        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание источника'})
        }
        labels = {
            'url': 'URL источника',
            'description': 'Описание'
        }

# Create formset for QA references (up to 3)
ReferenceFormSet = modelformset_factory(
    QA_Reference,
    form=QAReferenceForm,
    extra=1,
    max_num=3,
    validate_max=True,
    can_delete=True
)

class UserForm(forms.ModelForm):
    """Form for user creation and editing"""
    
    class Meta:
        model = User
        fields = [
            'email', 'first_name', 'last_name', 'patronymic', 'role', 'sex',
            'birth_date', 'region', 'address', 'organization', 'position', 'phone'
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'patronymic': 'Отчество',
            'role': 'Роль',
            'sex': 'Пол',
            'birth_date': 'Дата рождения',
            'region': 'Регион',
            'address': 'Адрес',
            'organization': 'Организация',
            'position': 'Должность',
            'phone': 'Телефон'
        }
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['patronymic'].required = False
        
        # If we're editing an existing user, the email field should be readonly
        if self.instance and self.instance.pk:
            self.fields['email'].widget.attrs['readonly'] = True

class ChangeRoleForm(forms.ModelForm):
    """Form for changing user role"""
    
    class Meta:
        model = User
        fields = ['role']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'role': 'Новая роль'
        }
    
    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop('current_user', None)
        super(ChangeRoleForm, self).__init__(*args, **kwargs)
        
        # Limit role choices based on the current user's role
        if self.current_user and self.current_user.role == 'curator':
            self.fields['role'].choices = [
                (choice[0], choice[1]) for choice in self.fields['role'].choices 
                if choice[0] not in ['admin', 'curator']
            ]

class ReviewForm(forms.Form):
    """Form for reviewing materials"""
    DECISION_CHOICES = (
        ('accepted', 'Принято'),
        ('accepted_with_changes', 'Принято с изменениями'),
        ('rejected', 'Отклонено'),
    )
    
    decision = forms.ChoiceField(
        choices=DECISION_CHOICES,
        widget=forms.RadioSelect,
        label='Решение'
    )
    
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        label='Комментарий',
        required=False
    )
    
    def clean(self):
        cleaned_data = super().clean()
        decision = cleaned_data.get('decision')
        comment = cleaned_data.get('comment')
        
        if decision == 'rejected' and not comment:
            raise ValidationError('При отклонении материала необходимо указать причину в комментарии.')
        
        return cleaned_data

class PendingStatusLevelForm(forms.ModelForm):
    """Form for editing pending status levels"""
    
    class Meta:
        model = PendingStatusLevel
        fields = ['min_hours', 'max_hours', 'color_code']
        widgets = {
            'min_hours': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'max_hours': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'color_code': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'})
        }
        labels = {
            'min_hours': 'Минимальное время (часы)',
            'max_hours': 'Максимальное время (часы)',
            'color_code': 'Цвет'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        min_hours = cleaned_data.get('min_hours')
        max_hours = cleaned_data.get('max_hours')
        
        if min_hours is not None and max_hours is not None and min_hours >= max_hours:
            raise ValidationError('Минимальное время должно быть меньше максимального.')
        
        return cleaned_data
