from django.shortcuts import render

def setsession(request):
    request.session['name']='Steve Roger'
    request.session['heroic_name']='Captain'
    return render(request,'core/setsession.html')

def getsession(request):
    # name =request.session['name']
    name =request.session.get('name',default='Guest')
    h_name =request.session.get('heroic_name',default='Guest')
    return render(request,'core/getsession.html',{'name':name,'h_name':h_name})

def deletesession(request):
    del request.session['name']      # With this we will delete value but session data will be remain in database and in cookies of the browser
    del request.session['heroic_name']
    return render(request,'core/deletesession.html')