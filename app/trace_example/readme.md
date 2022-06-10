## trace logs

python3 -m trace --trace trace_example/main.py - this performs the tracing to the console
python3 -m trace --count app/trace_example/main.py - outputs the tracing to a log output

https://pymotw.com/2/trace/

## logging as a json

https://github.com/madzak/python-json-logger

## Monitoring

https://www.fullstackpython.com/monitoring.html

## differences 

https://www.bmc.com/blogs/monitoring-logging-tracing/  
Logging - this is what the developers want to see. Error statements, alerts and useful pieces of information for diagnosing issues.  
Tracing - A wider view of the application. Showing exactly what was passed (variables, functions, classes).  
Monitoring - This is for creating things like metrics of your system. For example, reaching storage limits or alerting developers when something isn't working. 

## Where does open telemetry fit in with this?

Open telemetry collects these log outputs and correlates them into a standardized format 

https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/logs/overview.md