<a id="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://fbn-ci.lusid.com/candela*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentsApi* | [**add_agent**](docs/AgentsApi.md#add_agent) | **PUT** /api/agents/{scope} | [EARLY ACCESS] AddAgent: Create a new custom Agent
*AgentsApi* | [**delete_agent**](docs/AgentsApi.md#delete_agent) | **DELETE** /api/agents/{scope}/{code} | [EARLY ACCESS] DeleteAgent: Delete an agent
*AgentsApi* | [**get_agent**](docs/AgentsApi.md#get_agent) | **GET** /api/agents/{scope}/{code} | [EARLY ACCESS] GetAgent: Get an agent
*AgentsApi* | [**list_agents**](docs/AgentsApi.md#list_agents) | **GET** /api/agents/{scope} | [EARLY ACCESS] ListAgents: List all system agents and agents in the specified scope
*ApplicationMetadataApi* | [**list_access_controlled_resources**](docs/ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /api/metadata/access/resources | [EARLY ACCESS] ListAccessControlledResources: Get resources available for access control
*TracesApi* | [**delete_trace**](docs/TracesApi.md#delete_trace) | **DELETE** /api/traces/{scope}/{traceId} | [EARLY ACCESS] DeleteTrace: 
*TracesApi* | [**get_trace**](docs/TracesApi.md#get_trace) | **GET** /api/traces/{scope}/{traceId} | [EARLY ACCESS] GetTrace: 
*TracesApi* | [**get_trace_events**](docs/TracesApi.md#get_trace_events) | **GET** /api/traces/events/{scope}/{traceId} | [EARLY ACCESS] GetTraceEvents: 
*TracesApi* | [**list_traces**](docs/TracesApi.md#list_traces) | **GET** /api/traces | [EARLY ACCESS] ListTraces: 


<a id="documentation-for-models"></a>
## Documentation for Models

 - [AccessControlledAction](docs/AccessControlledAction.md)
 - [AccessControlledResource](docs/AccessControlledResource.md)
 - [ActionId](docs/ActionId.md)
 - [AddAgentRequest](docs/AddAgentRequest.md)
 - [AgentDefinition](docs/AgentDefinition.md)
 - [IdSelectorDefinition](docs/IdSelectorDefinition.md)
 - [IdentifierPartSchema](docs/IdentifierPartSchema.md)
 - [Link](docs/Link.md)
 - [LusidProblemDetails](docs/LusidProblemDetails.md)
 - [LusidValidationProblemDetails](docs/LusidValidationProblemDetails.md)
 - [PagedResourceListOfAgentDefinition](docs/PagedResourceListOfAgentDefinition.md)
 - [PagedResourceListOfTraceDefinition](docs/PagedResourceListOfTraceDefinition.md)
 - [PagedResourceListOfTraceEventDefinition](docs/PagedResourceListOfTraceEventDefinition.md)
 - [ResourceListOfAccessControlledResource](docs/ResourceListOfAccessControlledResource.md)
 - [TraceDefinition](docs/TraceDefinition.md)
 - [TraceEventDefinition](docs/TraceEventDefinition.md)

