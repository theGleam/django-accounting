from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$',
        views.DashboardView.as_view(),
        name="dashboard"),

    # Organizations
    url(r'^organization/$',
        views.OrganizationListView.as_view(),
        name="organization-list"),
    url(r'^organization/selector/$',
        views.OrganizationSelectorView.as_view(),
        name="organization-selector"),
    url(r'^organization/create/$',
        views.OrganizationCreateView.as_view(),
        name="organization-create"),
    url(r'^organization/(?P<pk>\d+)/edit/$',
        views.OrganizationUpdateView.as_view(),
        name="organization-edit"),
    url(r'^organization/(?P<pk>\d+)/detail/$',
        views.OrganizationDetailView.as_view(),
        name="organization-detail"),
    url(r'^organization/(?P<pk>\d+)/select/$',
        views.OrganizationSelectionView.as_view(),
        name="organization-select"),

    # Invoices
    url(r'^invoice/$',
        views.InvoiceListView.as_view(),
        name="invoice-list"),
    url(r'^invoice/create/$',
        views.InvoiceCreateView.as_view(),
        name="invoice-create"),
    url(r'^invoice/(?P<pk>\d+)/edit/$',
        views.InvoiceUpdateView.as_view(),
        name="invoice-edit"),
    url(r'^invoice/(?P<pk>\d+)/delete/$',
        views.InvoiceDeleteView.as_view(),
        name="invoice-delete"),
    url(r'^invoice/(?P<pk>\d+)/detail/$',
        views.InvoiceDetailView.as_view(),
        name="invoice-detail"),

    # Bills
    url(r'^bill/$',
        views.BillListView.as_view(),
        name="bill-list"),
    url(r'^bill/create/$',
        views.BillCreateView.as_view(),
        name="bill-create"),
    url(r'^bill/(?P<pk>\d+)/edit/$',
        views.BillUpdateView.as_view(),
        name="bill-edit"),
    url(r'^bill/(?P<pk>\d+)/delete/$',
        views.BillDeleteView.as_view(),
        name="bill-delete"),
    url(r'^bill/(?P<pk>\d+)/detail/$',
        views.BillDetailView.as_view(),
        name="bill-detail"),

    # Payments
    url(r'^payment/(?P<pk>\d+)/edit/$',
        views.PaymentUpdateView.as_view(),
        name="payment-edit"),
    url(r'^payment/(?P<pk>\d+)/delete/$',
        views.PaymentDeleteView.as_view(),
        name="payment-delete"),
)
