from .models import Ramen

def fetch_all_shoyu_ramen():
    
    ramens = Ramen.objects.all()
    return ramens

def fetch_afternoon_foods():
    return

def fetch_evening_foods():
    return

def fetch_recently_added_foods():
    return

def fetch_top_rated_foods():
    return

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
