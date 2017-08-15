from django.shortcuts import render, HttpResponse, redirect
from .models import Rental,Rental10Pa,Cat ,Stdid #Record ,Category
# from .forms import RecordForm
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms2 import PostForm
from django.http import JsonResponse
from django.db.models import Q #複雜查詢 https://stackoverflow.com/questions/739776/django-filters-or
import json
from django_ajax.decorators import ajax

# Create your views here.


def front_page(request): 
	return render(request,'app/front_page.html',locals())

# @csrf_exempt

def ajax_dict(request):
	abc = {'a':'1','b':'2','c':'3'}
	return JsonResponse(abc)


def add_my_love(request):

	url = request.GET.get('url',None)
	title = request.GET.get('title',None)
	address = request.GET.get('address',None)
	rent = request.GET.get('rent',None)
	space = request.GET.get('space',None)
	pattern = request.GET.get('pattern',None)
	floor = request.GET.get('floor',None)
	stories = request.GET.get('stories',None)
	lat = request.GET.get('lat',None)
	lng = request.GET.get('lng',None)
	other_obj = request.GET.get('other_obj',None)

	dict_redis={'url':url,'title':title,'address':address,'rent':rent,'space':space,'pattern':pattern,
	'floor':floor,'stories':stories,'lat':lat,'lng':lng,'other_obj':other_obj}

	message = save_redis(url,dict_redis)
	print(url)
	print(message)
	no_thing = '無須理會'

	return JsonResponse(no_thing,safe=False) 

def visualize_page(request): 
	RO = Rental.objects 
	RO = RO.all()[:10]
	# RO = RO.filter(cityid='1')[:200]
	
	# RO = RO[:4] 
	# return render(request,'app/visualize_page.html',locals())

	# RO = Stdid.objects 
	# RO = RO.all()[:100000]
	# RO = RO.filter(cityid='1')[:200]
	# RO = RO.filter(cityid='1').filter(cityid='1')

	# RO = RO.filter(Q(catid=562200)|Q(catid=920012)|Q(catid=920013)|Q(catid=920014)|Q(catid=920015)|Q(catid=920016)|Q(catid=920017)|Q(catid=920018)|Q(catid=920019)|Q(catid=932411)|Q(catid=932412)|Q(catid=932499))
	# print('we have '+str(len(RO)))
	# RO = RO[:4]
	
	 
	return render(request,'app/visualize_page.html',locals())

def spartan(request):
	return render(request,'app/spartan.html',locals())

def error_page(request):
	return render(request,'app/error_page.html',locals())

def select_page(request):
	post_data = request.POST
	RO = Rental.objects  
	R10 = Rental10Pa.objects
	H = 3 #參考選擇數量 有一個選擇就是0  簡單卻又好用的鳥方法
	fraction = 0 #環境影響評分
	fraction_number = 0 #環境影響數量
	sum_for_public = 0 #環境分數總平均

	# RO的設計是讓RentalDetail.objects便成一個物，接著不斷傳遞下去 原本想用ntalDetail.objects.all()
	# 但每次拉出程式庫所有再比較會增加效率，故直接 RO =RentalDetail.objects 傳遞資料庫物件
	
	if post_data['city']: #求地區
		RO = RO.filter(cityid=post_data['city'])
		R10 = R10.filter(cityid=post_data['city'])
		H = H - 1

	if post_data['area']:  #求用途  
		RO = RO.filter(area=post_data['area'])
		R10 = R10.filter(area=post_data['area'])
		H = H - 1

	if post_data['rent']: #求金額範圍
		lower,upper = post_data['rent'].split(',') #因為html只能回傳字串，無法list，故在此切割出高低限制金額
		RO = RO.filter(rent__range=(lower,upper)).order_by('-rent') #排序 前面加上負表示倒過來
		H = H - 1

	if H == 3:   #如果都沒選 回傳全部
		RO = RO.all() 

	RO = RO.filter(label='H') #這裡確認最後跑出僅有租屋
	RO = RO.exclude(lat='0')

	if len(RO) == 0:

		return render(request,'app/error_page.html',locals())
	#如果有環境值被填寫，選擇
	elif post_data['food'] or post_data['green'] or post_data['leasure'] or post_data['hospital'] or post_data['mrt']:

		#以下規則，只要有一個便編入搜尋條件，沒填選的給予預設值 1 
		#如果條件蒐尋後僅有0個物件則彈出錯誤頁面

		# if post_data['food'] == '': #食物條件
		# 	list_food = 5
		# else:
		# 	list_food = post_data['food']

		# if post_data['green'] == '': #食物條件
		# 	list_green = 5
		# else:
		# 	list_green = post_data['green']

		# if post_data['leasure'] == '': #食物條件
		# 	list_leasure = 5
		# else:
		# 	list_leasure = post_data['leasure']

		# if post_data['hospital'] == '': #食物條件
		# 	list_hospital = 5
		# else:
		# 	list_hospital = post_data['hospital']

		# if post_data['mrt'] == '': #食物條件
		# 	list_mrt = 5
		# else:
		# 	list_mrt = post_data['mrt']

		# #在這裡做塞選 #這裡要注意，環境塞選後是得出前一百個匹配的物件，然後再去跟基本條件做交配
		# R10 = R10.filter(food=list_food,green=list_green,leasure=list_leasure,hospital=list_hospital,mrt=list_mrt)[:100]
		# env_url_list = [] #環境list
		# new_pass_env = [] #匹配成功list

		# for objs in R10: #把一百環境條件達到的加入到物件中
		# 	env_url_list.append(objs.url)

		# for objs in RO:  #比對，基本條件url也符合環建url list的則擺到新的list
		# 	if objs.url in env_url_list:
		# 		print(objs.title)
		# 		new_pass_env.append(objs)
		# 		if len(new_pass_env) == 5: #如果已經集滿五個，則結束迴圈
		# 			break

		# RO = new_pass_env #匹配成功list 丟回去變成RO
		# print('\n環境篩選完成，一共有'+str(len(RO))+'筆資料\n')

		# if len(RO) == 0: #第二層，如果公共洗出來沒東西回傳
		# 	print('\n回傳失敗，一共僅有'+str(len(RO))+'筆資料\n')
		# 	return render(request,'app/error_page.html',locals())
		# else:
			
		# 	query_object = url_to_info(RO[0].url) #選第一個做預備展示
		# 	RO = RO_to_pub(RO) #把公共的值轉成中文，能看的懂得

			# return render(request,'app/area_result_page.html',locals())

		# 專題修改部分
		query_object = url_to_info(RO[0].url)
		RO = RO_to_pub(RO)[:5]
		return render(request,'app/area_result_page.html',locals())

	else:
		RO = RO[:5] #確保搜尋欄位結果最多三個

		return render(request,'app/select_page.html',locals())
	# return render(request,'app/select_page.html',locals())

