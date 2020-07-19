from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.db import transaction

from cms.helper_functions import *
from cms.models import *

from datetime import datetime

import os

# Create your views here.
@login_required
def index(request):
  report_menus = ReportMenu.objects.values('code', 'display_name').filter(is_active=True).order_by('code')
  
  context = {
    'report_menus': report_menus,
    'title'       : 'Home'
  }
  return render(request, 'cms/index.html', context)

def _login(request):
  if request.method == "POST":
    def guard():
      tbl_usersprofiles = TblUsersprofile.objects.using('control_db').values_list('useremail', flat=True)
      tbl_usersprofiles = [tbl_usersprofile.strip().lower() for tbl_usersprofile in tbl_usersprofiles]
      if username.find('@') == -1:
        return False, "Please use email as a username."
      elif password == '':
        return False, "Password must not empty."
      elif username not in tbl_usersprofiles:
        return False, 'This username is not have privileges.'
      else:
        return True, "success"
    
    username = request.POST.get("username").lower()
    password = request.POST.get("password", None)
    
    guard_status, msg = guard()

    if guard_status:
      if this_user_in_ldap(username, password):
        if username not in list(User.objects.values_list('username', flat=True)):
          temp_name = username.lower()[:username.find('@')].split(".")
          User.objects.create_user(
            username   = username,
            password   = password,
            email      = username,
            first_name = temp_name[0],
            last_name  = temp_name[-1],
            is_active  = True
          )
        else:
          user = User.objects.get(username=username)
          user.set_password(password)
          user.save()
        
        user = authenticate(request, username=username, password=password)
        login(request, user)
      else:
        msg = "Username or password is incorrect."
    else:
      pass

    context = {
      'msg': msg,
      'title': 'Login'
    }
    return JsonResponse(context)
  else:
    context = {'title': 'Login'}
    return render(request, 'login.html', context)

def _logout(request):
  logout(request)
  context = {'title': 'Login'}
  return render(request, 'login.html', context)

# cms
@login_required
def mpic_movie_imp_cms(request):
  page = request.GET.get('page', 1)
  
  report_menus = ReportMenu.objects.values('code', 'display_name').filter(is_active=True).order_by('code')

  tbl_mpic_movie_imp_axs = TblMpicMovieImpAx.objects.using('mjcdata').all().order_by('-tbl_id')
  tbl_mvs = TblMv.objects.using('ticket_sale').values('mv_tname', 'mv_kname', 'mv_sname', 'mv_ename').order_by('-mv_id')
  
  for tbl_mpic_movie_imp_ax in tbl_mpic_movie_imp_axs:
    if tbl_mpic_movie_imp_ax.amend_date:
      tbl_mpic_movie_imp_ax.amend_date = tbl_mpic_movie_imp_ax.amend_date.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

  search_key = request.GET.get('search_key', '')
  if search_key:
    tbl_mpic_movie_imp_axs = search(search_key, tbl_mpic_movie_imp_axs)

  paginator = Paginator(tbl_mpic_movie_imp_axs, 10)
  try:
    tbl_mpic_movie_imp_axs = paginator.page(page)
  except EmptyPage:
    tbl_mpic_movie_imp_axs = paginator.page(paginator.num_pages)
  
  context = {
    'tbl_mpic_movie_imp_axs': tbl_mpic_movie_imp_axs,
    'tbl_mvs'               : tbl_mvs,
    'search_key'            : search_key,
    'report_menus'          : report_menus,
    'title'                 : 'CMS: Movie'
  }
  return render(request, 'cms/mpic_movie_imp_cms.html', context)

@login_required
def mpic_customer_imp_cms(request):
  page = request.GET.get('page', 1)

  report_menus = ReportMenu.objects.values('code', 'display_name').filter(is_active=True).order_by('code')
  tbl_mpic_customer_imp_axs = TblMpicCustomerImpAx.objects.using('mjcdata').all().order_by('-tbl_id')

  for tbl_mpic_customer_imp_ax in tbl_mpic_customer_imp_axs:
    if tbl_mpic_customer_imp_ax.amend_date:
      tbl_mpic_customer_imp_ax.amend_date = tbl_mpic_customer_imp_ax.amend_date.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

  search_key = request.GET.get('search_key', '')
  if search_key:
    tbl_mpic_customer_imp_axs = search(search_key, tbl_mpic_customer_imp_axs)

  paginator = Paginator(tbl_mpic_customer_imp_axs, 10)
  try:
    tbl_mpic_customer_imp_axs = paginator.page(page)
  except EmptyPage:
    tbl_mpic_customer_imp_axs = paginator.page(paginator.num_pages)
  
  context = {
    'tbl_mpic_customer_imp_axs': tbl_mpic_customer_imp_axs,
    'search_key'               : search_key,
    'report_menus'             : report_menus,
    'title'                    : 'CMS: Customer'
  }
  return render(request, 'cms/mpic_customer_imp_cms.html', context)
