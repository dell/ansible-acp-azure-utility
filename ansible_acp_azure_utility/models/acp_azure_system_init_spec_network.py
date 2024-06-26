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

class ACPAzureSystemInitSpecNetwork(object):
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
        'host_network': 'ACPAzureSystemInitSpecNetworkHostNetwork',
        'infrastructure_network': 'list[InfrastructureNetworkSpec]'
    }

    attribute_map = {
        'host_network': 'host_network',
        'infrastructure_network': 'infrastructure_network'
    }

    def __init__(self, host_network=None, infrastructure_network=None):  # noqa: E501
        """ACPAzureSystemInitSpecNetwork - a model defined in Swagger"""  # noqa: E501
        self._host_network = None
        self._infrastructure_network = None
        self.discriminator = None
        if host_network is not None:
            self.host_network = host_network
        if infrastructure_network is not None:
            self.infrastructure_network = infrastructure_network

    @property
    def host_network(self):
        """Gets the host_network of this ACPAzureSystemInitSpecNetwork.  # noqa: E501


        :return: The host_network of this ACPAzureSystemInitSpecNetwork.  # noqa: E501
        :rtype: ACPAzureSystemInitSpecNetworkHostNetwork
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this ACPAzureSystemInitSpecNetwork.


        :param host_network: The host_network of this ACPAzureSystemInitSpecNetwork.  # noqa: E501
        :type: ACPAzureSystemInitSpecNetworkHostNetwork
        """

        self._host_network = host_network

    @property
    def infrastructure_network(self):
        """Gets the infrastructure_network of this ACPAzureSystemInitSpecNetwork.  # noqa: E501


        :return: The infrastructure_network of this ACPAzureSystemInitSpecNetwork.  # noqa: E501
        :rtype: list[InfrastructureNetworkSpec]
        """
        return self._infrastructure_network

    @infrastructure_network.setter
    def infrastructure_network(self, infrastructure_network):
        """Sets the infrastructure_network of this ACPAzureSystemInitSpecNetwork.


        :param infrastructure_network: The infrastructure_network of this ACPAzureSystemInitSpecNetwork.  # noqa: E501
        :type: list[InfrastructureNetworkSpec]
        """

        self._infrastructure_network = infrastructure_network

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
        if issubclass(ACPAzureSystemInitSpecNetwork, dict):
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
        if not isinstance(other, ACPAzureSystemInitSpecNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
