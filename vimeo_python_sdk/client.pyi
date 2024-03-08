# coding: utf-8
"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

import typing
import inspect
from datetime import date, datetime
from vimeo_python_sdk.client_custom import ClientCustom
from vimeo_python_sdk.configuration import Configuration
from vimeo_python_sdk.api_client import ApiClient
from vimeo_python_sdk.type_util import copy_signature
from vimeo_python_sdk.apis.tags.api_information_essentials_api import APIInformationEssentialsApi
from vimeo_python_sdk.apis.tags.authentication_extras_authenticate_api import AuthenticationExtrasAuthenticateApi
from vimeo_python_sdk.apis.tags.authentication_extras_convert_api import AuthenticationExtrasConvertApi
from vimeo_python_sdk.apis.tags.authentication_extras_essentials_api import AuthenticationExtrasEssentialsApi
from vimeo_python_sdk.apis.tags.authentication_extras_exchange_api import AuthenticationExtrasExchangeApi
from vimeo_python_sdk.apis.tags.categories_channels_api import CategoriesChannelsApi
from vimeo_python_sdk.apis.tags.categories_essentials_api import CategoriesEssentialsApi
from vimeo_python_sdk.apis.tags.categories_groups_api import CategoriesGroupsApi
from vimeo_python_sdk.apis.tags.categories_users_api import CategoriesUsersApi
from vimeo_python_sdk.apis.tags.categories_videos_api import CategoriesVideosApi
from vimeo_python_sdk.apis.tags.channels_categories_api import ChannelsCategoriesApi
from vimeo_python_sdk.apis.tags.channels_essentials_api import ChannelsEssentialsApi
from vimeo_python_sdk.apis.tags.channels_moderators_api import ChannelsModeratorsApi
from vimeo_python_sdk.apis.tags.channels_private_channel_members_api import ChannelsPrivateChannelMembersApi
from vimeo_python_sdk.apis.tags.channels_subscriptions_and_subscribers_api import ChannelsSubscriptionsAndSubscribersApi
from vimeo_python_sdk.apis.tags.channels_tags_api import ChannelsTagsApi
from vimeo_python_sdk.apis.tags.channels_videos_api import ChannelsVideosApi
from vimeo_python_sdk.apis.tags.embed_presets_custom_logos_api import EmbedPresetsCustomLogosApi
from vimeo_python_sdk.apis.tags.embed_presets_essentials_api import EmbedPresetsEssentialsApi
from vimeo_python_sdk.apis.tags.embed_presets_timeline_events_api import EmbedPresetsTimelineEventsApi
from vimeo_python_sdk.apis.tags.embed_presets_videos_api import EmbedPresetsVideosApi
from vimeo_python_sdk.apis.tags.folders_essentials_api import FoldersEssentialsApi
from vimeo_python_sdk.apis.tags.folders_items_api import FoldersItemsApi
from vimeo_python_sdk.apis.tags.folders_videos_api import FoldersVideosApi
from vimeo_python_sdk.apis.tags.groups_essentials_api import GroupsEssentialsApi
from vimeo_python_sdk.apis.tags.groups_subscriptions_api import GroupsSubscriptionsApi
from vimeo_python_sdk.apis.tags.groups_users_api import GroupsUsersApi
from vimeo_python_sdk.apis.tags.groups_videos_api import GroupsVideosApi
from vimeo_python_sdk.apis.tags.likes_essentials_api import LikesEssentialsApi
from vimeo_python_sdk.apis.tags.live_embed_privacy_api import LiveEmbedPrivacyApi
from vimeo_python_sdk.apis.tags.live_essentials_api import LiveEssentialsApi
from vimeo_python_sdk.apis.tags.live_event_m3_u8_playback_api import LiveEventM3U8PlaybackApi
from vimeo_python_sdk.apis.tags.live_event_activation_api import LiveEventActivationApi
from vimeo_python_sdk.apis.tags.live_event_automated_closed_captions_api import LiveEventAutomatedClosedCaptionsApi
from vimeo_python_sdk.apis.tags.live_event_destinations_api import LiveEventDestinationsApi
from vimeo_python_sdk.apis.tags.live_event_end_api import LiveEventEndApi
from vimeo_python_sdk.apis.tags.live_event_low_latency_api import LiveEventLowLatencyApi
from vimeo_python_sdk.apis.tags.live_event_sessions_api import LiveEventSessionsApi
from vimeo_python_sdk.apis.tags.live_event_thumbnails_api import LiveEventThumbnailsApi
from vimeo_python_sdk.apis.tags.live_event_videos_api import LiveEventVideosApi
from vimeo_python_sdk.apis.tags.on_demand_backgrounds_api import OnDemandBackgroundsApi
from vimeo_python_sdk.apis.tags.on_demand_essentials_api import OnDemandEssentialsApi
from vimeo_python_sdk.apis.tags.on_demand_genres_api import OnDemandGenresApi
from vimeo_python_sdk.apis.tags.on_demand_posters_api import OnDemandPostersApi
from vimeo_python_sdk.apis.tags.on_demand_promotions_api import OnDemandPromotionsApi
from vimeo_python_sdk.apis.tags.on_demand_purchases_and_rentals_api import OnDemandPurchasesAndRentalsApi
from vimeo_python_sdk.apis.tags.on_demand_regions_api import OnDemandRegionsApi
from vimeo_python_sdk.apis.tags.on_demand_seasons_api import OnDemandSeasonsApi
from vimeo_python_sdk.apis.tags.on_demand_videos_api import OnDemandVideosApi
from vimeo_python_sdk.apis.tags.payments_essentials_api import PaymentsEssentialsApi
from vimeo_python_sdk.apis.tags.portfolios_essentials_api import PortfoliosEssentialsApi
from vimeo_python_sdk.apis.tags.portfolios_videos_api import PortfoliosVideosApi
from vimeo_python_sdk.apis.tags.showcases_custom_showcase_logos_api import ShowcasesCustomShowcaseLogosApi
from vimeo_python_sdk.apis.tags.showcases_custom_showcase_thumbnails_api import ShowcasesCustomShowcaseThumbnailsApi
from vimeo_python_sdk.apis.tags.showcases_essentials_api import ShowcasesEssentialsApi
from vimeo_python_sdk.apis.tags.showcases_showcase_videos_api import ShowcasesShowcaseVideosApi
from vimeo_python_sdk.apis.tags.subscription_plans_essentials_api import SubscriptionPlansEssentialsApi
from vimeo_python_sdk.apis.tags.tags_essentials_api import TagsEssentialsApi
from vimeo_python_sdk.apis.tags.teams_members_api import TeamsMembersApi
from vimeo_python_sdk.apis.tags.tutorial_essentials_api import TutorialEssentialsApi
from vimeo_python_sdk.apis.tags.users_analytics_api import UsersAnalyticsApi
from vimeo_python_sdk.apis.tags.users_essentials_api import UsersEssentialsApi
from vimeo_python_sdk.apis.tags.users_feeds_api import UsersFeedsApi
from vimeo_python_sdk.apis.tags.users_followers_api import UsersFollowersApi
from vimeo_python_sdk.apis.tags.users_pictures_api import UsersPicturesApi
from vimeo_python_sdk.apis.tags.users_search_api import UsersSearchApi
from vimeo_python_sdk.apis.tags.users_watch_history_api import UsersWatchHistoryApi
from vimeo_python_sdk.apis.tags.videos_animated_thumbnails_api import VideosAnimatedThumbnailsApi
from vimeo_python_sdk.apis.tags.videos_chapters_api import VideosChaptersApi
from vimeo_python_sdk.apis.tags.videos_content_ratings_api import VideosContentRatingsApi
from vimeo_python_sdk.apis.tags.videos_creative_commons_api import VideosCreativeCommonsApi
from vimeo_python_sdk.apis.tags.videos_credits_api import VideosCreditsApi
from vimeo_python_sdk.apis.tags.videos_embed_privacy_api import VideosEmbedPrivacyApi
from vimeo_python_sdk.apis.tags.videos_essentials_api import VideosEssentialsApi
from vimeo_python_sdk.apis.tags.videos_fragments_api import VideosFragmentsApi
from vimeo_python_sdk.apis.tags.videos_languages_api import VideosLanguagesApi
from vimeo_python_sdk.apis.tags.videos_live_m3_u8_playback_api import VideosLiveM3U8PlaybackApi
from vimeo_python_sdk.apis.tags.videos_nondestructive_trimming_api import VideosNondestructiveTrimmingApi
from vimeo_python_sdk.apis.tags.videos_recommendations_api import VideosRecommendationsApi
from vimeo_python_sdk.apis.tags.videos_showcases_api import VideosShowcasesApi
from vimeo_python_sdk.apis.tags.videos_tags_api import VideosTagsApi
from vimeo_python_sdk.apis.tags.videos_text_tracks_api import VideosTextTracksApi
from vimeo_python_sdk.apis.tags.videos_thumbnails_api import VideosThumbnailsApi
from vimeo_python_sdk.apis.tags.videos_transcripts_api import VideosTranscriptsApi
from vimeo_python_sdk.apis.tags.videos_unlisted_videos_api import VideosUnlistedVideosApi
from vimeo_python_sdk.apis.tags.videos_uploads_api import VideosUploadsApi
from vimeo_python_sdk.apis.tags.videos_versions_api import VideosVersionsApi
from vimeo_python_sdk.apis.tags.videos_video_comments_api import VideosVideoCommentsApi
from vimeo_python_sdk.apis.tags.watch_later_queue_essentials_api import WatchLaterQueueEssentialsApi
from vimeo_python_sdk.apis.tags.webinar_emails_api import WebinarEmailsApi
from vimeo_python_sdk.apis.tags.webinar_essentials_api import WebinarEssentialsApi
from vimeo_python_sdk.apis.tags.webinar_registrations_api import WebinarRegistrationsApi



