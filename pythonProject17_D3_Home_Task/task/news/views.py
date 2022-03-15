# импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView  # импортируем класс получения деталей объекта
from .models import  Post

#Новости
class PostsList(ListView):
    model = Post
    template_name = 'newsall.html'
    context_object_name = 'newsall'
    queryset = Post.objects.order_by('-dateCreation') # выводим статьи в обратном порядке

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value1'] =f"Все новости . общее количество новостей ->>{Post.objects.all().count()}"
        return context

class PostDetail(DetailView):

    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'news.html'  # название шаблона будет product.html
    context_object_name = 'news'  # название объекта. в нём будет

