from django.urls import path

from financial.views.financial_entry import FinancialEntryView, FinancialEntryDetailView

urlpatterns = [
    path('', FinancialEntryView.as_view(), name='financial_entry_view'),
    path('/<id>', FinancialEntryDetailView.as_view(), name='financial_entry_detail_view'),
]