class Vimeo(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.api_information\essentials: APIInformationEssentialsApi = APIInformationEssentialsApi(api_client)
        self.authentication_extras\authenticate: AuthenticationExtrasAuthenticateApi = AuthenticationExtrasAuthenticateApi(api_client)
        self.authentication_extras\convert: AuthenticationExtrasConvertApi = AuthenticationExtrasConvertApi(api_client)
        self.authentication_extras\essentials: AuthenticationExtrasEssentialsApi = AuthenticationExtrasEssentialsApi(api_client)
        self.authentication_extras\exchange: AuthenticationExtrasExchangeApi = AuthenticationExtrasExchangeApi(api_client)
        self.categories\channels: CategoriesChannelsApi = CategoriesChannelsApi(api_client)
        self.categories\essentials: CategoriesEssentialsApi = CategoriesEssentialsApi(api_client)
        self.categories\groups: CategoriesGroupsApi = CategoriesGroupsApi(api_client)
        self.categories\users: CategoriesUsersApi = CategoriesUsersApi(api_client)
        self.categories\videos: CategoriesVideosApi = CategoriesVideosApi(api_client)
        self.channels\categories: ChannelsCategoriesApi = ChannelsCategoriesApi(api_client)
        self.channels\essentials: ChannelsEssentialsApi = ChannelsEssentialsApi(api_client)
        self.channels\moderators: ChannelsModeratorsApi = ChannelsModeratorsApi(api_client)
        self.channels\private_channel_members: ChannelsPrivateChannelMembersApi = ChannelsPrivateChannelMembersApi(api_client)
        self.channels\subscriptions_and_subscribers: ChannelsSubscriptionsAndSubscribersApi = ChannelsSubscriptionsAndSubscribersApi(api_client)
        self.channels\tags: ChannelsTagsApi = ChannelsTagsApi(api_client)
        self.channels\videos: ChannelsVideosApi = ChannelsVideosApi(api_client)
        self.embed_presets\custom_logos: EmbedPresetsCustomLogosApi = EmbedPresetsCustomLogosApi(api_client)
        self.embed_presets\essentials: EmbedPresetsEssentialsApi = EmbedPresetsEssentialsApi(api_client)
        self.embed_presets\timeline_events: EmbedPresetsTimelineEventsApi = EmbedPresetsTimelineEventsApi(api_client)
        self.embed_presets\videos: EmbedPresetsVideosApi = EmbedPresetsVideosApi(api_client)
        self.folders\essentials: FoldersEssentialsApi = FoldersEssentialsApi(api_client)
        self.folders\items: FoldersItemsApi = FoldersItemsApi(api_client)
        self.folders\videos: FoldersVideosApi = FoldersVideosApi(api_client)
        self.groups\essentials: GroupsEssentialsApi = GroupsEssentialsApi(api_client)
        self.groups\subscriptions: GroupsSubscriptionsApi = GroupsSubscriptionsApi(api_client)
        self.groups\users: GroupsUsersApi = GroupsUsersApi(api_client)
        self.groups\videos: GroupsVideosApi = GroupsVideosApi(api_client)
        self.likes\essentials: LikesEssentialsApi = LikesEssentialsApi(api_client)
        self.live\embed_privacy: LiveEmbedPrivacyApi = LiveEmbedPrivacyApi(api_client)
        self.live\essentials: LiveEssentialsApi = LiveEssentialsApi(api_client)
        self.live\event_m3_u8_playback: LiveEventM3U8PlaybackApi = LiveEventM3U8PlaybackApi(api_client)
        self.live\event_activation: LiveEventActivationApi = LiveEventActivationApi(api_client)
        self.live\event_automated_closed_captions: LiveEventAutomatedClosedCaptionsApi = LiveEventAutomatedClosedCaptionsApi(api_client)
        self.live\event_destinations: LiveEventDestinationsApi = LiveEventDestinationsApi(api_client)
        self.live\event_end: LiveEventEndApi = LiveEventEndApi(api_client)
        self.live\event_low_latency: LiveEventLowLatencyApi = LiveEventLowLatencyApi(api_client)
        self.live\event_sessions: LiveEventSessionsApi = LiveEventSessionsApi(api_client)
        self.live\event_thumbnails: LiveEventThumbnailsApi = LiveEventThumbnailsApi(api_client)
        self.live\event_videos: LiveEventVideosApi = LiveEventVideosApi(api_client)
        self.on_demand\backgrounds: OnDemandBackgroundsApi = OnDemandBackgroundsApi(api_client)
        self.on_demand\essentials: OnDemandEssentialsApi = OnDemandEssentialsApi(api_client)
        self.on_demand\genres: OnDemandGenresApi = OnDemandGenresApi(api_client)
        self.on_demand\posters: OnDemandPostersApi = OnDemandPostersApi(api_client)
        self.on_demand\promotions: OnDemandPromotionsApi = OnDemandPromotionsApi(api_client)
        self.on_demand\purchases_and_rentals: OnDemandPurchasesAndRentalsApi = OnDemandPurchasesAndRentalsApi(api_client)
        self.on_demand\regions: OnDemandRegionsApi = OnDemandRegionsApi(api_client)
        self.on_demand\seasons: OnDemandSeasonsApi = OnDemandSeasonsApi(api_client)
        self.on_demand\videos: OnDemandVideosApi = OnDemandVideosApi(api_client)
        self.payments\essentials: PaymentsEssentialsApi = PaymentsEssentialsApi(api_client)
        self.portfolios\essentials: PortfoliosEssentialsApi = PortfoliosEssentialsApi(api_client)
        self.portfolios\videos: PortfoliosVideosApi = PortfoliosVideosApi(api_client)
        self.showcases\custom_showcase_logos: ShowcasesCustomShowcaseLogosApi = ShowcasesCustomShowcaseLogosApi(api_client)
        self.showcases\custom_showcase_thumbnails: ShowcasesCustomShowcaseThumbnailsApi = ShowcasesCustomShowcaseThumbnailsApi(api_client)
        self.showcases\essentials: ShowcasesEssentialsApi = ShowcasesEssentialsApi(api_client)
        self.showcases\showcase_videos: ShowcasesShowcaseVideosApi = ShowcasesShowcaseVideosApi(api_client)
        self.subscription_plans\essentials: SubscriptionPlansEssentialsApi = SubscriptionPlansEssentialsApi(api_client)
        self.tags\essentials: TagsEssentialsApi = TagsEssentialsApi(api_client)
        self.teams\members: TeamsMembersApi = TeamsMembersApi(api_client)
        self.tutorial\essentials: TutorialEssentialsApi = TutorialEssentialsApi(api_client)
        self.users\analytics: UsersAnalyticsApi = UsersAnalyticsApi(api_client)
        self.users\essentials: UsersEssentialsApi = UsersEssentialsApi(api_client)
        self.users\feeds: UsersFeedsApi = UsersFeedsApi(api_client)
        self.users\followers: UsersFollowersApi = UsersFollowersApi(api_client)
        self.users\pictures: UsersPicturesApi = UsersPicturesApi(api_client)
        self.users\search: UsersSearchApi = UsersSearchApi(api_client)
        self.users\watch_history: UsersWatchHistoryApi = UsersWatchHistoryApi(api_client)
        self.videos\animated_thumbnails: VideosAnimatedThumbnailsApi = VideosAnimatedThumbnailsApi(api_client)
        self.videos\chapters: VideosChaptersApi = VideosChaptersApi(api_client)
        self.videos\content_ratings: VideosContentRatingsApi = VideosContentRatingsApi(api_client)
        self.videos\creative_commons: VideosCreativeCommonsApi = VideosCreativeCommonsApi(api_client)
        self.videos\credits: VideosCreditsApi = VideosCreditsApi(api_client)
        self.videos\embed_privacy: VideosEmbedPrivacyApi = VideosEmbedPrivacyApi(api_client)
        self.videos\essentials: VideosEssentialsApi = VideosEssentialsApi(api_client)
        self.videos\fragments: VideosFragmentsApi = VideosFragmentsApi(api_client)
        self.videos\languages: VideosLanguagesApi = VideosLanguagesApi(api_client)
        self.videos\live_m3_u8_playback: VideosLiveM3U8PlaybackApi = VideosLiveM3U8PlaybackApi(api_client)
        self.videos\nondestructive_trimming: VideosNondestructiveTrimmingApi = VideosNondestructiveTrimmingApi(api_client)
        self.videos\recommendations: VideosRecommendationsApi = VideosRecommendationsApi(api_client)
        self.videos\showcases: VideosShowcasesApi = VideosShowcasesApi(api_client)
        self.videos\tags: VideosTagsApi = VideosTagsApi(api_client)
        self.videos\text_tracks: VideosTextTracksApi = VideosTextTracksApi(api_client)
        self.videos\thumbnails: VideosThumbnailsApi = VideosThumbnailsApi(api_client)
        self.videos\transcripts: VideosTranscriptsApi = VideosTranscriptsApi(api_client)
        self.videos\unlisted_videos: VideosUnlistedVideosApi = VideosUnlistedVideosApi(api_client)
        self.videos\uploads: VideosUploadsApi = VideosUploadsApi(api_client)
        self.videos\versions: VideosVersionsApi = VideosVersionsApi(api_client)
        self.videos\video_comments: VideosVideoCommentsApi = VideosVideoCommentsApi(api_client)
        self.watch_later_queue\essentials: WatchLaterQueueEssentialsApi = WatchLaterQueueEssentialsApi(api_client)
        self.webinar\emails: WebinarEmailsApi = WebinarEmailsApi(api_client)
        self.webinar\essentials: WebinarEssentialsApi = WebinarEssentialsApi(api_client)
        self.webinar\registrations: WebinarRegistrationsApi = WebinarRegistrationsApi(api_client)
