from django.contrib import admin
from django.shortcuts import render

class ModifyIndex:
    def __init__(self,original_method):
        self.method = original_method
        
    def target_index(self,request,*args,**kwargs):
        return self.method(request,extra_context={"prueba":"mundo"})