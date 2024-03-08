import requests
import signal


def run_requests(url, method='GET', timeout=5, **kwargs):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)  # 设置超时时间为 5 秒

    session = requests.Session()
    try:
        response = session.request(method, url, **kwargs)
        return response
    except Exception as f:
        raise f
    finally:
        signal.alarm(0)


def timeout_handler(signum, frame):
    raise TimeoutError("Request timed out")



