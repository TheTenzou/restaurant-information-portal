from django.contrib import admin
from ..models import News, NewsPicture


class NewsPictures(admin.TabularInline):
    model = NewsPicture
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    fields = ('headline', 'news_type', 'news_text', 'card_picture')
    inlines = [
        NewsPictures,
    ]
    list_display = ('headline', 'news_type', 'publication_date')
    list_filter = ['news_type', 'publication_date']
    search_fields = ['headline', 'news_text']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, kwargs)
        form.base_fields['headline'].label = 'Заголовок'
        form.base_fields['news_text'].label = 'Текст'
        # form.base_fields['publication_date'].label = 'Дата публикации'
        form.base_fields['news_type'].label = 'Тип новости'
        form.base_fields['card_picture'].label = 'Картинка карточки'
        return form


admin.site.register(News, NewsAdmin)