# coding: utf-8

"""
    FINBOURNE Candela Platform Web API

    FINBOURNE Technology  # noqa: E501

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic.v1 import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from pydantic.v1 import StrictInt, StrictStr

from typing import Any, Dict, List

from finbourne_candela.models.slot_data import SlotData
from finbourne_candela.models.slots_put_response import SlotsPutResponse

from finbourne_candela.api_client import ApiClient
from finbourne_candela.api_response import ApiResponse
from finbourne_candela.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from finbourne_candela.extensions.configuration_options import ConfigurationOptions


class SystemApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def admin_delete_slot(self, slot_id : StrictStr, **kwargs) -> None:  # noqa: E501
        ...

    @overload
    def admin_delete_slot(self, slot_id : StrictStr, async_req: Optional[bool]=True, **kwargs) -> None:  # noqa: E501
        ...

    @validate_arguments
    def admin_delete_slot(self, slot_id : StrictStr, async_req: Optional[bool]=None, **kwargs) -> Union[None, Awaitable[None]]:  # noqa: E501
        """Deletes a slot from the system without replacing it  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.admin_delete_slot(slot_id, async_req=True)
        >>> result = thread.get()

        :param slot_id: (required)
        :type slot_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the admin_delete_slot_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.admin_delete_slot_with_http_info(slot_id, **kwargs)  # noqa: E501

    @validate_arguments
    def admin_delete_slot_with_http_info(self, slot_id : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """Deletes a slot from the system without replacing it  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.admin_delete_slot_with_http_info(slot_id, async_req=True)
        >>> result = thread.get()

        :param slot_id: (required)
        :type slot_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'slot_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method admin_delete_slot" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('slot_id') is not None:  # noqa: E501
            _query_params.append(('slot_id', _params['slot_id']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['HTTPBearer']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/system/slot', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def get_domain_state(self, **kwargs) -> object:  # noqa: E501
        ...

    @overload
    def get_domain_state(self, async_req: Optional[bool]=True, **kwargs) -> object:  # noqa: E501
        ...

    @validate_arguments
    def get_domain_state(self, async_req: Optional[bool]=None, **kwargs) -> Union[object, Awaitable[object]]:  # noqa: E501
        """Get the current status of your Candela platform slots infrastructure.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_state(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_domain_state_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_domain_state_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_domain_state_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Get the current status of your Candela platform slots infrastructure.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_state_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_domain_state" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['HTTPBearer']  # noqa: E501

        _response_types_map = {
            '200': "object",
        }

        return self.api_client.call_api(
            '/system/status', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def list_slots(self, **kwargs) -> List[SlotData]:  # noqa: E501
        ...

    @overload
    def list_slots(self, async_req: Optional[bool]=True, **kwargs) -> List[SlotData]:  # noqa: E501
        ...

    @validate_arguments
    def list_slots(self, async_req: Optional[bool]=None, **kwargs) -> Union[List[SlotData], Awaitable[List[SlotData]]]:  # noqa: E501
        """List the current slots in your Candela platform.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_slots(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[SlotData]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_slots_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.list_slots_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def list_slots_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """List the current slots in your Candela platform.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_slots_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[SlotData], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_slots" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['HTTPBearer']  # noqa: E501

        _response_types_map = {
            '200': "List[SlotData]",
        }

        return self.api_client.call_api(
            '/system/list_slots', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def set_free_slots_target(self, slot_type : StrictStr, target_free_slots : StrictInt, **kwargs) -> SlotsPutResponse:  # noqa: E501
        ...

    @overload
    def set_free_slots_target(self, slot_type : StrictStr, target_free_slots : StrictInt, async_req: Optional[bool]=True, **kwargs) -> SlotsPutResponse:  # noqa: E501
        ...

    @validate_arguments
    def set_free_slots_target(self, slot_type : StrictStr, target_free_slots : StrictInt, async_req: Optional[bool]=None, **kwargs) -> Union[SlotsPutResponse, Awaitable[SlotsPutResponse]]:  # noqa: E501
        """Set the target number of free slots  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_free_slots_target(slot_type, target_free_slots, async_req=True)
        >>> result = thread.get()

        :param slot_type: (required)
        :type slot_type: str
        :param target_free_slots: (required)
        :type target_free_slots: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SlotsPutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the set_free_slots_target_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.set_free_slots_target_with_http_info(slot_type, target_free_slots, **kwargs)  # noqa: E501

    @validate_arguments
    def set_free_slots_target_with_http_info(self, slot_type : StrictStr, target_free_slots : StrictInt, **kwargs) -> ApiResponse:  # noqa: E501
        """Set the target number of free slots  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_free_slots_target_with_http_info(slot_type, target_free_slots, async_req=True)
        >>> result = thread.get()

        :param slot_type: (required)
        :type slot_type: str
        :param target_free_slots: (required)
        :type target_free_slots: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SlotsPutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'slot_type',
            'target_free_slots'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_free_slots_target" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('slot_type') is not None:  # noqa: E501
            _query_params.append(('slot_type', _params['slot_type']))

        if _params.get('target_free_slots') is not None:  # noqa: E501
            _query_params.append(('target_free_slots', _params['target_free_slots']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['HTTPBearer']  # noqa: E501

        _response_types_map = {
            '200': "SlotsPutResponse",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/system/free_slots_target', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def set_max_slots(self, slot_type : StrictStr, max_slots : StrictInt, **kwargs) -> SlotsPutResponse:  # noqa: E501
        ...

    @overload
    def set_max_slots(self, slot_type : StrictStr, max_slots : StrictInt, async_req: Optional[bool]=True, **kwargs) -> SlotsPutResponse:  # noqa: E501
        ...

    @validate_arguments
    def set_max_slots(self, slot_type : StrictStr, max_slots : StrictInt, async_req: Optional[bool]=None, **kwargs) -> Union[SlotsPutResponse, Awaitable[SlotsPutResponse]]:  # noqa: E501
        """Set the maximum number of slots.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_max_slots(slot_type, max_slots, async_req=True)
        >>> result = thread.get()

        :param slot_type: (required)
        :type slot_type: str
        :param max_slots: (required)
        :type max_slots: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SlotsPutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the set_max_slots_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.set_max_slots_with_http_info(slot_type, max_slots, **kwargs)  # noqa: E501

    @validate_arguments
    def set_max_slots_with_http_info(self, slot_type : StrictStr, max_slots : StrictInt, **kwargs) -> ApiResponse:  # noqa: E501
        """Set the maximum number of slots.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_max_slots_with_http_info(slot_type, max_slots, async_req=True)
        >>> result = thread.get()

        :param slot_type: (required)
        :type slot_type: str
        :param max_slots: (required)
        :type max_slots: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SlotsPutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'slot_type',
            'max_slots'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_max_slots" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('slot_type') is not None:  # noqa: E501
            _query_params.append(('slot_type', _params['slot_type']))

        if _params.get('max_slots') is not None:  # noqa: E501
            _query_params.append(('max_slots', _params['max_slots']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['HTTPBearer']  # noqa: E501

        _response_types_map = {
            '200': "SlotsPutResponse",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/system/max_slots', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
