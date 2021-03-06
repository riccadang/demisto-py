# coding: utf-8

"""
    Demisto API

    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from demisto_client.demisto_api.models.argument import Argument  # noqa: F401,E501
from demisto_client.demisto_api.models.output import Output  # noqa: F401,E501
from demisto_client.demisto_api.models.script_target import ScriptTarget  # noqa: F401,E501
from demisto_client.demisto_api.models.script_type import ScriptType  # noqa: F401,E501


class AutomationScriptAPI(object):
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
        'arguments': 'list[Argument]',
        'comment': 'str',
        'context_keys': 'list[str]',
        'depends_on': 'dict(str, list[str])',
        'deprecated': 'bool',
        'docker_image': 'str',
        'enabled': 'bool',
        'hidden': 'bool',
        'id': 'str',
        'locked': 'bool',
        'modified': 'datetime',
        'name': 'str',
        'outputs': 'list[Output]',
        'permitted': 'bool',
        'roles': 'list[str]',
        'run_as': 'str',
        'script_target': 'ScriptTarget',
        'system': 'bool',
        'tags': 'list[str]',
        'type': 'ScriptType',
        'user': 'str',
        'version': 'int'
    }

    attribute_map = {
        'arguments': 'arguments',
        'comment': 'comment',
        'context_keys': 'contextKeys',
        'depends_on': 'dependsOn',
        'deprecated': 'deprecated',
        'docker_image': 'dockerImage',
        'enabled': 'enabled',
        'hidden': 'hidden',
        'id': 'id',
        'locked': 'locked',
        'modified': 'modified',
        'name': 'name',
        'outputs': 'outputs',
        'permitted': 'permitted',
        'roles': 'roles',
        'run_as': 'runAs',
        'script_target': 'scriptTarget',
        'system': 'system',
        'tags': 'tags',
        'type': 'type',
        'user': 'user',
        'version': 'version'
    }

    def __init__(self, arguments=None, comment=None, context_keys=None, depends_on=None, deprecated=None, docker_image=None, enabled=None, hidden=None, id=None, locked=None, modified=None, name=None, outputs=None, permitted=None, roles=None, run_as=None, script_target=None, system=None, tags=None, type=None, user=None, version=None):  # noqa: E501
        """AutomationScriptAPI - a model defined in Swagger"""  # noqa: E501

        self._arguments = None
        self._comment = None
        self._context_keys = None
        self._depends_on = None
        self._deprecated = None
        self._docker_image = None
        self._enabled = None
        self._hidden = None
        self._id = None
        self._locked = None
        self._modified = None
        self._name = None
        self._outputs = None
        self._permitted = None
        self._roles = None
        self._run_as = None
        self._script_target = None
        self._system = None
        self._tags = None
        self._type = None
        self._user = None
        self._version = None
        self.discriminator = None

        if arguments is not None:
            self.arguments = arguments
        if comment is not None:
            self.comment = comment
        if context_keys is not None:
            self.context_keys = context_keys
        if depends_on is not None:
            self.depends_on = depends_on
        if deprecated is not None:
            self.deprecated = deprecated
        if docker_image is not None:
            self.docker_image = docker_image
        if enabled is not None:
            self.enabled = enabled
        if hidden is not None:
            self.hidden = hidden
        if id is not None:
            self.id = id
        if locked is not None:
            self.locked = locked
        if modified is not None:
            self.modified = modified
        if name is not None:
            self.name = name
        if outputs is not None:
            self.outputs = outputs
        if permitted is not None:
            self.permitted = permitted
        if roles is not None:
            self.roles = roles
        if run_as is not None:
            self.run_as = run_as
        if script_target is not None:
            self.script_target = script_target
        if system is not None:
            self.system = system
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user
        if version is not None:
            self.version = version

    @property
    def arguments(self):
        """Gets the arguments of this AutomationScriptAPI.  # noqa: E501


        :return: The arguments of this AutomationScriptAPI.  # noqa: E501
        :rtype: list[Argument]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this AutomationScriptAPI.


        :param arguments: The arguments of this AutomationScriptAPI.  # noqa: E501
        :type: list[Argument]
        """

        self._arguments = arguments

    @property
    def comment(self):
        """Gets the comment of this AutomationScriptAPI.  # noqa: E501


        :return: The comment of this AutomationScriptAPI.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AutomationScriptAPI.


        :param comment: The comment of this AutomationScriptAPI.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def context_keys(self):
        """Gets the context_keys of this AutomationScriptAPI.  # noqa: E501


        :return: The context_keys of this AutomationScriptAPI.  # noqa: E501
        :rtype: list[str]
        """
        return self._context_keys

    @context_keys.setter
    def context_keys(self, context_keys):
        """Sets the context_keys of this AutomationScriptAPI.


        :param context_keys: The context_keys of this AutomationScriptAPI.  # noqa: E501
        :type: list[str]
        """

        self._context_keys = context_keys

    @property
    def depends_on(self):
        """Gets the depends_on of this AutomationScriptAPI.  # noqa: E501


        :return: The depends_on of this AutomationScriptAPI.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        """Sets the depends_on of this AutomationScriptAPI.


        :param depends_on: The depends_on of this AutomationScriptAPI.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._depends_on = depends_on

    @property
    def deprecated(self):
        """Gets the deprecated of this AutomationScriptAPI.  # noqa: E501


        :return: The deprecated of this AutomationScriptAPI.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this AutomationScriptAPI.


        :param deprecated: The deprecated of this AutomationScriptAPI.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def docker_image(self):
        """Gets the docker_image of this AutomationScriptAPI.  # noqa: E501


        :return: The docker_image of this AutomationScriptAPI.  # noqa: E501
        :rtype: str
        """
        return self._docker_image

    @docker_image.setter
    def docker_image(self, docker_image):
        """Sets the docker_image of this AutomationScriptAPI.


        :param docker_image: The docker_image of this AutomationScriptAPI.  # noqa: E501
        :type: str
        """

        self._docker_image = docker_image

    @property
    def enabled(self):
        """Gets the enabled of this AutomationScriptAPI.  # noqa: E501


        :return: The enabled of this AutomationScriptAPI.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AutomationScriptAPI.


        :param enabled: The enabled of this AutomationScriptAPI.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def hidden(self):
        """Gets the hidden of this AutomationScriptAPI.  # noqa: E501


        :return: The hidden of this AutomationScriptAPI.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this AutomationScriptAPI.


        :param hidden: The hidden of this AutomationScriptAPI.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def id(self):
        """Gets the id of this AutomationScriptAPI.  # noqa: E501


        :return: The id of this AutomationScriptAPI.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AutomationScriptAPI.


        :param id: The id of this AutomationScriptAPI.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def locked(self):
        """Gets the locked of this AutomationScriptAPI.  # noqa: E501


        :return: The locked of this AutomationScriptAPI.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this AutomationScriptAPI.


        :param locked: The locked of this AutomationScriptAPI.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def modified(self):
        """Gets the modified of this AutomationScriptAPI.  # noqa: E501


        :return: The modified of this AutomationScriptAPI.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this AutomationScriptAPI.


        :param modified: The modified of this AutomationScriptAPI.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this AutomationScriptAPI.  # noqa: E501


        :return: The name of this AutomationScriptAPI.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AutomationScriptAPI.


        :param name: The name of this AutomationScriptAPI.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def outputs(self):
        """Gets the outputs of this AutomationScriptAPI.  # noqa: E501


        :return: The outputs of this AutomationScriptAPI.  # noqa: E501
        :rtype: list[Output]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this AutomationScriptAPI.


        :param outputs: The outputs of this AutomationScriptAPI.  # noqa: E501
        :type: list[Output]
        """

        self._outputs = outputs

    @property
    def permitted(self):
        """Gets the permitted of this AutomationScriptAPI.  # noqa: E501


        :return: The permitted of this AutomationScriptAPI.  # noqa: E501
        :rtype: bool
        """
        return self._permitted

    @permitted.setter
    def permitted(self, permitted):
        """Sets the permitted of this AutomationScriptAPI.


        :param permitted: The permitted of this AutomationScriptAPI.  # noqa: E501
        :type: bool
        """

        self._permitted = permitted

    @property
    def roles(self):
        """Gets the roles of this AutomationScriptAPI.  # noqa: E501


        :return: The roles of this AutomationScriptAPI.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AutomationScriptAPI.


        :param roles: The roles of this AutomationScriptAPI.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def run_as(self):
        """Gets the run_as of this AutomationScriptAPI.  # noqa: E501


        :return: The run_as of this AutomationScriptAPI.  # noqa: E501
        :rtype: str
        """
        return self._run_as

    @run_as.setter
    def run_as(self, run_as):
        """Sets the run_as of this AutomationScriptAPI.


        :param run_as: The run_as of this AutomationScriptAPI.  # noqa: E501
        :type: str
        """

        self._run_as = run_as

    @property
    def script_target(self):
        """Gets the script_target of this AutomationScriptAPI.  # noqa: E501


        :return: The script_target of this AutomationScriptAPI.  # noqa: E501
        :rtype: ScriptTarget
        """
        return self._script_target

    @script_target.setter
    def script_target(self, script_target):
        """Sets the script_target of this AutomationScriptAPI.


        :param script_target: The script_target of this AutomationScriptAPI.  # noqa: E501
        :type: ScriptTarget
        """

        self._script_target = script_target

    @property
    def system(self):
        """Gets the system of this AutomationScriptAPI.  # noqa: E501


        :return: The system of this AutomationScriptAPI.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this AutomationScriptAPI.


        :param system: The system of this AutomationScriptAPI.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def tags(self):
        """Gets the tags of this AutomationScriptAPI.  # noqa: E501


        :return: The tags of this AutomationScriptAPI.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AutomationScriptAPI.


        :param tags: The tags of this AutomationScriptAPI.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this AutomationScriptAPI.  # noqa: E501


        :return: The type of this AutomationScriptAPI.  # noqa: E501
        :rtype: ScriptType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AutomationScriptAPI.


        :param type: The type of this AutomationScriptAPI.  # noqa: E501
        :type: ScriptType
        """

        self._type = type

    @property
    def user(self):
        """Gets the user of this AutomationScriptAPI.  # noqa: E501


        :return: The user of this AutomationScriptAPI.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AutomationScriptAPI.


        :param user: The user of this AutomationScriptAPI.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def version(self):
        """Gets the version of this AutomationScriptAPI.  # noqa: E501


        :return: The version of this AutomationScriptAPI.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AutomationScriptAPI.


        :param version: The version of this AutomationScriptAPI.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(AutomationScriptAPI, dict):
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
        if not isinstance(other, AutomationScriptAPI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
