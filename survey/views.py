import random, json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.forms.models import model_to_dict

from djqscsv import render_to_csv_response

from .models import SurveyQuestion, SurveyQuestionResponse, SurveyResponse, SurveyABTestInstance, WineItem, get_random_wine_item


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

@csrf_exempt
def api_submit_ab_results(request):
    if request.is_ajax():
        if request.method == 'POST':
            results = request.POST
            print(results)

            if results['email']:
                survey_response_key = results['email']
            else:
                survey_response_key = None

            if survey_response_key:
                survey_response = SurveyResponse.objects.get(email=survey_response_key)
            else:
                survey_response = None

            survey_ab_test_instance = SurveyABTestInstance.objects.create(
                survey_response=survey_response,
                item_A=WineItem.objects.get(item_key=results['item_A_key']),
                item_B=WineItem.objects.get(item_key=results['item_B_key']),
                winner=WineItem.objects.get(item_key=results['winner']),
                loser=WineItem.objects.get(item_key=results['loser'])
            )

            return HttpResponse(status=201)

def api_get_ab_test(request):
    last = WineItem.objects.count() - 1
    index1 = random.randint(0, last)

    item_A = WineItem.objects.all()[index1]
    item_B = None

    while not item_B or item_B.wine_type != item_A.wine_type:
        index2 = random.randint(0, last)
        if index2 == index1:
            continue

        item_B = WineItem.objects.all()[index2]

    return JsonResponse(
        {
            'item_A': model_to_dict(item_A),
            'item_B': model_to_dict(item_B)
        }
        , safe=False
    )

def csv_question_responses(request):
    qs = SurveyQuestionResponse.objects.all()

    return render_to_csv_response(qs)

def csv_ab_responses(request):
    qs = SurveyABTestInstance.objects.all()

    return render_to_csv_response(qs)

def csv_wine_items(request):
    qs = WineItem.objects.all()

    return render_to_csv_response(qs)