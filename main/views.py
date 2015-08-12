from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

# Create your views here.

from main.models import State

def first_view(request):

    states = State.objects.all()

    state_list = ""
    for state in states:
        for city in state.city_set.all():
            state_list += "State: %s, City: %s, Zip: %s </br>" % (state.name, city.name, city.zip_code)


    return HttpResponse(state_list)


def city_search(request, city, state):
    states = State.objects.filter(name__startswith=state)

    city_string= ""

    for state in states:
        cities = state.city_set.filter(name__istartswith=city)
        for city in cities:
            city_string += "Sate:%s , City%s</br>" % (state.name, city.name)
    
    return HttpResponse(city_string)


    cities = the_state.city_set.filter(name__startswith=city)

    city_string = ""


    for city in cities:
        city_string += "%s </br>" % city.name
    
    return HttpResponse(city_string)


    def get_view(request):

        get_var1 = request.GET.get('var1', None)
        get_var2 = request.GET.get('var1', None)
        get_var3 = request.GET.get('var1', None)

        get_vars = "%s , %s , %s" % (get_var1, get_var2, get_var3)

        request = "<pre> %s </pre>" % request

        return HttpResponse(get_vars)

def get_city_state(request):


    city_state = ""
    state = request.GET.get('state',None)
    city = request.GET.get('city',None)

    # city_state = "%s , %s" % (city, state)
    


    if state != None and city != None:
        states = State.objects.filter(name__istartswith=state)

    for state in states:
        cities = state.city_set.filter(name__istartswith=city)
        for city in cities:
            city_state+="%s| %s </br>------------------- </br>" % (city.name, state.name)


    

    return HttpResponse(city_state)

@csrf_exempt
def post_city_state(request):
    


    city_state+= """
    <form action='/get_city_state' method='GET'>

    State:
    </br>
    <input type="text" name="state">
    </br>

    City
    </br>
    <input type="text" name="city">



    <input type="submit" value="Submit Me">


    </form>
        """

    if request.method == 'GET':

        return HttpResponse(city_state)

    if request.method == 'POST':

        state = requestPOST.POST('state', None)
        city = request.POST.POST('city', None)


        state = request.GET.get('state',None)
        city = request.GET.get('city',None)

     
        city_state+="""
    --------------------------------- </br>
    State | City    </br>
    --------------------------------- </br> </br>"""
        if state != None and city != None:
            states = State.objects.filter(name__istartswith=state)

        for state in states:
            cities = state.city_set.filter(name__istartswith=city)
            for city in cities:
                city_state+="%s| %s </br>------------------- </br>" % (city.name, state.name)


        

        return HttpResponse(city_state)

class GetPost(View):

    def get(self, request, *args, **kwargs):
        get_string = "This is a Get String"

        return HttpResponse(get_string)

    def post(self, request, *args, **kwargs):
        post_string = "This is a post String"

        return HttpResponse(post_string)