# cms

# create_or_update
def mpic_movie_imp_cms_edit_data(request):
  datas = request.POST
  try:
    tbl_mpic_movie_imp_axs = TblMpicMovieImpAx.objects.using('mjcdata').filter(mvcode=datas.get('mvcode'), mvtitle=datas.get('mvtitle')).latest('tbl_id')
  except:
    tbl_mpic_movie_imp_axs = ""
  
  if tbl_mpic_movie_imp_axs:
    tbl_mpic_movie_imp_axs.mvcode      = format_null_data(datas.get('mvcode'))
    tbl_mpic_movie_imp_axs.mvtitle     = format_null_data(datas.get('mvtitle'))
    tbl_mpic_movie_imp_axs.mvname      = format_null_data(datas.get('mvname'))
    tbl_mpic_movie_imp_axs.unit_price  = format_null_data(datas.get('unit_price'))
    tbl_mpic_movie_imp_axs.perc_disc   = format_null_data(datas.get('perc_disc'))
    tbl_mpic_movie_imp_axs.mvmapping   = format_null_data(datas.get('mvmapping'))
    tbl_mpic_movie_imp_axs.releasedate = format_null_data(datas.get('releasedate'))
    tbl_mpic_movie_imp_axs.finishdate  = format_null_data(datas.get('finishdate'))
    tbl_mpic_movie_imp_axs.amend_date  = format_null_data(datas.get('amend_date'))
    tbl_mpic_movie_imp_axs.amend_by    = format_null_data(datas.get('amend_by'))

    try:
      with transaction.atomic():
        tbl_mpic_movie_imp_axs.save()
        tbl_id = tbl_mpic_movie_imp_axs.tbl_id
        msg = 'success'
    except:
      tbl_id = ''
      msg = 'Error while update data in database.'
  else:
    try:
      with transaction.atomic():
        tbl_mpic_movie_imp_ax = TblMpicMovieImpAx.objects.using('mjcdata').create(
          mvcode      = format_null_data(datas.get('mvcode')),
          mvtitle     = format_null_data(datas.get('mvtitle')),
          mvname      = format_null_data(datas.get('mvname')),
          unit_price  = format_null_data(datas.get('unit_price')),
          perc_disc   = format_null_data(datas.get('perc_disc')),
          mvmapping   = format_null_data(datas.get('mvmapping')),
          releasedate = format_null_data(datas.get('releasedate')),
          finishdate  = format_null_data(datas.get('finishdate')),
          amend_date  = format_null_data(datas.get('amend_date')),
          amend_by    = format_null_data(datas.get('amend_by'))
        )
        tbl_id = tbl_mpic_movie_imp_ax.tbl_id
        msg = 'success'
    except:
      tbl_id = ''
      msg = 'Error while save data to database.'
  context = {
    'tbl_id': tbl_id,
    'msg'   : msg
  }
  return JsonResponse(context)

