from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Lesson, Quiz

def home(request):
    lessons = Lesson.objects.all()
    return render(request, 'learning/home.html', {'lessons': lessons})


def about_us(request):
    return render(request, 'learning/about_us.html')


#@login_required
def dashboard(request):
    beginner_lessons = Lesson.objects.filter(level='beginner')
    intermediate_lessons = Lesson.objects.filter(level='intermediate')
    advanced_lessons = Lesson.objects.filter(level='advanced')
    return render(request, 'learning/dashboard.html', {
        'beginner_lessons': beginner_lessons,
        'intermediate_lessons': intermediate_lessons,
        'advanced_lessons': advanced_lessons,
    })


def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'learning/lesson_list.html', {'lessons': lessons})


def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'learning/lesson_detail.html', {'lesson': lesson})


#@login_required
def quiz(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    quiz = get_object_or_404(Quiz, lesson=lesson)

    if request.method == "POST":
        selected_answer = request.POST.get('answer')
        is_correct = (selected_answer == quiz.correct_answer)

        next_lesson = Lesson.objects.filter(id__gt=lesson.id).order_by('id').first()

        return render(request, 'learning/quiz_result.html', {
            'lesson': lesson,
            'quiz': quiz,
            'is_correct': is_correct,
            'selected_answer': selected_answer,
            'next_lesson': next_lesson,
        })

    return render(request, 'learning/quiz.html', {'lesson': lesson, 'quiz': quiz})
