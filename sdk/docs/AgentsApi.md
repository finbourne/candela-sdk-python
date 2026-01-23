# finbourne_candela.AgentsApi

All URIs are relative to *https://fbn-ci.lusid.com/candela*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_agent**](AgentsApi.md#add_agent) | **PUT** /api/agents/{scope} | [EARLY ACCESS] AddAgent: Create a new custom Agent
[**delete_agent**](AgentsApi.md#delete_agent) | **DELETE** /api/agents/{scope}/{code} | [EARLY ACCESS] DeleteAgent: Delete an agent
[**get_agent**](AgentsApi.md#get_agent) | **GET** /api/agents/{scope}/{code} | [EARLY ACCESS] GetAgent: Get an agent
[**list_agents**](AgentsApi.md#list_agents) | **GET** /api/agents/{scope} | [EARLY ACCESS] ListAgents: List all system agents and agents in the specified scope


# **add_agent**
> AgentDefinition add_agent(scope, add_agent_request)

[EARLY ACCESS] AddAgent: Create a new custom Agent

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    AgentsApi
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
    api_instance = api_client_factory.build(AgentsApi)
    scope = 'default' # str | The scope of the agent - this is only used for access control. Default is \"default\" (default to 'default')

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # add_agent_request = AddAgentRequest.from_json("")
    # add_agent_request = AddAgentRequest.from_dict({})
    add_agent_request = AddAgentRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_agent(scope, add_agent_request, opts=opts)

        # [EARLY ACCESS] AddAgent: Create a new custom Agent
        api_response = api_instance.add_agent(scope, add_agent_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AgentsApi->add_agent: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the agent - this is only used for access control. Default is \&quot;default\&quot; | [default to &#39;default&#39;]
 **add_agent_request** | [**AddAgentRequest**](AddAgentRequest.md)| The details of the agent to be created | 

### Return type

[**AgentDefinition**](AgentDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_agent**
> delete_agent(code, scope, version=version)

[EARLY ACCESS] DeleteAgent: Delete an agent

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    AgentsApi
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
    api_instance = api_client_factory.build(AgentsApi)
    code = 'code_example' # str | The unique code of the scope
    scope = 'default' # str | The scope of the agent. Default is \"default\" (default to 'default')
    version = 56 # int | The version to delete (optional)

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.delete_agent(code, scope, version=version, opts=opts)

        # [EARLY ACCESS] DeleteAgent: Delete an agent
        api_instance.delete_agent(code, scope, version=version)
    except ApiException as e:
        print("Exception when calling AgentsApi->delete_agent: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The unique code of the scope | 
 **scope** | **str**| The scope of the agent. Default is \&quot;default\&quot; | [default to &#39;default&#39;]
 **version** | **int**| The version to delete | [optional] 

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
**404** | The agent was not found |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_agent**
> AgentDefinition get_agent(code, scope, version=version)

[EARLY ACCESS] GetAgent: Get an agent

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    AgentsApi
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
    api_instance = api_client_factory.build(AgentsApi)
    code = 'code_example' # str | The code of the agent
    scope = 'default' # str | The scope of the agent. Default is \"default\" (default to 'default')
    version = 56 # int | Optional. A specific version of the agent. Default is the latest version. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_agent(code, scope, version=version, opts=opts)

        # [EARLY ACCESS] GetAgent: Get an agent
        api_response = api_instance.get_agent(code, scope, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AgentsApi->get_agent: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the agent | 
 **scope** | **str**| The scope of the agent. Default is \&quot;default\&quot; | [default to &#39;default&#39;]
 **version** | **int**| Optional. A specific version of the agent. Default is the latest version. | [optional] 

### Return type

[**AgentDefinition**](AgentDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | The requested agent was not found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_agents**
> PagedResourceListOfAgentDefinition list_agents(scope, include_system_agents=include_system_agents)

[EARLY ACCESS] ListAgents: List all system agents and agents in the specified scope

Only the latest version of each agent is returned

### Example

```python
from finbourne_candela.exceptions import ApiException
from finbourne_candela.extensions.configuration_options import ConfigurationOptions
from finbourne_candela.models import *
from pprint import pprint
from finbourne_candela import (
    SyncApiClientFactory,
    AgentsApi
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
    api_instance = api_client_factory.build(AgentsApi)
    scope = 'default' # str | The scope of the agents to list. Default is \"default\" (default to 'default')
    include_system_agents = False # bool | Whether or not to include the immutable system provided agents in the results (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_agents(scope, include_system_agents=include_system_agents, opts=opts)

        # [EARLY ACCESS] ListAgents: List all system agents and agents in the specified scope
        api_response = api_instance.list_agents(scope, include_system_agents=include_system_agents)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AgentsApi->list_agents: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the agents to list. Default is \&quot;default\&quot; | [default to &#39;default&#39;]
 **include_system_agents** | **bool**| Whether or not to include the immutable system provided agents in the results | [optional] [default to False]

### Return type

[**PagedResourceListOfAgentDefinition**](PagedResourceListOfAgentDefinition.md)

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

