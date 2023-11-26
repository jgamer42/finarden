import os
import pandas as pd
import datetime
from expends.models import Expend,Income
from django.shortcuts import redirect

 
def uploadBankAccount(request):
    if request.method == "POST":
        file = request.FILES["bank_statement"]
        tmp_file = open(file.name,"wb+")
        for chunk in file.chunks():
            tmp_file.write(chunk)
        tmp_file.close()
        dataset = pd.read_csv(file.name)
        dataset = dataset.fillna(0)
        os.remove(file.name)
        incomes = []
        expends = []
        for _,row in dataset.iterrows():
            date = datetime.datetime.strptime(row["Fecha"], "%Y/%m/%d")
            if row["Valor Crédito"] <= 0:
                expends.append(Expend(detail="subio desde extracto",amount=abs(row["Valor Débito"]),where=row["Descripción"],owner=request.user,date=date))
            else:
                incomes.append(Income(detail=row["Descripción"],amount=abs(row["Valor Crédito"]),owner=request.user,date=date))
        Income.objects.bulk_create(incomes)
        Expend.objects.bulk_create(expends)
            
    return redirect("/homeexpends/expend/")