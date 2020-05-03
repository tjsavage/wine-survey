from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from djqscsv import render_to_csv_response

from .models import SurveyQuestion, SurveyQuestionResponse, SurveyResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def api_submit_survey(request):
    if request.is_ajax():
        if request.method == 'POST':
            results = request.POST

            response, created = SurveyResponse.objects.get_or_create(email=results['email'])
            
            for k, v in results.items():
                question, created = SurveyQuestion.objects.get_or_create(slug=k)

                question_response, created = SurveyQuestionResponse.objects.get_or_create(
                    survey_response=response,
                    survey_question=question
                )
                question_response.answer = v
                question_response.save()

            
            return HttpResponse(status=201)

def csv_question_responses(request):
    qs = SurveyQuestionResponse.objects.all()

    return render_to_csv_response(qs)