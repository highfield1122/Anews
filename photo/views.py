from django.views.generic import FormView
from django.urls import reverse_lazy
from . import forms
from django.contrib import messages
from django.core.mail import EmailMessage

from django.shortcuts import render
# django.views.genericからTemplateView、ListViewをインポート
from django.views.generic import TemplateView, ListView
#
from .models import Blog
from .models import Category, tokomodel,Blog
from django.shortcuts import get_object_or_404
# django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
# formsモジュールからPhotoPostFormをインポート
# method_decoratorをインポート
from django.utils.decorators import method_decorator
# login_requiredをインポート
from django.contrib.auth.decorators import login_required
# modelsモジュールからモデルPhotoPostをインポート
from .models import tokomodel
# django.views.genericからDetailViewをインポート
from django.views.generic import DetailView
# django.views.genericからDeleteViewをインポート
from django.views.generic import DeleteView
from django.shortcuts import render, redirect
from .forms import CategoryForm

class ContactView(FormView):
    """お問い合わせ"""

    # テンプレート
    template_name = "contact.html"
    # フォーム
    form_class = forms.ContactForm
    # お問い合わせ送信成功後URL
    success_url = reverse_lazy("photo:contact")

    def form_valid(self, form):
        """お問い合わせ送信処理"""

        # パラメータ取得
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        title = form.cleaned_data["title"]
        message_param = form.cleaned_data["message"]

        # お問い合わせメールの送信処理（例として、自分自身にメールを送る設定）
        subject = f"お問い合わせ: {title}"
        message = f"名前: {name}\nメールアドレス: {email}\n\n{message_param}"
        from_email = "XXXXXX@example.com"  # 送信元のメールアドレス
        recipient_list = ["aio12345x@gmail.com"]  # 受信者のメールアドレスリスト

        msg = EmailMessage(
            subject=subject, body=message, from_email=from_email, to=recipient_list
        )

        try:
            msg.send()
            messages.success(self.request, "送信完了しました。")
        except Exception as e:
            messages.error(self.request, f"送信に失敗しました。エラー：{e}")

        return super().form_valid(form)
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def blog_by_category(request, categoryhyouji):
    # カテゴリ名を元にカテゴリを取得
    category = get_object_or_404(Category, name=categoryhyouji)

    # カテゴリに関連するブログを取得
    blogs = Blog.objects.filter(category=category)

    # レンダリング
    return render(request, 'blog_by_category.html', {'blogs': blogs})

def blog_detail(request, slug):

    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})
    
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})


def add_category_success(request):
    return render(request, 'add_category_success.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('photo:add_category_success')  # リダイレクト先のURLを指定
    else:
        form = CategoryForm()

    return render(request, 'your_template_name.html', {'form': form})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = category.tokomodel_set.all()

    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category_detail.html', context)
class IndexView(ListView):
    '''トップページのビュー
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    model = tokomodel
    # 投稿日時の降順で並べ替える
    paginate_by = 9
class Index2View(ListView):
    template_name='index2.html'
        # モデルBlogPostのオブジェクトにorder_by()を適用して
    # 投稿日時の降順で並べ替える
    model = tokomodel
    paginate_by = 9
class Category2View(ListView):
    template_name='categori.html'
    model = tokomodel
    paginate_by = 9
class AboutView(ListView):
    template_name='about.html'
    model = tokomodel
    paginate_by = 9
class Latest_newsView(ListView):
    template_name='latest_news.html'
    model = tokomodel
    paginate_by = 9
class ElementsView(ListView):
    template_name='elements.html'
    model = tokomodel
    paginate_by = 9
class BlogView(ListView):
    template_name='blog.html'
    model = tokomodel

    paginate_by = 9
class SingleblogView(ListView):
    template_name='singleblog.html'
    model = tokomodel

    paginate_by = 9
class DetailsView(ListView):
    template_name='details.html'
    model = tokomodel

    paginate_by = 9


    paginate_by = 9
class Page2View(ListView):
    template_name='Page2.html'
    model = tokomodel

    paginate_by = 9
class TaikiView(ListView):
    template_name='taiki1.html'
    model = tokomodel

    paginate_by = 9
class Taiki2View(ListView):
    template_name='taiki2.html'
    model = tokomodel

    paginate_by = 9
    
class Taiki3View(ListView):
    template_name='taiki3.html'
    model = tokomodel

    paginate_by = 9
    
class Taiki4View(ListView):
    template_name='taiki4.html'
    model = tokomodel

    paginate_by = 9
    
class Taiki5View(ListView):
    template_name='taiki5.html'
    model = tokomodel

    paginate_by = 9
    

def blog(request):
    categories = Category.objects.all()
    posts = tokomodel.objects.all()

    context = {
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)

# デコレーターにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる







