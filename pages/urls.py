from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("about/", views.about_page, name="about"),
    path("article/list/", views.article_list, name="article_list"),
    path("article/<int:pk>/", views.article_detail, name="article_detail"),
    path("quizzes/", views.quiz_list, name="quiz_list"),
    path("quiz/<int:quiz_id>/", views.quiz_detail, name="quiz_detail"),
    path("quiz/<int:quiz_id>/submit/", views.submit_quiz, name="submit_quiz"),
    path("profile/", views.profile_page, name="profile"),
    path("contact/", views.contact_page, name="contact"),
    path("donation/", views.donation_page, name="donation"),
]
