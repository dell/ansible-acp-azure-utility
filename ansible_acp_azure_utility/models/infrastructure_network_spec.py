# coding: utf-8

"""
    Dell APEX Cloud Platform for Microsoft Azure REST API

    Dell APEX Cloud Platform REST API provides a programmatic interface for performing administrative tasks on Dell APEX Cloud Platform for Microsoft Azure. The data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 1.0.000
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InfrastructureNetworkSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'subnet_mask': 'str',
        'vlan_id': 'int',
        'gateway': 'str',
        'ip_pools': 'list[IPPoolsSpec]'
    }

    attribute_map = {
        'subnet_mask': 'subnet_mask',
        'vlan_id': 'vlan_id',
        'gateway': 'gateway',
        'ip_pools': 'ip_pools'
    }

    def __init__(self, subnet_mask=None, vlan_id=None, gateway=None, ip_pools=None):  # noqa: E501
        """InfrastructureNetworkSpec - a model defined in Swagger"""  # noqa: E501
        self._subnet_mask = None
        self._vlan_id = None
        self._gateway = None
        self._ip_pools = None
        self.discriminator = None
        if subnet_mask is not None:
            self.subnet_mask = subnet_mask
        if vlan_id is not None:
            self.vlan_id = vlan_id
        if gateway is not None:
            self.gateway = gateway
        if ip_pools is not None:
            self.ip_pools = ip_pools

    @property
    def subnet_mask(self):
        """Gets the subnet_mask of this InfrastructureNetworkSpec.  # noqa: E501

        Subnet mask that matches the provided IP address space.  # noqa: E501

        :return: The subnet_mask of this InfrastructureNetworkSpec.  # noqa: E501
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        """Sets the subnet_mask of this InfrastructureNetworkSpec.

        Subnet mask that matches the provided IP address space.  # noqa: E501

        :param subnet_mask: The subnet_mask of this InfrastructureNetworkSpec.  # noqa: E501
        :type: str
        """

        self._subnet_mask = subnet_mask

    @property
    def vlan_id(self):
        """Gets the vlan_id of this InfrastructureNetworkSpec.  # noqa: E501

        The Vlan ID is specified for the infrastructure network.  # noqa: E501

        :return: The vlan_id of this InfrastructureNetworkSpec.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this InfrastructureNetworkSpec.

        The Vlan ID is specified for the infrastructure network.  # noqa: E501

        :param vlan_id: The vlan_id of this InfrastructureNetworkSpec.  # noqa: E501
        :type: int
        """

        self._vlan_id = vlan_id

    @property
    def gateway(self):
        """Gets the gateway of this InfrastructureNetworkSpec.  # noqa: E501

        Default Gateway that should be used for the provided IP address space.  # noqa: E501

        :return: The gateway of this InfrastructureNetworkSpec.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this InfrastructureNetworkSpec.

        Default Gateway that should be used for the provided IP address space.  # noqa: E501

        :param gateway: The gateway of this InfrastructureNetworkSpec.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def ip_pools(self):
        """Gets the ip_pools of this InfrastructureNetworkSpec.  # noqa: E501


        :return: The ip_pools of this InfrastructureNetworkSpec.  # noqa: E501
        :rtype: list[IPPoolsSpec]
        """
        return self._ip_pools

    @ip_pools.setter
    def ip_pools(self, ip_pools):
        """Sets the ip_pools of this InfrastructureNetworkSpec.


        :param ip_pools: The ip_pools of this InfrastructureNetworkSpec.  # noqa: E501
        :type: list[IPPoolsSpec]
        """

        self._ip_pools = ip_pools

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InfrastructureNetworkSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InfrastructureNetworkSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
