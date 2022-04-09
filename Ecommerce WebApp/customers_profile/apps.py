from django.apps import AppConfig


class CustomersProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers_profile'

    def ready(self):
        import customers_profile.signals
