# finbourne_candela.ToolModulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tool_module**](ToolModulesApi.md#add_tool_module) | **PUT** /tool_modules/ | Add a tool module to Candela.
[**delete_tool_module**](ToolModulesApi.md#delete_tool_module) | **DELETE** /tool_modules/ | Delete a tool module from Candela.
[**get_tool_metadata**](ToolModulesApi.md#get_tool_metadata) | **GET** /tool_modules/tool/metadata | Get the metadata associated with a specific tool in Candela.
[**get_tool_module**](ToolModulesApi.md#get_tool_module) | **GET** /tool_modules/ | Get the content of a given tool module from Candela.
[**get_tool_module_metadata**](ToolModulesApi.md#get_tool_module_metadata) | **GET** /tool_modules/metadata | Get the metadata associated with a tool module in Candela.
[**list_tool_modules**](ToolModulesApi.md#list_tool_modules) | **GET** /tool_modules/list | List all tool modules available in Candela.
[**list_tools**](ToolModulesApi.md#list_tools) | **GET** /tool_modules/tool/list | List all tools contained in all modules in Candela.
[**tool_exists**](ToolModulesApi.md#tool_exists) | **GET** /tool_modules/tool/exists | Check whether a tool with a given name exists in a scope in Candela.
[**tool_module_exists**](ToolModulesApi.md#tool_module_exists) | **GET** /tool_modules/exists | Check whether a given tool module exists in Candela.


# **add_tool_module**
> ToolModuleMetadata add_tool_module(post_tool_module, system_level=system_level)

Add a tool module to Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    ToolModulesApi
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
    api_instance = api_client_factory.build(ToolModulesApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # post_tool_module = PostToolModule.from_json("")
    # post_tool_module = PostToolModule.from_dict({})
    post_tool_module = PostToolModule()
    system_level = False # bool |  (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_tool_module(post_tool_module, system_level=system_level, opts=opts)

        # Add a tool module to Candela.
        api_response = api_instance.add_tool_module(post_tool_module, system_level=system_level)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ToolModulesApi->add_tool_module: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_tool_module** | [**PostToolModule**](PostToolModule.md)|  | 
 **system_level** | **bool**|  | [optional] [default to False]

### Return type

[**ToolModuleMetadata**](ToolModuleMetadata.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_tool_module**
> List[ToolModuleMetadata] delete_tool_module(scope, identifier, version=version)

Delete a tool module from Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    ToolModulesApi
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
    api_instance = api_client_factory.build(ToolModulesApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_tool_module(scope, identifier, version=version, opts=opts)

        # Delete a tool module from Candela.
        api_response = api_instance.delete_tool_module(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ToolModulesApi->delete_tool_module: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **identifier** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

[**List[ToolModuleMetadata]**](ToolModuleMetadata.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_tool_metadata**
> ToolMetadata get_tool_metadata(scope, name)

Get the metadata associated with a specific tool in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    ToolModulesApi
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
    api_instance = api_client_factory.build(ToolModulesApi)
    scope = 'scope_example' # str | 
    name = 'name_example' # str | 

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_tool_metadata(scope, name, opts=opts)

        # Get the metadata associated with a specific tool in Candela.
        api_response = api_instance.get_tool_metadata(scope, name)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ToolModulesApi->get_tool_metadata: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**ToolMetadata**](ToolMetadata.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_tool_module**
> ToolModule get_tool_module(scope, identifier, version=version)

Get the content of a given tool module from Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    ToolModulesApi
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
    api_instance = api_client_factory.build(ToolModulesApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_tool_module(scope, identifier, version=version, opts=opts)

        # Get the content of a given tool module from Candela.
        api_response = api_instance.get_tool_module(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ToolModulesApi->get_tool_module: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **identifier** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

[**ToolModule**](ToolModule.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_tool_module_metadata**
> ToolModuleMetadata get_tool_module_metadata(scope, identifier, version=version)

Get the metadata associated with a tool module in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    ToolModulesApi
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
    api_instance = api_client_factory.build(ToolModulesApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_tool_module_metadata(scope, identifier, version=version, opts=opts)

        # Get the metadata associated with a tool module in Candela.
        api_response = api_instance.get_tool_module_metadata(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ToolModulesApi->get_tool_module_metadata: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **identifier** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

[**ToolModuleMetadata**](ToolModuleMetadata.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_tool_modules**
> List[ToolModuleMetadata] list_tool_modules(all_versions=all_versions)

List all tool modules available in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    ToolModulesApi
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
    api_instance = api_client_factory.build(ToolModulesApi)
    all_versions = False # bool |  (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_tool_modules(all_versions=all_versions, opts=opts)

        # List all tool modules available in Candela.
        api_response = api_instance.list_tool_modules(all_versions=all_versions)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ToolModulesApi->list_tool_modules: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all_versions** | **bool**|  | [optional] [default to False]

### Return type

[**List[ToolModuleMetadata]**](ToolModuleMetadata.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_tools**
> List[ToolMetadata] list_tools(all_versions=all_versions)

List all tools contained in all modules in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    ToolModulesApi
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
    api_instance = api_client_factory.build(ToolModulesApi)
    all_versions = False # bool |  (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_tools(all_versions=all_versions, opts=opts)

        # List all tools contained in all modules in Candela.
        api_response = api_instance.list_tools(all_versions=all_versions)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ToolModulesApi->list_tools: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all_versions** | **bool**|  | [optional] [default to False]

### Return type

[**List[ToolMetadata]**](ToolMetadata.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **tool_exists**
> bool tool_exists(scope, name)

Check whether a tool with a given name exists in a scope in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    ToolModulesApi
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
    api_instance = api_client_factory.build(ToolModulesApi)
    scope = 'scope_example' # str | 
    name = 'name_example' # str | 

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.tool_exists(scope, name, opts=opts)

        # Check whether a tool with a given name exists in a scope in Candela.
        api_response = api_instance.tool_exists(scope, name)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ToolModulesApi->tool_exists: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **name** | **str**|  | 

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

# **tool_module_exists**
> bool tool_module_exists(scope, identifier, version=version)

Check whether a given tool module exists in Candela.

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    ToolModulesApi
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
    api_instance = api_client_factory.build(ToolModulesApi)
    scope = 'scope_example' # str | 
    identifier = 'identifier_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.tool_module_exists(scope, identifier, version=version, opts=opts)

        # Check whether a given tool module exists in Candela.
        api_response = api_instance.tool_module_exists(scope, identifier, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ToolModulesApi->tool_module_exists: %s\n" % e)

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

