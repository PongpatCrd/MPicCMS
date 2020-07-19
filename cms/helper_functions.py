import ldap
import pandas as pd
import cms.configs as cfgs

from django.db.models import Q
from cms.models import *
from django.forms.models import model_to_dict

def this_user_in_ldap(username, password):
  connect = ldap.initialize(cfgs.ldap_url)
  connect.set_option(ldap.OPT_REFERRALS, 0)
  try:
    connect.simple_bind_s(username, password)
    return True
  except:
    return False

def format_null_data(data):
  if data == 'None' or data == 'nan':
    data = None
  return data

# search by split word and order by % search key match
def search(search_key, all_object):
  items = []
  count_search_key_founds = []

  search_keys = search_key.strip().lower().split(' ')
  for obj in all_object:
    temp = str(model_to_dict(obj)).lower()
    found_search_key = False
    count_search_key_found = 0
    for search_key in search_keys:
      if search_key in temp:
        found_search_key = True
        count_search_key_found += 1
    
    if found_search_key:
      use_idx = 0
      if count_search_key_founds:
        for idx in range(len(count_search_key_founds)):
          if count_search_key_founds[idx] <= count_search_key_found:
            use_idx =  idx+1
        count_search_key_founds.insert(use_idx, count_search_key_found)
      else:
        count_search_key_founds.append(count_search_key_found)
      items.insert(use_idx, obj)
    else:
      pass
  items.reverse()
  return items

def create_mpic_movie_imp_ax_obj_list(import_file):
  df = pd.read_excel(import_file, header=None)
  df = df.where(pd.notnull(df), None)

  new_tbl_mpic_movie_imp_axs = []
  code_title_checks  = []
  titles = []
  found_same = False

  tbl_mpic_movie_imp_axs = TblMpicMovieImpAx.objects.using('mjcdata').all()
  in_db_codes_title_checks = [tbl_mpic_movie_imp_ax.mvcode.strip()+tbl_mpic_movie_imp_ax.mvtitle.strip() for tbl_mpic_movie_imp_ax in tbl_mpic_movie_imp_axs]
  
  for row in df.values.tolist():
    temp_code_title = row[0]+row[1]
    if temp_code_title in code_title_checks or temp_code_title in in_db_codes_title_checks:
      found_same = True
      break
    else:
      new_tbl_mpic_movie_imp_axs.append(
        TblMpicMovieImpAx(
          mvcode     = row[0],
          mvtitle    = row[1],
          mvname     = row[2],
          unit_price = row[3],
          perc_disc  = row[4]
        )
      )

      code_title_checks.append(temp_code_title)
  
  return new_tbl_mpic_movie_imp_axs, found_same

def create_mpic_customer_imp_ax_obj_list(import_file):
  df = pd.read_excel(import_file, header=None)
  df = df.where(pd.notnull(df), None)

  new_tbl_mpic_customer_imp_axs = []
  used_custcodes = []
  found_same = False

  custcodes = TblMpicCustomerImpAx.objects.using('mjcdata').values_list('custcode', flat=True)
  in_db_custcodes = [custcode.strip() for custcode in custcodes]
  
  for row in df.values.tolist():
    row[0] = str(row[0])
    if row[0] in used_custcodes or row[0] in in_db_custcodes:
      found_same = True
      break
    else:
      new_tbl_mpic_customer_imp_axs.append(
        TblMpicCustomerImpAx(
          custcode    = row[0],
          custname    = row[1],
          custaddress = row[2],
          custgroup   = row[3],
          postprofile = row[4],
          site        = row[5],
          warehouse   = row[6],
          buax        = row[7],
          divax       = row[8],
          locax       = row[9],
          intercocd   = row[10],
          custmapping = row[11]
        )
      )

      used_custcodes.append(row[0])
  
  return new_tbl_mpic_customer_imp_axs, found_same
