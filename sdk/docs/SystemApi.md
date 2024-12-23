# finbourne_candela.SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_delete_slot**](SystemApi.md#admin_delete_slot) | **DELETE** /system/slot | Deletes a slot from the system without replacing it
[**get_domain_state**](SystemApi.md#get_domain_state) | **GET** /system/status | Get the current status of your Candela platform slots infrastructure.
[**list_slots**](SystemApi.md#list_slots) | **GET** /system/list_slots | List the current slots in your Candela platform.
[**set_free_slots_target**](SystemApi.md#set_free_slots_target) | **PUT** /system/free_slots_target | Set the target number of free slots
[**set_max_slots**](SystemApi.md#set_max_slots) | **PUT** /system/max_slots | Set the maximum number of slots.


# **admin_delete_slot**
> admin_delete_slot(slot_id)

Deletes a slot from the system without replacing it

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SystemApi
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
    api_instance = api_client_factory.build(SystemApi)
    slot_id = 'slot_id_example' # str | 

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.admin_delete_slot(slot_id, opts=opts)

        # Deletes a slot from the system without replacing it
        api_instance.admin_delete_slot(slot_id)
    except ApiException as e:
        print("Exception when calling SystemApi->admin_delete_slot: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_id** | **str**|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_domain_state**
> object get_domain_state()

Get the current status of your Candela platform slots infrastructure.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SystemApi
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
    api_instance = api_client_factory.build(SystemApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_domain_state(opts=opts)

        # Get the current status of your Candela platform slots infrastructure.
        api_response = api_instance.get_domain_state()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SystemApi->get_domain_state: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_slots**
> List[SlotData] list_slots()

List the current slots in your Candela platform.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SystemApi
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
    api_instance = api_client_factory.build(SystemApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_slots(opts=opts)

        # List the current slots in your Candela platform.
        api_response = api_instance.list_slots()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SystemApi->list_slots: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[SlotData]**](SlotData.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_free_slots_target**
> SlotsPutResponse set_free_slots_target(slot_type, target_free_slots)

Set the target number of free slots

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SystemApi
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
    api_instance = api_client_factory.build(SystemApi)
    slot_type = 'slot_type_example' # str | 
    target_free_slots = 56 # int | 

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_free_slots_target(slot_type, target_free_slots, opts=opts)

        # Set the target number of free slots
        api_response = api_instance.set_free_slots_target(slot_type, target_free_slots)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SystemApi->set_free_slots_target: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_type** | **str**|  | 
 **target_free_slots** | **int**|  | 

### Return type

[**SlotsPutResponse**](SlotsPutResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_max_slots**
> SlotsPutResponse set_max_slots(slot_type, max_slots)

Set the maximum number of slots.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    SystemApi
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
    api_instance = api_client_factory.build(SystemApi)
    slot_type = 'slot_type_example' # str | 
    max_slots = 56 # int | 

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_max_slots(slot_type, max_slots, opts=opts)

        # Set the maximum number of slots.
        api_response = api_instance.set_max_slots(slot_type, max_slots)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SystemApi->set_max_slots: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_type** | **str**|  | 
 **max_slots** | **int**|  | 

### Return type

[**SlotsPutResponse**](SlotsPutResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

