import time

from django.utils.deprecation import MiddlewareMixin

from core.metrics import http_requests_total, http_request_duration_seconds


class PrometheusMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        (http_requests_total.labels(
            method=request.method,
            endpoint=request.path)
         .inc())
        duration = time.time() - request.start_time
        (http_request_duration_seconds.labels(
            method=request.method,
            endpoint=request.path)
         .observe(duration))

        return response
