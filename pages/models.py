from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser


class Article(models.Model):
    image = models.ImageField(upload_to="article_images/", blank=True, null=True)
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    body = models.TextField(verbose_name=_("Body"))
    pdf = models.FileField(upload_to="article_pdfs/", blank=True, null=False)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text} ({self.text})"


class UserQuizStats(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    # Add any additional fields you might need, e.g., date_taken

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - Score: {self.score}"
