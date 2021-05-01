from django.apps import AppConfig


class WeatherConfig(AppConfig):
    name = 'Weather'

    def ready(self):
        print("Start Scheduler ...")
        from Weather.weather_scheduler import weather_updater
        weather_updater.start()
