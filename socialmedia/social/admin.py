from django.contrib import admin
from .models import Friendship, Follow

class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'user1', 'user2', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user1__username', 'user2__username')

class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'followee', 'created_at')
    search_fields = ('follower__username', 'followee__username')

admin.site.register(Friendship, FriendshipAdmin)
admin.site.register(Follow, FollowAdmin)
