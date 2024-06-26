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

class TypedAccountSpec(object):
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
        'type': 'str',
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'type': 'type',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, type=None, username=None, password=None):  # noqa: E501
        """TypedAccountSpec - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._username = None
        self._password = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

    @property
    def type(self):
        """Gets the type of this TypedAccountSpec.  # noqa: E501

        account type.  # noqa: E501

        :return: The type of this TypedAccountSpec.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TypedAccountSpec.

        account type.  # noqa: E501

        :param type: The type of this TypedAccountSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["MANAGEMENT", "ROOT", "SERVICE", "ADMIN", "WAC_GATEWAY_ADMINISTRATOR"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def username(self):
        """Gets the username of this TypedAccountSpec.  # noqa: E501

        Account username  # noqa: E501

        :return: The username of this TypedAccountSpec.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TypedAccountSpec.

        Account username  # noqa: E501

        :param username: The username of this TypedAccountSpec.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this TypedAccountSpec.  # noqa: E501

        Account password  # noqa: E501

        :return: The password of this TypedAccountSpec.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TypedAccountSpec.

        Account password  # noqa: E501

        :param password: The password of this TypedAccountSpec.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(TypedAccountSpec, dict):
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
        if not isinstance(other, TypedAccountSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
