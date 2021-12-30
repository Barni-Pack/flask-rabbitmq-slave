class Config(object):
	"""
	Configuration base, for all environments.
	"""
	DEBUG = True
	TESTING = True
	SECRET_KEY = "sheesh"
	CSRF_ENABLED = True