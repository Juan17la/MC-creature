from django.apps import AppConfig

class CreateCreatureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'create_creature'

    def ready(self):
        import create_creature.signals
        