from django.urls import path
from reports.views import *

app_name = 'reports'
urlpatterns = [
    # path('', index, name='index'),
    path('', RatingCountListView.as_view(), name = 'rating-list'),
    path('xls/', RatingToXls.as_view(), name='xlsTofile'),

    ]