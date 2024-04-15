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

class SystemInitRequestValidationInfo(object):
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
        'cursory': 'SystemInitRequestValidationInfoCursory',
        'thorough': 'SystemInitRequestValidationInfoCursory'
    }

    attribute_map = {
        'cursory': 'cursory',
        'thorough': 'thorough'
    }

    def __init__(self, cursory=None, thorough=None):  # noqa: E501
        """SystemInitRequestValidationInfo - a model defined in Swagger"""  # noqa: E501
        self._cursory = None
        self._thorough = None
        self.discriminator = None
        self.cursory = cursory
        self.thorough = thorough

    @property
    def cursory(self):
        """Gets the cursory of this SystemInitRequestValidationInfo.  # noqa: E501


        :return: The cursory of this SystemInitRequestValidationInfo.  # noqa: E501
        :rtype: SystemInitRequestValidationInfoCursory
        """
        return self._cursory

    @cursory.setter
    def cursory(self, cursory):
        """Sets the cursory of this SystemInitRequestValidationInfo.


        :param cursory: The cursory of this SystemInitRequestValidationInfo.  # noqa: E501
        :type: SystemInitRequestValidationInfoCursory
        """
        if cursory is None:
            raise ValueError("Invalid value for `cursory`, must not be `None`")  # noqa: E501

        self._cursory = cursory

    @property
    def thorough(self):
        """Gets the thorough of this SystemInitRequestValidationInfo.  # noqa: E501


        :return: The thorough of this SystemInitRequestValidationInfo.  # noqa: E501
        :rtype: SystemInitRequestValidationInfoCursory
        """
        return self._thorough

    @thorough.setter
    def thorough(self, thorough):
        """Sets the thorough of this SystemInitRequestValidationInfo.


        :param thorough: The thorough of this SystemInitRequestValidationInfo.  # noqa: E501
        :type: SystemInitRequestValidationInfoCursory
        """
        if thorough is None:
            raise ValueError("Invalid value for `thorough`, must not be `None`")  # noqa: E501

        self._thorough = thorough

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
        if issubclass(SystemInitRequestValidationInfo, dict):
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
        if not isinstance(other, SystemInitRequestValidationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other