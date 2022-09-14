# ----------------------------------------------
# Enviromental variables
#
SECRET_KEY = 'django-insecure-qhr9@h9ywr89w4&0c)n7!^o#*u0u^hov)q-#&_p*i15y%kj1^4'

# ----------------------------------------------
# Custom settings
#
ADMIN_SITE_URL = "custom_admin/"

# ----------------------------------------------
# DRF settings
#
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',)
}
