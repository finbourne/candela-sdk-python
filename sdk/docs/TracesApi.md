# finbourne_candela.TracesApi

All URIs are relative to *https://fbn-ci.lusid.com/candela*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_trace**](TracesApi.md#delete_trace) | **DELETE** /api/traces/{scope}/{traceId} | [EARLY ACCESS] DeleteTrace: 
[**get_trace**](TracesApi.md#get_trace) | **GET** /api/traces/{scope}/{traceId} | [EARLY ACCESS] GetTrace: 
[**get_trace_events**](TracesApi.md#get_trace_events) | **GET** /api/traces/events/{scope}/{traceId} | [EARLY ACCESS] GetTraceEvents: 
[**list_traces**](TracesApi.md#list_traces) | **GET** /api/traces | [EARLY ACCESS] ListTraces: 


# **delete_trace**
> delete_trace(trace_id, scope)

[EARLY ACCESS] DeleteTrace: 

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    TracesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com/candela",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_candela SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(TracesApi)
    trace_id = 'trace_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.delete_trace(trace_id, scope, opts=opts)

        # [EARLY ACCESS] DeleteTrace: 
        api_instance.delete_trace(trace_id, scope)
    except ApiException as e:
        print("Exception when calling TracesApi->delete_trace: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**|  | 
 **scope** | **str**|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**404** | The trace was not found |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_trace**
> TraceDefinition get_trace(trace_id, scope)

[EARLY ACCESS] GetTrace: 

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    TracesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com/candela",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_candela SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(TracesApi)
    trace_id = 'trace_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_trace(trace_id, scope, opts=opts)

        # [EARLY ACCESS] GetTrace: 
        api_response = api_instance.get_trace(trace_id, scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TracesApi->get_trace: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**|  | 
 **scope** | **str**|  | 

### Return type

[**TraceDefinition**](TraceDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_trace_events**
> PagedResourceListOfTraceEventDefinition get_trace_events(trace_id, scope)

[EARLY ACCESS] GetTraceEvents: 

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    TracesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com/candela",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_candela SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(TracesApi)
    trace_id = 'trace_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_trace_events(trace_id, scope, opts=opts)

        # [EARLY ACCESS] GetTraceEvents: 
        api_response = api_instance.get_trace_events(trace_id, scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TracesApi->get_trace_events: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**|  | 
 **scope** | **str**|  | 

### Return type

[**PagedResourceListOfTraceEventDefinition**](PagedResourceListOfTraceEventDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_traces**
> PagedResourceListOfTraceDefinition list_traces()

[EARLY ACCESS] ListTraces: 

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    TracesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com/candela",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_candela SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(TracesApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_traces(opts=opts)

        # [EARLY ACCESS] ListTraces: 
        api_response = api_instance.list_traces()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TracesApi->list_traces: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PagedResourceListOfTraceDefinition**](PagedResourceListOfTraceDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

