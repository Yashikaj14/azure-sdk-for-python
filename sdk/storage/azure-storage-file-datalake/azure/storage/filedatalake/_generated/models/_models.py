# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class AclFailedEntry(msrest.serialization.Model):
    """AclFailedEntry.

    :ivar name:
    :vartype name: str
    :ivar type:
    :vartype type: str
    :ivar error_message:
    :vartype error_message: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword name:
        :paramtype name: str
        :keyword type:
        :paramtype type: str
        :keyword error_message:
        :paramtype error_message: str
        """
        super(AclFailedEntry, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.error_message = kwargs.get('error_message', None)


class BlobHierarchyListSegment(msrest.serialization.Model):
    """BlobHierarchyListSegment.

    All required parameters must be populated in order to send to Azure.

    :ivar blob_prefixes:
    :vartype blob_prefixes: list[~azure.storage.filedatalake.models.BlobPrefix]
    :ivar blob_items: Required.
    :vartype blob_items: list[~azure.storage.filedatalake.models.BlobItemInternal]
    """

    _validation = {
        'blob_items': {'required': True},
    }

    _attribute_map = {
        'blob_prefixes': {'key': 'BlobPrefixes', 'type': '[BlobPrefix]'},
        'blob_items': {'key': 'BlobItems', 'type': '[BlobItemInternal]'},
    }
    _xml_map = {
        'name': 'Blobs'
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword blob_prefixes:
        :paramtype blob_prefixes: list[~azure.storage.filedatalake.models.BlobPrefix]
        :keyword blob_items: Required.
        :paramtype blob_items: list[~azure.storage.filedatalake.models.BlobItemInternal]
        """
        super(BlobHierarchyListSegment, self).__init__(**kwargs)
        self.blob_prefixes = kwargs.get('blob_prefixes', None)
        self.blob_items = kwargs['blob_items']


class BlobItemInternal(msrest.serialization.Model):
    """An Azure Storage blob.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar deleted: Required.
    :vartype deleted: bool
    :ivar snapshot: Required.
    :vartype snapshot: str
    :ivar version_id:
    :vartype version_id: str
    :ivar is_current_version:
    :vartype is_current_version: bool
    :ivar properties: Required. Properties of a blob.
    :vartype properties: ~azure.storage.filedatalake.models.BlobPropertiesInternal
    :ivar deletion_id:
    :vartype deletion_id: str
    """

    _validation = {
        'name': {'required': True},
        'deleted': {'required': True},
        'snapshot': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'deleted': {'key': 'Deleted', 'type': 'bool'},
        'snapshot': {'key': 'Snapshot', 'type': 'str'},
        'version_id': {'key': 'VersionId', 'type': 'str'},
        'is_current_version': {'key': 'IsCurrentVersion', 'type': 'bool'},
        'properties': {'key': 'Properties', 'type': 'BlobPropertiesInternal'},
        'deletion_id': {'key': 'DeletionId', 'type': 'str'},
    }
    _xml_map = {
        'name': 'Blob'
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword name: Required.
        :paramtype name: str
        :keyword deleted: Required.
        :paramtype deleted: bool
        :keyword snapshot: Required.
        :paramtype snapshot: str
        :keyword version_id:
        :paramtype version_id: str
        :keyword is_current_version:
        :paramtype is_current_version: bool
        :keyword properties: Required. Properties of a blob.
        :paramtype properties: ~azure.storage.filedatalake.models.BlobPropertiesInternal
        :keyword deletion_id:
        :paramtype deletion_id: str
        """
        super(BlobItemInternal, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.deleted = kwargs['deleted']
        self.snapshot = kwargs['snapshot']
        self.version_id = kwargs.get('version_id', None)
        self.is_current_version = kwargs.get('is_current_version', None)
        self.properties = kwargs['properties']
        self.deletion_id = kwargs.get('deletion_id', None)


class BlobPrefix(msrest.serialization.Model):
    """BlobPrefix.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword name: Required.
        :paramtype name: str
        """
        super(BlobPrefix, self).__init__(**kwargs)
        self.name = kwargs['name']


class BlobPropertiesInternal(msrest.serialization.Model):
    """Properties of a blob.

    All required parameters must be populated in order to send to Azure.

    :ivar creation_time:
    :vartype creation_time: ~datetime.datetime
    :ivar last_modified: Required.
    :vartype last_modified: ~datetime.datetime
    :ivar etag: Required.
    :vartype etag: str
    :ivar content_length: Size in bytes.
    :vartype content_length: long
    :ivar content_type:
    :vartype content_type: str
    :ivar content_encoding:
    :vartype content_encoding: str
    :ivar content_language:
    :vartype content_language: str
    :ivar content_md5:
    :vartype content_md5: bytearray
    :ivar content_disposition:
    :vartype content_disposition: str
    :ivar cache_control:
    :vartype cache_control: str
    :ivar blob_sequence_number:
    :vartype blob_sequence_number: long
    :ivar copy_id:
    :vartype copy_id: str
    :ivar copy_source:
    :vartype copy_source: str
    :ivar copy_progress:
    :vartype copy_progress: str
    :ivar copy_completion_time:
    :vartype copy_completion_time: ~datetime.datetime
    :ivar copy_status_description:
    :vartype copy_status_description: str
    :ivar server_encrypted:
    :vartype server_encrypted: bool
    :ivar incremental_copy:
    :vartype incremental_copy: bool
    :ivar destination_snapshot:
    :vartype destination_snapshot: str
    :ivar deleted_time:
    :vartype deleted_time: ~datetime.datetime
    :ivar remaining_retention_days:
    :vartype remaining_retention_days: int
    :ivar access_tier_inferred:
    :vartype access_tier_inferred: bool
    :ivar customer_provided_key_sha256:
    :vartype customer_provided_key_sha256: str
    :ivar encryption_scope: The name of the encryption scope under which the blob is encrypted.
    :vartype encryption_scope: str
    :ivar access_tier_change_time:
    :vartype access_tier_change_time: ~datetime.datetime
    :ivar tag_count:
    :vartype tag_count: int
    :ivar expires_on:
    :vartype expires_on: ~datetime.datetime
    :ivar is_sealed:
    :vartype is_sealed: bool
    :ivar last_accessed_on:
    :vartype last_accessed_on: ~datetime.datetime
    :ivar delete_time:
    :vartype delete_time: ~datetime.datetime
    """

    _validation = {
        'last_modified': {'required': True},
        'etag': {'required': True},
    }

    _attribute_map = {
        'creation_time': {'key': 'Creation-Time', 'type': 'rfc-1123'},
        'last_modified': {'key': 'Last-Modified', 'type': 'rfc-1123'},
        'etag': {'key': 'Etag', 'type': 'str'},
        'content_length': {'key': 'Content-Length', 'type': 'long'},
        'content_type': {'key': 'Content-Type', 'type': 'str'},
        'content_encoding': {'key': 'Content-Encoding', 'type': 'str'},
        'content_language': {'key': 'Content-Language', 'type': 'str'},
        'content_md5': {'key': 'Content-MD5', 'type': 'bytearray'},
        'content_disposition': {'key': 'Content-Disposition', 'type': 'str'},
        'cache_control': {'key': 'Cache-Control', 'type': 'str'},
        'blob_sequence_number': {'key': 'x-ms-blob-sequence-number', 'type': 'long'},
        'copy_id': {'key': 'CopyId', 'type': 'str'},
        'copy_source': {'key': 'CopySource', 'type': 'str'},
        'copy_progress': {'key': 'CopyProgress', 'type': 'str'},
        'copy_completion_time': {'key': 'CopyCompletionTime', 'type': 'rfc-1123'},
        'copy_status_description': {'key': 'CopyStatusDescription', 'type': 'str'},
        'server_encrypted': {'key': 'ServerEncrypted', 'type': 'bool'},
        'incremental_copy': {'key': 'IncrementalCopy', 'type': 'bool'},
        'destination_snapshot': {'key': 'DestinationSnapshot', 'type': 'str'},
        'deleted_time': {'key': 'DeletedTime', 'type': 'rfc-1123'},
        'remaining_retention_days': {'key': 'RemainingRetentionDays', 'type': 'int'},
        'access_tier_inferred': {'key': 'AccessTierInferred', 'type': 'bool'},
        'customer_provided_key_sha256': {'key': 'CustomerProvidedKeySha256', 'type': 'str'},
        'encryption_scope': {'key': 'EncryptionScope', 'type': 'str'},
        'access_tier_change_time': {'key': 'AccessTierChangeTime', 'type': 'rfc-1123'},
        'tag_count': {'key': 'TagCount', 'type': 'int'},
        'expires_on': {'key': 'Expiry-Time', 'type': 'rfc-1123'},
        'is_sealed': {'key': 'Sealed', 'type': 'bool'},
        'last_accessed_on': {'key': 'LastAccessTime', 'type': 'rfc-1123'},
        'delete_time': {'key': 'DeleteTime', 'type': 'rfc-1123'},
    }
    _xml_map = {
        'name': 'Properties'
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword creation_time:
        :paramtype creation_time: ~datetime.datetime
        :keyword last_modified: Required.
        :paramtype last_modified: ~datetime.datetime
        :keyword etag: Required.
        :paramtype etag: str
        :keyword content_length: Size in bytes.
        :paramtype content_length: long
        :keyword content_type:
        :paramtype content_type: str
        :keyword content_encoding:
        :paramtype content_encoding: str
        :keyword content_language:
        :paramtype content_language: str
        :keyword content_md5:
        :paramtype content_md5: bytearray
        :keyword content_disposition:
        :paramtype content_disposition: str
        :keyword cache_control:
        :paramtype cache_control: str
        :keyword blob_sequence_number:
        :paramtype blob_sequence_number: long
        :keyword copy_id:
        :paramtype copy_id: str
        :keyword copy_source:
        :paramtype copy_source: str
        :keyword copy_progress:
        :paramtype copy_progress: str
        :keyword copy_completion_time:
        :paramtype copy_completion_time: ~datetime.datetime
        :keyword copy_status_description:
        :paramtype copy_status_description: str
        :keyword server_encrypted:
        :paramtype server_encrypted: bool
        :keyword incremental_copy:
        :paramtype incremental_copy: bool
        :keyword destination_snapshot:
        :paramtype destination_snapshot: str
        :keyword deleted_time:
        :paramtype deleted_time: ~datetime.datetime
        :keyword remaining_retention_days:
        :paramtype remaining_retention_days: int
        :keyword access_tier_inferred:
        :paramtype access_tier_inferred: bool
        :keyword customer_provided_key_sha256:
        :paramtype customer_provided_key_sha256: str
        :keyword encryption_scope: The name of the encryption scope under which the blob is encrypted.
        :paramtype encryption_scope: str
        :keyword access_tier_change_time:
        :paramtype access_tier_change_time: ~datetime.datetime
        :keyword tag_count:
        :paramtype tag_count: int
        :keyword expires_on:
        :paramtype expires_on: ~datetime.datetime
        :keyword is_sealed:
        :paramtype is_sealed: bool
        :keyword last_accessed_on:
        :paramtype last_accessed_on: ~datetime.datetime
        :keyword delete_time:
        :paramtype delete_time: ~datetime.datetime
        """
        super(BlobPropertiesInternal, self).__init__(**kwargs)
        self.creation_time = kwargs.get('creation_time', None)
        self.last_modified = kwargs['last_modified']
        self.etag = kwargs['etag']
        self.content_length = kwargs.get('content_length', None)
        self.content_type = kwargs.get('content_type', None)
        self.content_encoding = kwargs.get('content_encoding', None)
        self.content_language = kwargs.get('content_language', None)
        self.content_md5 = kwargs.get('content_md5', None)
        self.content_disposition = kwargs.get('content_disposition', None)
        self.cache_control = kwargs.get('cache_control', None)
        self.blob_sequence_number = kwargs.get('blob_sequence_number', None)
        self.copy_id = kwargs.get('copy_id', None)
        self.copy_source = kwargs.get('copy_source', None)
        self.copy_progress = kwargs.get('copy_progress', None)
        self.copy_completion_time = kwargs.get('copy_completion_time', None)
        self.copy_status_description = kwargs.get('copy_status_description', None)
        self.server_encrypted = kwargs.get('server_encrypted', None)
        self.incremental_copy = kwargs.get('incremental_copy', None)
        self.destination_snapshot = kwargs.get('destination_snapshot', None)
        self.deleted_time = kwargs.get('deleted_time', None)
        self.remaining_retention_days = kwargs.get('remaining_retention_days', None)
        self.access_tier_inferred = kwargs.get('access_tier_inferred', None)
        self.customer_provided_key_sha256 = kwargs.get('customer_provided_key_sha256', None)
        self.encryption_scope = kwargs.get('encryption_scope', None)
        self.access_tier_change_time = kwargs.get('access_tier_change_time', None)
        self.tag_count = kwargs.get('tag_count', None)
        self.expires_on = kwargs.get('expires_on', None)
        self.is_sealed = kwargs.get('is_sealed', None)
        self.last_accessed_on = kwargs.get('last_accessed_on', None)
        self.delete_time = kwargs.get('delete_time', None)


class FileSystem(msrest.serialization.Model):
    """FileSystem.

    :ivar name:
    :vartype name: str
    :ivar last_modified:
    :vartype last_modified: str
    :ivar e_tag:
    :vartype e_tag: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword name:
        :paramtype name: str
        :keyword last_modified:
        :paramtype last_modified: str
        :keyword e_tag:
        :paramtype e_tag: str
        """
        super(FileSystem, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.last_modified = kwargs.get('last_modified', None)
        self.e_tag = kwargs.get('e_tag', None)


class FileSystemList(msrest.serialization.Model):
    """FileSystemList.

    :ivar filesystems:
    :vartype filesystems: list[~azure.storage.filedatalake.models.FileSystem]
    """

    _attribute_map = {
        'filesystems': {'key': 'filesystems', 'type': '[FileSystem]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword filesystems:
        :paramtype filesystems: list[~azure.storage.filedatalake.models.FileSystem]
        """
        super(FileSystemList, self).__init__(**kwargs)
        self.filesystems = kwargs.get('filesystems', None)


class LeaseAccessConditions(msrest.serialization.Model):
    """Parameter group.

    :ivar lease_id: If specified, the operation only succeeds if the resource's lease is active and
     matches this ID.
    :vartype lease_id: str
    """

    _attribute_map = {
        'lease_id': {'key': 'leaseId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword lease_id: If specified, the operation only succeeds if the resource's lease is active
         and matches this ID.
        :paramtype lease_id: str
        """
        super(LeaseAccessConditions, self).__init__(**kwargs)
        self.lease_id = kwargs.get('lease_id', None)


class ListBlobsHierarchySegmentResponse(msrest.serialization.Model):
    """An enumeration of blobs.

    All required parameters must be populated in order to send to Azure.

    :ivar service_endpoint: Required.
    :vartype service_endpoint: str
    :ivar container_name: Required.
    :vartype container_name: str
    :ivar prefix:
    :vartype prefix: str
    :ivar marker:
    :vartype marker: str
    :ivar max_results:
    :vartype max_results: int
    :ivar delimiter:
    :vartype delimiter: str
    :ivar segment: Required.
    :vartype segment: ~azure.storage.filedatalake.models.BlobHierarchyListSegment
    :ivar next_marker:
    :vartype next_marker: str
    """

    _validation = {
        'service_endpoint': {'required': True},
        'container_name': {'required': True},
        'segment': {'required': True},
    }

    _attribute_map = {
        'service_endpoint': {'key': 'ServiceEndpoint', 'type': 'str', 'xml': {'attr': True}},
        'container_name': {'key': 'ContainerName', 'type': 'str', 'xml': {'attr': True}},
        'prefix': {'key': 'Prefix', 'type': 'str'},
        'marker': {'key': 'Marker', 'type': 'str'},
        'max_results': {'key': 'MaxResults', 'type': 'int'},
        'delimiter': {'key': 'Delimiter', 'type': 'str'},
        'segment': {'key': 'Segment', 'type': 'BlobHierarchyListSegment'},
        'next_marker': {'key': 'NextMarker', 'type': 'str'},
    }
    _xml_map = {
        'name': 'EnumerationResults'
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword service_endpoint: Required.
        :paramtype service_endpoint: str
        :keyword container_name: Required.
        :paramtype container_name: str
        :keyword prefix:
        :paramtype prefix: str
        :keyword marker:
        :paramtype marker: str
        :keyword max_results:
        :paramtype max_results: int
        :keyword delimiter:
        :paramtype delimiter: str
        :keyword segment: Required.
        :paramtype segment: ~azure.storage.filedatalake.models.BlobHierarchyListSegment
        :keyword next_marker:
        :paramtype next_marker: str
        """
        super(ListBlobsHierarchySegmentResponse, self).__init__(**kwargs)
        self.service_endpoint = kwargs['service_endpoint']
        self.container_name = kwargs['container_name']
        self.prefix = kwargs.get('prefix', None)
        self.marker = kwargs.get('marker', None)
        self.max_results = kwargs.get('max_results', None)
        self.delimiter = kwargs.get('delimiter', None)
        self.segment = kwargs['segment']
        self.next_marker = kwargs.get('next_marker', None)


class ModifiedAccessConditions(msrest.serialization.Model):
    """Parameter group.

    :ivar if_modified_since: Specify this header value to operate only on a blob if it has been
     modified since the specified date/time.
    :vartype if_modified_since: ~datetime.datetime
    :ivar if_unmodified_since: Specify this header value to operate only on a blob if it has not
     been modified since the specified date/time.
    :vartype if_unmodified_since: ~datetime.datetime
    :ivar if_match: Specify an ETag value to operate only on blobs with a matching value.
    :vartype if_match: str
    :ivar if_none_match: Specify an ETag value to operate only on blobs without a matching value.
    :vartype if_none_match: str
    """

    _attribute_map = {
        'if_modified_since': {'key': 'ifModifiedSince', 'type': 'rfc-1123'},
        'if_unmodified_since': {'key': 'ifUnmodifiedSince', 'type': 'rfc-1123'},
        'if_match': {'key': 'ifMatch', 'type': 'str'},
        'if_none_match': {'key': 'ifNoneMatch', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword if_modified_since: Specify this header value to operate only on a blob if it has been
         modified since the specified date/time.
        :paramtype if_modified_since: ~datetime.datetime
        :keyword if_unmodified_since: Specify this header value to operate only on a blob if it has not
         been modified since the specified date/time.
        :paramtype if_unmodified_since: ~datetime.datetime
        :keyword if_match: Specify an ETag value to operate only on blobs with a matching value.
        :paramtype if_match: str
        :keyword if_none_match: Specify an ETag value to operate only on blobs without a matching
         value.
        :paramtype if_none_match: str
        """
        super(ModifiedAccessConditions, self).__init__(**kwargs)
        self.if_modified_since = kwargs.get('if_modified_since', None)
        self.if_unmodified_since = kwargs.get('if_unmodified_since', None)
        self.if_match = kwargs.get('if_match', None)
        self.if_none_match = kwargs.get('if_none_match', None)


class Path(msrest.serialization.Model):
    """Path.

    :ivar name:
    :vartype name: str
    :ivar is_directory:
    :vartype is_directory: bool
    :ivar last_modified:
    :vartype last_modified: str
    :ivar e_tag:
    :vartype e_tag: str
    :ivar content_length:
    :vartype content_length: long
    :ivar owner:
    :vartype owner: str
    :ivar group:
    :vartype group: str
    :ivar permissions:
    :vartype permissions: str
    :ivar encryption_scope: The name of the encryption scope under which the blob is encrypted.
    :vartype encryption_scope: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_directory': {'key': 'isDirectory', 'type': 'bool'},
        'last_modified': {'key': 'lastModified', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'content_length': {'key': 'contentLength', 'type': 'long'},
        'owner': {'key': 'owner', 'type': 'str'},
        'group': {'key': 'group', 'type': 'str'},
        'permissions': {'key': 'permissions', 'type': 'str'},
        'encryption_scope': {'key': 'EncryptionScope', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword name:
        :paramtype name: str
        :keyword is_directory:
        :paramtype is_directory: bool
        :keyword last_modified:
        :paramtype last_modified: str
        :keyword e_tag:
        :paramtype e_tag: str
        :keyword content_length:
        :paramtype content_length: long
        :keyword owner:
        :paramtype owner: str
        :keyword group:
        :paramtype group: str
        :keyword permissions:
        :paramtype permissions: str
        :keyword encryption_scope: The name of the encryption scope under which the blob is encrypted.
        :paramtype encryption_scope: str
        """
        super(Path, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.is_directory = kwargs.get('is_directory', False)
        self.last_modified = kwargs.get('last_modified', None)
        self.e_tag = kwargs.get('e_tag', None)
        self.content_length = kwargs.get('content_length', None)
        self.owner = kwargs.get('owner', None)
        self.group = kwargs.get('group', None)
        self.permissions = kwargs.get('permissions', None)
        self.encryption_scope = kwargs.get('encryption_scope', None)


class PathHTTPHeaders(msrest.serialization.Model):
    """Parameter group.

    :ivar cache_control: Optional. Sets the blob's cache control. If specified, this property is
     stored with the blob and returned with a read request.
    :vartype cache_control: str
    :ivar content_encoding: Optional. Sets the blob's content encoding. If specified, this property
     is stored with the blob and returned with a read request.
    :vartype content_encoding: str
    :ivar content_language: Optional. Set the blob's content language. If specified, this property
     is stored with the blob and returned with a read request.
    :vartype content_language: str
    :ivar content_disposition: Optional. Sets the blob's Content-Disposition header.
    :vartype content_disposition: str
    :ivar content_type: Optional. Sets the blob's content type. If specified, this property is
     stored with the blob and returned with a read request.
    :vartype content_type: str
    :ivar content_md5: Specify the transactional md5 for the body, to be validated by the service.
    :vartype content_md5: bytearray
    :ivar transactional_content_hash: Specify the transactional md5 for the body, to be validated
     by the service.
    :vartype transactional_content_hash: bytearray
    """

    _attribute_map = {
        'cache_control': {'key': 'cacheControl', 'type': 'str'},
        'content_encoding': {'key': 'contentEncoding', 'type': 'str'},
        'content_language': {'key': 'contentLanguage', 'type': 'str'},
        'content_disposition': {'key': 'contentDisposition', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'content_md5': {'key': 'contentMD5', 'type': 'bytearray'},
        'transactional_content_hash': {'key': 'transactionalContentHash', 'type': 'bytearray'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword cache_control: Optional. Sets the blob's cache control. If specified, this property is
         stored with the blob and returned with a read request.
        :paramtype cache_control: str
        :keyword content_encoding: Optional. Sets the blob's content encoding. If specified, this
         property is stored with the blob and returned with a read request.
        :paramtype content_encoding: str
        :keyword content_language: Optional. Set the blob's content language. If specified, this
         property is stored with the blob and returned with a read request.
        :paramtype content_language: str
        :keyword content_disposition: Optional. Sets the blob's Content-Disposition header.
        :paramtype content_disposition: str
        :keyword content_type: Optional. Sets the blob's content type. If specified, this property is
         stored with the blob and returned with a read request.
        :paramtype content_type: str
        :keyword content_md5: Specify the transactional md5 for the body, to be validated by the
         service.
        :paramtype content_md5: bytearray
        :keyword transactional_content_hash: Specify the transactional md5 for the body, to be
         validated by the service.
        :paramtype transactional_content_hash: bytearray
        """
        super(PathHTTPHeaders, self).__init__(**kwargs)
        self.cache_control = kwargs.get('cache_control', None)
        self.content_encoding = kwargs.get('content_encoding', None)
        self.content_language = kwargs.get('content_language', None)
        self.content_disposition = kwargs.get('content_disposition', None)
        self.content_type = kwargs.get('content_type', None)
        self.content_md5 = kwargs.get('content_md5', None)
        self.transactional_content_hash = kwargs.get('transactional_content_hash', None)


class PathList(msrest.serialization.Model):
    """PathList.

    :ivar paths:
    :vartype paths: list[~azure.storage.filedatalake.models.Path]
    """

    _attribute_map = {
        'paths': {'key': 'paths', 'type': '[Path]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword paths:
        :paramtype paths: list[~azure.storage.filedatalake.models.Path]
        """
        super(PathList, self).__init__(**kwargs)
        self.paths = kwargs.get('paths', None)


class SetAccessControlRecursiveResponse(msrest.serialization.Model):
    """SetAccessControlRecursiveResponse.

    :ivar directories_successful:
    :vartype directories_successful: int
    :ivar files_successful:
    :vartype files_successful: int
    :ivar failure_count:
    :vartype failure_count: int
    :ivar failed_entries:
    :vartype failed_entries: list[~azure.storage.filedatalake.models.AclFailedEntry]
    """

    _attribute_map = {
        'directories_successful': {'key': 'directoriesSuccessful', 'type': 'int'},
        'files_successful': {'key': 'filesSuccessful', 'type': 'int'},
        'failure_count': {'key': 'failureCount', 'type': 'int'},
        'failed_entries': {'key': 'failedEntries', 'type': '[AclFailedEntry]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword directories_successful:
        :paramtype directories_successful: int
        :keyword files_successful:
        :paramtype files_successful: int
        :keyword failure_count:
        :paramtype failure_count: int
        :keyword failed_entries:
        :paramtype failed_entries: list[~azure.storage.filedatalake.models.AclFailedEntry]
        """
        super(SetAccessControlRecursiveResponse, self).__init__(**kwargs)
        self.directories_successful = kwargs.get('directories_successful', None)
        self.files_successful = kwargs.get('files_successful', None)
        self.failure_count = kwargs.get('failure_count', None)
        self.failed_entries = kwargs.get('failed_entries', None)


class SourceModifiedAccessConditions(msrest.serialization.Model):
    """Parameter group.

    :ivar source_if_match: Specify an ETag value to operate only on blobs with a matching value.
    :vartype source_if_match: str
    :ivar source_if_none_match: Specify an ETag value to operate only on blobs without a matching
     value.
    :vartype source_if_none_match: str
    :ivar source_if_modified_since: Specify this header value to operate only on a blob if it has
     been modified since the specified date/time.
    :vartype source_if_modified_since: ~datetime.datetime
    :ivar source_if_unmodified_since: Specify this header value to operate only on a blob if it has
     not been modified since the specified date/time.
    :vartype source_if_unmodified_since: ~datetime.datetime
    """

    _attribute_map = {
        'source_if_match': {'key': 'sourceIfMatch', 'type': 'str'},
        'source_if_none_match': {'key': 'sourceIfNoneMatch', 'type': 'str'},
        'source_if_modified_since': {'key': 'sourceIfModifiedSince', 'type': 'rfc-1123'},
        'source_if_unmodified_since': {'key': 'sourceIfUnmodifiedSince', 'type': 'rfc-1123'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword source_if_match: Specify an ETag value to operate only on blobs with a matching value.
        :paramtype source_if_match: str
        :keyword source_if_none_match: Specify an ETag value to operate only on blobs without a
         matching value.
        :paramtype source_if_none_match: str
        :keyword source_if_modified_since: Specify this header value to operate only on a blob if it
         has been modified since the specified date/time.
        :paramtype source_if_modified_since: ~datetime.datetime
        :keyword source_if_unmodified_since: Specify this header value to operate only on a blob if it
         has not been modified since the specified date/time.
        :paramtype source_if_unmodified_since: ~datetime.datetime
        """
        super(SourceModifiedAccessConditions, self).__init__(**kwargs)
        self.source_if_match = kwargs.get('source_if_match', None)
        self.source_if_none_match = kwargs.get('source_if_none_match', None)
        self.source_if_modified_since = kwargs.get('source_if_modified_since', None)
        self.source_if_unmodified_since = kwargs.get('source_if_unmodified_since', None)


class StorageError(msrest.serialization.Model):
    """StorageError.

    :ivar error: The service error response object.
    :vartype error: ~azure.storage.filedatalake.models.StorageErrorError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'StorageErrorError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword error: The service error response object.
        :paramtype error: ~azure.storage.filedatalake.models.StorageErrorError
        """
        super(StorageError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class StorageErrorError(msrest.serialization.Model):
    """The service error response object.

    :ivar code: The service error code.
    :vartype code: str
    :ivar message: The service error message.
    :vartype message: str
    """

    _attribute_map = {
        'code': {'key': 'Code', 'type': 'str'},
        'message': {'key': 'Message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword code: The service error code.
        :paramtype code: str
        :keyword message: The service error message.
        :paramtype message: str
        """
        super(StorageErrorError, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
