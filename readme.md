
for now 
```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
```

We would also need a service to run a producer module and a consumer module

TODO:

- look into [python open telemetry](https://github.com/open-telemetry/opentelemetry-python)
- look into [apache spark](https://spark.apache.org/docs/0.9.1/python-programming-guide.html)
