# finbourne_candela.CircuitsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_circuit**](CircuitsApi.md#add_circuit) | **PUT** /circuits/ | Add a circuit to Candela.
[**circuit_exists**](CircuitsApi.md#circuit_exists) | **GET** /circuits/exists | Check that a given circuit exists in Candela.
[**delete_circuit**](CircuitsApi.md#delete_circuit) | **DELETE** /circuits/ | Delete a given circuit from Candela.
[**get_circuit**](CircuitsApi.md#get_circuit) | **GET** /circuits/ | Get a given circuit from Candela.
[**get_circuit_metadata**](CircuitsApi.md#get_circuit_metadata) | **GET** /circuits/metadata | Get a given circuit&#39;s metadata from Candela
[**list_circuits**](CircuitsApi.md#list_circuits) | **GET** /circuits/list | List all the circuits available to you in Candela.


# **add_circuit**
> ObjectMetadata add_circuit(post_circuit, system_level=system_level)

Add a circuit to Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    CircuitsApi
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
    api_instance = api_client_factory.build(CircuitsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # post_circuit = PostCircuit.from_json("")
    # post_circuit = PostCircuit.from_dict({})
    post_circuit = PostCircuit()
    system_level = False # bool |  (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_circuit(post_circuit, system_level=system_level, opts=opts)

        # Add a circuit to Candela.
        api_response = api_instance.add_circuit(post_circuit, system_level=system_level)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CircuitsApi->add_circuit: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_circuit** | [**PostCircuit**](PostCircuit.md)|  | 
 **system_level** | **bool**|  | [optional] [default to False]

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

# **circuit_exists**
> bool circuit_exists(scope, identifier, version=version)

Check that a given circuit exists in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    CircuitsApi
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
    api_instance = api_client_factory.build(CircuitsApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.circuit_exists(scope, identifier, version=version, opts=opts)

        # Check that a given circuit exists in Candela.
        api_response = api_instance.circuit_exists(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CircuitsApi->circuit_exists: %s\n" % e)

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

# **delete_circuit**
> List[ObjectMetadata] delete_circuit(scope, identifier, version=version)

Delete a given circuit from Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    CircuitsApi
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
    api_instance = api_client_factory.build(CircuitsApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_circuit(scope, identifier, version=version, opts=opts)

        # Delete a given circuit from Candela.
        api_response = api_instance.delete_circuit(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CircuitsApi->delete_circuit: %s\n" % e)

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

# **get_circuit**
> Circuit get_circuit(scope, identifier, version=version)

Get a given circuit from Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    CircuitsApi
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
    api_instance = api_client_factory.build(CircuitsApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_circuit(scope, identifier, version=version, opts=opts)

        # Get a given circuit from Candela.
        api_response = api_instance.get_circuit(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CircuitsApi->get_circuit: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **identifier** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

[**Circuit**](Circuit.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_circuit_metadata**
> ObjectMetadata get_circuit_metadata(scope, identifier, version=version)

Get a given circuit's metadata from Candela

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    CircuitsApi
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
    api_instance = api_client_factory.build(CircuitsApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_circuit_metadata(scope, identifier, version=version, opts=opts)

        # Get a given circuit's metadata from Candela
        api_response = api_instance.get_circuit_metadata(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CircuitsApi->get_circuit_metadata: %s\n" % e)

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

# **list_circuits**
> List[ObjectMetadata] list_circuits(all_versions=all_versions)

List all the circuits available to you in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    CircuitsApi
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
    api_instance = api_client_factory.build(CircuitsApi)
    all_versions = False # bool |  (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_circuits(all_versions=all_versions, opts=opts)

        # List all the circuits available to you in Candela.
        api_response = api_instance.list_circuits(all_versions=all_versions)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CircuitsApi->list_circuits: %s\n" % e)

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