def mpic_customer_imp_cms_edit_data(request):
  datas = request.POST
  try:
    tbl_mpic_customer_imp_axs = TblMpicCustomerImpAx.objects.using('mjcdata').filter(custcode=datas.get('custcode')).latest('tbl_id')
  except:
    tbl_mpic_customer_imp_axs = ""
  
  if tbl_mpic_customer_imp_axs:
    tbl_mpic_customer_imp_axs.custcode    = format_null_data(datas.get('custcode'))
    tbl_mpic_customer_imp_axs.custname    = format_null_data(datas.get('custname'))
    tbl_mpic_customer_imp_axs.custaddress = format_null_data(datas.get('custaddress'))
    tbl_mpic_customer_imp_axs.custgroup   = format_null_data(datas.get('custgroup'))
    tbl_mpic_customer_imp_axs.postprofile = format_null_data(datas.get('postprofile'))
    tbl_mpic_customer_imp_axs.site        = format_null_data(datas.get('site'))
    tbl_mpic_customer_imp_axs.warehouse   = format_null_data(datas.get('warehouse'))
    tbl_mpic_customer_imp_axs.buax        = format_null_data(datas.get('buax'))
    tbl_mpic_customer_imp_axs.divax       = format_null_data(datas.get('divax'))
    tbl_mpic_customer_imp_axs.locax       = format_null_data(datas.get('locax'))
    tbl_mpic_customer_imp_axs.intercocd   = format_null_data(datas.get('intercocd'))
    tbl_mpic_customer_imp_axs.custmapping = format_null_data(datas.get('custmapping'))
    tbl_mpic_customer_imp_axs.amend_date  = format_null_data(datas.get('amend_date'))
    tbl_mpic_customer_imp_axs.amend_by    = format_null_data(datas.get('amend_by'))
    
    tbl_mpic_customer_imp_axs.save()
    try:
      with transaction.atomic():
        tbl_mpic_customer_imp_axs.save()
        tbl_id = tbl_mpic_customer_imp_axs.tbl_id
        msg = 'success'
    except:
      tbl_id = ''
      msg = 'Error while update data in database.'
  else:
    try:
      with transaction.atomic():
        tbl_mpic_customer_imp_ax = TblMpicCustomerImpAx.objects.using('mjcdata').create(
          custcode    = format_null_data(datas.get('custcode')),
          custname    = format_null_data(datas.get('custname')),
          custaddress = format_null_data(datas.get('custaddress')),
          custgroup   = format_null_data(datas.get('custgroup')),
          postprofile = format_null_data(datas.get('postprofile')),
          site        = format_null_data(datas.get('site')),
          warehouse   = format_null_data(datas.get('warehouse')),
          buax        = format_null_data(datas.get('buax')),
          divax       = format_null_data(datas.get('divax')),
          locax       = format_null_data(datas.get('locax')),
          intercocd   = format_null_data(datas.get('intercocd')),
          custmapping = format_null_data(datas.get('custmapping')),
          amend_date  = format_null_data(datas.get('amend_date')),
          amend_by    = format_null_data(datas.get('amend_by'))
        )
        tbl_id = tbl_mpic_customer_imp_ax.tbl_id
        msg = 'success'
    except:
      tbl_id = ""
      msg = 'Error while save data to database.'
  
  context = {
    'tbl_id': tbl_id,
    'msg'   : msg
  }
  return JsonResponse(context)
# create_or_update

# report
@login_required
def report_render(request, report_code):
  report_menus = ReportMenu.objects.values('code', 'display_name').filter(is_active=True).order_by('code')
  report_link = TblReportmenus.objects.using('control_db').get(mnucod=report_code).rptlink
  context = {
    'report_link'  : report_link,
    'report_menus' : report_menus,
    'title'        : 'Report: {}'.format(report_code)
  }
  return render(request, 'cms/report_template.html', context)
# report

# delete
def mpic_customer_imp_cms_delete(request):
  try:
    tbl_id = int(request.POST.get('tbl_id'))

    try:
      with transaction.atomic():
        TblMpicCustomerImpAx.objects.using('mjcdata').filter(tbl_id=request.POST.get('tbl_id')).delete()
        msg = 'success'
    except:
      msg = 'Error while delete in database.'
  except:
    # success becuase tbl_id from reuqest is ref to noting
    msg = "success"
  return JsonResponse({'msg': msg})

def mpic_movie_imp_cms_delete(request):
  try:
    tbl_id = int(request.POST.get('tbl_id'))

    try:
      with transaction.atomic():
        TblMpicMovieImpAx.objects.using('mjcdata').filter(tbl_id=request.POST.get('tbl_id')).delete()
        msg = 'success'
    except:
      msg = 'Error while delete in database.'
  except:
    # success becuase tbl_id from reuqest is ref to noting
    msg = 'success'
  return JsonResponse({'msg': msg})
# delete

