from django.conf.urls import include, url
import shopping.views as v

urlpatterns = [
	url(r'artists/$', v.artist_list_view, name="artist_list"),
	url(r'artist/$', v.artist_view, name="artist"),
	url(r'item/$', v.item_view, name="item"),
    url(r'^$', v.index, name='index'),

    url(r'artists_list/$', v.get_artist_list, name="get_artists_list"),
    url(r'artists_profile/$', v.get_artist_profile, name="get_artist_profile"),
    url(r'item_info/$', v.get_item_info, name="get_item_info"),

    

]