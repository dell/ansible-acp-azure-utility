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

class AccessRefreshTokenInfo(object):
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
        'access_token': 'str',
        'refresh_token': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'refresh_token': 'refresh_token'
    }

    def __init__(self, access_token=None, refresh_token=None):  # noqa: E501
        """AccessRefreshTokenInfo - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._refresh_token = None
        self.discriminator = None
        self.access_token = access_token
        self.refresh_token = refresh_token

    @property
    def access_token(self):
        """Gets the access_token of this AccessRefreshTokenInfo.  # noqa: E501

        The access token  # noqa: E501

        :return: The access_token of this AccessRefreshTokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this AccessRefreshTokenInfo.

        The access token  # noqa: E501

        :param access_token: The access_token of this AccessRefreshTokenInfo.  # noqa: E501
        :type: str
        """
        if access_token is None:
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def refresh_token(self):
        """Gets the refresh_token of this AccessRefreshTokenInfo.  # noqa: E501

        The refresh token  # noqa: E501

        :return: The refresh_token of this AccessRefreshTokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this AccessRefreshTokenInfo.

        The refresh token  # noqa: E501

        :param refresh_token: The refresh_token of this AccessRefreshTokenInfo.  # noqa: E501
        :type: str
        """
        if refresh_token is None:
            raise ValueError("Invalid value for `refresh_token`, must not be `None`")  # noqa: E501

        self._refresh_token = refresh_token

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
        if issubclass(AccessRefreshTokenInfo, dict):
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
        if not isinstance(other, AccessRefreshTokenInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other