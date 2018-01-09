from django.contrib import admin

# Register your models here.
from app01.models import Area, PicInfo


# class AreaAdmin(admin.ModelAdmin):
#     # 每页显示多少条
#     list_per_page = 10
#     # 配置显示哪些字段(指定的是类属性)
#     list_display = ['id', 'title', 'parent_area']
#
# # 注册后才会在后台显示出来,进行管理
# admin.site.register(Area, AreaAdmin)


class PicInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'path']


admin.site.register(PicInfo, PicInfoAdmin)

