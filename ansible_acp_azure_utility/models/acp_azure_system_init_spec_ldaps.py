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

class ACPAzureSystemInitSpecLdaps(object):
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
        'fqdn': 'str',
        'port': 'int'
    }

    attribute_map = {
        'fqdn': 'fqdn',
        'port': 'port'
    }

    def __init__(self, fqdn=None, port=None):  # noqa: E501
        """ACPAzureSystemInitSpecLdaps - a model defined in Swagger"""  # noqa: E501
        self._fqdn = None
        self._port = None
        self.discriminator = None
        if fqdn is not None:
            self.fqdn = fqdn
        if port is not None:
            self.port = port

    @property
    def fqdn(self):
        """Gets the fqdn of this ACPAzureSystemInitSpecLdaps.  # noqa: E501

        The Fully Qualified Domain Name (FQDN) of the LDAP server.  # noqa: E501

        :return: The fqdn of this ACPAzureSystemInitSpecLdaps.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this ACPAzureSystemInitSpecLdaps.

        The Fully Qualified Domain Name (FQDN) of the LDAP server.  # noqa: E501

        :param fqdn: The fqdn of this ACPAzureSystemInitSpecLdaps.  # noqa: E501
        :type: str
        """

        self._fqdn = fqdn

    @property
    def port(self):
        """Gets the port of this ACPAzureSystemInitSpecLdaps.  # noqa: E501

        The LDAP port number.  # noqa: E501

        :return: The port of this ACPAzureSystemInitSpecLdaps.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ACPAzureSystemInitSpecLdaps.

        The LDAP port number.  # noqa: E501

        :param port: The port of this ACPAzureSystemInitSpecLdaps.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if issubclass(ACPAzureSystemInitSpecLdaps, dict):
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
        if not isinstance(other, ACPAzureSystemInitSpecLdaps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
