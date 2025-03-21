from django.apps import AppConfig

class MoneyTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'money_tracker'

    def ready(self):
        import money_tracker.signals
