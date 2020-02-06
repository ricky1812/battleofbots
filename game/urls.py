from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
			path('',views.index,name='b_index1'),
			path('signup/',views.signup,name='signup'),
			path('login/',views.login_view,name='login'),
			path('signout/',views.logout_view,name='logout'),
			path('index2/',views.index2,name = 'b_index2'),
			path('index1/',views.index1,name='index1'),
               ##weapons
			path('index2/play/',views.play,name = 'play'),
			path('index2/play/<key>',views.ordering_weapons,name='ordering-weapons'),
			path('index2/play/<key>/confirm',views.ordered_weapons,name='confirm-add'),
			path('index2/sell',views.sell_weapons_list,name = 'sell-weapons'),
			path('index2/sell/<key>/delete',views.sell_weapons,name='confirm-del'),
			##defence
			path('index2/play2/',views.play2,name = 'play2'),
			path('index2/play2/<key>',views.ordering_defences,name='ordering-defences'),
			path('index2/play2/<key>/confirm2',views.ordered_defences,name='confirm-add-2'),
			path('index2/sell2',views.sell_defence_list,name = 'sell-defence'),   ##error
			path('index2/sell2/<key>/delete',views.sell_defence,name='confirm-del-2'),
            path('index2/load/',views.load,name='load'),
			##main
			path('index2/main',views.match,name= 'match_test'),
			path('index2/main1',views.match1,name= 'match_test_1'),
			path('index2/main2',views.match2,name= 'match_test_2'),
			path('index2/main3',views.match3,name= 'match_test_3'),
			

		]
			