from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from datetime import datetime
from django.shortcuts import redirect
from .models import insertable
from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponseRedirect
from .forms import NameForm
from django.utils.translation import gettext as _
import random
from project import settings
def index(request):
    now = datetime.now()
    insertable.objects.create(method = request.method, path = request.path, datetime = now.strftime("%H:%M:%S %d/%m/%Y"))
    return HttpResponse("Hello, world. You're at the polls index.")

def site(request):
    # response = HttpResponse("Here's the text of the web page.")
    # response = HttpResponse("Text only, please.", content_type="text/plain")
    # response = HttpResponse(b'Bytestrings are also accepted.')
    now = datetime.now()
    insertable.objects.create(method = request.method, path = request.path, date = now.strftime("%m/%Y"),company_id = "companyz", time =now.strftime("%H:%M:%S"),day= now.strftime("%d"),client_id = 2)
   
    return redirect('/site/company')

def locale(request):
    # response = HttpResponse("Here's the text of the web page.")
    # response = HttpResponse("Text only, please.", content_type="text/plain")
    # response = HttpResponse(b'Bytestrings are also accepted.')
    output = _("Welcome to my site.")
    return HttpResponse(settings.LOCALE_PATHS)
    
def company(request):
    cid=request.POST.get("company","")
    date=request.POST.get("date","")
    querry = (insertable.objects
    .values('date','company_id','client_id').filter(company_id=cid,date=date).annotate(number=Count('company_id')).order_by('client_id')
    )
    
    object={'querry':querry}
    return render(request, 'company.html',object)

