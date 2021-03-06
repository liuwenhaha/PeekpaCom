import ssl
import pymongo
from django.views.generic import View
from django.shortcuts import render
from .decorators import peekpa_code_required
from django.utils.decorators import method_decorator
from apps.base.tracking_view import peekpa_tracking
from django.core.paginator import Paginator


@method_decorator(peekpa_code_required, name='get')
@method_decorator(peekpa_tracking, name='get')
class JpEarthView(View):
    TYPE_ALL = 1
    TYPE_SEARCH = 2
    client = pymongo.MongoClient(
        "mongodb+srv://peekpa-user:peekpa2020@peekpa.ofyco.mongodb.net/Peekpa?retryWrites=true&w=majority",
        ssl_cert_reqs=ssl.CERT_NONE)
    db = client['PeekpaMongoData']
    collection = db['JpEarth']

    def get(self, request):
        page = int(request.GET.get('p', 1))
        handle_type, search_key = self.process_paramter(request)
        list_data = self.get_data_from_db(handle_type, search_key)
        paginator = Paginator(list(list_data), 15)
        page_obj = paginator.page(page)
        context = {
            "list_data": page_obj.object_list,
        }
        context.update(self.get_pagination_data(paginator, page_obj))
        return render(request, 'datacenter/jpearth/manage.html', context=context);

    def get_data_from_db(self, handle_type, search_key):
        if handle_type == self.TYPE_ALL:
            # 搜索全部结果
            result = self.collection.find()

            # 降序排列
            #result = self.collection.find().sort('jp_time_num', pymongo.DESCENDING)

            # 升序排列
            # result = self.collection.find().sort('jp_time_num', pymongo.ASCENDING)

            # 只 返回 地震地点 还有 地震时间
            # result = self.collection.find({},{'jp_title', 'jp_location'})

            # 不 返回 地震地点 还有 地震时间
            # result = self.collection.find({},{'jp_title':False, 'jp_location':False})

            # find_one()单个数据搜索
            #result = self.collection.find_one({"jp_location":"福島県沖"})
        else:
            # 通过地址(jp_location) 精确查找
            #result = self.collection.find({"jp_location": search_key})
            # 通过地址(jp_location) 模糊查找
            result = self.collection.find({"jp_location": {'$regex': ".*" + search_key + ".*"}})
        return list(result)

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        num_pages = paginator.num_pages

        left_has_more = False
        right_has_more = False

        if current_page <= around_count + 15:
            left_pages = range(1, current_page)
        else:
            left_has_more = True
            left_pages = range(current_page - around_count, current_page)

        if current_page >= num_pages - around_count - 1:
            right_pages = range(current_page + 1, num_pages + 1)
        else:
            right_has_more = True
            right_pages = range(current_page + 1, current_page + around_count + 1)

        return {
            # left_pages：代表的是当前这页的左边的页的页码
            'left_pages': left_pages,
            # right_pages：代表的是当前这页的右边的页的页码
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': num_pages
        }

    def process_paramter(self, request):
        search_key = request.GET.get('search')
        handle_type = self.TYPE_ALL if search_key is None else self.TYPE_SEARCH
        return handle_type, search_key
