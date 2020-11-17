# Generated with https://app.quicktype.io/
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = node_info_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class MrfObjectAge:
    actions: List[str]
    threshold: int

    @staticmethod
    def from_dict(obj: Any) -> 'MrfObjectAge':
        assert isinstance(obj, dict)
        actions = from_list(from_str, obj.get("actions"))
        threshold = from_int(obj.get("threshold"))
        return MrfObjectAge(actions, threshold)

    def to_dict(self) -> dict:
        result: dict = {}
        result["actions"] = from_list(from_str, self.actions)
        result["threshold"] = from_int(self.threshold)
        return result


@dataclass
class MrfSimple:
    accept: List[Any]
    avatar_removal: List[Any]
    banner_removal: List[Any]
    federated_timeline_removal: List[Any]
    followers_only: List[Any]
    media_nsfw: List[Any]
    media_removal: List[Any]
    reject: List[str]
    reject_deletes: List[Any]
    report_removal: List[Any]

    @staticmethod
    def from_dict(obj: Any) -> 'MrfSimple':
        assert isinstance(obj, dict)
        accept = from_list(lambda x: x, obj.get("accept"))
        avatar_removal = from_list(lambda x: x, obj.get("avatar_removal"))
        banner_removal = from_list(lambda x: x, obj.get("banner_removal"))
        federated_timeline_removal = from_list(lambda x: x, obj.get("federated_timeline_removal"))
        followers_only = from_list(lambda x: x, obj.get("followers_only"))
        media_nsfw = from_list(lambda x: x, obj.get("media_nsfw"))
        media_removal = from_list(lambda x: x, obj.get("media_removal"))
        reject = from_list(from_str, obj.get("reject"))
        reject_deletes = from_list(lambda x: x, obj.get("reject_deletes"))
        report_removal = from_list(lambda x: x, obj.get("report_removal"))
        return MrfSimple(accept, avatar_removal, banner_removal, federated_timeline_removal, followers_only, media_nsfw, media_removal, reject, reject_deletes, report_removal)

    def to_dict(self) -> dict:
        result: dict = {}
        result["accept"] = from_list(lambda x: x, self.accept)
        result["avatar_removal"] = from_list(lambda x: x, self.avatar_removal)
        result["banner_removal"] = from_list(lambda x: x, self.banner_removal)
        result["federated_timeline_removal"] = from_list(lambda x: x, self.federated_timeline_removal)
        result["followers_only"] = from_list(lambda x: x, self.followers_only)
        result["media_nsfw"] = from_list(lambda x: x, self.media_nsfw)
        result["media_removal"] = from_list(lambda x: x, self.media_removal)
        result["reject"] = from_list(from_str, self.reject)
        result["reject_deletes"] = from_list(lambda x: x, self.reject_deletes)
        result["report_removal"] = from_list(lambda x: x, self.report_removal)
        return result


@dataclass
class Federation:
    enabled: bool
    exclusions: bool
    mrf_object_age: MrfObjectAge
    mrf_policies: List[str]
    mrf_simple: MrfSimple
    quarantined_instances: List[Any]

    @staticmethod
    def from_dict(obj: Any) -> 'Federation':
        assert isinstance(obj, dict)
        enabled = from_bool(obj.get("enabled"))
        exclusions = from_bool(obj.get("exclusions"))
        mrf_object_age = MrfObjectAge.from_dict(obj.get("mrf_object_age"))
        mrf_policies = from_list(from_str, obj.get("mrf_policies"))
        mrf_simple = MrfSimple.from_dict(obj.get("mrf_simple"))
        quarantined_instances = from_list(lambda x: x, obj.get("quarantined_instances"))
        return Federation(enabled, exclusions, mrf_object_age, mrf_policies, mrf_simple, quarantined_instances)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enabled"] = from_bool(self.enabled)
        result["exclusions"] = from_bool(self.exclusions)
        result["mrf_object_age"] = to_class(MrfObjectAge, self.mrf_object_age)
        result["mrf_policies"] = from_list(from_str, self.mrf_policies)
        result["mrf_simple"] = to_class(MrfSimple, self.mrf_simple)
        result["quarantined_instances"] = from_list(lambda x: x, self.quarantined_instances)
        return result


