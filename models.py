from db import db
from quicktype_types import *


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    modified_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.current_timestamp(), nullable=False)


class FediInstance(db.Model, TimestampMixin):  
    id = db.Column(db.Integer, primary_key=True)
    Address = db.Column(db.String(120), nullable=False)
    Features = db.Column(db.Text)
    NodeName = db.Column(db.Text)
    NodeDescription = db.Column(db.Text)
    OpenRegistrations = db.Column(db.Boolean)
    Software = db.Column(db.Text)
    SoftwareVersion = db.Column(db.Text)
    NumPosts = db.Column(db.Integer)
    NumUsers = db.Column(db.Integer)

    __table_args__ = (
        db.UniqueConstraint('Address', 'NodeName', name='uniq_address_nodename'),
    )


    MRF_Policies = db.Column(db.Text) # list of active policies
    MRF_Accept = db.Column(db.Text) # MRF simple stuff etc ...
    MRF_AvatarRemoval = db.Column(db.Text)
    MRF_BannerRemoval = db.Column(db.Text)
    MRF_FediTimelineRemoval = db.Column(db.Text)
    MRF_FollowersOnly = db.Column(db.Text)
    MRF_MediaNSFW = db.Column(db.Text)
    MRF_MediaRemoval = db.Column(db.Text)
    MRF_Reject = db.Column(db.Text)
    MRF_RejectDeletes = db.Column(db.Text)
    MRF_ReportRemoval = db.Column(db.Text)

    @staticmethod
    def get_or_create_from_quicktype(address: str, ni: NodeInfo):

        fi = FediInstance.query.filter(FediInstance.Address==address or FediInstance.NodeName==ni.metadata.node_name).first()
        if fi is None:
            fi = FediInstance()

        fi.Address = address
        fi.Features = ', '.join(ni.metadata.features)
        fi.NodeName = ni.metadata.node_name
        fi.NodeDescription = ni.metadata.node_description
        fi.OpenRegistrations = ni.open_registrations
        fi.Software = ni.software.name
        fi.SoftwareVersion = ni.software.version
        fi.NumPosts = ni.usage.local_posts
        fi.NumUsers = ni.usage.users.total
        fi.MRF_Policies = ', '.join(ni.metadata.federation.mrf_policies)

        fi.MRF_Accept = ', '.join(ni.metadata.federation.mrf_simple.accept) or None
        fi.MRF_AvatarRemoval = ', '.join(ni.metadata.federation.mrf_simple.avatar_removal) or None
        fi.MRF_BannerRemoval = ', '.join(ni.metadata.federation.mrf_simple.banner_removal) or None
        fi.MRF_FediTimelineRemoval = ', '.join(ni.metadata.federation.mrf_simple.federated_timeline_removal) or None
        fi.MRF_FollowersOnly = ', '.join(ni.metadata.federation.mrf_simple.followers_only) or None
        fi.MRF_MediaNSFW = ', '.join(ni.metadata.federation.mrf_simple.media_nsfw) or None
        fi.MRF_MediaRemoval = ', '.join(ni.metadata.federation.mrf_simple.media_removal) or None
        fi.MRF_Reject = ', '.join(ni.metadata.federation.mrf_simple.reject) or None
        fi.MRF_RejectDeletes = ', '.join(ni.metadata.federation.mrf_simple.reject_deletes) or None
        fi.MRF_ReportRemoval = ', '.join(ni.metadata.federation.mrf_simple.report_removal) or None

        return fi
        

