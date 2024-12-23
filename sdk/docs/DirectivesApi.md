# finbourne_candela.DirectivesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_directive**](DirectivesApi.md#add_directive) | **PUT** /directives/ | Add a directive to Candela.
[**delete_directive**](DirectivesApi.md#delete_directive) | **DELETE** /directives/ | Delete a directive from Candela.
[**directive_exists**](DirectivesApi.md#directive_exists) | **GET** /directives/exists | Check if a particular directive exists in Candela.
[**get_directive**](DirectivesApi.md#get_directive) | **GET** /directives/ | Get a directive from Candela.
[**get_directive_metadata**](DirectivesApi.md#get_directive_metadata) | **GET** /directives/metadata | Get a directive&#39;s metadata from Candela.
[**list_directives**](DirectivesApi.md#list_directives) | **GET** /directives/list | List your available directives in Candela.


# **add_directive**
> ObjectMetadata add_directive(post_directive, system_level=system_level)

Add a directive to Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    DirectivesApi
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
    api_instance = api_client_factory.build(DirectivesApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # post_directive = PostDirective.from_json("")
    # post_directive = PostDirective.from_dict({})
    post_directive = PostDirective()
    system_level = False # bool |  (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_directive(post_directive, system_level=system_level, opts=opts)

        # Add a directive to Candela.
        api_response = api_instance.add_directive(post_directive, system_level=system_level)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DirectivesApi->add_directive: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_directive** | [**PostDirective**](PostDirective.md)|  | 
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

# **delete_directive**
> List[ObjectMetadata] delete_directive(scope, identifier, version=version)

Delete a directive from Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    DirectivesApi
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
    api_instance = api_client_factory.build(DirectivesApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_directive(scope, identifier, version=version, opts=opts)

        # Delete a directive from Candela.
        api_response = api_instance.delete_directive(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DirectivesApi->delete_directive: %s\n" % e)

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

# **directive_exists**
> bool directive_exists(scope, identifier, version=version)

Check if a particular directive exists in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    DirectivesApi
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
    api_instance = api_client_factory.build(DirectivesApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.directive_exists(scope, identifier, version=version, opts=opts)

        # Check if a particular directive exists in Candela.
        api_response = api_instance.directive_exists(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DirectivesApi->directive_exists: %s\n" % e)

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

# **get_directive**
> Directive get_directive(scope, identifier, version=version)

Get a directive from Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    DirectivesApi
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
    api_instance = api_client_factory.build(DirectivesApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_directive(scope, identifier, version=version, opts=opts)

        # Get a directive from Candela.
        api_response = api_instance.get_directive(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DirectivesApi->get_directive: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **identifier** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

[**Directive**](Directive.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_directive_metadata**
> ObjectMetadata get_directive_metadata(scope, identifier, version=version)

Get a directive's metadata from Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    DirectivesApi
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
    api_instance = api_client_factory.build(DirectivesApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_directive_metadata(scope, identifier, version=version, opts=opts)

        # Get a directive's metadata from Candela.
        api_response = api_instance.get_directive_metadata(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DirectivesApi->get_directive_metadata: %s\n" % e)

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

# **list_directives**
> List[ObjectMetadata] list_directives(all_versions=all_versions)

List your available directives in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    DirectivesApi
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
    api_instance = api_client_factory.build(DirectivesApi)
    all_versions = False # bool |  (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_directives(all_versions=all_versions, opts=opts)

        # List your available directives in Candela.
        api_response = api_instance.list_directives(all_versions=all_versions)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DirectivesApi->list_directives: %s\n" % e)

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

