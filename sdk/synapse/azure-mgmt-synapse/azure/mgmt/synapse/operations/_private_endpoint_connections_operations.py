# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class PrivateEndpointConnectionsOperations(object):
    """PrivateEndpointConnectionsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for this operation. Constant value: "2020-12-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-12-01"

        self.config = config

    def get(
            self, resource_group_name, workspace_name, private_endpoint_connection_name, custom_headers=None, raw=False, **operation_config):
        """Gets a private endpoint connection.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param private_endpoint_connection_name: The name of the private
         endpoint connection.
        :type private_endpoint_connection_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PrivateEndpointConnection or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.synapse.models.PrivateEndpointConnection or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.synapse.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
            'privateEndpointConnectionName': self._serialize.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PrivateEndpointConnection', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/privateEndpointConnections/{privateEndpointConnectionName}'}


    def _create_initial(
            self, resource_group_name, workspace_name, private_endpoint_connection_name, private_endpoint=None, private_link_service_connection_state=None, custom_headers=None, raw=False, **operation_config):
        request = models.PrivateEndpointConnection(private_endpoint=private_endpoint, private_link_service_connection_state=private_link_service_connection_state)

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
            'privateEndpointConnectionName': self._serialize.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(request, 'PrivateEndpointConnection')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PrivateEndpointConnection', response)
        if response.status_code == 201:
            deserialized = self._deserialize('PrivateEndpointConnection', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create(
            self, resource_group_name, workspace_name, private_endpoint_connection_name, private_endpoint=None, private_link_service_connection_state=None, custom_headers=None, raw=False, polling=True, **operation_config):
        """Approve or reject a private endpoint connection.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param private_endpoint_connection_name: The name of the private
         endpoint connection.
        :type private_endpoint_connection_name: str
        :param private_endpoint: The private endpoint which the connection
         belongs to.
        :type private_endpoint: ~azure.mgmt.synapse.models.PrivateEndpoint
        :param private_link_service_connection_state: Connection state of the
         private endpoint connection.
        :type private_link_service_connection_state:
         ~azure.mgmt.synapse.models.PrivateLinkServiceConnectionState
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns
         PrivateEndpointConnection or
         ClientRawResponse<PrivateEndpointConnection> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.synapse.models.PrivateEndpointConnection]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.synapse.models.PrivateEndpointConnection]]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.synapse.models.ErrorResponseException>`
        """
        raw_result = self._create_initial(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            private_endpoint=private_endpoint,
            private_link_service_connection_state=private_link_service_connection_state,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('PrivateEndpointConnection', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/privateEndpointConnections/{privateEndpointConnectionName}'}


    def _delete_initial(
            self, resource_group_name, workspace_name, private_endpoint_connection_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
            'privateEndpointConnectionName': self._serialize.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202, 204]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 202:
            deserialized = self._deserialize('OperationResource', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def delete(
            self, resource_group_name, workspace_name, private_endpoint_connection_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """Delete a private endpoint connection.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param private_endpoint_connection_name: The name of the private
         endpoint connection.
        :type private_endpoint_connection_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns OperationResource or
         ClientRawResponse<OperationResource> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.synapse.models.OperationResource]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.synapse.models.OperationResource]]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.synapse.models.ErrorResponseException>`
        """
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('OperationResource', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/privateEndpointConnections/{privateEndpointConnectionName}'}

    def list(
            self, resource_group_name, workspace_name, custom_headers=None, raw=False, **operation_config):
        """Lists private endpoint connection in workspace.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of PrivateEndpointConnection
        :rtype:
         ~azure.mgmt.synapse.models.PrivateEndpointConnectionPaged[~azure.mgmt.synapse.models.PrivateEndpointConnection]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.synapse.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.PrivateEndpointConnectionPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/privateEndpointConnections'}
