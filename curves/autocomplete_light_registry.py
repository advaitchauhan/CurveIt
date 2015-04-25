import autocomplete_light
from models import Course_Specific


autocomplete_light.register(Course_Specific,
	search_fields = ['titleString', 'prof'],
    attrs={
    # This will set the input placeholder attribute:
    'placeholder': 'Select a Class',
    # This will set the yourlabs.Autocomplete.minimumCharacters
    # options, the naming conversion is handled by jQuery
    'data-autocomplete-minimum-characters': 1,
	},
	
	# This will set the data-widget-maximum-values attribute on the
	# widget container element, and will be set to
	# yourlabs.Widget.maximumValues (jQuery handles the naming
	# conversion).
	widget_attrs={
	    # 'data-widget-maximum-values': 4,
	    'class': 'modern-style',
    },	
)