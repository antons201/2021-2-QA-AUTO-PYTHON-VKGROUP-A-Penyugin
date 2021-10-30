import time


class TimeoutException(Exception):
    pass


def wait(method, error=Exception, timeout=10, interval=0.5, **kwargs):
    started = time.time()
    last_exception = None
    while time.time() - started < timeout:
        try:
            method(**kwargs)
            return
        except error as e:
            last_exception = e

        time.sleep(interval)

    raise TimeoutException(f'Method {method.__name__} timeout out in {timeout} sec with exception: {last_exception}')