@dataclass
class FieldsLimits:
    max_fields: int
    max_remote_fields: int
    name_length: int
    value_length: int

    @staticmethod
    def from_dict(obj: Any) -> 'FieldsLimits':
        assert isinstance(obj, dict)
        max_fields = from_int(obj.get("maxFields"))
        max_remote_fields = from_int(obj.get("maxRemoteFields"))
        name_length = from_int(obj.get("nameLength"))
        value_length = from_int(obj.get("valueLength"))
        return FieldsLimits(max_fields, max_remote_fields, name_length, value_length)

    def to_dict(self) -> dict:
        result: dict = {}
        result["maxFields"] = from_int(self.max_fields)
        result["maxRemoteFields"] = from_int(self.max_remote_fields)
        result["nameLength"] = from_int(self.name_length)
        result["valueLength"] = from_int(self.value_length)
        return result


@dataclass
class PollLimits:
    max_expiration: int
    max_option_chars: int
    max_options: int
    min_expiration: int

    @staticmethod
    def from_dict(obj: Any) -> 'PollLimits':
        assert isinstance(obj, dict)
        max_expiration = from_int(obj.get("max_expiration"))
        max_option_chars = from_int(obj.get("max_option_chars"))
        max_options = from_int(obj.get("max_options"))
        min_expiration = from_int(obj.get("min_expiration"))
        return PollLimits(max_expiration, max_option_chars, max_options, min_expiration)

    def to_dict(self) -> dict:
        result: dict = {}
        result["max_expiration"] = from_int(self.max_expiration)
        result["max_option_chars"] = from_int(self.max_option_chars)
        result["max_options"] = from_int(self.max_options)
        result["min_expiration"] = from_int(self.min_expiration)
        return result


