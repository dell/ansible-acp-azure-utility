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

class IPPoolsSpec(object):
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
        'starting_address': 'str',
        'ending_address': 'str'
    }

    attribute_map = {
        'starting_address': 'starting_address',
        'ending_address': 'ending_address'
    }

    def __init__(self, starting_address=None, ending_address=None):  # noqa: E501
        """IPPoolsSpec - a model defined in Swagger"""  # noqa: E501
        self._starting_address = None
        self._ending_address = None
        self.discriminator = None
        if starting_address is not None:
            self.starting_address = starting_address
        if ending_address is not None:
            self.ending_address = ending_address

    @property
    def starting_address(self):
        """Gets the starting_address of this IPPoolsSpec.  # noqa: E501

        Provide the starting IP for the management network. A minimum of 1 free, contiguous IPv4 addresses (excluding your host IPs) are needed for infrastructure services such as clustering. Cluster IP will use the first IP of the range.  # noqa: E501

        :return: The starting_address of this IPPoolsSpec.  # noqa: E501
        :rtype: str
        """
        return self._starting_address

    @starting_address.setter
    def starting_address(self, starting_address):
        """Sets the starting_address of this IPPoolsSpec.

        Provide the starting IP for the management network. A minimum of 1 free, contiguous IPv4 addresses (excluding your host IPs) are needed for infrastructure services such as clustering. Cluster IP will use the first IP of the range.  # noqa: E501

        :param starting_address: The starting_address of this IPPoolsSpec.  # noqa: E501
        :type: str
        """

        self._starting_address = starting_address

    @property
    def ending_address(self):
        """Gets the ending_address of this IPPoolsSpec.  # noqa: E501

        Provide the ending IP for the management network. A minimum of 1 free, contiguous IPv4 addresses (excluding your host IPs) are needed for infrastructure services such as clustering.  # noqa: E501

        :return: The ending_address of this IPPoolsSpec.  # noqa: E501
        :rtype: str
        """
        return self._ending_address

    @ending_address.setter
    def ending_address(self, ending_address):
        """Sets the ending_address of this IPPoolsSpec.

        Provide the ending IP for the management network. A minimum of 1 free, contiguous IPv4 addresses (excluding your host IPs) are needed for infrastructure services such as clustering.  # noqa: E501

        :param ending_address: The ending_address of this IPPoolsSpec.  # noqa: E501
        :type: str
        """

        self._ending_address = ending_address

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
        if issubclass(IPPoolsSpec, dict):
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
        if not isinstance(other, IPPoolsSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other