@login_required
def coffee(request): #登入
	re = request.GET
	print(re)
	#query_object_ob = RentalDetail.objects.get(url='http://www.etwarm.com.tw/rent-77604')
	#address = query_object_ob.address

	return render(request,'app/coffee.html',locals())

def result_page(request): #查詢 在這裡直接賦予值，而不是在內頁  obgect.class
	posted_data = request.POST
	url = posted_data['hidden_url'] #從隱藏欄位尋找url
	query_object = Rental.objects.get(url=url)
	query_object.query_other = []
	name_other_list = ['抽菸：smoke：'+query_object.smoke,'寵物：pet：'+query_object.pet,'廚房：cook：'+query_object.cook,'公園：parking：'+query_object.parking,'性別限制：sex：'+query_object.sex]
	
	for other in name_other_list: #丟進迴圈，再把迴圈給網頁

		other_key = other.split('：')[0]
		other_attr = other.split('：')[1]
		other_value = other.split('：')[2]

		if other_value == '': #判斷空值就不加入迴圈
			continue
		elif other_value == 'M':
			other_value = '皆可'
		elif other_value == 'B':
			other_value = '限男'
		elif other_value == 'F':
			other_value = '限女'
		elif other_value == 'Y':
			other_value = '有'
		elif other_value == 'N':
			other_value = '無'
		else:
			other_value = ''

		query_object.query_other.append(other_key + '：' + other_value)

	if len(query_object.query_other) !=0: #如果ｌｉｓｔ不是空的就給他文字顯現：其他條件
		query_object.other_title = '其他條件'
	else:
		query_object.other_title = ''

	return render(request,'app/result_page.html',locals())
	#return render(request,'app/coffee.html',locals())

def RO_to_pub(RO): #該死技術債 全部RO pub - value改值

  for obj_RO in RO:

    #抽菸
    if obj_RO.smoke == 'N':
      obj_RO.smoke = '無'
    elif obj_RO.smoke =='Y':
      obj_RO.smoke = '有'
    else:
      obj_RO.smoke = ''
    #寵物
    if obj_RO.pet == 'N':
      obj_RO.pet = '無'
    elif obj_RO.pet =='Y':
      obj_RO.pet = '有'
    else:
      obj_RO.pet = ''

    #廚房
    if obj_RO.cook == 'N':
      obj_RO.cook = '無'
    elif obj_RO.cook =='Y':
      obj_RO.cook = '有'
    else:
      obj_RO.cook = ''

    #公園
    if obj_RO.parking == 'N':
      obj_RO.parking = '無'
    elif obj_RO.parking =='Y':
      obj_RO.parking = '有'
    else:
      obj_RO.parking = ''

    #性別限制
    if obj_RO.parking == 'M':
      obj_RO.parking = '限男'
    elif obj_RO.parking =='F':
      obj_RO.parking = '限女'
    elif obj_RO.parking =='B':
      obj_RO.parking = '皆可'
    else:
      obj_RO.parking = ''

  return RO  

def url_to_info(url):

	query_object = Rental.objects.get(url=url)
	query_object.query_other = []
	name_other_list = ['抽菸：smoke：'+query_object.smoke,'寵物：pet：'+query_object.pet,'廚房：cook：'+query_object.cook,'公園：parking：'+query_object.parking,'性別限制：sex：'+query_object.sex]
	
	for other in name_other_list: #丟進迴圈，再把迴圈給網頁

		other_key = other.split('：')[0]
		other_attr = other.split('：')[1]
		other_value = other.split('：')[2]

		if other_value == '': #判斷空值就不加入迴圈
		  other_value = ''
		elif other_value == 'M':
		  other_value = '皆可'
		elif other_value == 'B':
		  other_value = '限男'
		elif other_value == 'F':
		  other_value = '限女'
		elif other_value == 'Y':
		  other_value = '有'
		elif other_value == 'N':
		  other_value = '無'
		else:
		  other_value = ''

		query_object.query_other.append((other_key + '：' + other_value,other_attr)) #這裡用truple去裝值

	if len(query_object.query_other) !=0: #如果ｌｉｓｔ不是空的就給他文字顯現：其他條件
		query_object.other_title = '其他條件'
	else:
		query_object.other_title = ''

	return query_object

def save_redis(url,dict):
    
    try:
        import redis
        r = redis.StrictRedis(host='localhost',port=6379,db=0,decode_responses=True) 
        r.hmset(url,dict)
        message = 'success'
    except Exception as ex:
        message = ex
        
    return message