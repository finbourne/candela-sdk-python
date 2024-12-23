# finbourne_candela.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_session**](SessionsApi.md#delete_session) | **DELETE** /sessions/ | Delete all data associated with a session in Candela.
[**get_session**](SessionsApi.md#get_session) | **GET** /sessions/ | Get the details of a session in Candela.
[**get_session_metadata**](SessionsApi.md#get_session_metadata) | **GET** /sessions/metadata | Get the metadata associated with a session in Candela.
[**list_sessions**](SessionsApi.md#list_sessions) | **GET** /sessions/list | Start an agent/pipeline session on your assigned slot in Candela.
[**session_exists**](SessionsApi.md#session_exists) | **GET** /sessions/exists | Check whether a session with a given ID exists.
[**start_dev_session**](SessionsApi.md#start_dev_session) | **POST** /session/dev | Start an agent/pipeline session on your slot.
[**start_session**](SessionsApi.md#start_session) | **POST** /session | Start an agent/pipeline session on your slot.
[**stop_session**](SessionsApi.md#stop_session) | **GET** /session/stop | Stop an agent/pipeline session.
[**submit_pipeline_prompt**](SessionsApi.md#submit_pipeline_prompt) | **POST** /session/pipeline_submit | Send a prompt to a running pipeline session.
[**submit_prompt_to_agent**](SessionsApi.md#submit_prompt_to_agent) | **POST** /session/agent_submit | Send a prompt to a running agent session.


# **delete_session**
> List[ObjectMetadata] delete_session(scope, identifier, version=version)

Delete all data associated with a session in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SessionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com",
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
    api_instance = api_client_factory.build(SessionsApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_session(scope, identifier, version=version, opts=opts)

        # Delete all data associated with a session in Candela.
        api_response = api_instance.delete_session(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SessionsApi->delete_session: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **identifier** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

[**List[ObjectMetadata]**](ObjectMetadata.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_session**
> Session get_session(scope, identifier, version=version)

Get the details of a session in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SessionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com",
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
    api_instance = api_client_factory.build(SessionsApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_session(scope, identifier, version=version, opts=opts)

        # Get the details of a session in Candela.
        api_response = api_instance.get_session(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SessionsApi->get_session: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **identifier** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

[**Session**](Session.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_session_metadata**
> ObjectMetadata get_session_metadata(scope, identifier, version=version)

Get the metadata associated with a session in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SessionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com",
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
    api_instance = api_client_factory.build(SessionsApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_session_metadata(scope, identifier, version=version, opts=opts)

        # Get the metadata associated with a session in Candela.
        api_response = api_instance.get_session_metadata(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SessionsApi->get_session_metadata: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **identifier** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

[**ObjectMetadata**](ObjectMetadata.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_sessions**
> List[ObjectMetadata] list_sessions(all_versions=all_versions)

Start an agent/pipeline session on your assigned slot in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SessionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com",
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
    api_instance = api_client_factory.build(SessionsApi)
    all_versions = False # bool |  (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_sessions(all_versions=all_versions, opts=opts)

        # Start an agent/pipeline session on your assigned slot in Candela.
        api_response = api_instance.list_sessions(all_versions=all_versions)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SessionsApi->list_sessions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all_versions** | **bool**|  | [optional] [default to False]

### Return type

[**List[ObjectMetadata]**](ObjectMetadata.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **session_exists**
> bool session_exists(scope, identifier, version=version)

Check whether a session with a given ID exists.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SessionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com",
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
    api_instance = api_client_factory.build(SessionsApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.session_exists(scope, identifier, version=version, opts=opts)

        # Check whether a session with a given ID exists.
        api_response = api_instance.session_exists(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SessionsApi->session_exists: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **identifier** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

**bool**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **start_dev_session**
> ObjectMetadata start_dev_session(dev_session_start_request)

Start an agent/pipeline session on your slot.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SessionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com",
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
    api_instance = api_client_factory.build(SessionsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # dev_session_start_request = DevSessionStartRequest.from_json("")
    # dev_session_start_request = DevSessionStartRequest.from_dict({})
    dev_session_start_request = DevSessionStartRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.start_dev_session(dev_session_start_request, opts=opts)

        # Start an agent/pipeline session on your slot.
        api_response = api_instance.start_dev_session(dev_session_start_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SessionsApi->start_dev_session: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_session_start_request** | [**DevSessionStartRequest**](DevSessionStartRequest.md)|  | 

### Return type

[**ObjectMetadata**](ObjectMetadata.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **start_session**
> ObjectMetadata start_session(session_start_request)

Start an agent/pipeline session on your slot.

Starts up an agent/pipeline session given an app and a model.  One can also specify the following:  - **scope** - the scope for the session to exist in (scope = default if not specified)  - **circuit override** - replace the circuit in the app specification with another in the same scope  - **directive override** - replace the directive in the app specification with another in the same scope  Returns: - ObjectMetadata: an object containing metadata for the new session.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SessionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com",
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
    api_instance = api_client_factory.build(SessionsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # session_start_request = SessionStartRequest.from_json("")
    # session_start_request = SessionStartRequest.from_dict({})
    session_start_request = SessionStartRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.start_session(session_start_request, opts=opts)

        # Start an agent/pipeline session on your slot.
        api_response = api_instance.start_session(session_start_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SessionsApi->start_session: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_start_request** | [**SessionStartRequest**](SessionStartRequest.md)|  | 

### Return type

[**ObjectMetadata**](ObjectMetadata.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **stop_session**
> stop_session()

Stop an agent/pipeline session.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SessionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com",
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
    api_instance = api_client_factory.build(SessionsApi)

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.stop_session(opts=opts)

        # Stop an agent/pipeline session.
        api_instance.stop_session()
    except ApiException as e:
        print("Exception when calling SessionsApi->stop_session: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **submit_pipeline_prompt**
> object submit_pipeline_prompt(submit_prompt)

Send a prompt to a running pipeline session.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SessionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com",
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
    api_instance = api_client_factory.build(SessionsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # submit_prompt = SubmitPrompt.from_json("")
    # submit_prompt = SubmitPrompt.from_dict({})
    submit_prompt = SubmitPrompt()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.submit_pipeline_prompt(submit_prompt, opts=opts)

        # Send a prompt to a running pipeline session.
        api_response = api_instance.submit_pipeline_prompt(submit_prompt)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SessionsApi->submit_pipeline_prompt: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_prompt** | [**SubmitPrompt**](SubmitPrompt.md)|  | 

### Return type

**object**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **submit_prompt_to_agent**
> Event submit_prompt_to_agent(submit_prompt)

Send a prompt to a running agent session.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SessionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "candelaUrl":"https://<your-domain>.lusid.com",
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
    api_instance = api_client_factory.build(SessionsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # submit_prompt = SubmitPrompt.from_json("")
    # submit_prompt = SubmitPrompt.from_dict({})
    submit_prompt = SubmitPrompt()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.submit_prompt_to_agent(submit_prompt, opts=opts)

        # Send a prompt to a running agent session.
        api_response = api_instance.submit_prompt_to_agent(submit_prompt)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SessionsApi->submit_prompt_to_agent: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_prompt** | [**SubmitPrompt**](SubmitPrompt.md)|  | 

### Return type

[**Event**](Event.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/x-ndjson

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A stream of json-serialised events forming the agent response and other data. |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

