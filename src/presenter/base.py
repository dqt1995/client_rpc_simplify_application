class BasePresenter(object):
	def __init__(self, model, project_name='default'):
		self.model = model
		self.project_name = project_name