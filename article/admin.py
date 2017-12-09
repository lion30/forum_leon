from django.contrib import admin

from comment.models import Comment
from .models import Article

'''设置文章内联'''
class CommentInline(admin.TabularInline):
	model = Comment
	can_delete = False


class Articleadmin(admin.ModelAdmin):
	list_display = ('block', 'title', 'content', 'status', 'create_timestamp', 'last_update_timestamp')

	'''设置下拉选项'''
	actions = ['make_picked']
	'''内联名称'''
	inlines = [CommentInline]
	'''显示折叠样式'''
	fieldsets = (
		("基本", {"classes": ("",), "fields": ("title", "content")}),
		("高级", {"classes": ("collapse",), "fields": ("status", )})
	)
	readonly_fields = ("owner", "content", "status", "create_timestamp")


'''设置文章精华'''
	def make_picked(self, request, queryset):
		for a in queryset:
			a.status = 10
			a.save()
	make_picked.short_description = '设置精华'


admin.site.register(Article, Articleadmin)
