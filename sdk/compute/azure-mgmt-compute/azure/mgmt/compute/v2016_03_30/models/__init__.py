# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AdditionalUnattendContent
from ._models_py3 import ApiEntityReference
from ._models_py3 import ApiError
from ._models_py3 import ApiErrorBase
from ._models_py3 import AvailabilitySet
from ._models_py3 import AvailabilitySetListResult
from ._models_py3 import BootDiagnostics
from ._models_py3 import BootDiagnosticsInstanceView
from ._models_py3 import ComputeLongRunningOperationProperties
from ._models_py3 import DataDisk
from ._models_py3 import DataDiskImage
from ._models_py3 import DiagnosticsProfile
from ._models_py3 import DiskEncryptionSettings
from ._models_py3 import DiskInstanceView
from ._models_py3 import HardwareProfile
from ._models_py3 import ImageReference
from ._models_py3 import InnerError
from ._models_py3 import InstanceViewStatus
from ._models_py3 import KeyVaultKeyReference
from ._models_py3 import KeyVaultSecretReference
from ._models_py3 import LinuxConfiguration
from ._models_py3 import ListUsagesResult
from ._models_py3 import NetworkInterfaceReference
from ._models_py3 import NetworkProfile
from ._models_py3 import OSDisk
from ._models_py3 import OSDiskImage
from ._models_py3 import OSProfile
from ._models_py3 import OperationStatusResponse
from ._models_py3 import Plan
from ._models_py3 import PurchasePlan
from ._models_py3 import Resource
from ._models_py3 import Sku
from ._models_py3 import SshConfiguration
from ._models_py3 import SshPublicKey
from ._models_py3 import StorageProfile
from ._models_py3 import SubResource
from ._models_py3 import UpdateResource
from ._models_py3 import UpgradePolicy
from ._models_py3 import Usage
from ._models_py3 import UsageName
from ._models_py3 import VaultCertificate
from ._models_py3 import VaultSecretGroup
from ._models_py3 import VirtualHardDisk
from ._models_py3 import VirtualMachine
from ._models_py3 import VirtualMachineAgentInstanceView
from ._models_py3 import VirtualMachineCaptureParameters
from ._models_py3 import VirtualMachineCaptureResult
from ._models_py3 import VirtualMachineExtension
from ._models_py3 import VirtualMachineExtensionHandlerInstanceView
from ._models_py3 import VirtualMachineExtensionImage
from ._models_py3 import VirtualMachineExtensionInstanceView
from ._models_py3 import VirtualMachineExtensionUpdate
from ._models_py3 import VirtualMachineExtensionsListResult
from ._models_py3 import VirtualMachineIdentity
from ._models_py3 import VirtualMachineImage
from ._models_py3 import VirtualMachineImageResource
from ._models_py3 import VirtualMachineInstanceView
from ._models_py3 import VirtualMachineListResult
from ._models_py3 import VirtualMachineScaleSet
from ._models_py3 import VirtualMachineScaleSetExtension
from ._models_py3 import VirtualMachineScaleSetExtensionProfile
from ._models_py3 import VirtualMachineScaleSetIPConfiguration
from ._models_py3 import VirtualMachineScaleSetIdentity
from ._models_py3 import VirtualMachineScaleSetInstanceView
from ._models_py3 import VirtualMachineScaleSetInstanceViewStatusesSummary
from ._models_py3 import VirtualMachineScaleSetListResult
from ._models_py3 import VirtualMachineScaleSetListSkusResult
from ._models_py3 import VirtualMachineScaleSetListWithLinkResult
from ._models_py3 import VirtualMachineScaleSetNetworkConfiguration
from ._models_py3 import VirtualMachineScaleSetNetworkProfile
from ._models_py3 import VirtualMachineScaleSetOSDisk
from ._models_py3 import VirtualMachineScaleSetOSProfile
from ._models_py3 import VirtualMachineScaleSetSku
from ._models_py3 import VirtualMachineScaleSetSkuCapacity
from ._models_py3 import VirtualMachineScaleSetStorageProfile
from ._models_py3 import VirtualMachineScaleSetVM
from ._models_py3 import VirtualMachineScaleSetVMExtensionsSummary
from ._models_py3 import VirtualMachineScaleSetVMInstanceIDs
from ._models_py3 import VirtualMachineScaleSetVMInstanceRequiredIDs
from ._models_py3 import VirtualMachineScaleSetVMInstanceView
from ._models_py3 import VirtualMachineScaleSetVMListResult
from ._models_py3 import VirtualMachineScaleSetVMProfile
from ._models_py3 import VirtualMachineSize
from ._models_py3 import VirtualMachineSizeListResult
from ._models_py3 import VirtualMachineStatusCodeCount
from ._models_py3 import WinRMConfiguration
from ._models_py3 import WinRMListener
from ._models_py3 import WindowsConfiguration


