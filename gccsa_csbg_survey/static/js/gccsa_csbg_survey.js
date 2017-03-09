$(document).ready(function() {
	// Requremetns Page
	$('.requirements-cb').change(function() {
		if($('.requirements-cb').is(':checked')){
			// alert('checked');
			$( ".requirement-continue" ).prop( "disabled", false );
		}else{
			// alert('unchecked');
			$( ".requirement-continue" ).prop( "disabled", true );
		}
	});

	$('.about-continue').on('click', function() {
		$('.content-form').each(function(){
			$(this).submit();
		});
	});

	// Head of Household, Household Page	
	$("#id_head_of_household_member_info__0-ssn").mask("999-99-9999");
	$("#id_alternate_contact_info__0-alt_contact_home_phone").mask("(999) 999-9999");
	$("#id_alternate_contact_info__0-alt_contact_mobile_phone").mask("(999) 999-9999");
	$("#id_head_of_household_member_info__0-mobile_phone").mask("(999) 999-9999");
	$("#id_household_member__1-home_phone").mask("(999) 999-9999");
	$("id_household_member__1-zip_code").mask("99999-99999");

	$('#id_head_of_household_member_info__0-household_relationship').on('change', function() {
		if($(this).val() == "other") {
			$('#id_head_of_household_member_info__0-household_relationship_other').attr('required', '');
		} else {
			$('#id_head_of_household_member_info__0-household_relationship_other').attr('required', null);
		}
	});

	$('#id_household_member__1-housing').on('change', function() {
		if($(this).val() == "other") {
			$('#id_household_member__1-housing_other').attr('required', '');
		} else {
			$('#id_household_member__1-housing_other').attr('required', null);
		}
	});

	$('#id_household_member__1-type_of_household').on('change', function() {
		if($(this).val() == "other") {
			$('#id_household_member__1-type_of_household_other').attr('required', '');
		} else {
			$('#id_household_member__1-type_of_household_other').attr('required', null);
		}
	});

	$('#id_alternate_contact_info__0-preferred_phone').on('change', function() {
		if($(this).val() == "home") {
			$('#id_alternate_contact_info__0-alt_contact_home_phone').attr('required', '');
			$('#id_alternate_contact_info__0-alt_contact_mobile_phone').attr('required', null);
		} if($(this).val() == "mobile") {
			$('#id_alternate_contact_info__0-alt_contact_home_phone').attr('required', null);
			$('#id_alternate_contact_info__0-alt_contact_mobile_phone').attr('required', '');
		}
	});
   
});