@dataclass
class Suggestions:
    enabled: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Suggestions':
        assert isinstance(obj, dict)
        enabled = from_bool(obj.get("enabled"))
        return Suggestions(enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enabled"] = from_bool(self.enabled)
        return result


@dataclass
class UploadLimits:
    avatar: int
    background: int
    banner: int
    general: int

    @staticmethod
    def from_dict(obj: Any) -> 'UploadLimits':
        assert isinstance(obj, dict)
        avatar = from_int(obj.get("avatar"))
        background = from_int(obj.get("background"))
        banner = from_int(obj.get("banner"))
        general = from_int(obj.get("general"))
        return UploadLimits(avatar, background, banner, general)

    def to_dict(self) -> dict:
        result: dict = {}
        result["avatar"] = from_int(self.avatar)
        result["background"] = from_int(self.background)
        result["banner"] = from_int(self.banner)
        result["general"] = from_int(self.general)
        return result


@dataclass
class Metadata:
    account_activation_required: bool
    features: List[str]
    federation: Federation
    fields_limits: FieldsLimits
    invites_enabled: bool
    mailer_enabled: bool
    node_description: str
    node_name: str
    poll_limits: PollLimits
    post_formats: List[str]
    private: bool
    restricted_nicknames: List[str]
    skip_thread_containment: bool
    staff_accounts: List[str]
    suggestions: Suggestions
    upload_limits: UploadLimits

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        assert isinstance(obj, dict)
        account_activation_required = from_bool(obj.get("accountActivationRequired"))
        features = from_list(from_str, obj.get("features"))
        federation = Federation.from_dict(obj.get("federation"))
        fields_limits = FieldsLimits.from_dict(obj.get("fieldsLimits"))
        invites_enabled = from_bool(obj.get("invitesEnabled"))
        mailer_enabled = from_bool(obj.get("mailerEnabled"))
        node_description = from_str(obj.get("nodeDescription"))
        node_name = from_str(obj.get("nodeName"))
        poll_limits = PollLimits.from_dict(obj.get("pollLimits"))
        post_formats = from_list(from_str, obj.get("postFormats"))
        private = from_bool(obj.get("private"))
        restricted_nicknames = from_list(from_str, obj.get("restrictedNicknames"))
        skip_thread_containment = from_bool(obj.get("skipThreadContainment"))
        staff_accounts = from_list(from_str, obj.get("staffAccounts"))
        suggestions = Suggestions.from_dict(obj.get("suggestions"))
        upload_limits = UploadLimits.from_dict(obj.get("uploadLimits"))
        return Metadata(account_activation_required, features, federation, fields_limits, invites_enabled, mailer_enabled, node_description, node_name, poll_limits, post_formats, private, restricted_nicknames, skip_thread_containment, staff_accounts, suggestions, upload_limits)

    def to_dict(self) -> dict:
        result: dict = {}
        result["accountActivationRequired"] = from_bool(self.account_activation_required)
        result["features"] = from_list(from_str, self.features)
        result["federation"] = to_class(Federation, self.federation)
        result["fieldsLimits"] = to_class(FieldsLimits, self.fields_limits)
        result["invitesEnabled"] = from_bool(self.invites_enabled)
        result["mailerEnabled"] = from_bool(self.mailer_enabled)
        result["nodeDescription"] = from_str(self.node_description)
        result["nodeName"] = from_str(self.node_name)
        result["pollLimits"] = to_class(PollLimits, self.poll_limits)
        result["postFormats"] = from_list(from_str, self.post_formats)
        result["private"] = from_bool(self.private)
        result["restrictedNicknames"] = from_list(from_str, self.restricted_nicknames)
        result["skipThreadContainment"] = from_bool(self.skip_thread_containment)
        result["staffAccounts"] = from_list(from_str, self.staff_accounts)
        result["suggestions"] = to_class(Suggestions, self.suggestions)
        result["uploadLimits"] = to_class(UploadLimits, self.upload_limits)
        return result


@dataclass
class Services:
    inbound: List[Any]
    outbound: List[Any]

    @staticmethod
    def from_dict(obj: Any) -> 'Services':
        assert isinstance(obj, dict)
        inbound = from_list(lambda x: x, obj.get("inbound"))
        outbound = from_list(lambda x: x, obj.get("outbound"))
        return Services(inbound, outbound)

    def to_dict(self) -> dict:
        result: dict = {}
        result["inbound"] = from_list(lambda x: x, self.inbound)
        result["outbound"] = from_list(lambda x: x, self.outbound)
        return result


@dataclass
class Software:
    name: str
    repository: str
    version: str

    @staticmethod
    def from_dict(obj: Any) -> 'Software':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        repository = from_str(obj.get("repository"))
        version = from_str(obj.get("version"))
        return Software(name, repository, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["repository"] = from_str(self.repository)
        result["version"] = from_str(self.version)
        return result


@dataclass
class Users:
    total: int

    @staticmethod
    def from_dict(obj: Any) -> 'Users':
        assert isinstance(obj, dict)
        total = from_int(obj.get("total"))
        return Users(total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["total"] = from_int(self.total)
        return result


@dataclass
class Usage:
    local_posts: int
    users: Users

    @staticmethod
    def from_dict(obj: Any) -> 'Usage':
        assert isinstance(obj, dict)
        local_posts = from_int(obj.get("localPosts"))
        users = Users.from_dict(obj.get("users"))
        return Usage(local_posts, users)

    def to_dict(self) -> dict:
        result: dict = {}
        result["localPosts"] = from_int(self.local_posts)
        result["users"] = to_class(Users, self.users)
        return result


@dataclass
class NodeInfo:
    metadata: Metadata
    open_registrations: bool
    protocols: List[str]
    services: Services
    software: Software
    usage: Usage
    version: str

    @staticmethod
    def from_dict(obj: Any) -> 'NodeInfo':
        assert isinstance(obj, dict)
        metadata = Metadata.from_dict(obj.get("metadata"))
        open_registrations = from_bool(obj.get("openRegistrations"))
        protocols = from_list(from_str, obj.get("protocols"))
        services = Services.from_dict(obj.get("services"))
        software = Software.from_dict(obj.get("software"))
        usage = Usage.from_dict(obj.get("usage"))
        version = from_str(obj.get("version"))
        return NodeInfo(metadata, open_registrations, protocols, services, software, usage, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["metadata"] = to_class(Metadata, self.metadata)
        result["openRegistrations"] = from_bool(self.open_registrations)
        result["protocols"] = from_list(from_str, self.protocols)
        result["services"] = to_class(Services, self.services)
        result["software"] = to_class(Software, self.software)
        result["usage"] = to_class(Usage, self.usage)
        result["version"] = from_str(self.version)
        return result


def node_info_from_dict(s: Any) -> NodeInfo:
    return NodeInfo.from_dict(s)


def node_info_to_dict(x: NodeInfo) -> Any:
    return to_class(NodeInfo, x)
