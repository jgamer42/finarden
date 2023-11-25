from tips.models import Tip
from expends.models import Expend,Income,Bill
from datetime import datetime
class ModifyIndex:
    def __init__(self,original_method):
        self.method = original_method
        
    def build_donut_plot(self,expends,bills)->dict:
        total_bills = sum([bill.amount for bill in bills])
        total_expends = sum([expend.amount for expend in expends])
        return {
            "labels":["Fijos","Variables"],
                "datasets":[{
                    "data":[total_bills,total_expends],
                    "backgroundColor": [
                        'rgb(255, 99, 132)',
                        'rgb(255, 205, 86)',
                    ],
            }]}
    
    def build_scatter_plot(self,expends)->dict:
        days_maps = {
            0:"lunes",
            1:"martes",
            2:"miercoles",
            3:"jueves",
            4:"viernes",
            5:"sabado",
            6:"domingo"
        }
        raw_data = [{"x":days_maps[expend.date.weekday()],"y":expend.date.hour}for expend in expends]
            
        return {
                "datasets": [{
                    "label": 'Gastos',
                    "data":raw_data,
                    "backgroundColor": 'rgb(255, 99, 132)'
                }]}
        
    def build_bar_plot(self,bills):
        days = set()
        amounts = {}
        values = []
        for bill in bills:
            days.add(bill.cutoff)
            if bill.cutoff in amounts.keys():
                amounts[bill.cutoff] += bill.amount
            else:
                amounts[bill.cutoff] = bill.amount
        days = sorted(list(days))
        values = [0]*len(days)
        for i,day in enumerate(days):
            values[i] = amounts[day]
            
        return { 
                "labels": days,
                "datasets": [
                    {
                        "label": 'Fecha corte facturas',
                        "data": values,
                        "borderWidth": 1
                    }
                ]
            }
        
    def build_timeline_plot(self,incomes,bills,expends):
        days = set()
        incomes_map = {}
        expends_map = {}
        for income in incomes:
            days.add(income.date.day)
            if income.date.day in incomes_map.keys():
                incomes_map[income.date.day] += income.amount
            else:
                incomes_map[income.date.day] = income.amount
                
        for expend in expends:
            days.add(expend.date.day)
            if expend.date.day in expends_map.keys():
                expends_map[expend.date.day] += expend.amount
            else:
                expends_map[expend.date.day] = expend.amount
                
        for bill in bills:
            days.add(bill.cutoff)
            if bill.cutoff in expends_map.keys():
                expends_map[bill.cutoff] += bill.amount
            else:
                expends_map[bill.cutoff] = bill.amount
        days = sorted(list(days))
        incomes = {
            "label":"Ingresos",
            "fill": "true",
            "data": [incomes_map.get(day,0)for day in days],
            "borderColor": 'rgb(0, 128, 0)',
            "tension": 0.1
        }
        expends = {
            "label":"Egresos",
            "fill": "true",
            "data": [expends_map.get(day,0)for day in days],
            "borderColor": 'rgb(128, 0, 0)',
            "tension": 0.1
        }
        
        return {
                "labels": days,
                "datasets": [incomes,expends]
            }
    def target_index(self,request,*args,**kwargs):
        today = datetime.now()
        tip_of_day = Tip.objects.values("detail").order_by("created").filter(active=True).last()
        if not tip_of_day:
            tip_of_day={'detail':""}
        if request.user.is_superuser:
            incomes = Income.objects.filter(date__month=today.month)
            expends = Expend.objects.filter(date__month=today.month)
            bills = Bill.objects.filter(active=True)
        else:
            incomes = Income.objects.filter(owner=request.user,date__month=today.month)
            expends = Expend.objects.filter(owner=request.user,date__month=today.month)
            bills = Bill.objects.filter(owner=request.user,active=True)
        timeline_data = []
        scatter_data = []
        bar_data = []
        donut_data = []
        if expends.exists():
            scatter_data = self.build_scatter_plot(expends)
        if bills.exists():
            bar_data = self.build_bar_plot(bills)
        if expends.exists() and bills.exists():
            donut_data = self.build_donut_plot(expends,bills)
        if incomes.exists() and (expends.exists() or bills.exists()):
            timeline_data = self.build_timeline_plot(incomes,bills,expends)

        dashboard_data = {
            "donut":donut_data,
            "timeline":timeline_data,
            "scatter":scatter_data,
            "bar":bar_data
        }
        return self.method(request,extra_context={"tip_of_day":tip_of_day["detail"],"dashboard_data":dashboard_data})