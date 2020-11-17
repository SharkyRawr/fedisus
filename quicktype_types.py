# Generated with https://app.quicktype.io/
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = node_info20_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


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
    actions: Optional[List[str]] = None
    threshold: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MrfObjectAge':
        assert isinstance(obj, dict)
        actions = from_union([lambda x: from_list(from_str, x), from_none], obj.get("actions"))
        threshold = from_union([from_int, from_none], obj.get("threshold"))
        return MrfObjectAge(actions, threshold)

    def to_dict(self) -> dict:
        result: dict = {}
        result["actions"] = from_union([lambda x: from_list(from_str, x), from_none], self.actions)
        result["threshold"] = from_union([from_int, from_none], self.threshold)
        return result


@dataclass
class MrfSimple:
    accept: Optional[List[Any]] = None
    avatar_removal: Optional[List[Any]] = None
    banner_removal: Optional[List[Any]] = None
    federated_timeline_removal: Optional[List[Any]] = None
    followers_only: Optional[List[Any]] = None
    media_nsfw: Optional[List[Any]] = None
    media_removal: Optional[List[Any]] = None
    reject: Optional[List[str]] = None
    reject_deletes: Optional[List[Any]] = None
    report_removal: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MrfSimple':
        assert isinstance(obj, dict)
        accept = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("accept"))
        avatar_removal = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("avatar_removal"))
        banner_removal = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("banner_removal"))
        federated_timeline_removal = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("federated_timeline_removal"))
        followers_only = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("followers_only"))
        media_nsfw = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("media_nsfw"))
        media_removal = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("media_removal"))
        reject = from_union([lambda x: from_list(from_str, x), from_none], obj.get("reject"))
        reject_deletes = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("reject_deletes"))
        report_removal = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("report_removal"))
        return MrfSimple(accept, avatar_removal, banner_removal, federated_timeline_removal, followers_only, media_nsfw, media_removal, reject, reject_deletes, report_removal)

    def to_dict(self) -> dict:
        result: dict = {}
        result["accept"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.accept)
        result["avatar_removal"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.avatar_removal)
        result["banner_removal"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.banner_removal)
        result["federated_timeline_removal"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.federated_timeline_removal)
        result["followers_only"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.followers_only)
        result["media_nsfw"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.media_nsfw)
        result["media_removal"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.media_removal)
        result["reject"] = from_union([lambda x: from_list(from_str, x), from_none], self.reject)
        result["reject_deletes"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.reject_deletes)
        result["report_removal"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.report_removal)
        return result


@dataclass
class Federation:
    enabled: Optional[bool] = None
    exclusions: Optional[bool] = None
    mrf_object_age: Optional[MrfObjectAge] = None
    mrf_policies: Optional[List[str]] = None
    mrf_simple: Optional[MrfSimple] = None
    quarantined_instances: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Federation':
        assert isinstance(obj, dict)
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        exclusions = from_union([from_bool, from_none], obj.get("exclusions"))
        mrf_object_age = from_union([MrfObjectAge.from_dict, from_none], obj.get("mrf_object_age"))
        mrf_policies = from_union([lambda x: from_list(from_str, x), from_none], obj.get("mrf_policies"))
        mrf_simple = from_union([MrfSimple.from_dict, from_none], obj.get("mrf_simple"))
        quarantined_instances = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("quarantined_instances"))
        return Federation(enabled, exclusions, mrf_object_age, mrf_policies, mrf_simple, quarantined_instances)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enabled"] = from_union([from_bool, from_none], self.enabled)
        result["exclusions"] = from_union([from_bool, from_none], self.exclusions)
        result["mrf_object_age"] = from_union([lambda x: to_class(MrfObjectAge, x), from_none], self.mrf_object_age)
        result["mrf_policies"] = from_union([lambda x: from_list(from_str, x), from_none], self.mrf_policies)
        result["mrf_simple"] = from_union([lambda x: to_class(MrfSimple, x), from_none], self.mrf_simple)
        result["quarantined_instances"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.quarantined_instances)
        return result


@dataclass
class FieldsLimits:
    max_fields: Optional[int] = None
    max_remote_fields: Optional[int] = None
    name_length: Optional[int] = None
    value_length: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FieldsLimits':
        assert isinstance(obj, dict)
        max_fields = from_union([from_int, from_none], obj.get("maxFields"))
        max_remote_fields = from_union([from_int, from_none], obj.get("maxRemoteFields"))
        name_length = from_union([from_int, from_none], obj.get("nameLength"))
        value_length = from_union([from_int, from_none], obj.get("valueLength"))
        return FieldsLimits(max_fields, max_remote_fields, name_length, value_length)

    def to_dict(self) -> dict:
        result: dict = {}
        result["maxFields"] = from_union([from_int, from_none], self.max_fields)
        result["maxRemoteFields"] = from_union([from_int, from_none], self.max_remote_fields)
        result["nameLength"] = from_union([from_int, from_none], self.name_length)
        result["valueLength"] = from_union([from_int, from_none], self.value_length)
        return result


