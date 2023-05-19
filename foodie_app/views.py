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

def ramen_type_view(request, ramen_type):

    ramen_list = utils.fetch_ramen_type_list(ramen_type)
    context = {'ramen_list': ramen_list, 'category': ramen_type }

    return render(request, "category_list_page.html", context)

def recently_added_view(request):
    
    ramen_list = utils.fetch_recently_added_list()
    context = {'ramen_list': ramen_list, 'category': "Recent Ramen Additions"}

    return render(request, "category_list_page.html", context)

def top_rated_view(request):
    
    ramen_list = utils.fetch_top_rated_list()
    context = {'ramen_list': ramen_list, 'category': "Top Rated Ramen"}

    return render(request, "category_list_page.html", context)

# def ramen_detail_view(request, pk):

#     ramen = utils.fetch_ramen_detail(pk)
#     context = {'ramen': ramen, 'shop': ramen.shop}

#     return render(request, "ramen_detail_page.html", context)

def submit_ramen(request):

    if request.method == 'POST':
        utils.save_ramen(request)
    
    return redirect('home')