# import file
def import_mpic_movie_imp_cms(request):
  import_file = request.FILES.get('import_file', '')
  if import_file:
    new_tbl_mpic_movie_imp_axs, found_same = create_mpic_movie_imp_ax_obj_list(import_file)
    new_tbl_mpic_movie_imp_ax_dicts = []
    
    if not found_same:
      now = datetime.now()
      try:
        with transaction.atomic():
          for obj in new_tbl_mpic_movie_imp_axs:
            tbl_mpic_movie_imp_ax = TblMpicMovieImpAx.objects.using('mjcdata').create(
              mvcode      = obj.mvcode,
              mvtitle     = obj.mvtitle,
              mvname      = obj.mvname,
              unit_price  = obj.unit_price,
              perc_disc   = obj.perc_disc,
              mvmapping   = obj.mvmapping,
              releasedate = obj.releasedate,
              finishdate  = obj.finishdate,
              amend_date  = now,
              amend_by    = request.user.username
            )
            new_tbl_mpic_movie_imp_ax_dicts.append(
              {
                'tbl_id'      : tbl_mpic_movie_imp_ax.tbl_id,
                'mvcode'      : tbl_mpic_movie_imp_ax.mvcode,
                'mvtitle'     : tbl_mpic_movie_imp_ax.mvtitle,
                'mvname'      : tbl_mpic_movie_imp_ax.mvname,
                'unit_price'  : tbl_mpic_movie_imp_ax.unit_price,
                'perc_disc'   : tbl_mpic_movie_imp_ax.perc_disc,
                'mvmapping'   : tbl_mpic_movie_imp_ax.mvmapping,
                'releasedate' : tbl_mpic_movie_imp_ax.releasedate,
                'finishdate'  : tbl_mpic_movie_imp_ax.finishdate,
                'amend_date'  : tbl_mpic_movie_imp_ax.amend_date.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
                'amend_by'    : tbl_mpic_movie_imp_ax.amend_by
              }
            )
          msg = 'success'
      except:
        msg = 'Error while import datas to database.'
    else:
      msg = 'Found movie that has same code and title in file or database.'

    context = {
      'new_tbl_mpic_movie_imp_ax_dicts': new_tbl_mpic_movie_imp_ax_dicts,
      'msg': msg
    }
  else:
    context = {
      'new_tbl_mpic_movie_imp_ax_dicts': [],
      'msg': 'success'
    }
  return JsonResponse(context)

def import_mpic_customer_imp_cms(request):
  import_file = request.FILES.get('import_file', '')
  if import_file:
    new_tbl_mpic_customer_imp_axs, found_same = create_mpic_customer_imp_ax_obj_list(import_file)
    new_tbl_mpic_customer_imp_ax_dicts = []
    
    if not found_same:
      now = datetime.now()
      try:
        with transaction.atomic():
          for obj in new_tbl_mpic_customer_imp_axs:
            tbl_mpic_customer_imp_ax = TblMpicCustomerImpAx.objects.using('mjcdata').create(
              custcode    = obj.custcode,
              custname    = obj.custname,
              custaddress = obj.custaddress,
              custgroup   = obj.custgroup,
              postprofile = obj.postprofile,
              site        = obj.site,
              warehouse   = obj.warehouse,
              buax        = obj.buax,
              divax       = obj.divax,
              locax       = obj.locax,
              intercocd   = obj.intercocd,
              custmapping = obj.custmapping,
              amend_date  = now,
              amend_by    = request.user.username
            )
            new_tbl_mpic_customer_imp_ax_dicts.append(
              {
                'tbl_id'      : tbl_mpic_customer_imp_ax.tbl_id,
                'custcode'    : tbl_mpic_customer_imp_ax.custcode,
                'custname'    : tbl_mpic_customer_imp_ax.custname,
                'custaddress' : tbl_mpic_customer_imp_ax.custaddress,
                'custgroup'   : tbl_mpic_customer_imp_ax.custgroup,
                'postprofile' : tbl_mpic_customer_imp_ax.postprofile,
                'site'        : tbl_mpic_customer_imp_ax.site,
                'warehouse'   : tbl_mpic_customer_imp_ax.warehouse,
                'buax'        : tbl_mpic_customer_imp_ax.buax,
                'divax'       : tbl_mpic_customer_imp_ax.divax,
                'locax'       : tbl_mpic_customer_imp_ax.locax,
                'intercocd'   : tbl_mpic_customer_imp_ax.intercocd,
                'custmapping' : tbl_mpic_customer_imp_ax.custmapping,
                'amend_date'  : tbl_mpic_customer_imp_ax.amend_date.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
                'amend_by'    : tbl_mpic_customer_imp_ax.amend_by
              }
            )
          msg = 'success'
      except:
        msg = 'Error while import datas to database.'
    else:
      msg = 'Found customer that has same code file or database.'

    context = {
      'new_tbl_mpic_customer_imp_ax_dicts': new_tbl_mpic_customer_imp_ax_dicts,
      'msg': msg
    }
  else:
    context = {
      'new_tbl_mpic_customer_imp_ax_dicts': [],
      'msg': 'success'
    }
  return JsonResponse(context)
# import file

# download
def download_example_import_movie_file(request):
  file_path = os.path.join(settings.MEDIA_ROOT, 'template_movie_cms_import_file.xlsx')
  f = open(file_path, 'rb')
  response = HttpResponse(f.read(), content_type="application/force-download")
  response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
  return response

def download_example_import_customer_file(request):
  file_path = os.path.join(settings.MEDIA_ROOT, 'template_customer_cms_import_file.xlsx')
  f = open(file_path, 'rb')
  response = HttpResponse(f.read(), content_type="application/force-download")
  response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
  return response
# download