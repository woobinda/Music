from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Category, Tag, Article, Comment


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug')
    list_display_links = ('name',)
    search_fields = ['name', 'slug', 'description']
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    search_fields = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}
    # actions = None

admin.site.register(Tag, TagAdmin)


def make_published(queryset):
    queryset.update(status='P')
make_published.short_description = "Mark selected stories as published"


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


def make_draft(queryset):
    queryset.update(status='D')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'views', 'status',
                    'was_published_recently', 'owner', 'icon')
    list_filter = ['created_date']
    search_fields = ['title']
    ordering = ['-publish_date']
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = 'publish_date'
    filter_horizontal = ('tags',)
    readonly_fields = ('publish_date', 'created_date')

    fieldsets = [
        ('Item',             {'fields': [('title', 'slug'),
                                         'icon', 'category', 'content']}),
        ('Date information', {'fields': [('publish_date', 'created_date')],
                              'classes': ['collapse']}),
        ('Related tags',     {'fields': ['tags']}),
        ('Metas',            {'fields': [('status', 'views', 'owner')]}),
    ]

    actions = ['delete_selected', make_published, 'make_draft']
    form = ArticleAdminForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()

    make_draft.short_description = "Mark selected stories as draft"

    def make_expired(self, request, queryset):
        rows_updated = queryset.update(status='E')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(
            request, "%s successfully marked as expired." % message_bit)
    make_expired.short_description = "Mark selected stories as expired"


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
