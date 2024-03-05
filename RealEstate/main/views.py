from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse


properties=[
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
def main_page(request:HttpRequest):

    return render(request, "main/main_page.html")

def properties_page(request:HttpRequest):
    context={'properties':properties}
    
    return render(request, "main/properties_page.html" ,context ) 



def contact_page(request:HttpRequest):
    
    return render(request, "main/contact_page.html")
    