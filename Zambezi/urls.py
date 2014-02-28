from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url("^home/$", 'booker.views.home', name='home'),

    url("^new_book/$", 'booker.views.new_book', name='new_book'),

    url('^show_books/$', 'booker.views.show_books', name='show_books'),

    url('^edit_book/(?P<book_id>\w+)/$', 'booker.views.edit_book', name='edit_book'),

    url('^show_books/(?P<book_id>\w+)/$', 'booker.views.show_book', name='show_book'),

    url('^add_owner/(?P<book_id>\w+)/$', 'booker.views.add_owner', name='add_owner')

)
