from .models import Ramen



def fetch_ramen_type_list(ramen_type: str):

    ramen_list = Ramen.objects.filter(ramenType=ramen_type)

    return ramen_list[:3]

def fetch_recently_added_list():

    ramen_list = Ramen.objects.order_by('-dateAdded')[:3]

    return ramen_list

def fetch_top_rated_foods():
    
    ramen_list = Ramen.objects.order_by('-avgRating')[:3]

    return ramen_list

def save_ramen(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    shop = request.POST.get('shop')
    address = request.POST.get('address')
    typical_meal_time = request.POST.get('typical_meal_time')

    # データベースに新しいRamenオブジェクトを作成して保存
    ramen = Ramen(
        name=name, 
        description=description, 
        shop=shop, 
        address=address, 
        typical_meal_time=typical_meal_time)
    
    ramen.save()
