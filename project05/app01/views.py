from django.core.paginator import Paginator
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from app01.models import PicInfo, Area
from project05.settings import MEDIA_ROOT


def show_static(request):
    '''进入静态文件演示界面'''
    return render(request, 'app01/show_static.html')

def show_upload_image(request):
    """进入上传图片界面"""
    return render(request, 'app01/show_upload_image.html')


# def show_image(request):
#     PicInfo = request.
#     return None

def do_upload(request):
    # 1.获取上传的图片对象
    pic_info = request.FILES.get('pic_info')

    print(type(pic_info))
    print(pic_info.name)  # name:上传图片的文件名

    # 2.定义图片保存的目录
    abs_path = '%s/app01/%s' % (MEDIA_ROOT, pic_info.name)
    # 3.保存图片到指定目录下
    with open(abs_path, 'wb') as file:
        for data in pic_info.chunks():
            file.write(data)

    # 4.数据库表新增一条记录,保存图片路径
    pic = PicInfo()
    pic.path = 'app01/%s' % pic_info.name
    pic.save()
    # 5.响应浏览器
    return HttpResponse('上传成功')

def show_images(request):
    '''显示上传图片'''
    # 通过模型类查询所有的图片
    images = PicInfo.objects.all()
    my_dict = {'images':images}
    return render(request, 'app01/show_images.html', my_dict)


def index(request):
    '''进入首页'''
    return HttpResponse('首页')


def show_page(request, page_no=1):
    '''显示分页数据'''

    # 查询所有的省份
    provinces = Area.objects.filter(parent_id=1) # id=1 表示的是中国

    # 显示数据

    # 创建分页对象(每页显示10条)
    paginator = Paginator(provinces, 10)
    print(paginator.count) # 总条数
    print(paginator.num_pages) # 总页码
    print(paginator.page_range) # 页码列表,比如[1,2,3,4]
    # 获取第一页数据的Pager类对象
    page = paginator.page(page_no) # 第1页数据
    print(type(page))
    print(page.object_list) # 当前页的所有的数据
    print(page.number) # 当前是第几页
    print(page.paginator) # 分页器对象
    # 显示数据
    my_dict = {'page': page}
    return render(request, 'app01/show_page.html', my_dict)

def show_area(request):
    '''显示区域案例界面'''
    return render(request, 'app01/show_area.html')

def get_provinces(request):
    """获取所有的省份数据"""
    # 查询所有的省份
    provinces = Area.objects.filter(parent_id=1) # id=1表示的是中国
    # id=1表示的是中国
    my_list = []
    for p in provinces:
        my_list.append((p.id, p.title))

    my_dict = {'provinces': my_list}
    return JsonResponse(my_dict)


def get_children(request, pid):
    """
        根据上级区域id,获取下级区域
        :param request:
        :param pid: 上级区域id
        :return:
        """

    # 获取下级区域
    children = Area.objects.filter(parent_id=pid)

    # 手动拼接字符串
    my_list = []
    for p in children:
        my_list.append((p.id, p.title))

    my_dict = {'children': my_list}
    return JsonResponse(my_dict)