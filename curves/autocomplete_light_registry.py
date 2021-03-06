import autocomplete_light
from models import Course_Specific


class Course_SpecificAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['titleString']
    attrs={
    # This will set the input placeholder attribute:
    'placeholder': 'Select a Class',
    # This will set the yourlabs.Autocomplete.minimumCharacters
    # options, the naming conversion is handled by jQuery
    'data-autocomplete-minimum-characters': 1,
    }
    widget_attrs={
	    # 'data-widget-maximum-values': 4,
	    'class': 'modern-style',
    }
autocomplete_light.register(Course_SpecificAutocomplete, choices=Course_Specific.objects.filter(semester="S2015"))
# autocomplete_light.register(Course_Specific,
# 	search_fields = ['titleString', 'prof'],
#     attrs={
#     # This will set the input placeholder attribute:
#     'placeholder': 'Select a Class',
#     # This will set the yourlabs.Autocomplete.minimumCharacters
#     # options, the naming conversion is handled by jQuery
#     'data-autocomplete-minimum-characters': 1,
# 	},
	
# 	# This will set the data-widget-maximum-values attribute on the
# 	# widget container element, and will be set to
# 	# yourlabs.Widget.maximumValues (jQuery handles the naming
# 	# conversion).
# 	widget_attrs={
# 	    # 'data-widget-maximum-values': 4,
# 	    'class': 'modern-style',
#     },	
# )