from django.shortcuts import render, redirect

from . import utils

def home(request):

    shoyu_ramen_list = utils.fetch_ramen_type_list('Shoyu')
    miso_ramen_list = utils.fetch_ramen_type_list('Miso')
    tonkotsu_ramen_list = utils.fetch_ramen_type_list('Tonkotsu')
    recently_added_list = utils.fetch_recently_added_list()
    top_rated_list = utils.fetch_top_rated_list()

    context = {'shoyu_ramen_list': shoyu_ramen_list, 
               'miso_ramen_list': miso_ramen_list,
               'tonkotsu_ramen_list': tonkotsu_ramen_list,
               'recently_added_list': recently_added_list,
               'top_rated_list': top_rated_list
               }

    return render(request, "home.html", context)

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
