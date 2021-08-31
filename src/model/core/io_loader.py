import json
import numbers
from datetime import datetime

from . import record_forms

def _raw_loader(data):
	# directly load data as raw
	return data

def _form_loader(data):
    form_class = getattr(record_forms, data.pop("_form_name"))
    return form_class(data)

def _datetime_loader(data):
	return datetime.fromtimestamp(data)

def _model_loader(data):
	# to load exactly data, we need to get exactly model object of it, and the id in model object
	return 
	pass