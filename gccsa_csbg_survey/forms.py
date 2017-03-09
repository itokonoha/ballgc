from django import forms
from betterforms.multiform import MultiModelForm
from collections import OrderedDict
from .models import HouseholdMember, Household, HeadOfHouseholdMember, HouseholdReferral, HouseholdMemberDemographics

class HeadOfHouseholdMemberInfo(forms.ModelForm):
	class Meta:
		model = HouseholdMember
		fields = ('__all__')
	
	def __init__(self, *args, **kwargs):
		super(HeadOfHouseholdMemberInfo, self).__init__(*args, **kwargs)
		self.fields.pop('household')

	# def clean(self):
	# 	super(HeadOfHouseholdMemberInfo, self).clean()
	# 	self.add_error('first_name', 'msg')
	# 	data = self.cleaned_data	
	# 	raise forms.ValidationError(
 #                    "Did not send for 'help' in the subject despite "
 #                    "CC'ing yourself."
 #                )	
	# 	self.validate_required_field(self.cleaned_data, 'first_name')
	# 	self.first_name = "AAA"
	# 	if data.get('household_relationship', none) == "other" :
	# 		self._errors['household_relationship'] = self.error_class(['message'])
	# 	else :
	# 		self._errors['household_relationship'] = self.error_class(['message'])
	
class AlternateContactInfo(forms.ModelForm):
	class Meta:
		model = HeadOfHouseholdMember
		fields = ('__all__')
	def __init__(self, *args, **kwargs):
		super(AlternateContactInfo, self).__init__(*args, **kwargs)
		self.fields.pop('household_member')

class HeadOfHousehold(MultiModelForm):
	base_fields = {}
	form_classes = OrderedDict((
        ('head_of_household_member_info', HeadOfHouseholdMemberInfo),
        ('alternate_contact_info', AlternateContactInfo),        
    ))

class HouseholdInfo(forms.ModelForm):
	class Meta:
		model = Household
		fields = ('__all__')
	def __init__(self, *args, **kwargs):
		super(HouseholdInfo, self).__init__(*args, **kwargs)
		self.fields.pop('survey')

class HouseholdReferralInfo(forms.ModelForm):
	class Meta:
		model = HouseholdReferral
		fields = ('__all__')
	def __init__(self, *args, **kwargs):
		super(HouseholdReferralInfo, self).__init__(*args, **kwargs)
		self.fields.pop('household')

class Household(MultiModelForm):
	base_fields = {}
	form_classes = OrderedDict((
		('household_member', HouseholdInfo),
		('household_referral_info', HouseholdReferralInfo),
	))

class HouseholdMemberDemographicsInfo(forms.ModelForm):
	class Meta:
		model = HouseholdMemberDemographics
		fields = ('__all__')
	def __init__(self, *args, **kwargs):
		super(HouseholdMemberDemographicsInfo, self).__init__(*args, **kwargs)
		self.fields.pop('household_member')