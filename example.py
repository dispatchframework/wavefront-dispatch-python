import wavefront_dispatch
import random

@wavefront_dispatch.wrapper
def handle(ctx, payload):

    # Fibonacci
    f_2, f_1 = 0, 1
    for n in range(random.randint(800, 900)):
        f = f_1 + f_2
        f_2, f_1 = f_1, f

    # Customized metrics
    registry = wavefront_dispatch.get_registry()

    # Report Gauge
    gauge_val = registry.gauge("dispatch.function.wf.testgauge")
    gauge_val.set_value(200)

    # Report Counter
    counter = registry.counter("dispatch.function.wf.testcounter")
    counter.inc()



if __name__ == "__main__":
    ctx = {
        "secrets": {
            "wavefront_server_url":"https://<INSTANCE>.wavefront.com",
            "wavefront_auth_token":"<AUTH_TOKEN>"}
        }
    payload = {}
    handle(ctx, payload)