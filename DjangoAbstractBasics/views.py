from django.shortcuts import render

# Create your views here.

def IndexView(request):
	return render(request, 'index.html', {})

'''
Do you want to start a django project with an Abstract Base User? or perhaps you would prefer the email field to the username 
field provided by django default user model....Well DjangoAbstractStartPoint is a great place to 
begin your django project with pre-written, easily editable AbstractBaseUser with email as the primary login field, 
media and static settings already included, simple and refined homepage, login and registration function, 
and best of all, you can easily integrate it to your django project and voila 
you proceed to writing inportant codes and DjangoAbstractStartPoint would take care of the rest....
'''