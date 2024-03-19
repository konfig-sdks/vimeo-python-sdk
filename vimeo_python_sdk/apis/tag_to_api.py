import typing_extensions

from vimeo_python_sdk.apis.tags import TagValues
from vimeo_python_sdk.apis.tags.live_essentials_api import LiveEssentialsApi
from vimeo_python_sdk.apis.tags.live_event_destinations_api import LiveEventDestinationsApi
from vimeo_python_sdk.apis.tags.showcases_showcase_videos_api import ShowcasesShowcaseVideosApi
from vimeo_python_sdk.apis.tags.live_event_thumbnails_api import LiveEventThumbnailsApi
from vimeo_python_sdk.apis.tags.live_event_videos_api import LiveEventVideosApi
from vimeo_python_sdk.apis.tags.users_followers_api import UsersFollowersApi
from vimeo_python_sdk.apis.tags.videos_chapters_api import VideosChaptersApi
from vimeo_python_sdk.apis.tags.videos_essentials_api import VideosEssentialsApi
from vimeo_python_sdk.apis.tags.folders_essentials_api import FoldersEssentialsApi
from vimeo_python_sdk.apis.tags.likes_essentials_api import LikesEssentialsApi
from vimeo_python_sdk.apis.tags.showcases_essentials_api import ShowcasesEssentialsApi
from vimeo_python_sdk.apis.tags.folders_videos_api import FoldersVideosApi
from vimeo_python_sdk.apis.tags.users_pictures_api import UsersPicturesApi
from vimeo_python_sdk.apis.tags.videos_video_comments_api import VideosVideoCommentsApi
from vimeo_python_sdk.apis.tags.categories_users_api import CategoriesUsersApi
from vimeo_python_sdk.apis.tags.embed_presets_custom_logos_api import EmbedPresetsCustomLogosApi
from vimeo_python_sdk.apis.tags.embed_presets_essentials_api import EmbedPresetsEssentialsApi
from vimeo_python_sdk.apis.tags.on_demand_genres_api import OnDemandGenresApi
from vimeo_python_sdk.apis.tags.on_demand_regions_api import OnDemandRegionsApi
from vimeo_python_sdk.apis.tags.portfolios_videos_api import PortfoliosVideosApi
from vimeo_python_sdk.apis.tags.videos_credits_api import VideosCreditsApi
from vimeo_python_sdk.apis.tags.watch_later_queue_essentials_api import WatchLaterQueueEssentialsApi
from vimeo_python_sdk.apis.tags.webinar_registrations_api import WebinarRegistrationsApi
from vimeo_python_sdk.apis.tags.channels_essentials_api import ChannelsEssentialsApi
from vimeo_python_sdk.apis.tags.channels_moderators_api import ChannelsModeratorsApi
from vimeo_python_sdk.apis.tags.channels_subscriptions_and_subscribers_api import ChannelsSubscriptionsAndSubscribersApi
from vimeo_python_sdk.apis.tags.channels_videos_api import ChannelsVideosApi
from vimeo_python_sdk.apis.tags.on_demand_essentials_api import OnDemandEssentialsApi
from vimeo_python_sdk.apis.tags.videos_text_tracks_api import VideosTextTracksApi
from vimeo_python_sdk.apis.tags.videos_thumbnails_api import VideosThumbnailsApi
from vimeo_python_sdk.apis.tags.webinar_essentials_api import WebinarEssentialsApi
from vimeo_python_sdk.apis.tags.live_embed_privacy_api import LiveEmbedPrivacyApi
from vimeo_python_sdk.apis.tags.videos_tags_api import VideosTagsApi
from vimeo_python_sdk.apis.tags.videos_unlisted_videos_api import VideosUnlistedVideosApi
from vimeo_python_sdk.apis.tags.videos_versions_api import VideosVersionsApi
from vimeo_python_sdk.apis.tags.channels_tags_api import ChannelsTagsApi
from vimeo_python_sdk.apis.tags.embed_presets_videos_api import EmbedPresetsVideosApi
from vimeo_python_sdk.apis.tags.groups_users_api import GroupsUsersApi
from vimeo_python_sdk.apis.tags.on_demand_backgrounds_api import OnDemandBackgroundsApi
from vimeo_python_sdk.apis.tags.on_demand_promotions_api import OnDemandPromotionsApi
from vimeo_python_sdk.apis.tags.showcases_custom_showcase_logos_api import ShowcasesCustomShowcaseLogosApi
from vimeo_python_sdk.apis.tags.showcases_custom_showcase_thumbnails_api import ShowcasesCustomShowcaseThumbnailsApi
from vimeo_python_sdk.apis.tags.videos_animated_thumbnails_api import VideosAnimatedThumbnailsApi
from vimeo_python_sdk.apis.tags.categories_videos_api import CategoriesVideosApi
from vimeo_python_sdk.apis.tags.channels_categories_api import ChannelsCategoriesApi
from vimeo_python_sdk.apis.tags.channels_private_channel_members_api import ChannelsPrivateChannelMembersApi
from vimeo_python_sdk.apis.tags.groups_essentials_api import GroupsEssentialsApi
from vimeo_python_sdk.apis.tags.groups_subscriptions_api import GroupsSubscriptionsApi
from vimeo_python_sdk.apis.tags.groups_videos_api import GroupsVideosApi
from vimeo_python_sdk.apis.tags.on_demand_posters_api import OnDemandPostersApi
from vimeo_python_sdk.apis.tags.on_demand_videos_api import OnDemandVideosApi
from vimeo_python_sdk.apis.tags.portfolios_essentials_api import PortfoliosEssentialsApi
from vimeo_python_sdk.apis.tags.users_essentials_api import UsersEssentialsApi
from vimeo_python_sdk.apis.tags.videos_uploads_api import VideosUploadsApi
from vimeo_python_sdk.apis.tags.webinar_emails_api import WebinarEmailsApi
from vimeo_python_sdk.apis.tags.folders_items_api import FoldersItemsApi
from vimeo_python_sdk.apis.tags.live_event_activation_api import LiveEventActivationApi
from vimeo_python_sdk.apis.tags.live_event_automated_closed_captions_api import LiveEventAutomatedClosedCaptionsApi
from vimeo_python_sdk.apis.tags.live_event_end_api import LiveEventEndApi
from vimeo_python_sdk.apis.tags.live_event_low_latency_api import LiveEventLowLatencyApi
from vimeo_python_sdk.apis.tags.on_demand_purchases_and_rentals_api import OnDemandPurchasesAndRentalsApi
from vimeo_python_sdk.apis.tags.on_demand_seasons_api import OnDemandSeasonsApi
from vimeo_python_sdk.apis.tags.payments_essentials_api import PaymentsEssentialsApi
from vimeo_python_sdk.apis.tags.teams_members_api import TeamsMembersApi
from vimeo_python_sdk.apis.tags.users_watch_history_api import UsersWatchHistoryApi
from vimeo_python_sdk.apis.tags.videos_embed_privacy_api import VideosEmbedPrivacyApi
from vimeo_python_sdk.apis.tags.videos_fragments_api import VideosFragmentsApi
from vimeo_python_sdk.apis.tags.authentication_extras_essentials_api import AuthenticationExtrasEssentialsApi
from vimeo_python_sdk.apis.tags.categories_essentials_api import CategoriesEssentialsApi
from vimeo_python_sdk.apis.tags.embed_presets_timeline_events_api import EmbedPresetsTimelineEventsApi
from vimeo_python_sdk.apis.tags.live_event_m3_u8_playback_api import LiveEventM3U8PlaybackApi
from vimeo_python_sdk.apis.tags.users_analytics_api import UsersAnalyticsApi
from vimeo_python_sdk.apis.tags.users_feeds_api import UsersFeedsApi
from vimeo_python_sdk.apis.tags.videos_live_m3_u8_playback_api import VideosLiveM3U8PlaybackApi
from vimeo_python_sdk.apis.tags.videos_nondestructive_trimming_api import VideosNondestructiveTrimmingApi
from vimeo_python_sdk.apis.tags.videos_showcases_api import VideosShowcasesApi
from vimeo_python_sdk.apis.tags.api_information_essentials_api import APIInformationEssentialsApi
from vimeo_python_sdk.apis.tags.authentication_extras_authenticate_api import AuthenticationExtrasAuthenticateApi
from vimeo_python_sdk.apis.tags.authentication_extras_convert_api import AuthenticationExtrasConvertApi
from vimeo_python_sdk.apis.tags.authentication_extras_exchange_api import AuthenticationExtrasExchangeApi
from vimeo_python_sdk.apis.tags.categories_channels_api import CategoriesChannelsApi
from vimeo_python_sdk.apis.tags.categories_groups_api import CategoriesGroupsApi
from vimeo_python_sdk.apis.tags.live_event_sessions_api import LiveEventSessionsApi
from vimeo_python_sdk.apis.tags.subscription_plans_essentials_api import SubscriptionPlansEssentialsApi
from vimeo_python_sdk.apis.tags.tags_essentials_api import TagsEssentialsApi
from vimeo_python_sdk.apis.tags.tutorial_essentials_api import TutorialEssentialsApi
from vimeo_python_sdk.apis.tags.users_search_api import UsersSearchApi
from vimeo_python_sdk.apis.tags.videos_content_ratings_api import VideosContentRatingsApi
from vimeo_python_sdk.apis.tags.videos_creative_commons_api import VideosCreativeCommonsApi
from vimeo_python_sdk.apis.tags.videos_languages_api import VideosLanguagesApi
from vimeo_python_sdk.apis.tags.videos_recommendations_api import VideosRecommendationsApi
from vimeo_python_sdk.apis.tags.videos_transcripts_api import VideosTranscriptsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.LIVEESSENTIALS: LiveEssentialsApi,
        TagValues.LIVEEVENT_DESTINATIONS: LiveEventDestinationsApi,
        TagValues.SHOWCASESSHOWCASE_VIDEOS: ShowcasesShowcaseVideosApi,
        TagValues.LIVEEVENT_THUMBNAILS: LiveEventThumbnailsApi,
        TagValues.LIVEEVENT_VIDEOS: LiveEventVideosApi,
        TagValues.USERSFOLLOWERS: UsersFollowersApi,
        TagValues.VIDEOSCHAPTERS: VideosChaptersApi,
        TagValues.VIDEOSESSENTIALS: VideosEssentialsApi,
        TagValues.FOLDERSESSENTIALS: FoldersEssentialsApi,
        TagValues.LIKESESSENTIALS: LikesEssentialsApi,
        TagValues.SHOWCASESESSENTIALS: ShowcasesEssentialsApi,
        TagValues.FOLDERSVIDEOS: FoldersVideosApi,
        TagValues.USERSPICTURES: UsersPicturesApi,
        TagValues.VIDEOSVIDEO_COMMENTS: VideosVideoCommentsApi,
        TagValues.CATEGORIESUSERS: CategoriesUsersApi,
        TagValues.EMBED_PRESETSCUSTOM_LOGOS: EmbedPresetsCustomLogosApi,
        TagValues.EMBED_PRESETSESSENTIALS: EmbedPresetsEssentialsApi,
        TagValues.ON_DEMANDGENRES: OnDemandGenresApi,
        TagValues.ON_DEMANDREGIONS: OnDemandRegionsApi,
        TagValues.PORTFOLIOSVIDEOS: PortfoliosVideosApi,
        TagValues.VIDEOSCREDITS: VideosCreditsApi,
        TagValues.WATCH_LATER_QUEUEESSENTIALS: WatchLaterQueueEssentialsApi,
        TagValues.WEBINARREGISTRATIONS: WebinarRegistrationsApi,
        TagValues.CHANNELSESSENTIALS: ChannelsEssentialsApi,
        TagValues.CHANNELSMODERATORS: ChannelsModeratorsApi,
        TagValues.CHANNELSSUBSCRIPTIONS_AND_SUBSCRIBERS: ChannelsSubscriptionsAndSubscribersApi,
        TagValues.CHANNELSVIDEOS: ChannelsVideosApi,
        TagValues.ON_DEMANDESSENTIALS: OnDemandEssentialsApi,
        TagValues.VIDEOSTEXT_TRACKS: VideosTextTracksApi,
        TagValues.VIDEOSTHUMBNAILS: VideosThumbnailsApi,
        TagValues.WEBINARESSENTIALS: WebinarEssentialsApi,
        TagValues.LIVEEMBED_PRIVACY: LiveEmbedPrivacyApi,
        TagValues.VIDEOSTAGS: VideosTagsApi,
        TagValues.VIDEOSUNLISTED_VIDEOS: VideosUnlistedVideosApi,
        TagValues.VIDEOSVERSIONS: VideosVersionsApi,
        TagValues.CHANNELSTAGS: ChannelsTagsApi,
        TagValues.EMBED_PRESETSVIDEOS: EmbedPresetsVideosApi,
        TagValues.GROUPSUSERS: GroupsUsersApi,
        TagValues.ON_DEMANDBACKGROUNDS: OnDemandBackgroundsApi,
        TagValues.ON_DEMANDPROMOTIONS: OnDemandPromotionsApi,
        TagValues.SHOWCASESCUSTOM_SHOWCASE_LOGOS: ShowcasesCustomShowcaseLogosApi,
        TagValues.SHOWCASESCUSTOM_SHOWCASE_THUMBNAILS: ShowcasesCustomShowcaseThumbnailsApi,
        TagValues.VIDEOSANIMATED_THUMBNAILS: VideosAnimatedThumbnailsApi,
        TagValues.CATEGORIESVIDEOS: CategoriesVideosApi,
        TagValues.CHANNELSCATEGORIES: ChannelsCategoriesApi,
        TagValues.CHANNELSPRIVATE_CHANNEL_MEMBERS: ChannelsPrivateChannelMembersApi,
        TagValues.GROUPSESSENTIALS: GroupsEssentialsApi,
        TagValues.GROUPSSUBSCRIPTIONS: GroupsSubscriptionsApi,
        TagValues.GROUPSVIDEOS: GroupsVideosApi,
        TagValues.ON_DEMANDPOSTERS: OnDemandPostersApi,
        TagValues.ON_DEMANDVIDEOS: OnDemandVideosApi,
        TagValues.PORTFOLIOSESSENTIALS: PortfoliosEssentialsApi,
        TagValues.USERSESSENTIALS: UsersEssentialsApi,
        TagValues.VIDEOSUPLOADS: VideosUploadsApi,
        TagValues.WEBINAREMAILS: WebinarEmailsApi,
        TagValues.FOLDERSITEMS: FoldersItemsApi,
        TagValues.LIVEEVENT_ACTIVATION: LiveEventActivationApi,
        TagValues.LIVEEVENT_AUTOMATED_CLOSED_CAPTIONS: LiveEventAutomatedClosedCaptionsApi,
        TagValues.LIVEEVENT_END: LiveEventEndApi,
        TagValues.LIVEEVENT_LOW_LATENCY: LiveEventLowLatencyApi,
        TagValues.ON_DEMANDPURCHASES_AND_RENTALS: OnDemandPurchasesAndRentalsApi,
        TagValues.ON_DEMANDSEASONS: OnDemandSeasonsApi,
        TagValues.PAYMENTSESSENTIALS: PaymentsEssentialsApi,
        TagValues.TEAMSMEMBERS: TeamsMembersApi,
        TagValues.USERSWATCH_HISTORY: UsersWatchHistoryApi,
        TagValues.VIDEOSEMBED_PRIVACY: VideosEmbedPrivacyApi,
        TagValues.VIDEOSFRAGMENTS: VideosFragmentsApi,
        TagValues.AUTHENTICATION_EXTRASESSENTIALS: AuthenticationExtrasEssentialsApi,
        TagValues.CATEGORIESESSENTIALS: CategoriesEssentialsApi,
        TagValues.EMBED_PRESETSTIMELINE_EVENTS: EmbedPresetsTimelineEventsApi,
        TagValues.LIVEEVENT_M3U8_PLAYBACK: LiveEventM3U8PlaybackApi,
        TagValues.USERSANALYTICS: UsersAnalyticsApi,
        TagValues.USERSFEEDS: UsersFeedsApi,
        TagValues.VIDEOSLIVE_M3U8_PLAYBACK: VideosLiveM3U8PlaybackApi,
        TagValues.VIDEOSNONDESTRUCTIVE_TRIMMING: VideosNondestructiveTrimmingApi,
        TagValues.VIDEOSSHOWCASES: VideosShowcasesApi,
        TagValues.API_INFORMATIONESSENTIALS: APIInformationEssentialsApi,
        TagValues.AUTHENTICATION_EXTRASAUTHENTICATE: AuthenticationExtrasAuthenticateApi,
        TagValues.AUTHENTICATION_EXTRASCONVERT: AuthenticationExtrasConvertApi,
        TagValues.AUTHENTICATION_EXTRASEXCHANGE: AuthenticationExtrasExchangeApi,
        TagValues.CATEGORIESCHANNELS: CategoriesChannelsApi,
        TagValues.CATEGORIESGROUPS: CategoriesGroupsApi,
        TagValues.LIVEEVENT_SESSIONS: LiveEventSessionsApi,
        TagValues.SUBSCRIPTION_PLANSESSENTIALS: SubscriptionPlansEssentialsApi,
        TagValues.TAGSESSENTIALS: TagsEssentialsApi,
        TagValues.TUTORIALESSENTIALS: TutorialEssentialsApi,
        TagValues.USERSSEARCH: UsersSearchApi,
        TagValues.VIDEOSCONTENT_RATINGS: VideosContentRatingsApi,
        TagValues.VIDEOSCREATIVE_COMMONS: VideosCreativeCommonsApi,
        TagValues.VIDEOSLANGUAGES: VideosLanguagesApi,
        TagValues.VIDEOSRECOMMENDATIONS: VideosRecommendationsApi,
        TagValues.VIDEOSTRANSCRIPTS: VideosTranscriptsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.LIVEESSENTIALS: LiveEssentialsApi,
        TagValues.LIVEEVENT_DESTINATIONS: LiveEventDestinationsApi,
        TagValues.SHOWCASESSHOWCASE_VIDEOS: ShowcasesShowcaseVideosApi,
        TagValues.LIVEEVENT_THUMBNAILS: LiveEventThumbnailsApi,
        TagValues.LIVEEVENT_VIDEOS: LiveEventVideosApi,
        TagValues.USERSFOLLOWERS: UsersFollowersApi,
        TagValues.VIDEOSCHAPTERS: VideosChaptersApi,
        TagValues.VIDEOSESSENTIALS: VideosEssentialsApi,
        TagValues.FOLDERSESSENTIALS: FoldersEssentialsApi,
        TagValues.LIKESESSENTIALS: LikesEssentialsApi,
        TagValues.SHOWCASESESSENTIALS: ShowcasesEssentialsApi,
        TagValues.FOLDERSVIDEOS: FoldersVideosApi,
        TagValues.USERSPICTURES: UsersPicturesApi,
        TagValues.VIDEOSVIDEO_COMMENTS: VideosVideoCommentsApi,
        TagValues.CATEGORIESUSERS: CategoriesUsersApi,
        TagValues.EMBED_PRESETSCUSTOM_LOGOS: EmbedPresetsCustomLogosApi,
        TagValues.EMBED_PRESETSESSENTIALS: EmbedPresetsEssentialsApi,
        TagValues.ON_DEMANDGENRES: OnDemandGenresApi,
        TagValues.ON_DEMANDREGIONS: OnDemandRegionsApi,
        TagValues.PORTFOLIOSVIDEOS: PortfoliosVideosApi,
        TagValues.VIDEOSCREDITS: VideosCreditsApi,
        TagValues.WATCH_LATER_QUEUEESSENTIALS: WatchLaterQueueEssentialsApi,
        TagValues.WEBINARREGISTRATIONS: WebinarRegistrationsApi,
        TagValues.CHANNELSESSENTIALS: ChannelsEssentialsApi,
        TagValues.CHANNELSMODERATORS: ChannelsModeratorsApi,
        TagValues.CHANNELSSUBSCRIPTIONS_AND_SUBSCRIBERS: ChannelsSubscriptionsAndSubscribersApi,
        TagValues.CHANNELSVIDEOS: ChannelsVideosApi,
        TagValues.ON_DEMANDESSENTIALS: OnDemandEssentialsApi,
        TagValues.VIDEOSTEXT_TRACKS: VideosTextTracksApi,
        TagValues.VIDEOSTHUMBNAILS: VideosThumbnailsApi,
        TagValues.WEBINARESSENTIALS: WebinarEssentialsApi,
        TagValues.LIVEEMBED_PRIVACY: LiveEmbedPrivacyApi,
        TagValues.VIDEOSTAGS: VideosTagsApi,
        TagValues.VIDEOSUNLISTED_VIDEOS: VideosUnlistedVideosApi,
        TagValues.VIDEOSVERSIONS: VideosVersionsApi,
        TagValues.CHANNELSTAGS: ChannelsTagsApi,
        TagValues.EMBED_PRESETSVIDEOS: EmbedPresetsVideosApi,
        TagValues.GROUPSUSERS: GroupsUsersApi,
        TagValues.ON_DEMANDBACKGROUNDS: OnDemandBackgroundsApi,
        TagValues.ON_DEMANDPROMOTIONS: OnDemandPromotionsApi,
        TagValues.SHOWCASESCUSTOM_SHOWCASE_LOGOS: ShowcasesCustomShowcaseLogosApi,
        TagValues.SHOWCASESCUSTOM_SHOWCASE_THUMBNAILS: ShowcasesCustomShowcaseThumbnailsApi,
        TagValues.VIDEOSANIMATED_THUMBNAILS: VideosAnimatedThumbnailsApi,
        TagValues.CATEGORIESVIDEOS: CategoriesVideosApi,
        TagValues.CHANNELSCATEGORIES: ChannelsCategoriesApi,
        TagValues.CHANNELSPRIVATE_CHANNEL_MEMBERS: ChannelsPrivateChannelMembersApi,
        TagValues.GROUPSESSENTIALS: GroupsEssentialsApi,
        TagValues.GROUPSSUBSCRIPTIONS: GroupsSubscriptionsApi,
        TagValues.GROUPSVIDEOS: GroupsVideosApi,
        TagValues.ON_DEMANDPOSTERS: OnDemandPostersApi,
        TagValues.ON_DEMANDVIDEOS: OnDemandVideosApi,
        TagValues.PORTFOLIOSESSENTIALS: PortfoliosEssentialsApi,
        TagValues.USERSESSENTIALS: UsersEssentialsApi,
        TagValues.VIDEOSUPLOADS: VideosUploadsApi,
        TagValues.WEBINAREMAILS: WebinarEmailsApi,
        TagValues.FOLDERSITEMS: FoldersItemsApi,
        TagValues.LIVEEVENT_ACTIVATION: LiveEventActivationApi,
        TagValues.LIVEEVENT_AUTOMATED_CLOSED_CAPTIONS: LiveEventAutomatedClosedCaptionsApi,
        TagValues.LIVEEVENT_END: LiveEventEndApi,
        TagValues.LIVEEVENT_LOW_LATENCY: LiveEventLowLatencyApi,
        TagValues.ON_DEMANDPURCHASES_AND_RENTALS: OnDemandPurchasesAndRentalsApi,
        TagValues.ON_DEMANDSEASONS: OnDemandSeasonsApi,
        TagValues.PAYMENTSESSENTIALS: PaymentsEssentialsApi,
        TagValues.TEAMSMEMBERS: TeamsMembersApi,
        TagValues.USERSWATCH_HISTORY: UsersWatchHistoryApi,
        TagValues.VIDEOSEMBED_PRIVACY: VideosEmbedPrivacyApi,
        TagValues.VIDEOSFRAGMENTS: VideosFragmentsApi,
        TagValues.AUTHENTICATION_EXTRASESSENTIALS: AuthenticationExtrasEssentialsApi,
        TagValues.CATEGORIESESSENTIALS: CategoriesEssentialsApi,
        TagValues.EMBED_PRESETSTIMELINE_EVENTS: EmbedPresetsTimelineEventsApi,
        TagValues.LIVEEVENT_M3U8_PLAYBACK: LiveEventM3U8PlaybackApi,
        TagValues.USERSANALYTICS: UsersAnalyticsApi,
        TagValues.USERSFEEDS: UsersFeedsApi,
        TagValues.VIDEOSLIVE_M3U8_PLAYBACK: VideosLiveM3U8PlaybackApi,
        TagValues.VIDEOSNONDESTRUCTIVE_TRIMMING: VideosNondestructiveTrimmingApi,
        TagValues.VIDEOSSHOWCASES: VideosShowcasesApi,
        TagValues.API_INFORMATIONESSENTIALS: APIInformationEssentialsApi,
        TagValues.AUTHENTICATION_EXTRASAUTHENTICATE: AuthenticationExtrasAuthenticateApi,
        TagValues.AUTHENTICATION_EXTRASCONVERT: AuthenticationExtrasConvertApi,
        TagValues.AUTHENTICATION_EXTRASEXCHANGE: AuthenticationExtrasExchangeApi,
        TagValues.CATEGORIESCHANNELS: CategoriesChannelsApi,
        TagValues.CATEGORIESGROUPS: CategoriesGroupsApi,
        TagValues.LIVEEVENT_SESSIONS: LiveEventSessionsApi,
        TagValues.SUBSCRIPTION_PLANSESSENTIALS: SubscriptionPlansEssentialsApi,
        TagValues.TAGSESSENTIALS: TagsEssentialsApi,
        TagValues.TUTORIALESSENTIALS: TutorialEssentialsApi,
        TagValues.USERSSEARCH: UsersSearchApi,
        TagValues.VIDEOSCONTENT_RATINGS: VideosContentRatingsApi,
        TagValues.VIDEOSCREATIVE_COMMONS: VideosCreativeCommonsApi,
        TagValues.VIDEOSLANGUAGES: VideosLanguagesApi,
        TagValues.VIDEOSRECOMMENDATIONS: VideosRecommendationsApi,
        TagValues.VIDEOSTRANSCRIPTS: VideosTranscriptsApi,
    }
)
