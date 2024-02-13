from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from . import models
from .models import Answer, Question, Quiz, UserQuizStats


@login_required
def submit_quiz(request, quiz_id):
    if request.method == "POST":
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        user = request.user
        score = 0
        questions = quiz.question_set.all()

        for question in questions:
            answer_id = request.POST.get(f"question_{question.id}")
            if answer_id:
                selected_answer = get_object_or_404(Answer, pk=answer_id)
                if selected_answer.is_correct:
                    score += 1

        # Save user quiz statistics
        user_quiz_stats = models.UserQuizStats(user=user, quiz=quiz, score=score)
        user_quiz_stats.save()

        return render(
            request,
            "quiz/quiz_result.html",
            {"quiz": quiz, "score": score, "questions": questions},
        )

    return redirect("quiz_list")


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, "quiz/quiz_list.html", {"quizzes": quizzes})


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.all()
    return render(
        request, "quiz/quiz_detail.html", {"quiz": quiz, "questions": questions}
    )


def home_page(request):
    return render(request, "pages/home.html")


def about_page(request):
    return render(request, "pages/about.html")


def article_list(request):
    articles = models.Article.objects.all()
    return render(
        request,
        "pages/article_list.html",
        {"articles": articles},
    )


def article_detail(request, pk):
    article = models.Article.objects.get(pk=pk)
    return render(
        request,
        "pages/article_detail.html",
        {"article": article},
    )


def profile_page(request):
    user = request.user
    quiz_stats = UserQuizStats.objects.filter(user=user)
    return render(
        request, "account/profile.html", {"user": user, "quiz_stats": quiz_stats}
    )


def contact_page(request):
    return render(request, "pages/contact.html")


def donation_page(request):
    return render(request, "pages/donation.html")
