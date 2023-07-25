from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
	path('', views.home_view, name='home_view'),
	path('result/', views.result_view, name='result_view'),
	path('create/', views.create_quiz, name='create_quiz'),
	path('add/', views.add_question, name='add_question'),
	path('<pk>/', views.question_view, name='question_view'),
	path('<pk>/detail/', views.question_detail_view, name='question_detail_view'),
	path('<pk>/save/', views.save_answer_view, name='save_answer_view'),
]