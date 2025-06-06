from django.db import models
from django.contrib.auth.models import User


class Lesson(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    content = models.TextField()  # You could use RichText if you want with a package!
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    image = models.ImageField(upload_to='lesson_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_level_display()})"

class Quiz(models.Model):
    lesson = models.OneToOneField('Lesson', on_delete=models.CASCADE, related_name='quiz')
    question = models.TextField()
    correct_answer = models.CharField(max_length=200)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)

    def __str__(self):
        return f"Quiz for {self.lesson.title}"