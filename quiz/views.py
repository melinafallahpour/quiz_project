from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Topic, Quiz, Question, Result
from .forms import QuizForm, QuestionForm


def home_view(request):
	quiz = Quiz.objects.annotate(number_of_question=Count('question'))
	quiz = quiz.order_by("-created_time").all()
	paginator = Paginator(quiz, 6)
	page_number = request.GET.get('page')
	objects = paginator.get_page(page_number)
	form1 = QuizForm()
	form2 = QuestionForm()
	context = {
		'objects': objects,
		'form1': form1,
		'form2': form2,
	}
	return render(request, 'quiz/main.html', context)
	

@login_required
def result_view(request):
	results = Result.objects.filter(user=request.user)
	results = results.order_by("-created").all()
	return render(request, 'quiz/result.html', {'results': results})

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@login_required
def create_quiz(request):
	if is_ajax(request):
		form = QuizForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.created_by = request.user
			instance.save()
			return JsonResponse({
				'quiz_title': instance.quiz_title,
				'topic': instance.topic.topic_title,
				'time': instance.time,
				'created_by': instance.created_by.username,
				'id': instance.id
			})


@login_required
def add_question(request):
	if is_ajax(request):
		form = QuestionForm(request.POST)
		if form.is_valid():
			pk = request.POST.get('pk')
			quiz = Quiz.objects.get(pk=pk)
			instance = form.save(commit=False)
			instance.quiz = quiz
			instance.save()
			return JsonResponse({})


def question_view(request, pk):
	quiz = Quiz.objects.get(pk=pk)
	questions = quiz.get_questions()
	return render(request, 'quiz/question.html', 
		{
		'quiz': quiz,
		'que':  questions,
		}
	)


def question_detail_view(request, pk):
	quiz = Quiz.objects.get(pk=pk)
	ques = quiz.get_questions()
	questions = []
	for q in ques:
		ques_answers = [
			q.option_one,
			q.option_two,
			q.option_three,
			q.option_four
		]
		questions.append({q.question_text: ques_answers})

	return JsonResponse({
		'time': quiz.time,
		'questions': questions,
	})


def save_answer_view(request, pk):
	if is_ajax(request):
		answer = request.POST
		answer_ = dict(answer.lists())
		answer_.pop('csrfmiddlewaretoken')
		quiz = Quiz.objects.get(pk=pk)
		questions = [
			Question.objects.get(question_text=key, quiz=quiz)
			for key in answer_.keys()
		]

		score = 0
		results = []
		for q in questions:
			message = ""
			ans = answer_[q.question_text][0]
			options = {
				1: q.option_one,
				2: q.option_two,
				3: q.option_three,
				4: q.option_four
			}
			if (ans == options[q.correct_num]):
				score += 1
				message = "Correct!"
			else:
				message = f"Your answer: {ans}, Correct: {q.correct_num} - {options[q.correct_num]}"
			results.append({str(q.question_text): message})
		num_of_q = len(quiz.get_questions())
		score_ = round(score * 100 / num_of_q, 2)

		# If user logged in, save the result
		if request.user.is_authenticated:
			Result.objects.create(
				quiz=quiz,
				user=request.user,
				score=score_
			)

		return JsonResponse({'results': results, 'score': score_})