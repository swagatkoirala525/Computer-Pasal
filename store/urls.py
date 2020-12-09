from django.urls import path

from .middlewares.auth import auth_middleware
from .views.about import About
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.contact import Contact
from .views.customer import Customer
from .views.details import Details
from .views.home import Index, store
from .views.login import Login, logout
from .views.orders import OrderView
from .views.search import Search
from .views.signup import Signup
from .views.start import Start
from .views.wishlist import Wishlist

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('start', Start.as_view(), name='start'),
    path('store', store, name='store'),
    path('about', About.as_view(), name='about'),
    path('contact', Contact.as_view(), name='contact'),
    path('search', Search.as_view(), name='search'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('customer', Customer.as_view(), name='customer'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('wishlist', Wishlist.as_view(), name='wishlist'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('product-details/<slug>/', Details.as_view(), name='product-details'),

]
