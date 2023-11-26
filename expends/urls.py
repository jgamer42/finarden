
from django.urls import path
from expends.views import uploadBankAccount
urlpatterns = [
    path('/importexpends',uploadBankAccount,name="importexpends")
]