@dataclass
class PollLimits:
    max_expiration: Optional[int] = None
    max_option_chars: Optional[int] = None
    max_options: Optional[int] = None
    min_expiration: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PollLimits':
        assert isinstance(obj, dict)
        max_expiration = from_union([from_int, from_none], obj.get("max_expiration"))
        max_option_chars = from_union([from_int, from_none], obj.get("max_option_chars"))
        max_options = from_union([from_int, from_none], obj.get("max_options"))
        min_expiration = from_union([from_int, from_none], obj.get("min_expiration"))
        return PollLimits(max_expiration, max_option_chars, max_options, min_expiration)

    def to_dict(self) -> dict:
        result: dict = {}
        result["max_expiration"] = from_union([from_int, from_none], self.max_expiration)
        result["max_option_chars"] = from_union([from_int, from_none], self.max_option_chars)
        result["max_options"] = from_union([from_int, from_none], self.max_options)
        result["min_expiration"] = from_union([from_int, from_none], self.min_expiration)
        return result


@dataclass
class Suggestions:
    enabled: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Suggestions':
        assert isinstance(obj, dict)
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        return Suggestions(enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enabled"] = from_union([from_bool, from_none], self.enabled)
        return result


@dataclass
class UploadLimits:
    avatar: Optional[int] = None
    background: Optional[int] = None
    banner: Optional[int] = None
    general: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UploadLimits':
        assert isinstance(obj, dict)
        avatar = from_union([from_int, from_none], obj.get("avatar"))
        background = from_union([from_int, from_none], obj.get("background"))
        banner = from_union([from_int, from_none], obj.get("banner"))
        general = from_union([from_int, from_none], obj.get("general"))
        return UploadLimits(avatar, background, banner, general)

    def to_dict(self) -> dict:
        result: dict = {}
        result["avatar"] = from_union([from_int, from_none], self.avatar)
        result["background"] = from_union([from_int, from_none], self.background)
        result["banner"] = from_union([from_int, from_none], self.banner)
        result["general"] = from_union([from_int, from_none], self.general)
        return result


@dataclass
class Metadata:
    account_activation_required: Optional[bool] = None
    features: Optional[List[str]] = None
    federation: Optional[Federation] = None
    fields_limits: Optional[FieldsLimits] = None
    invites_enabled: Optional[bool] = None
    mailer_enabled: Optional[bool] = None
    node_description: Optional[str] = None
    node_name: Optional[str] = None
    poll_limits: Optional[PollLimits] = None
    post_formats: Optional[List[str]] = None
    private: Optional[bool] = None
    restricted_nicknames: Optional[List[str]] = None
    skip_thread_containment: Optional[bool] = None
    staff_accounts: Optional[List[str]] = None
    suggestions: Optional[Suggestions] = None
    upload_limits: Optional[UploadLimits] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        assert isinstance(obj, dict)
        account_activation_required = from_union([from_bool, from_none], obj.get("accountActivationRequired"))
        features = from_union([lambda x: from_list(from_str, x), from_none], obj.get("features"))
        federation = from_union([Federation.from_dict, from_none], obj.get("federation"))
        fields_limits = from_union([FieldsLimits.from_dict, from_none], obj.get("fieldsLimits"))
        invites_enabled = from_union([from_bool, from_none], obj.get("invitesEnabled"))
        mailer_enabled = from_union([from_bool, from_none], obj.get("mailerEnabled"))
        node_description = from_union([from_str, from_none], obj.get("nodeDescription"))
        node_name = from_union([from_str, from_none], obj.get("nodeName"))
        poll_limits = from_union([PollLimits.from_dict, from_none], obj.get("pollLimits"))
        post_formats = from_union([lambda x: from_list(from_str, x), from_none], obj.get("postFormats"))
        private = from_union([from_bool, from_none], obj.get("private"))
        restricted_nicknames = from_union([lambda x: from_list(from_str, x), from_none], obj.get("restrictedNicknames"))
        skip_thread_containment = from_union([from_bool, from_none], obj.get("skipThreadContainment"))
        staff_accounts = from_union([lambda x: from_list(from_str, x), from_none], obj.get("staffAccounts"))
        suggestions = from_union([Suggestions.from_dict, from_none], obj.get("suggestions"))
        upload_limits = from_union([UploadLimits.from_dict, from_none], obj.get("uploadLimits"))
        return Metadata(account_activation_required, features, federation, fields_limits, invites_enabled, mailer_enabled, node_description, node_name, poll_limits, post_formats, private, restricted_nicknames, skip_thread_containment, staff_accounts, suggestions, upload_limits)

    def to_dict(self) -> dict:
        result: dict = {}
        result["accountActivationRequired"] = from_union([from_bool, from_none], self.account_activation_required)
        result["features"] = from_union([lambda x: from_list(from_str, x), from_none], self.features)
        result["federation"] = from_union([lambda x: to_class(Federation, x), from_none], self.federation)
        result["fieldsLimits"] = from_union([lambda x: to_class(FieldsLimits, x), from_none], self.fields_limits)
        result["invitesEnabled"] = from_union([from_bool, from_none], self.invites_enabled)
        result["mailerEnabled"] = from_union([from_bool, from_none], self.mailer_enabled)
        result["nodeDescription"] = from_union([from_str, from_none], self.node_description)
        result["nodeName"] = from_union([from_str, from_none], self.node_name)
        result["pollLimits"] = from_union([lambda x: to_class(PollLimits, x), from_none], self.poll_limits)
        result["postFormats"] = from_union([lambda x: from_list(from_str, x), from_none], self.post_formats)
        result["private"] = from_union([from_bool, from_none], self.private)
        result["restrictedNicknames"] = from_union([lambda x: from_list(from_str, x), from_none], self.restricted_nicknames)
        result["skipThreadContainment"] = from_union([from_bool, from_none], self.skip_thread_containment)
        result["staffAccounts"] = from_union([lambda x: from_list(from_str, x), from_none], self.staff_accounts)
        result["suggestions"] = from_union([lambda x: to_class(Suggestions, x), from_none], self.suggestions)
        result["uploadLimits"] = from_union([lambda x: to_class(UploadLimits, x), from_none], self.upload_limits)
        return result


@dataclass
class Services:
    inbound: Optional[List[Any]] = None
    outbound: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Services':
        assert isinstance(obj, dict)
        inbound = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("inbound"))
        outbound = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("outbound"))
        return Services(inbound, outbound)

    def to_dict(self) -> dict:
        result: dict = {}
        result["inbound"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.inbound)
        result["outbound"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.outbound)
        return result


