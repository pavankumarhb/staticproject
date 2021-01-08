from django.shortcuts import render
def view1(request):
    myName="pavan"
    favPlayer="msdhoni"
    favAnimal="lion"
    favSubject="Python"
    d={'name':myName,'player':favPlayer,'animal':favAnimal,'subject':favSubject}
    return render(request,'staticApp1/1.html',d)
