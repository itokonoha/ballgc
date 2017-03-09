import os, json, logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.core.files import File
from formtools.wizard.views import SessionWizardView
from .forms import HeadOfHouseholdMemberInfo, AlternateContactInfo, HouseholdInfo, HouseholdReferralInfo, HeadOfHousehold, Household, HouseholdMemberDemographicsInfo

logger = logging.getLogger(__name__)

def about(request):
   settings_dir = os.path.dirname(__file__)
   PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
   CONFIG_FOLDER = os.path.join(PROJECT_ROOT, 'org_info/')

   with open(CONFIG_FOLDER + 'gccsa/config/config.json') as config_data:
      config = json.load(config_data)
   title = config['org']['survey']['csbg']['title']
   about_file_name = config['org']['survey']['csbg']['about_file']
   file = open(CONFIG_FOLDER + 'gccsa/tpl/' + about_file_name)

   return render(request, "about.html", {"about_content" : file.read(), "title" : title});

def requirement(request):
   settings_dir = os.path.dirname(__file__)
   PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
   CONFIG_FOLDER = os.path.join(PROJECT_ROOT, 'org_info/')

   with open(CONFIG_FOLDER + 'gccsa/config/config.json') as config_data:
      config = json.load(config_data)
   title = 'Requirements'
   requirements_file_name = config['org']['survey']['csbg']['requirements_file']
   
   if len(requirements_file_name) > 0:
      file = open(CONFIG_FOLDER + 'gccsa/tpl/' + requirements_file_name)
      return render(request, "requirement.html", {"requirements_content" : file.read(), "title" : title});
   else:
      return redirect(handler404)
   
def householdmember(request):
    return render(request, "householdmember.html"); 

def handler404(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response

TEMPLATES = ["head_of_household.html", "household.html","household_member", "household_member_demographics.html"]

class InformationWizard(SessionWizardView):
  # template_name = "template.html"

  def get_template_names(self):
    logger.error("***  OUTPUT - current *** : " + self.steps.current)

    current_step = self.storage.current_step
    str1 = str(current_step)
    str2 = eval(str1)
    logger.error("***  OUTPUT - cur_step_data *** : " + str1)

    initial = self.initial_dict.get('0', {})
    str1 = str(initial)
    logger.error("***  OUTPUT - cur_initial_dict *** : " + str1)

    # if current_step == '1':
    #         prev_data = self.storage.get_step_data('0')
    #         str1 = str(prev_data)
    #         str2 = eval(str1)
    #         logger.error("***  OUTPUT - prev_step_data *** : " + str1)

    #         first_name = prev_data.get('step1-some_var','')

    return [TEMPLATES[int(self.steps.current)]]

  def get_form_initial(self, step):
    logger.error("***  OUTPUT - current 002 *** : " + step)

    prev_data = self.storage.get_step_data('0')
    first_name = prev_data.get('head_of_household_member_info__0-first_name','')
    logger.error("***  OUTPUT - prev_first_name *** : " + first_name)
    
    return self.initial_dict.get(step, {'first_name': first_name})

  def done(self, form_list, **kwargs):
      form_data = process_form_data(form_list)
      return render_to_response('done.html', {'form_data' : form_data})

def process_form_data(form_list):
  form_data = [form.cleaned_data for form in form_list]

  return form_data