@dataclass
class Software:
    name: Optional[str] = None
    version: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Software':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        version = from_union([from_str, from_none], obj.get("version"))
        return Software(name, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["version"] = from_union([from_str, from_none], self.version)
        return result


@dataclass
class Users:
    total: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Users':
        assert isinstance(obj, dict)
        total = from_union([from_int, from_none], obj.get("total"))
        return Users(total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["total"] = from_union([from_int, from_none], self.total)
        return result


@dataclass
class Usage:
    local_posts: Optional[int] = None
    users: Optional[Users] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Usage':
        assert isinstance(obj, dict)
        local_posts = from_union([from_int, from_none], obj.get("localPosts"))
        users = from_union([Users.from_dict, from_none], obj.get("users"))
        return Usage(local_posts, users)

    def to_dict(self) -> dict:
        result: dict = {}
        result["localPosts"] = from_union([from_int, from_none], self.local_posts)
        result["users"] = from_union([lambda x: to_class(Users, x), from_none], self.users)
        return result


@dataclass
class NodeInfo20:
    metadata: Optional[Metadata] = None
    open_registrations: Optional[bool] = None
    protocols: Optional[List[str]] = None
    services: Optional[Services] = None
    software: Optional[Software] = None
    usage: Optional[Usage] = None
    version: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NodeInfo20':
        assert isinstance(obj, dict)
        metadata = from_union([Metadata.from_dict, from_none], obj.get("metadata"))
        open_registrations = from_union([from_bool, from_none], obj.get("openRegistrations"))
        protocols = from_union([lambda x: from_list(from_str, x), from_none], obj.get("protocols"))
        services = from_union([Services.from_dict, from_none], obj.get("services"))
        software = from_union([Software.from_dict, from_none], obj.get("software"))
        usage = from_union([Usage.from_dict, from_none], obj.get("usage"))
        version = from_union([from_str, from_none], obj.get("version"))
        return NodeInfo20(metadata, open_registrations, protocols, services, software, usage, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["metadata"] = from_union([lambda x: to_class(Metadata, x), from_none], self.metadata)
        result["openRegistrations"] = from_union([from_bool, from_none], self.open_registrations)
        result["protocols"] = from_union([lambda x: from_list(from_str, x), from_none], self.protocols)
        result["services"] = from_union([lambda x: to_class(Services, x), from_none], self.services)
        result["software"] = from_union([lambda x: to_class(Software, x), from_none], self.software)
        result["usage"] = from_union([lambda x: to_class(Usage, x), from_none], self.usage)
        result["version"] = from_union([from_str, from_none], self.version)
        return result


def node_info20_from_dict(s: Any) -> NodeInfo20:
    return NodeInfo20.from_dict(s)


def node_info20_to_dict(x: NodeInfo20) -> Any:
    return to_class(NodeInfo20, x)

