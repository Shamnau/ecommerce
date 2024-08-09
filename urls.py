from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('contact', views.contact),
    path('chocolate', views.chocolate),
    path('about',views.about),
    path('testimonial',views.testimonial),
    path('pro',views.pro,name='pro'),
    path('viewproduct', views.viewproduct, name='viewproduct'),
    path('edit <int:id>', views.edit, name='edit'),
    path('delete <int:id>', views.delete, name='delete'),
    path('signup',views.signup),
    path('login',views.loginpage,name='loginpage'),
    path('logout',views.logoutpage,name='logoutpage'),

    path('removecart <int:id>',views.removecart,name='removecart'),
    path('shipping',views.shipping,name='shipping'),
    path('orders',views.orders,name='orders'),
    path('editaddr',views.editaddr,name='editaddr'),
    path('deleteaddr <int:id>',views.deleteaddr,name='deleteaddr'),
    path('orderconf',views.orderconf,name='orderconf'),






    #path('cartitem', views.cartitem, name='cartitem'),
    path('proview <int:id>',views.proview,name='proview'),
    #path('addtocart<int:id>',views.addtocart,name='addtocart'),
    path('cart',views.cart,name='cart'),
    ]

