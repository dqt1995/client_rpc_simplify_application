import numbers
import json
from datetime import datetime
from .record_forms.base import BaseForm

def _raw_recorder(obj):
	# directly record obj as raw data
	return obj

def _form_recorder(obj):
	return obj.__dict__

def _datetime_recorder(obj):
	return obj.timestamp()

def _model_recorder(obj):
	# to load exactly data, we need to get exactly model object of it, and the id in model object
	return 
	pass