from django.shortcuts import render

def setsession(request):
    request.session['name']='Steve Roger'
    # request.session.set_expiry(30)            # set the session for 30 second and page will expires in 30 seconds
    return render(request,'core/setsession.html')

def getsession(request):
    name =request.session.get('name',default='Guest')
    key = request.session.keys()                   # gives us all the key 
    items = request.session.items()
    return render(request,'core/getsession.html',{'name':name,'key':key,'items':items})

def deletesession(request):
    # request.session.flush()                  # clears the session data from the current request but doesn't delete it from the session store (e.g., database). 
    # request.session.clear_expired()          # Clear the expired session from the database
    # request.session.delete()
    request.session.clear()
    return render(request,'core/deletesession.html')