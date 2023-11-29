from django.urls import path
from . import views
from .views import blog, category_detail
from .views import add_category,blog_list,blog_detail
from .views import category_list, blog_by_category 

# URLパターンを逆引きできるように名前を付ける
app_name = 'photo'

# URLパターンを登録する変数
urlpatterns = [
    # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', blog_list, name='blog_list'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('add_category/', add_category, name='add_category'),
    path('add_category_success/', views.add_category_success, name='add_category_success'),
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<slug:slug>/', blog_detail, name='blog_detail'),  # これが必要
    path('categoryhyouji/', category_list, name='category_list'),
    path('categoryhyouji/<str:categoryhyouji>/', views.blog_by_category, name='blog_by_category'),

    
    # 写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    #kaeru
    path('index2/', views.Index2View.as_view(), name='index'),
    path('categori/', views.Category2View.as_view(), name='categori'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('latest_news/', views.Latest_newsView.as_view(), name='latest_news'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('elements/', views.ElementsView.as_view(), name='elements'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('single-blog/', views.SingleblogView.as_view(), name='single-blog'),
    path('details/', views.DetailsView.as_view(), name='details'),
    path('page2/', views.Page2View.as_view(), name='details'),
    path('taiki1/', views.TaikiView.as_view(), name='details'),
    path('taiki2/', views.Taiki2View.as_view(), name='details'),
    path('taiki3/', views.Taiki3View.as_view(), name='details'),
    path('taiki4/', views.Taiki4View.as_view(), name='details'),
    path('taiki5/', views.Taiki5View.as_view(), name='details'),




]
