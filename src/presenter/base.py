from ..import model
import grpc

class BasePresenter(object):
	def __init__(self, model, project=None):
		self.model = model
		if project is None:
			project = model.core.session.get_default()
		self.session = project_name