from ._compute_management_client_enums import (
    CachingTypes,
    DiskCreateOptionTypes,
    OperatingSystemTypes,
    ProtocolTypes,
    SettingNames,
    StatusLevelTypes,
    UpgradeMode,
    VirtualMachineScaleSetSkuScaleType,
    VirtualMachineSizeTypes,
)

__all__ = [
    'AdditionalUnattendContent',
    'ApiEntityReference',
    'ApiError',
    'ApiErrorBase',
    'AvailabilitySet',
    'AvailabilitySetListResult',
    'BootDiagnostics',
    'BootDiagnosticsInstanceView',
    'ComputeLongRunningOperationProperties',
    'DataDisk',
    'DataDiskImage',
    'DiagnosticsProfile',
    'DiskEncryptionSettings',
    'DiskInstanceView',
    'HardwareProfile',
    'ImageReference',
    'InnerError',
    'InstanceViewStatus',
    'KeyVaultKeyReference',
    'KeyVaultSecretReference',
    'LinuxConfiguration',
    'ListUsagesResult',
    'NetworkInterfaceReference',
    'NetworkProfile',
    'OSDisk',
    'OSDiskImage',
    'OSProfile',
    'OperationStatusResponse',
    'Plan',
    'PurchasePlan',
    'Resource',
    'Sku',
    'SshConfiguration',
    'SshPublicKey',
    'StorageProfile',
    'SubResource',
    'UpdateResource',
    'UpgradePolicy',
    'Usage',
    'UsageName',
    'VaultCertificate',
    'VaultSecretGroup',
    'VirtualHardDisk',
    'VirtualMachine',
    'VirtualMachineAgentInstanceView',
    'VirtualMachineCaptureParameters',
    'VirtualMachineCaptureResult',
    'VirtualMachineExtension',
    'VirtualMachineExtensionHandlerInstanceView',
    'VirtualMachineExtensionImage',
    'VirtualMachineExtensionInstanceView',
    'VirtualMachineExtensionUpdate',
    'VirtualMachineExtensionsListResult',
    'VirtualMachineIdentity',
    'VirtualMachineImage',
    'VirtualMachineImageResource',
    'VirtualMachineInstanceView',
    'VirtualMachineListResult',
    'VirtualMachineScaleSet',
    'VirtualMachineScaleSetExtension',
    'VirtualMachineScaleSetExtensionProfile',
    'VirtualMachineScaleSetIPConfiguration',
    'VirtualMachineScaleSetIdentity',
    'VirtualMachineScaleSetInstanceView',
    'VirtualMachineScaleSetInstanceViewStatusesSummary',
    'VirtualMachineScaleSetListResult',
    'VirtualMachineScaleSetListSkusResult',
    'VirtualMachineScaleSetListWithLinkResult',
    'VirtualMachineScaleSetNetworkConfiguration',
    'VirtualMachineScaleSetNetworkProfile',
    'VirtualMachineScaleSetOSDisk',
    'VirtualMachineScaleSetOSProfile',
    'VirtualMachineScaleSetSku',
    'VirtualMachineScaleSetSkuCapacity',
    'VirtualMachineScaleSetStorageProfile',
    'VirtualMachineScaleSetVM',
    'VirtualMachineScaleSetVMExtensionsSummary',
    'VirtualMachineScaleSetVMInstanceIDs',
    'VirtualMachineScaleSetVMInstanceRequiredIDs',
    'VirtualMachineScaleSetVMInstanceView',
    'VirtualMachineScaleSetVMListResult',
    'VirtualMachineScaleSetVMProfile',
    'VirtualMachineSize',
    'VirtualMachineSizeListResult',
    'VirtualMachineStatusCodeCount',
    'WinRMConfiguration',
    'WinRMListener',
    'WindowsConfiguration',
    'CachingTypes',
    'DiskCreateOptionTypes',
    'OperatingSystemTypes',
    'ProtocolTypes',
    'SettingNames',
    'StatusLevelTypes',
    'UpgradeMode',
    'VirtualMachineScaleSetSkuScaleType',
    'VirtualMachineSizeTypes',
]
