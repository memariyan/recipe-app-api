from prometheus_client import Counter, Histogram

http_requests_total = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint']
)

http_request_duration_seconds = Histogram(
    'http_request_duration_seconds',
    'Histogram of HTTP request duration in seconds',
    ['method', 'endpoint']
)
