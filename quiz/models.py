from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import random

TOPIC_CHOICES = (
	('Html', 'Html'),
	('Css', 'Css'),
	('Django', 'Django'),
	('Python', 'Python'),
	('JavaScript', 'JavaScript'),
	('React', 'React'),
	('Others', 'Others'),
)


class Topic(models.Model):
	topic_title = models.CharField(max_length=30, choices=TOPIC_CHOICES)

	def __str__(self):
		return str(self.topic_title)


class Quiz(models.Model):
	quiz_title = models.CharField(max_length=200)
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	time = models.PositiveIntegerField(help_text='duration of the quiz in minutes')
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	created_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.quiz_title)

	def get_questions(self):
		questions = list(self.question_set.all())
		random.shuffle(questions)
		return questions

	class Meta:
		verbose_name_plural = 'Quizzes'
		ordering = ("-created_time",)


class Question(models.Model):
	question_text = models.TextField()
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	correct_num = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
	option_one = models.CharField(max_length=200)
	option_two = models.CharField(max_length=200)
	option_three = models.CharField(max_length=200)
	option_four = models.CharField(max_length=200)

	def __str__(self):
		return f"{self.question_text} - correct: {self.correct_num}"


class Result(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
	score = models.FloatField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.quiz} - {self.user} - {self.score}% - {self.created}"