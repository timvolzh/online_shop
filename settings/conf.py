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
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',)
}

# ----------------------------------------------
# Django Debug Toolbar Configuration
#
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# ----------------------------------------------
# Shell plus configuration
#
SHELL_PLUS_PRE_IMPORTS = [
    ('django.db', ('connection', 'reset_queries', 'connections')),
    ('datetime', ('datetime', 'timedelta', 'date')),
    ('json', ('loads', 'dumps')),
]
SHELL_PLUS_MODEL_ALIASES = {
    'auths': {
        'CustomUser': 'U',
    },
    # 'university': {
    #     'Student': 'S',
    #     'Account': 'A',
    #     'Group': 'G',
    #     'Professor': 'P',
    #     'Homework': 'H',
    #     'File': 'FF',
    # },
}
SHELL_PLUS = 'ipython'
SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS_PRINT_SQL_TRUNCATE = 1000
