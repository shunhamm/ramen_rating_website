from django.shortcuts import render, redirect

from . import utils

def home(request):

    # morning_foods = utils.fetch_morning_foods()
    # afternoon_foods = utils.fetch_afternoon_foods()
    # evening_foods = utils.fetch_evening_foods()
    # recently_added_foods = utils.fetch_recently_added_foods()
    # top_rated_foods = utils.fetch_top_rated_foods

    # context = {'morning_foods': morning_foods, 
    #            'afternoon_foods': afternoon_foods,
    #            'evening_foods': evening_foods,
    #            'recently_added_foods':  recently_added_foods,
    #            'top_rated_foods': top_rated_foods
    #            }

    return render(request, "home.html")

def shoyu_ramen(request):

    shoyu_ramen = utils.fetch_()

    context = {'shoyu_ramen' shoyu_ramen}

    return render(request, "category_list_page.html", context)

def miso_ramen(request):
    pass

def tonkotsu_ramen(request):
    pass

def recently_added(request):
    pass

def top_rated(request):
    pass

def ramen_detail(request):
    pass

def submit_ramen(request):

    if request.method == 'POST':
        utils.save_ramen(request)
    
    return redirect('home')
