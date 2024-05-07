import datetime

from rest_framework import throttling

"""
Администраторы сервера настоятельно попросили выделить им
2 часа в сутки (с трёх до пяти утра) на нагрузочное тестирование
запросов к котикам.
"""
class WorkingHoursRateThrottle(throttling.BaseThrottle):

    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        if now >= 3 and now < 5:
            return False
        return True