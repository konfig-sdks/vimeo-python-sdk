import typing_extensions

from vimeo_python_sdk.paths import PathValues
from vimeo_python_sdk.apis.paths.root import Root
from vimeo_python_sdk.apis.paths.albums_album_id_available_videos import AlbumsAlbumIdAvailableVideos
from vimeo_python_sdk.apis.paths.categories import Categories
from vimeo_python_sdk.apis.paths.categories_category import CategoriesCategory
from vimeo_python_sdk.apis.paths.categories_category_channels import CategoriesCategoryChannels
from vimeo_python_sdk.apis.paths.categories_category_groups import CategoriesCategoryGroups
from vimeo_python_sdk.apis.paths.categories_category_videos import CategoriesCategoryVideos
from vimeo_python_sdk.apis.paths.categories_category_videos_video_id import CategoriesCategoryVideosVideoId
from vimeo_python_sdk.apis.paths.channels import Channels
from vimeo_python_sdk.apis.paths.channels_channel_id import ChannelsChannelId
from vimeo_python_sdk.apis.paths.channels_channel_id_categories import ChannelsChannelIdCategories
from vimeo_python_sdk.apis.paths.channels_channel_id_categories_category import ChannelsChannelIdCategoriesCategory
from vimeo_python_sdk.apis.paths.channels_channel_id_moderators import ChannelsChannelIdModerators
from vimeo_python_sdk.apis.paths.channels_channel_id_moderators_user_id import ChannelsChannelIdModeratorsUserId
from vimeo_python_sdk.apis.paths.channels_channel_id_privacy_users import ChannelsChannelIdPrivacyUsers
from vimeo_python_sdk.apis.paths.channels_channel_id_privacy_users_user_id import ChannelsChannelIdPrivacyUsersUserId
from vimeo_python_sdk.apis.paths.channels_channel_id_tags import ChannelsChannelIdTags
from vimeo_python_sdk.apis.paths.channels_channel_id_tags_word import ChannelsChannelIdTagsWord
from vimeo_python_sdk.apis.paths.channels_channel_id_users import ChannelsChannelIdUsers
from vimeo_python_sdk.apis.paths.channels_channel_id_videos import ChannelsChannelIdVideos
from vimeo_python_sdk.apis.paths.channels_channel_id_videos_video_id import ChannelsChannelIdVideosVideoId
from vimeo_python_sdk.apis.paths.channels_channel_id_videos_video_id_comments import ChannelsChannelIdVideosVideoIdComments
from vimeo_python_sdk.apis.paths.channels_channel_id_videos_video_id_credits import ChannelsChannelIdVideosVideoIdCredits
from vimeo_python_sdk.apis.paths.channels_channel_id_videos_video_id_likes import ChannelsChannelIdVideosVideoIdLikes
from vimeo_python_sdk.apis.paths.channels_channel_id_videos_video_id_pictures import ChannelsChannelIdVideosVideoIdPictures
from vimeo_python_sdk.apis.paths.channels_channel_id_videos_video_id_privacy_users import ChannelsChannelIdVideosVideoIdPrivacyUsers
from vimeo_python_sdk.apis.paths.channels_channel_id_videos_video_id_texttracks import ChannelsChannelIdVideosVideoIdTexttracks
from vimeo_python_sdk.apis.paths.channels_channel_id_videos_video_id_versions import ChannelsChannelIdVideosVideoIdVersions
from vimeo_python_sdk.apis.paths.contentratings import Contentratings
from vimeo_python_sdk.apis.paths.creativecommons import Creativecommons
from vimeo_python_sdk.apis.paths.destination_destination_id import DestinationDestinationId
from vimeo_python_sdk.apis.paths.groups import Groups
from vimeo_python_sdk.apis.paths.groups_group_id import GroupsGroupId
from vimeo_python_sdk.apis.paths.groups_group_id_users import GroupsGroupIdUsers
from vimeo_python_sdk.apis.paths.groups_group_id_videos import GroupsGroupIdVideos
from vimeo_python_sdk.apis.paths.groups_group_id_videos_video_id import GroupsGroupIdVideosVideoId
from vimeo_python_sdk.apis.paths.languages import Languages
from vimeo_python_sdk.apis.paths.live_events import LiveEvents
from vimeo_python_sdk.apis.paths.live_events_live_event_id import LiveEventsLiveEventId
from vimeo_python_sdk.apis.paths.live_events_live_event_id_activate import LiveEventsLiveEventIdActivate
from vimeo_python_sdk.apis.paths.live_events_live_event_id_auto_cc import LiveEventsLiveEventIdAutoCc
from vimeo_python_sdk.apis.paths.live_events_live_event_id_end import LiveEventsLiveEventIdEnd
from vimeo_python_sdk.apis.paths.live_events_live_event_id_low_latency import LiveEventsLiveEventIdLowLatency
from vimeo_python_sdk.apis.paths.live_events_live_event_id_pictures import LiveEventsLiveEventIdPictures
from vimeo_python_sdk.apis.paths.live_events_live_event_id_pictures_thumbnail_id import LiveEventsLiveEventIdPicturesThumbnailId
from vimeo_python_sdk.apis.paths.live_events_live_event_id_privacy_domains import LiveEventsLiveEventIdPrivacyDomains
from vimeo_python_sdk.apis.paths.live_events_live_event_id_videos import LiveEventsLiveEventIdVideos
from vimeo_python_sdk.apis.paths.live_events_live_event_id_videos_video_id import LiveEventsLiveEventIdVideosVideoId
from vimeo_python_sdk.apis.paths.me import Me
from vimeo_python_sdk.apis.paths.me_albums import MeAlbums
from vimeo_python_sdk.apis.paths.me_albums_album_id import MeAlbumsAlbumId
from vimeo_python_sdk.apis.paths.me_albums_album_id_videos import MeAlbumsAlbumIdVideos
from vimeo_python_sdk.apis.paths.me_albums_album_id_videos_video_id import MeAlbumsAlbumIdVideosVideoId
from vimeo_python_sdk.apis.paths.me_albums_album_id_videos_video_id_set_album_thumbnail import MeAlbumsAlbumIdVideosVideoIdSetAlbumThumbnail
from vimeo_python_sdk.apis.paths.me_albums_album_id_videos_video_id_set_featured_video import MeAlbumsAlbumIdVideosVideoIdSetFeaturedVideo
from vimeo_python_sdk.apis.paths.me_analytics import MeAnalytics
from vimeo_python_sdk.apis.paths.me_appearances import MeAppearances
from vimeo_python_sdk.apis.paths.me_categories import MeCategories
from vimeo_python_sdk.apis.paths.me_categories_category import MeCategoriesCategory
from vimeo_python_sdk.apis.paths.me_channels import MeChannels
from vimeo_python_sdk.apis.paths.me_channels_channel_id import MeChannelsChannelId
from vimeo_python_sdk.apis.paths.me_customlogos import MeCustomlogos
from vimeo_python_sdk.apis.paths.me_customlogos_logo_id import MeCustomlogosLogoId
from vimeo_python_sdk.apis.paths.me_destinations import MeDestinations
from vimeo_python_sdk.apis.paths.me_feed import MeFeed
from vimeo_python_sdk.apis.paths.me_followers import MeFollowers
from vimeo_python_sdk.apis.paths.me_following import MeFollowing
from vimeo_python_sdk.apis.paths.me_following_follow_user_id import MeFollowingFollowUserId
from vimeo_python_sdk.apis.paths.me_groups import MeGroups
from vimeo_python_sdk.apis.paths.me_groups_group_id import MeGroupsGroupId
from vimeo_python_sdk.apis.paths.me_likes import MeLikes
from vimeo_python_sdk.apis.paths.me_likes_video_id import MeLikesVideoId
from vimeo_python_sdk.apis.paths.me_live_events import MeLiveEvents
from vimeo_python_sdk.apis.paths.me_live_events_live_event_id import MeLiveEventsLiveEventId
from vimeo_python_sdk.apis.paths.me_live_events_live_event_id_activate import MeLiveEventsLiveEventIdActivate
from vimeo_python_sdk.apis.paths.me_live_events_live_event_id_auto_cc import MeLiveEventsLiveEventIdAutoCc
from vimeo_python_sdk.apis.paths.me_live_events_live_event_id_destinations import MeLiveEventsLiveEventIdDestinations
from vimeo_python_sdk.apis.paths.me_live_events_live_event_id_end import MeLiveEventsLiveEventIdEnd
from vimeo_python_sdk.apis.paths.me_live_events_live_event_id_low_latency import MeLiveEventsLiveEventIdLowLatency
from vimeo_python_sdk.apis.paths.me_live_events_live_event_id_m3u8_playback import MeLiveEventsLiveEventIdM3u8Playback
from vimeo_python_sdk.apis.paths.me_live_events_live_event_id_pictures import MeLiveEventsLiveEventIdPictures
from vimeo_python_sdk.apis.paths.me_live_events_live_event_id_pictures_thumbnail_id import MeLiveEventsLiveEventIdPicturesThumbnailId
from vimeo_python_sdk.apis.paths.me_live_events_live_event_id_privacy_domains import MeLiveEventsLiveEventIdPrivacyDomains
from vimeo_python_sdk.apis.paths.me_live_events_live_event_id_videos import MeLiveEventsLiveEventIdVideos
from vimeo_python_sdk.apis.paths.me_live_events_live_event_id_videos_video_id import MeLiveEventsLiveEventIdVideosVideoId
from vimeo_python_sdk.apis.paths.me_ondemand_pages import MeOndemandPages
from vimeo_python_sdk.apis.paths.me_ondemand_purchases import MeOndemandPurchases
from vimeo_python_sdk.apis.paths.me_ondemand_purchases_ondemand_id import MeOndemandPurchasesOndemandId
from vimeo_python_sdk.apis.paths.me_payment_methods import MePaymentMethods
from vimeo_python_sdk.apis.paths.me_payment_methods_payment_method_id import MePaymentMethodsPaymentMethodId
from vimeo_python_sdk.apis.paths.me_pictures import MePictures
from vimeo_python_sdk.apis.paths.me_pictures_portraitset_id import MePicturesPortraitsetId
from vimeo_python_sdk.apis.paths.me_portfolios import MePortfolios
from vimeo_python_sdk.apis.paths.me_portfolios_portfolio_id import MePortfoliosPortfolioId
from vimeo_python_sdk.apis.paths.me_portfolios_portfolio_id_videos import MePortfoliosPortfolioIdVideos
from vimeo_python_sdk.apis.paths.me_portfolios_portfolio_id_videos_video_id import MePortfoliosPortfolioIdVideosVideoId
from vimeo_python_sdk.apis.paths.me_presets import MePresets
from vimeo_python_sdk.apis.paths.me_presets_preset_id import MePresetsPresetId
from vimeo_python_sdk.apis.paths.me_presets_preset_id_videos import MePresetsPresetIdVideos
from vimeo_python_sdk.apis.paths.me_projects import MeProjects
from vimeo_python_sdk.apis.paths.me_projects_project_id import MeProjectsProjectId
from vimeo_python_sdk.apis.paths.me_projects_project_id_items import MeProjectsProjectIdItems
from vimeo_python_sdk.apis.paths.me_projects_project_id_videos import MeProjectsProjectIdVideos
from vimeo_python_sdk.apis.paths.me_projects_project_id_videos_video_id import MeProjectsProjectIdVideosVideoId
from vimeo_python_sdk.apis.paths.me_videos import MeVideos
from vimeo_python_sdk.apis.paths.me_videos_video_id import MeVideosVideoId
from vimeo_python_sdk.apis.paths.me_videos_video_id_destinations import MeVideosVideoIdDestinations
from vimeo_python_sdk.apis.paths.me_videos_video_id_m3u8_playback import MeVideosVideoIdM3u8Playback
from vimeo_python_sdk.apis.paths.me_watched_videos import MeWatchedVideos
from vimeo_python_sdk.apis.paths.me_watched_videos_video_id import MeWatchedVideosVideoId
from vimeo_python_sdk.apis.paths.me_watchlater import MeWatchlater
from vimeo_python_sdk.apis.paths.me_watchlater_video_id import MeWatchlaterVideoId
from vimeo_python_sdk.apis.paths.me_webinars import MeWebinars
from vimeo_python_sdk.apis.paths.me_webinars_webinar_id import MeWebinarsWebinarId
from vimeo_python_sdk.apis.paths.me_webinars_webinar_id_email_settings import MeWebinarsWebinarIdEmailSettings
from vimeo_python_sdk.apis.paths.me_webinars_webinar_id_registrants import MeWebinarsWebinarIdRegistrants
from vimeo_python_sdk.apis.paths.me_webinars_webinar_id_registrants_registrant_id import MeWebinarsWebinarIdRegistrantsRegistrantId
from vimeo_python_sdk.apis.paths.oauth_access_token import OauthAccessToken
from vimeo_python_sdk.apis.paths.oauth_authorize_client import OauthAuthorizeClient
from vimeo_python_sdk.apis.paths.oauth_authorize_vimeo_oauth1 import OauthAuthorizeVimeoOauth1
from vimeo_python_sdk.apis.paths.oauth_verify import OauthVerify
from vimeo_python_sdk.apis.paths.ondemand_genres import OndemandGenres
from vimeo_python_sdk.apis.paths.ondemand_genres_genre_id import OndemandGenresGenreId
from vimeo_python_sdk.apis.paths.ondemand_genres_genre_id_pages import OndemandGenresGenreIdPages
from vimeo_python_sdk.apis.paths.ondemand_genres_genre_id_pages_ondemand_id import OndemandGenresGenreIdPagesOndemandId
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id import OndemandPagesOndemandId
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_backgrounds import OndemandPagesOndemandIdBackgrounds
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_backgrounds_background_id import OndemandPagesOndemandIdBackgroundsBackgroundId
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_genres import OndemandPagesOndemandIdGenres
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_genres_genre_id import OndemandPagesOndemandIdGenresGenreId
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_likes import OndemandPagesOndemandIdLikes
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_pictures import OndemandPagesOndemandIdPictures
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_pictures_poster_id import OndemandPagesOndemandIdPicturesPosterId
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_promotions import OndemandPagesOndemandIdPromotions
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_promotions_promotion_id import OndemandPagesOndemandIdPromotionsPromotionId
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_promotions_promotion_id_codes import OndemandPagesOndemandIdPromotionsPromotionIdCodes
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_regions import OndemandPagesOndemandIdRegions
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_regions_country import OndemandPagesOndemandIdRegionsCountry
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_seasons import OndemandPagesOndemandIdSeasons
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_seasons_season_id import OndemandPagesOndemandIdSeasonsSeasonId
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_seasons_season_id_videos import OndemandPagesOndemandIdSeasonsSeasonIdVideos
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_videos import OndemandPagesOndemandIdVideos
from vimeo_python_sdk.apis.paths.ondemand_pages_ondemand_id_videos_video_id import OndemandPagesOndemandIdVideosVideoId
from vimeo_python_sdk.apis.paths.ondemand_regions import OndemandRegions
from vimeo_python_sdk.apis.paths.ondemand_regions_country import OndemandRegionsCountry
from vimeo_python_sdk.apis.paths.subscription_plans_tier import SubscriptionPlansTier
from vimeo_python_sdk.apis.paths.tags_word import TagsWord
from vimeo_python_sdk.apis.paths.tags_word_videos import TagsWordVideos
from vimeo_python_sdk.apis.paths.teammembers_code import TeammembersCode
from vimeo_python_sdk.apis.paths.tokens import Tokens
from vimeo_python_sdk.apis.paths.tutorial import Tutorial
from vimeo_python_sdk.apis.paths.users import Users
from vimeo_python_sdk.apis.paths.users_owner_id_folders_private_to_me import UsersOwnerIdFoldersPrivateToMe
from vimeo_python_sdk.apis.paths.users_user_id import UsersUserId
from vimeo_python_sdk.apis.paths.users_user_id_albums import UsersUserIdAlbums
from vimeo_python_sdk.apis.paths.users_user_id_albums_album_id import UsersUserIdAlbumsAlbumId
from vimeo_python_sdk.apis.paths.users_user_id_albums_album_id_custom_thumbnails import UsersUserIdAlbumsAlbumIdCustomThumbnails
from vimeo_python_sdk.apis.paths.users_user_id_albums_album_id_custom_thumbnails_thumbnail_id import UsersUserIdAlbumsAlbumIdCustomThumbnailsThumbnailId
from vimeo_python_sdk.apis.paths.users_user_id_albums_album_id_logos import UsersUserIdAlbumsAlbumIdLogos
from vimeo_python_sdk.apis.paths.users_user_id_albums_album_id_logos_logo_id import UsersUserIdAlbumsAlbumIdLogosLogoId
from vimeo_python_sdk.apis.paths.users_user_id_albums_album_id_videos import UsersUserIdAlbumsAlbumIdVideos
from vimeo_python_sdk.apis.paths.users_user_id_albums_album_id_videos_video_id import UsersUserIdAlbumsAlbumIdVideosVideoId
from vimeo_python_sdk.apis.paths.users_user_id_albums_album_id_videos_video_id_set_album_thumbnail import UsersUserIdAlbumsAlbumIdVideosVideoIdSetAlbumThumbnail
from vimeo_python_sdk.apis.paths.users_user_id_albums_album_id_videos_video_id_set_featured_video import UsersUserIdAlbumsAlbumIdVideosVideoIdSetFeaturedVideo
from vimeo_python_sdk.apis.paths.users_user_id_analytics import UsersUserIdAnalytics
from vimeo_python_sdk.apis.paths.users_user_id_appearances import UsersUserIdAppearances
from vimeo_python_sdk.apis.paths.users_user_id_categories import UsersUserIdCategories
from vimeo_python_sdk.apis.paths.users_user_id_categories_category import UsersUserIdCategoriesCategory
from vimeo_python_sdk.apis.paths.users_user_id_channels import UsersUserIdChannels
from vimeo_python_sdk.apis.paths.users_user_id_channels_channel_id import UsersUserIdChannelsChannelId
from vimeo_python_sdk.apis.paths.users_user_id_customlogos import UsersUserIdCustomlogos
from vimeo_python_sdk.apis.paths.users_user_id_customlogos_logo_id import UsersUserIdCustomlogosLogoId
from vimeo_python_sdk.apis.paths.users_user_id_destinations import UsersUserIdDestinations
from vimeo_python_sdk.apis.paths.users_user_id_feed import UsersUserIdFeed
from vimeo_python_sdk.apis.paths.users_user_id_followers import UsersUserIdFollowers
from vimeo_python_sdk.apis.paths.users_user_id_following import UsersUserIdFollowing
from vimeo_python_sdk.apis.paths.users_user_id_following_follow_user_id import UsersUserIdFollowingFollowUserId
from vimeo_python_sdk.apis.paths.users_user_id_groups import UsersUserIdGroups
from vimeo_python_sdk.apis.paths.users_user_id_groups_group_id import UsersUserIdGroupsGroupId
from vimeo_python_sdk.apis.paths.users_user_id_likes import UsersUserIdLikes
from vimeo_python_sdk.apis.paths.users_user_id_likes_video_id import UsersUserIdLikesVideoId
from vimeo_python_sdk.apis.paths.users_user_id_live_events import UsersUserIdLiveEvents
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id import UsersUserIdLiveEventsLiveEventId
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_activate import UsersUserIdLiveEventsLiveEventIdActivate
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_auto_cc import UsersUserIdLiveEventsLiveEventIdAutoCc
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_destinations import UsersUserIdLiveEventsLiveEventIdDestinations
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_end import UsersUserIdLiveEventsLiveEventIdEnd
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_low_latency import UsersUserIdLiveEventsLiveEventIdLowLatency
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_m3u8_playback import UsersUserIdLiveEventsLiveEventIdM3u8Playback
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_ott_destination_destination_id import UsersUserIdLiveEventsLiveEventIdOttDestinationDestinationId
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_ott_destinations import UsersUserIdLiveEventsLiveEventIdOttDestinations
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_pictures import UsersUserIdLiveEventsLiveEventIdPictures
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_pictures_thumbnail_id import UsersUserIdLiveEventsLiveEventIdPicturesThumbnailId
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_privacy_domains import UsersUserIdLiveEventsLiveEventIdPrivacyDomains
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_videos import UsersUserIdLiveEventsLiveEventIdVideos
from vimeo_python_sdk.apis.paths.users_user_id_live_events_live_event_id_videos_video_id import UsersUserIdLiveEventsLiveEventIdVideosVideoId
from vimeo_python_sdk.apis.paths.users_user_id_ondemand_pages import UsersUserIdOndemandPages
from vimeo_python_sdk.apis.paths.users_user_id_ondemand_purchases import UsersUserIdOndemandPurchases
from vimeo_python_sdk.apis.paths.users_user_id_pictures import UsersUserIdPictures
from vimeo_python_sdk.apis.paths.users_user_id_pictures_portraitset_id import UsersUserIdPicturesPortraitsetId
from vimeo_python_sdk.apis.paths.users_user_id_portfolios import UsersUserIdPortfolios
from vimeo_python_sdk.apis.paths.users_user_id_portfolios_portfolio_id import UsersUserIdPortfoliosPortfolioId
from vimeo_python_sdk.apis.paths.users_user_id_portfolios_portfolio_id_videos import UsersUserIdPortfoliosPortfolioIdVideos
from vimeo_python_sdk.apis.paths.users_user_id_portfolios_portfolio_id_videos_video_id import UsersUserIdPortfoliosPortfolioIdVideosVideoId
from vimeo_python_sdk.apis.paths.users_user_id_presets import UsersUserIdPresets
from vimeo_python_sdk.apis.paths.users_user_id_presets_preset_id import UsersUserIdPresetsPresetId
from vimeo_python_sdk.apis.paths.users_user_id_presets_preset_id_videos import UsersUserIdPresetsPresetIdVideos
from vimeo_python_sdk.apis.paths.users_user_id_projects import UsersUserIdProjects
from vimeo_python_sdk.apis.paths.users_user_id_projects_project_id import UsersUserIdProjectsProjectId
from vimeo_python_sdk.apis.paths.users_user_id_projects_project_id_items import UsersUserIdProjectsProjectIdItems
from vimeo_python_sdk.apis.paths.users_user_id_projects_project_id_videos import UsersUserIdProjectsProjectIdVideos
from vimeo_python_sdk.apis.paths.users_user_id_projects_project_id_videos_video_id import UsersUserIdProjectsProjectIdVideosVideoId
from vimeo_python_sdk.apis.paths.users_user_id_team_role import UsersUserIdTeamRole
from vimeo_python_sdk.apis.paths.users_user_id_team_users_team_user_id import UsersUserIdTeamUsersTeamUserId
from vimeo_python_sdk.apis.paths.users_user_id_uploads_upload_id import UsersUserIdUploadsUploadId
from vimeo_python_sdk.apis.paths.users_user_id_videos import UsersUserIdVideos
from vimeo_python_sdk.apis.paths.users_user_id_videos_video_id import UsersUserIdVideosVideoId
from vimeo_python_sdk.apis.paths.users_user_id_videos_video_id_destinations import UsersUserIdVideosVideoIdDestinations
from vimeo_python_sdk.apis.paths.users_user_id_videos_video_id_m3u8_playback import UsersUserIdVideosVideoIdM3u8Playback
from vimeo_python_sdk.apis.paths.users_user_id_watchlater import UsersUserIdWatchlater
from vimeo_python_sdk.apis.paths.users_user_id_watchlater_video_id import UsersUserIdWatchlaterVideoId
from vimeo_python_sdk.apis.paths.users_user_id_webinars import UsersUserIdWebinars
from vimeo_python_sdk.apis.paths.users_user_id_webinars_webinar_id import UsersUserIdWebinarsWebinarId
from vimeo_python_sdk.apis.paths.users_user_id_webinars_webinar_id_email_settings import UsersUserIdWebinarsWebinarIdEmailSettings
from vimeo_python_sdk.apis.paths.users_user_id_webinars_webinar_id_registrants import UsersUserIdWebinarsWebinarIdRegistrants
from vimeo_python_sdk.apis.paths.users_user_id_webinars_webinar_id_registrants_registrant_id import UsersUserIdWebinarsWebinarIdRegistrantsRegistrantId
from vimeo_python_sdk.apis.paths.videos import Videos
from vimeo_python_sdk.apis.paths.videos_video_id import VideosVideoId
from vimeo_python_sdk.apis.paths.videos_video_id_albums import VideosVideoIdAlbums
from vimeo_python_sdk.apis.paths.videos_video_id_animated_thumbsets import VideosVideoIdAnimatedThumbsets
from vimeo_python_sdk.apis.paths.videos_video_id_animated_thumbsets_picture_id import VideosVideoIdAnimatedThumbsetsPictureId
from vimeo_python_sdk.apis.paths.videos_video_id_animated_thumbsets_picture_id_status import VideosVideoIdAnimatedThumbsetsPictureIdStatus
from vimeo_python_sdk.apis.paths.videos_video_id_available_albums import VideosVideoIdAvailableAlbums
from vimeo_python_sdk.apis.paths.videos_video_id_available_channels import VideosVideoIdAvailableChannels
from vimeo_python_sdk.apis.paths.videos_video_id_categories import VideosVideoIdCategories
from vimeo_python_sdk.apis.paths.videos_video_id_chapters import VideosVideoIdChapters
from vimeo_python_sdk.apis.paths.videos_video_id_chapters_temporary_pictures import VideosVideoIdChaptersTemporaryPictures
from vimeo_python_sdk.apis.paths.videos_video_id_chapters_temporary_pictures_uid import VideosVideoIdChaptersTemporaryPicturesUid
from vimeo_python_sdk.apis.paths.videos_video_id_chapters_chapter_id import VideosVideoIdChaptersChapterId
from vimeo_python_sdk.apis.paths.videos_video_id_chapters_chapter_id_pictures import VideosVideoIdChaptersChapterIdPictures
from vimeo_python_sdk.apis.paths.videos_video_id_chapters_chapter_id_pictures_uid import VideosVideoIdChaptersChapterIdPicturesUid
from vimeo_python_sdk.apis.paths.videos_video_id_comments import VideosVideoIdComments
from vimeo_python_sdk.apis.paths.videos_video_id_comments_comment_id import VideosVideoIdCommentsCommentId
from vimeo_python_sdk.apis.paths.videos_video_id_comments_comment_id_replies import VideosVideoIdCommentsCommentIdReplies
from vimeo_python_sdk.apis.paths.videos_video_id_credits import VideosVideoIdCredits
from vimeo_python_sdk.apis.paths.videos_video_id_credits_available_users import VideosVideoIdCreditsAvailableUsers
from vimeo_python_sdk.apis.paths.videos_video_id_credits_credit_id import VideosVideoIdCreditsCreditId
from vimeo_python_sdk.apis.paths.videos_video_id_fragments import VideosVideoIdFragments
from vimeo_python_sdk.apis.paths.videos_video_id_likes import VideosVideoIdLikes
from vimeo_python_sdk.apis.paths.videos_video_id_pictures import VideosVideoIdPictures
from vimeo_python_sdk.apis.paths.videos_video_id_pictures_picture_id import VideosVideoIdPicturesPictureId
from vimeo_python_sdk.apis.paths.videos_video_id_presets_preset_id import VideosVideoIdPresetsPresetId
from vimeo_python_sdk.apis.paths.videos_video_id_privacy_domains import VideosVideoIdPrivacyDomains
from vimeo_python_sdk.apis.paths.videos_video_id_privacy_domains_domain import VideosVideoIdPrivacyDomainsDomain
from vimeo_python_sdk.apis.paths.videos_video_id_privacy_users import VideosVideoIdPrivacyUsers
from vimeo_python_sdk.apis.paths.videos_video_id_privacy_users_user_id import VideosVideoIdPrivacyUsersUserId
from vimeo_python_sdk.apis.paths.videos_video_id_sessions_status import VideosVideoIdSessionsStatus
from vimeo_python_sdk.apis.paths.videos_video_id_tags import VideosVideoIdTags
from vimeo_python_sdk.apis.paths.videos_video_id_tags_word import VideosVideoIdTagsWord
from vimeo_python_sdk.apis.paths.videos_video_id_texttracks import VideosVideoIdTexttracks
from vimeo_python_sdk.apis.paths.videos_video_id_texttracks_texttrack_id import VideosVideoIdTexttracksTexttrackId
from vimeo_python_sdk.apis.paths.videos_video_id_timelinethumbnails import VideosVideoIdTimelinethumbnails
from vimeo_python_sdk.apis.paths.videos_video_id_timelinethumbnails_thumbnail_id import VideosVideoIdTimelinethumbnailsThumbnailId
from vimeo_python_sdk.apis.paths.videos_video_id_transcripts_texttrack_id import VideosVideoIdTranscriptsTexttrackId
from vimeo_python_sdk.apis.paths.videos_video_id_trim import VideosVideoIdTrim
from vimeo_python_sdk.apis.paths.videos_video_id_versions import VideosVideoIdVersions
from vimeo_python_sdk.apis.paths.videos_video_id_versions_version_id import VideosVideoIdVersionsVersionId
from vimeo_python_sdk.apis.paths.videos_video_id_videos import VideosVideoIdVideos
from vimeo_python_sdk.apis.paths.webinars_webinar_id import WebinarsWebinarId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues._: Root,
        PathValues.ALBUMS_ALBUM_ID_AVAILABLE_VIDEOS: AlbumsAlbumIdAvailableVideos,
        PathValues.CATEGORIES: Categories,
        PathValues.CATEGORIES_CATEGORY: CategoriesCategory,
        PathValues.CATEGORIES_CATEGORY_CHANNELS: CategoriesCategoryChannels,
        PathValues.CATEGORIES_CATEGORY_GROUPS: CategoriesCategoryGroups,
        PathValues.CATEGORIES_CATEGORY_VIDEOS: CategoriesCategoryVideos,
        PathValues.CATEGORIES_CATEGORY_VIDEOS_VIDEO_ID: CategoriesCategoryVideosVideoId,
        PathValues.CHANNELS: Channels,
        PathValues.CHANNELS_CHANNEL_ID: ChannelsChannelId,
        PathValues.CHANNELS_CHANNEL_ID_CATEGORIES: ChannelsChannelIdCategories,
        PathValues.CHANNELS_CHANNEL_ID_CATEGORIES_CATEGORY: ChannelsChannelIdCategoriesCategory,
        PathValues.CHANNELS_CHANNEL_ID_MODERATORS: ChannelsChannelIdModerators,
        PathValues.CHANNELS_CHANNEL_ID_MODERATORS_USER_ID: ChannelsChannelIdModeratorsUserId,
        PathValues.CHANNELS_CHANNEL_ID_PRIVACY_USERS: ChannelsChannelIdPrivacyUsers,
        PathValues.CHANNELS_CHANNEL_ID_PRIVACY_USERS_USER_ID: ChannelsChannelIdPrivacyUsersUserId,
        PathValues.CHANNELS_CHANNEL_ID_TAGS: ChannelsChannelIdTags,
        PathValues.CHANNELS_CHANNEL_ID_TAGS_WORD: ChannelsChannelIdTagsWord,
        PathValues.CHANNELS_CHANNEL_ID_USERS: ChannelsChannelIdUsers,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS: ChannelsChannelIdVideos,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID: ChannelsChannelIdVideosVideoId,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_COMMENTS: ChannelsChannelIdVideosVideoIdComments,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_CREDITS: ChannelsChannelIdVideosVideoIdCredits,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_LIKES: ChannelsChannelIdVideosVideoIdLikes,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_PICTURES: ChannelsChannelIdVideosVideoIdPictures,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_PRIVACY_USERS: ChannelsChannelIdVideosVideoIdPrivacyUsers,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_TEXTTRACKS: ChannelsChannelIdVideosVideoIdTexttracks,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_VERSIONS: ChannelsChannelIdVideosVideoIdVersions,
        PathValues.CONTENTRATINGS: Contentratings,
        PathValues.CREATIVECOMMONS: Creativecommons,
        PathValues.DESTINATION_DESTINATION_ID: DestinationDestinationId,
        PathValues.GROUPS: Groups,
        PathValues.GROUPS_GROUP_ID: GroupsGroupId,
        PathValues.GROUPS_GROUP_ID_USERS: GroupsGroupIdUsers,
        PathValues.GROUPS_GROUP_ID_VIDEOS: GroupsGroupIdVideos,
        PathValues.GROUPS_GROUP_ID_VIDEOS_VIDEO_ID: GroupsGroupIdVideosVideoId,
        PathValues.LANGUAGES: Languages,
        PathValues.LIVE_EVENTS: LiveEvents,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID: LiveEventsLiveEventId,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_ACTIVATE: LiveEventsLiveEventIdActivate,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_AUTO_CC: LiveEventsLiveEventIdAutoCc,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_END: LiveEventsLiveEventIdEnd,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_LOW_LATENCY: LiveEventsLiveEventIdLowLatency,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_PICTURES: LiveEventsLiveEventIdPictures,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_PICTURES_THUMBNAIL_ID: LiveEventsLiveEventIdPicturesThumbnailId,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_PRIVACY_DOMAINS: LiveEventsLiveEventIdPrivacyDomains,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_VIDEOS: LiveEventsLiveEventIdVideos,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_VIDEOS_VIDEO_ID: LiveEventsLiveEventIdVideosVideoId,
        PathValues.ME: Me,
        PathValues.ME_ALBUMS: MeAlbums,
        PathValues.ME_ALBUMS_ALBUM_ID: MeAlbumsAlbumId,
        PathValues.ME_ALBUMS_ALBUM_ID_VIDEOS: MeAlbumsAlbumIdVideos,
        PathValues.ME_ALBUMS_ALBUM_ID_VIDEOS_VIDEO_ID: MeAlbumsAlbumIdVideosVideoId,
        PathValues.ME_ALBUMS_ALBUM_ID_VIDEOS_VIDEO_ID_SET_ALBUM_THUMBNAIL: MeAlbumsAlbumIdVideosVideoIdSetAlbumThumbnail,
        PathValues.ME_ALBUMS_ALBUM_ID_VIDEOS_VIDEO_ID_SET_FEATURED_VIDEO: MeAlbumsAlbumIdVideosVideoIdSetFeaturedVideo,
        PathValues.ME_ANALYTICS: MeAnalytics,
        PathValues.ME_APPEARANCES: MeAppearances,
        PathValues.ME_CATEGORIES: MeCategories,
        PathValues.ME_CATEGORIES_CATEGORY: MeCategoriesCategory,
        PathValues.ME_CHANNELS: MeChannels,
        PathValues.ME_CHANNELS_CHANNEL_ID: MeChannelsChannelId,
        PathValues.ME_CUSTOMLOGOS: MeCustomlogos,
        PathValues.ME_CUSTOMLOGOS_LOGO_ID: MeCustomlogosLogoId,
        PathValues.ME_DESTINATIONS: MeDestinations,
        PathValues.ME_FEED: MeFeed,
        PathValues.ME_FOLLOWERS: MeFollowers,
        PathValues.ME_FOLLOWING: MeFollowing,
        PathValues.ME_FOLLOWING_FOLLOW_USER_ID: MeFollowingFollowUserId,
        PathValues.ME_GROUPS: MeGroups,
        PathValues.ME_GROUPS_GROUP_ID: MeGroupsGroupId,
        PathValues.ME_LIKES: MeLikes,
        PathValues.ME_LIKES_VIDEO_ID: MeLikesVideoId,
        PathValues.ME_LIVE_EVENTS: MeLiveEvents,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID: MeLiveEventsLiveEventId,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_ACTIVATE: MeLiveEventsLiveEventIdActivate,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_AUTO_CC: MeLiveEventsLiveEventIdAutoCc,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_DESTINATIONS: MeLiveEventsLiveEventIdDestinations,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_END: MeLiveEventsLiveEventIdEnd,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_LOW_LATENCY: MeLiveEventsLiveEventIdLowLatency,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_M3U8_PLAYBACK: MeLiveEventsLiveEventIdM3u8Playback,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_PICTURES: MeLiveEventsLiveEventIdPictures,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_PICTURES_THUMBNAIL_ID: MeLiveEventsLiveEventIdPicturesThumbnailId,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_PRIVACY_DOMAINS: MeLiveEventsLiveEventIdPrivacyDomains,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_VIDEOS: MeLiveEventsLiveEventIdVideos,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_VIDEOS_VIDEO_ID: MeLiveEventsLiveEventIdVideosVideoId,
        PathValues.ME_ONDEMAND_PAGES: MeOndemandPages,
        PathValues.ME_ONDEMAND_PURCHASES: MeOndemandPurchases,
        PathValues.ME_ONDEMAND_PURCHASES_ONDEMAND_ID: MeOndemandPurchasesOndemandId,
        PathValues.ME_PAYMENT_METHODS: MePaymentMethods,
        PathValues.ME_PAYMENT_METHODS_PAYMENT_METHOD_ID: MePaymentMethodsPaymentMethodId,
        PathValues.ME_PICTURES: MePictures,
        PathValues.ME_PICTURES_PORTRAITSET_ID: MePicturesPortraitsetId,
        PathValues.ME_PORTFOLIOS: MePortfolios,
        PathValues.ME_PORTFOLIOS_PORTFOLIO_ID: MePortfoliosPortfolioId,
        PathValues.ME_PORTFOLIOS_PORTFOLIO_ID_VIDEOS: MePortfoliosPortfolioIdVideos,
        PathValues.ME_PORTFOLIOS_PORTFOLIO_ID_VIDEOS_VIDEO_ID: MePortfoliosPortfolioIdVideosVideoId,
        PathValues.ME_PRESETS: MePresets,
        PathValues.ME_PRESETS_PRESET_ID: MePresetsPresetId,
        PathValues.ME_PRESETS_PRESET_ID_VIDEOS: MePresetsPresetIdVideos,
        PathValues.ME_PROJECTS: MeProjects,
        PathValues.ME_PROJECTS_PROJECT_ID: MeProjectsProjectId,
        PathValues.ME_PROJECTS_PROJECT_ID_ITEMS: MeProjectsProjectIdItems,
        PathValues.ME_PROJECTS_PROJECT_ID_VIDEOS: MeProjectsProjectIdVideos,
        PathValues.ME_PROJECTS_PROJECT_ID_VIDEOS_VIDEO_ID: MeProjectsProjectIdVideosVideoId,
        PathValues.ME_VIDEOS: MeVideos,
        PathValues.ME_VIDEOS_VIDEO_ID: MeVideosVideoId,
        PathValues.ME_VIDEOS_VIDEO_ID_DESTINATIONS: MeVideosVideoIdDestinations,
        PathValues.ME_VIDEOS_VIDEO_ID_M3U8_PLAYBACK: MeVideosVideoIdM3u8Playback,
        PathValues.ME_WATCHED_VIDEOS: MeWatchedVideos,
        PathValues.ME_WATCHED_VIDEOS_VIDEO_ID: MeWatchedVideosVideoId,
        PathValues.ME_WATCHLATER: MeWatchlater,
        PathValues.ME_WATCHLATER_VIDEO_ID: MeWatchlaterVideoId,
        PathValues.ME_WEBINARS: MeWebinars,
        PathValues.ME_WEBINARS_WEBINAR_ID: MeWebinarsWebinarId,
        PathValues.ME_WEBINARS_WEBINAR_ID_EMAIL_SETTINGS: MeWebinarsWebinarIdEmailSettings,
        PathValues.ME_WEBINARS_WEBINAR_ID_REGISTRANTS: MeWebinarsWebinarIdRegistrants,
        PathValues.ME_WEBINARS_WEBINAR_ID_REGISTRANTS_REGISTRANT_ID: MeWebinarsWebinarIdRegistrantsRegistrantId,
        PathValues.OAUTH_ACCESS_TOKEN: OauthAccessToken,
        PathValues.OAUTH_AUTHORIZE_CLIENT: OauthAuthorizeClient,
        PathValues.OAUTH_AUTHORIZE_VIMEO_OAUTH1: OauthAuthorizeVimeoOauth1,
        PathValues.OAUTH_VERIFY: OauthVerify,
        PathValues.ONDEMAND_GENRES: OndemandGenres,
        PathValues.ONDEMAND_GENRES_GENRE_ID: OndemandGenresGenreId,
        PathValues.ONDEMAND_GENRES_GENRE_ID_PAGES: OndemandGenresGenreIdPages,
        PathValues.ONDEMAND_GENRES_GENRE_ID_PAGES_ONDEMAND_ID: OndemandGenresGenreIdPagesOndemandId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID: OndemandPagesOndemandId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_BACKGROUNDS: OndemandPagesOndemandIdBackgrounds,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_BACKGROUNDS_BACKGROUND_ID: OndemandPagesOndemandIdBackgroundsBackgroundId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_GENRES: OndemandPagesOndemandIdGenres,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_GENRES_GENRE_ID: OndemandPagesOndemandIdGenresGenreId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_LIKES: OndemandPagesOndemandIdLikes,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_PICTURES: OndemandPagesOndemandIdPictures,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_PICTURES_POSTER_ID: OndemandPagesOndemandIdPicturesPosterId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_PROMOTIONS: OndemandPagesOndemandIdPromotions,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_PROMOTIONS_PROMOTION_ID: OndemandPagesOndemandIdPromotionsPromotionId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_PROMOTIONS_PROMOTION_ID_CODES: OndemandPagesOndemandIdPromotionsPromotionIdCodes,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_REGIONS: OndemandPagesOndemandIdRegions,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_REGIONS_COUNTRY: OndemandPagesOndemandIdRegionsCountry,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_SEASONS: OndemandPagesOndemandIdSeasons,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_SEASONS_SEASON_ID: OndemandPagesOndemandIdSeasonsSeasonId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_SEASONS_SEASON_ID_VIDEOS: OndemandPagesOndemandIdSeasonsSeasonIdVideos,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_VIDEOS: OndemandPagesOndemandIdVideos,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_VIDEOS_VIDEO_ID: OndemandPagesOndemandIdVideosVideoId,
        PathValues.ONDEMAND_REGIONS: OndemandRegions,
        PathValues.ONDEMAND_REGIONS_COUNTRY: OndemandRegionsCountry,
        PathValues.SUBSCRIPTION_PLANS_TIER: SubscriptionPlansTier,
        PathValues.TAGS_WORD: TagsWord,
        PathValues.TAGS_WORD_VIDEOS: TagsWordVideos,
        PathValues.TEAMMEMBERS_CODE: TeammembersCode,
        PathValues.TOKENS: Tokens,
        PathValues.TUTORIAL: Tutorial,
        PathValues.USERS: Users,
        PathValues.USERS_OWNER_ID_FOLDERS_PRIVATE_TO_ME: UsersOwnerIdFoldersPrivateToMe,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS_USER_ID_ALBUMS: UsersUserIdAlbums,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID: UsersUserIdAlbumsAlbumId,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_CUSTOM_THUMBNAILS: UsersUserIdAlbumsAlbumIdCustomThumbnails,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_CUSTOM_THUMBNAILS_THUMBNAIL_ID: UsersUserIdAlbumsAlbumIdCustomThumbnailsThumbnailId,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_LOGOS: UsersUserIdAlbumsAlbumIdLogos,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_LOGOS_LOGO_ID: UsersUserIdAlbumsAlbumIdLogosLogoId,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_VIDEOS: UsersUserIdAlbumsAlbumIdVideos,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_VIDEOS_VIDEO_ID: UsersUserIdAlbumsAlbumIdVideosVideoId,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_VIDEOS_VIDEO_ID_SET_ALBUM_THUMBNAIL: UsersUserIdAlbumsAlbumIdVideosVideoIdSetAlbumThumbnail,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_VIDEOS_VIDEO_ID_SET_FEATURED_VIDEO: UsersUserIdAlbumsAlbumIdVideosVideoIdSetFeaturedVideo,
        PathValues.USERS_USER_ID_ANALYTICS: UsersUserIdAnalytics,
        PathValues.USERS_USER_ID_APPEARANCES: UsersUserIdAppearances,
        PathValues.USERS_USER_ID_CATEGORIES: UsersUserIdCategories,
        PathValues.USERS_USER_ID_CATEGORIES_CATEGORY: UsersUserIdCategoriesCategory,
        PathValues.USERS_USER_ID_CHANNELS: UsersUserIdChannels,
        PathValues.USERS_USER_ID_CHANNELS_CHANNEL_ID: UsersUserIdChannelsChannelId,
        PathValues.USERS_USER_ID_CUSTOMLOGOS: UsersUserIdCustomlogos,
        PathValues.USERS_USER_ID_CUSTOMLOGOS_LOGO_ID: UsersUserIdCustomlogosLogoId,
        PathValues.USERS_USER_ID_DESTINATIONS: UsersUserIdDestinations,
        PathValues.USERS_USER_ID_FEED: UsersUserIdFeed,
        PathValues.USERS_USER_ID_FOLLOWERS: UsersUserIdFollowers,
        PathValues.USERS_USER_ID_FOLLOWING: UsersUserIdFollowing,
        PathValues.USERS_USER_ID_FOLLOWING_FOLLOW_USER_ID: UsersUserIdFollowingFollowUserId,
        PathValues.USERS_USER_ID_GROUPS: UsersUserIdGroups,
        PathValues.USERS_USER_ID_GROUPS_GROUP_ID: UsersUserIdGroupsGroupId,
        PathValues.USERS_USER_ID_LIKES: UsersUserIdLikes,
        PathValues.USERS_USER_ID_LIKES_VIDEO_ID: UsersUserIdLikesVideoId,
        PathValues.USERS_USER_ID_LIVE_EVENTS: UsersUserIdLiveEvents,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID: UsersUserIdLiveEventsLiveEventId,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_ACTIVATE: UsersUserIdLiveEventsLiveEventIdActivate,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_AUTO_CC: UsersUserIdLiveEventsLiveEventIdAutoCc,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_DESTINATIONS: UsersUserIdLiveEventsLiveEventIdDestinations,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_END: UsersUserIdLiveEventsLiveEventIdEnd,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_LOW_LATENCY: UsersUserIdLiveEventsLiveEventIdLowLatency,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_M3U8_PLAYBACK: UsersUserIdLiveEventsLiveEventIdM3u8Playback,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_OTT_DESTINATION_DESTINATION_ID: UsersUserIdLiveEventsLiveEventIdOttDestinationDestinationId,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_OTT_DESTINATIONS: UsersUserIdLiveEventsLiveEventIdOttDestinations,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_PICTURES: UsersUserIdLiveEventsLiveEventIdPictures,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_PICTURES_THUMBNAIL_ID: UsersUserIdLiveEventsLiveEventIdPicturesThumbnailId,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_PRIVACY_DOMAINS: UsersUserIdLiveEventsLiveEventIdPrivacyDomains,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_VIDEOS: UsersUserIdLiveEventsLiveEventIdVideos,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_VIDEOS_VIDEO_ID: UsersUserIdLiveEventsLiveEventIdVideosVideoId,
        PathValues.USERS_USER_ID_ONDEMAND_PAGES: UsersUserIdOndemandPages,
        PathValues.USERS_USER_ID_ONDEMAND_PURCHASES: UsersUserIdOndemandPurchases,
        PathValues.USERS_USER_ID_PICTURES: UsersUserIdPictures,
        PathValues.USERS_USER_ID_PICTURES_PORTRAITSET_ID: UsersUserIdPicturesPortraitsetId,
        PathValues.USERS_USER_ID_PORTFOLIOS: UsersUserIdPortfolios,
        PathValues.USERS_USER_ID_PORTFOLIOS_PORTFOLIO_ID: UsersUserIdPortfoliosPortfolioId,
        PathValues.USERS_USER_ID_PORTFOLIOS_PORTFOLIO_ID_VIDEOS: UsersUserIdPortfoliosPortfolioIdVideos,
        PathValues.USERS_USER_ID_PORTFOLIOS_PORTFOLIO_ID_VIDEOS_VIDEO_ID: UsersUserIdPortfoliosPortfolioIdVideosVideoId,
        PathValues.USERS_USER_ID_PRESETS: UsersUserIdPresets,
        PathValues.USERS_USER_ID_PRESETS_PRESET_ID: UsersUserIdPresetsPresetId,
        PathValues.USERS_USER_ID_PRESETS_PRESET_ID_VIDEOS: UsersUserIdPresetsPresetIdVideos,
        PathValues.USERS_USER_ID_PROJECTS: UsersUserIdProjects,
        PathValues.USERS_USER_ID_PROJECTS_PROJECT_ID: UsersUserIdProjectsProjectId,
        PathValues.USERS_USER_ID_PROJECTS_PROJECT_ID_ITEMS: UsersUserIdProjectsProjectIdItems,
        PathValues.USERS_USER_ID_PROJECTS_PROJECT_ID_VIDEOS: UsersUserIdProjectsProjectIdVideos,
        PathValues.USERS_USER_ID_PROJECTS_PROJECT_ID_VIDEOS_VIDEO_ID: UsersUserIdProjectsProjectIdVideosVideoId,
        PathValues.USERS_USER_ID_TEAM_ROLE: UsersUserIdTeamRole,
        PathValues.USERS_USER_ID_TEAM_USERS_TEAM_USER_ID: UsersUserIdTeamUsersTeamUserId,
        PathValues.USERS_USER_ID_UPLOADS_UPLOAD_ID: UsersUserIdUploadsUploadId,
        PathValues.USERS_USER_ID_VIDEOS: UsersUserIdVideos,
        PathValues.USERS_USER_ID_VIDEOS_VIDEO_ID: UsersUserIdVideosVideoId,
        PathValues.USERS_USER_ID_VIDEOS_VIDEO_ID_DESTINATIONS: UsersUserIdVideosVideoIdDestinations,
        PathValues.USERS_USER_ID_VIDEOS_VIDEO_ID_M3U8_PLAYBACK: UsersUserIdVideosVideoIdM3u8Playback,
        PathValues.USERS_USER_ID_WATCHLATER: UsersUserIdWatchlater,
        PathValues.USERS_USER_ID_WATCHLATER_VIDEO_ID: UsersUserIdWatchlaterVideoId,
        PathValues.USERS_USER_ID_WEBINARS: UsersUserIdWebinars,
        PathValues.USERS_USER_ID_WEBINARS_WEBINAR_ID: UsersUserIdWebinarsWebinarId,
        PathValues.USERS_USER_ID_WEBINARS_WEBINAR_ID_EMAIL_SETTINGS: UsersUserIdWebinarsWebinarIdEmailSettings,
        PathValues.USERS_USER_ID_WEBINARS_WEBINAR_ID_REGISTRANTS: UsersUserIdWebinarsWebinarIdRegistrants,
        PathValues.USERS_USER_ID_WEBINARS_WEBINAR_ID_REGISTRANTS_REGISTRANT_ID: UsersUserIdWebinarsWebinarIdRegistrantsRegistrantId,
        PathValues.VIDEOS: Videos,
        PathValues.VIDEOS_VIDEO_ID: VideosVideoId,
        PathValues.VIDEOS_VIDEO_ID_ALBUMS: VideosVideoIdAlbums,
        PathValues.VIDEOS_VIDEO_ID_ANIMATED_THUMBSETS: VideosVideoIdAnimatedThumbsets,
        PathValues.VIDEOS_VIDEO_ID_ANIMATED_THUMBSETS_PICTURE_ID: VideosVideoIdAnimatedThumbsetsPictureId,
        PathValues.VIDEOS_VIDEO_ID_ANIMATED_THUMBSETS_PICTURE_ID_STATUS: VideosVideoIdAnimatedThumbsetsPictureIdStatus,
        PathValues.VIDEOS_VIDEO_ID_AVAILABLE_ALBUMS: VideosVideoIdAvailableAlbums,
        PathValues.VIDEOS_VIDEO_ID_AVAILABLE_CHANNELS: VideosVideoIdAvailableChannels,
        PathValues.VIDEOS_VIDEO_ID_CATEGORIES: VideosVideoIdCategories,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS: VideosVideoIdChapters,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS_TEMPORARY_PICTURES: VideosVideoIdChaptersTemporaryPictures,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS_TEMPORARY_PICTURES_UID: VideosVideoIdChaptersTemporaryPicturesUid,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS_CHAPTER_ID: VideosVideoIdChaptersChapterId,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS_CHAPTER_ID_PICTURES: VideosVideoIdChaptersChapterIdPictures,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS_CHAPTER_ID_PICTURES_UID: VideosVideoIdChaptersChapterIdPicturesUid,
        PathValues.VIDEOS_VIDEO_ID_COMMENTS: VideosVideoIdComments,
        PathValues.VIDEOS_VIDEO_ID_COMMENTS_COMMENT_ID: VideosVideoIdCommentsCommentId,
        PathValues.VIDEOS_VIDEO_ID_COMMENTS_COMMENT_ID_REPLIES: VideosVideoIdCommentsCommentIdReplies,
        PathValues.VIDEOS_VIDEO_ID_CREDITS: VideosVideoIdCredits,
        PathValues.VIDEOS_VIDEO_ID_CREDITS_AVAILABLE_USERS: VideosVideoIdCreditsAvailableUsers,
        PathValues.VIDEOS_VIDEO_ID_CREDITS_CREDIT_ID: VideosVideoIdCreditsCreditId,
        PathValues.VIDEOS_VIDEO_ID_FRAGMENTS: VideosVideoIdFragments,
        PathValues.VIDEOS_VIDEO_ID_LIKES: VideosVideoIdLikes,
        PathValues.VIDEOS_VIDEO_ID_PICTURES: VideosVideoIdPictures,
        PathValues.VIDEOS_VIDEO_ID_PICTURES_PICTURE_ID: VideosVideoIdPicturesPictureId,
        PathValues.VIDEOS_VIDEO_ID_PRESETS_PRESET_ID: VideosVideoIdPresetsPresetId,
        PathValues.VIDEOS_VIDEO_ID_PRIVACY_DOMAINS: VideosVideoIdPrivacyDomains,
        PathValues.VIDEOS_VIDEO_ID_PRIVACY_DOMAINS_DOMAIN: VideosVideoIdPrivacyDomainsDomain,
        PathValues.VIDEOS_VIDEO_ID_PRIVACY_USERS: VideosVideoIdPrivacyUsers,
        PathValues.VIDEOS_VIDEO_ID_PRIVACY_USERS_USER_ID: VideosVideoIdPrivacyUsersUserId,
        PathValues.VIDEOS_VIDEO_ID_SESSIONS_STATUS: VideosVideoIdSessionsStatus,
        PathValues.VIDEOS_VIDEO_ID_TAGS: VideosVideoIdTags,
        PathValues.VIDEOS_VIDEO_ID_TAGS_WORD: VideosVideoIdTagsWord,
        PathValues.VIDEOS_VIDEO_ID_TEXTTRACKS: VideosVideoIdTexttracks,
        PathValues.VIDEOS_VIDEO_ID_TEXTTRACKS_TEXTTRACK_ID: VideosVideoIdTexttracksTexttrackId,
        PathValues.VIDEOS_VIDEO_ID_TIMELINETHUMBNAILS: VideosVideoIdTimelinethumbnails,
        PathValues.VIDEOS_VIDEO_ID_TIMELINETHUMBNAILS_THUMBNAIL_ID: VideosVideoIdTimelinethumbnailsThumbnailId,
        PathValues.VIDEOS_VIDEO_ID_TRANSCRIPTS_TEXTTRACK_ID: VideosVideoIdTranscriptsTexttrackId,
        PathValues.VIDEOS_VIDEO_ID_TRIM: VideosVideoIdTrim,
        PathValues.VIDEOS_VIDEO_ID_VERSIONS: VideosVideoIdVersions,
        PathValues.VIDEOS_VIDEO_ID_VERSIONS_VERSION_ID: VideosVideoIdVersionsVersionId,
        PathValues.VIDEOS_VIDEO_ID_VIDEOS: VideosVideoIdVideos,
        PathValues.WEBINARS_WEBINAR_ID: WebinarsWebinarId,
    }
)

path_to_api = PathToApi(
    {
        PathValues._: Root,
        PathValues.ALBUMS_ALBUM_ID_AVAILABLE_VIDEOS: AlbumsAlbumIdAvailableVideos,
        PathValues.CATEGORIES: Categories,
        PathValues.CATEGORIES_CATEGORY: CategoriesCategory,
        PathValues.CATEGORIES_CATEGORY_CHANNELS: CategoriesCategoryChannels,
        PathValues.CATEGORIES_CATEGORY_GROUPS: CategoriesCategoryGroups,
        PathValues.CATEGORIES_CATEGORY_VIDEOS: CategoriesCategoryVideos,
        PathValues.CATEGORIES_CATEGORY_VIDEOS_VIDEO_ID: CategoriesCategoryVideosVideoId,
        PathValues.CHANNELS: Channels,
        PathValues.CHANNELS_CHANNEL_ID: ChannelsChannelId,
        PathValues.CHANNELS_CHANNEL_ID_CATEGORIES: ChannelsChannelIdCategories,
        PathValues.CHANNELS_CHANNEL_ID_CATEGORIES_CATEGORY: ChannelsChannelIdCategoriesCategory,
        PathValues.CHANNELS_CHANNEL_ID_MODERATORS: ChannelsChannelIdModerators,
        PathValues.CHANNELS_CHANNEL_ID_MODERATORS_USER_ID: ChannelsChannelIdModeratorsUserId,
        PathValues.CHANNELS_CHANNEL_ID_PRIVACY_USERS: ChannelsChannelIdPrivacyUsers,
        PathValues.CHANNELS_CHANNEL_ID_PRIVACY_USERS_USER_ID: ChannelsChannelIdPrivacyUsersUserId,
        PathValues.CHANNELS_CHANNEL_ID_TAGS: ChannelsChannelIdTags,
        PathValues.CHANNELS_CHANNEL_ID_TAGS_WORD: ChannelsChannelIdTagsWord,
        PathValues.CHANNELS_CHANNEL_ID_USERS: ChannelsChannelIdUsers,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS: ChannelsChannelIdVideos,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID: ChannelsChannelIdVideosVideoId,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_COMMENTS: ChannelsChannelIdVideosVideoIdComments,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_CREDITS: ChannelsChannelIdVideosVideoIdCredits,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_LIKES: ChannelsChannelIdVideosVideoIdLikes,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_PICTURES: ChannelsChannelIdVideosVideoIdPictures,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_PRIVACY_USERS: ChannelsChannelIdVideosVideoIdPrivacyUsers,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_TEXTTRACKS: ChannelsChannelIdVideosVideoIdTexttracks,
        PathValues.CHANNELS_CHANNEL_ID_VIDEOS_VIDEO_ID_VERSIONS: ChannelsChannelIdVideosVideoIdVersions,
        PathValues.CONTENTRATINGS: Contentratings,
        PathValues.CREATIVECOMMONS: Creativecommons,
        PathValues.DESTINATION_DESTINATION_ID: DestinationDestinationId,
        PathValues.GROUPS: Groups,
        PathValues.GROUPS_GROUP_ID: GroupsGroupId,
        PathValues.GROUPS_GROUP_ID_USERS: GroupsGroupIdUsers,
        PathValues.GROUPS_GROUP_ID_VIDEOS: GroupsGroupIdVideos,
        PathValues.GROUPS_GROUP_ID_VIDEOS_VIDEO_ID: GroupsGroupIdVideosVideoId,
        PathValues.LANGUAGES: Languages,
        PathValues.LIVE_EVENTS: LiveEvents,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID: LiveEventsLiveEventId,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_ACTIVATE: LiveEventsLiveEventIdActivate,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_AUTO_CC: LiveEventsLiveEventIdAutoCc,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_END: LiveEventsLiveEventIdEnd,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_LOW_LATENCY: LiveEventsLiveEventIdLowLatency,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_PICTURES: LiveEventsLiveEventIdPictures,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_PICTURES_THUMBNAIL_ID: LiveEventsLiveEventIdPicturesThumbnailId,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_PRIVACY_DOMAINS: LiveEventsLiveEventIdPrivacyDomains,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_VIDEOS: LiveEventsLiveEventIdVideos,
        PathValues.LIVE_EVENTS_LIVE_EVENT_ID_VIDEOS_VIDEO_ID: LiveEventsLiveEventIdVideosVideoId,
        PathValues.ME: Me,
        PathValues.ME_ALBUMS: MeAlbums,
        PathValues.ME_ALBUMS_ALBUM_ID: MeAlbumsAlbumId,
        PathValues.ME_ALBUMS_ALBUM_ID_VIDEOS: MeAlbumsAlbumIdVideos,
        PathValues.ME_ALBUMS_ALBUM_ID_VIDEOS_VIDEO_ID: MeAlbumsAlbumIdVideosVideoId,
        PathValues.ME_ALBUMS_ALBUM_ID_VIDEOS_VIDEO_ID_SET_ALBUM_THUMBNAIL: MeAlbumsAlbumIdVideosVideoIdSetAlbumThumbnail,
        PathValues.ME_ALBUMS_ALBUM_ID_VIDEOS_VIDEO_ID_SET_FEATURED_VIDEO: MeAlbumsAlbumIdVideosVideoIdSetFeaturedVideo,
        PathValues.ME_ANALYTICS: MeAnalytics,
        PathValues.ME_APPEARANCES: MeAppearances,
        PathValues.ME_CATEGORIES: MeCategories,
        PathValues.ME_CATEGORIES_CATEGORY: MeCategoriesCategory,
        PathValues.ME_CHANNELS: MeChannels,
        PathValues.ME_CHANNELS_CHANNEL_ID: MeChannelsChannelId,
        PathValues.ME_CUSTOMLOGOS: MeCustomlogos,
        PathValues.ME_CUSTOMLOGOS_LOGO_ID: MeCustomlogosLogoId,
        PathValues.ME_DESTINATIONS: MeDestinations,
        PathValues.ME_FEED: MeFeed,
        PathValues.ME_FOLLOWERS: MeFollowers,
        PathValues.ME_FOLLOWING: MeFollowing,
        PathValues.ME_FOLLOWING_FOLLOW_USER_ID: MeFollowingFollowUserId,
        PathValues.ME_GROUPS: MeGroups,
        PathValues.ME_GROUPS_GROUP_ID: MeGroupsGroupId,
        PathValues.ME_LIKES: MeLikes,
        PathValues.ME_LIKES_VIDEO_ID: MeLikesVideoId,
        PathValues.ME_LIVE_EVENTS: MeLiveEvents,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID: MeLiveEventsLiveEventId,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_ACTIVATE: MeLiveEventsLiveEventIdActivate,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_AUTO_CC: MeLiveEventsLiveEventIdAutoCc,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_DESTINATIONS: MeLiveEventsLiveEventIdDestinations,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_END: MeLiveEventsLiveEventIdEnd,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_LOW_LATENCY: MeLiveEventsLiveEventIdLowLatency,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_M3U8_PLAYBACK: MeLiveEventsLiveEventIdM3u8Playback,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_PICTURES: MeLiveEventsLiveEventIdPictures,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_PICTURES_THUMBNAIL_ID: MeLiveEventsLiveEventIdPicturesThumbnailId,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_PRIVACY_DOMAINS: MeLiveEventsLiveEventIdPrivacyDomains,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_VIDEOS: MeLiveEventsLiveEventIdVideos,
        PathValues.ME_LIVE_EVENTS_LIVE_EVENT_ID_VIDEOS_VIDEO_ID: MeLiveEventsLiveEventIdVideosVideoId,
        PathValues.ME_ONDEMAND_PAGES: MeOndemandPages,
        PathValues.ME_ONDEMAND_PURCHASES: MeOndemandPurchases,
        PathValues.ME_ONDEMAND_PURCHASES_ONDEMAND_ID: MeOndemandPurchasesOndemandId,
        PathValues.ME_PAYMENT_METHODS: MePaymentMethods,
        PathValues.ME_PAYMENT_METHODS_PAYMENT_METHOD_ID: MePaymentMethodsPaymentMethodId,
        PathValues.ME_PICTURES: MePictures,
        PathValues.ME_PICTURES_PORTRAITSET_ID: MePicturesPortraitsetId,
        PathValues.ME_PORTFOLIOS: MePortfolios,
        PathValues.ME_PORTFOLIOS_PORTFOLIO_ID: MePortfoliosPortfolioId,
        PathValues.ME_PORTFOLIOS_PORTFOLIO_ID_VIDEOS: MePortfoliosPortfolioIdVideos,
        PathValues.ME_PORTFOLIOS_PORTFOLIO_ID_VIDEOS_VIDEO_ID: MePortfoliosPortfolioIdVideosVideoId,
        PathValues.ME_PRESETS: MePresets,
        PathValues.ME_PRESETS_PRESET_ID: MePresetsPresetId,
        PathValues.ME_PRESETS_PRESET_ID_VIDEOS: MePresetsPresetIdVideos,
        PathValues.ME_PROJECTS: MeProjects,
        PathValues.ME_PROJECTS_PROJECT_ID: MeProjectsProjectId,
        PathValues.ME_PROJECTS_PROJECT_ID_ITEMS: MeProjectsProjectIdItems,
        PathValues.ME_PROJECTS_PROJECT_ID_VIDEOS: MeProjectsProjectIdVideos,
        PathValues.ME_PROJECTS_PROJECT_ID_VIDEOS_VIDEO_ID: MeProjectsProjectIdVideosVideoId,
        PathValues.ME_VIDEOS: MeVideos,
        PathValues.ME_VIDEOS_VIDEO_ID: MeVideosVideoId,
        PathValues.ME_VIDEOS_VIDEO_ID_DESTINATIONS: MeVideosVideoIdDestinations,
        PathValues.ME_VIDEOS_VIDEO_ID_M3U8_PLAYBACK: MeVideosVideoIdM3u8Playback,
        PathValues.ME_WATCHED_VIDEOS: MeWatchedVideos,
        PathValues.ME_WATCHED_VIDEOS_VIDEO_ID: MeWatchedVideosVideoId,
        PathValues.ME_WATCHLATER: MeWatchlater,
        PathValues.ME_WATCHLATER_VIDEO_ID: MeWatchlaterVideoId,
        PathValues.ME_WEBINARS: MeWebinars,
        PathValues.ME_WEBINARS_WEBINAR_ID: MeWebinarsWebinarId,
        PathValues.ME_WEBINARS_WEBINAR_ID_EMAIL_SETTINGS: MeWebinarsWebinarIdEmailSettings,
        PathValues.ME_WEBINARS_WEBINAR_ID_REGISTRANTS: MeWebinarsWebinarIdRegistrants,
        PathValues.ME_WEBINARS_WEBINAR_ID_REGISTRANTS_REGISTRANT_ID: MeWebinarsWebinarIdRegistrantsRegistrantId,
        PathValues.OAUTH_ACCESS_TOKEN: OauthAccessToken,
        PathValues.OAUTH_AUTHORIZE_CLIENT: OauthAuthorizeClient,
        PathValues.OAUTH_AUTHORIZE_VIMEO_OAUTH1: OauthAuthorizeVimeoOauth1,
        PathValues.OAUTH_VERIFY: OauthVerify,
        PathValues.ONDEMAND_GENRES: OndemandGenres,
        PathValues.ONDEMAND_GENRES_GENRE_ID: OndemandGenresGenreId,
        PathValues.ONDEMAND_GENRES_GENRE_ID_PAGES: OndemandGenresGenreIdPages,
        PathValues.ONDEMAND_GENRES_GENRE_ID_PAGES_ONDEMAND_ID: OndemandGenresGenreIdPagesOndemandId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID: OndemandPagesOndemandId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_BACKGROUNDS: OndemandPagesOndemandIdBackgrounds,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_BACKGROUNDS_BACKGROUND_ID: OndemandPagesOndemandIdBackgroundsBackgroundId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_GENRES: OndemandPagesOndemandIdGenres,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_GENRES_GENRE_ID: OndemandPagesOndemandIdGenresGenreId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_LIKES: OndemandPagesOndemandIdLikes,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_PICTURES: OndemandPagesOndemandIdPictures,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_PICTURES_POSTER_ID: OndemandPagesOndemandIdPicturesPosterId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_PROMOTIONS: OndemandPagesOndemandIdPromotions,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_PROMOTIONS_PROMOTION_ID: OndemandPagesOndemandIdPromotionsPromotionId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_PROMOTIONS_PROMOTION_ID_CODES: OndemandPagesOndemandIdPromotionsPromotionIdCodes,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_REGIONS: OndemandPagesOndemandIdRegions,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_REGIONS_COUNTRY: OndemandPagesOndemandIdRegionsCountry,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_SEASONS: OndemandPagesOndemandIdSeasons,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_SEASONS_SEASON_ID: OndemandPagesOndemandIdSeasonsSeasonId,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_SEASONS_SEASON_ID_VIDEOS: OndemandPagesOndemandIdSeasonsSeasonIdVideos,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_VIDEOS: OndemandPagesOndemandIdVideos,
        PathValues.ONDEMAND_PAGES_ONDEMAND_ID_VIDEOS_VIDEO_ID: OndemandPagesOndemandIdVideosVideoId,
        PathValues.ONDEMAND_REGIONS: OndemandRegions,
        PathValues.ONDEMAND_REGIONS_COUNTRY: OndemandRegionsCountry,
        PathValues.SUBSCRIPTION_PLANS_TIER: SubscriptionPlansTier,
        PathValues.TAGS_WORD: TagsWord,
        PathValues.TAGS_WORD_VIDEOS: TagsWordVideos,
        PathValues.TEAMMEMBERS_CODE: TeammembersCode,
        PathValues.TOKENS: Tokens,
        PathValues.TUTORIAL: Tutorial,
        PathValues.USERS: Users,
        PathValues.USERS_OWNER_ID_FOLDERS_PRIVATE_TO_ME: UsersOwnerIdFoldersPrivateToMe,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS_USER_ID_ALBUMS: UsersUserIdAlbums,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID: UsersUserIdAlbumsAlbumId,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_CUSTOM_THUMBNAILS: UsersUserIdAlbumsAlbumIdCustomThumbnails,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_CUSTOM_THUMBNAILS_THUMBNAIL_ID: UsersUserIdAlbumsAlbumIdCustomThumbnailsThumbnailId,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_LOGOS: UsersUserIdAlbumsAlbumIdLogos,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_LOGOS_LOGO_ID: UsersUserIdAlbumsAlbumIdLogosLogoId,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_VIDEOS: UsersUserIdAlbumsAlbumIdVideos,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_VIDEOS_VIDEO_ID: UsersUserIdAlbumsAlbumIdVideosVideoId,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_VIDEOS_VIDEO_ID_SET_ALBUM_THUMBNAIL: UsersUserIdAlbumsAlbumIdVideosVideoIdSetAlbumThumbnail,
        PathValues.USERS_USER_ID_ALBUMS_ALBUM_ID_VIDEOS_VIDEO_ID_SET_FEATURED_VIDEO: UsersUserIdAlbumsAlbumIdVideosVideoIdSetFeaturedVideo,
        PathValues.USERS_USER_ID_ANALYTICS: UsersUserIdAnalytics,
        PathValues.USERS_USER_ID_APPEARANCES: UsersUserIdAppearances,
        PathValues.USERS_USER_ID_CATEGORIES: UsersUserIdCategories,
        PathValues.USERS_USER_ID_CATEGORIES_CATEGORY: UsersUserIdCategoriesCategory,
        PathValues.USERS_USER_ID_CHANNELS: UsersUserIdChannels,
        PathValues.USERS_USER_ID_CHANNELS_CHANNEL_ID: UsersUserIdChannelsChannelId,
        PathValues.USERS_USER_ID_CUSTOMLOGOS: UsersUserIdCustomlogos,
        PathValues.USERS_USER_ID_CUSTOMLOGOS_LOGO_ID: UsersUserIdCustomlogosLogoId,
        PathValues.USERS_USER_ID_DESTINATIONS: UsersUserIdDestinations,
        PathValues.USERS_USER_ID_FEED: UsersUserIdFeed,
        PathValues.USERS_USER_ID_FOLLOWERS: UsersUserIdFollowers,
        PathValues.USERS_USER_ID_FOLLOWING: UsersUserIdFollowing,
        PathValues.USERS_USER_ID_FOLLOWING_FOLLOW_USER_ID: UsersUserIdFollowingFollowUserId,
        PathValues.USERS_USER_ID_GROUPS: UsersUserIdGroups,
        PathValues.USERS_USER_ID_GROUPS_GROUP_ID: UsersUserIdGroupsGroupId,
        PathValues.USERS_USER_ID_LIKES: UsersUserIdLikes,
        PathValues.USERS_USER_ID_LIKES_VIDEO_ID: UsersUserIdLikesVideoId,
        PathValues.USERS_USER_ID_LIVE_EVENTS: UsersUserIdLiveEvents,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID: UsersUserIdLiveEventsLiveEventId,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_ACTIVATE: UsersUserIdLiveEventsLiveEventIdActivate,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_AUTO_CC: UsersUserIdLiveEventsLiveEventIdAutoCc,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_DESTINATIONS: UsersUserIdLiveEventsLiveEventIdDestinations,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_END: UsersUserIdLiveEventsLiveEventIdEnd,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_LOW_LATENCY: UsersUserIdLiveEventsLiveEventIdLowLatency,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_M3U8_PLAYBACK: UsersUserIdLiveEventsLiveEventIdM3u8Playback,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_OTT_DESTINATION_DESTINATION_ID: UsersUserIdLiveEventsLiveEventIdOttDestinationDestinationId,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_OTT_DESTINATIONS: UsersUserIdLiveEventsLiveEventIdOttDestinations,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_PICTURES: UsersUserIdLiveEventsLiveEventIdPictures,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_PICTURES_THUMBNAIL_ID: UsersUserIdLiveEventsLiveEventIdPicturesThumbnailId,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_PRIVACY_DOMAINS: UsersUserIdLiveEventsLiveEventIdPrivacyDomains,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_VIDEOS: UsersUserIdLiveEventsLiveEventIdVideos,
        PathValues.USERS_USER_ID_LIVE_EVENTS_LIVE_EVENT_ID_VIDEOS_VIDEO_ID: UsersUserIdLiveEventsLiveEventIdVideosVideoId,
        PathValues.USERS_USER_ID_ONDEMAND_PAGES: UsersUserIdOndemandPages,
        PathValues.USERS_USER_ID_ONDEMAND_PURCHASES: UsersUserIdOndemandPurchases,
        PathValues.USERS_USER_ID_PICTURES: UsersUserIdPictures,
        PathValues.USERS_USER_ID_PICTURES_PORTRAITSET_ID: UsersUserIdPicturesPortraitsetId,
        PathValues.USERS_USER_ID_PORTFOLIOS: UsersUserIdPortfolios,
        PathValues.USERS_USER_ID_PORTFOLIOS_PORTFOLIO_ID: UsersUserIdPortfoliosPortfolioId,
        PathValues.USERS_USER_ID_PORTFOLIOS_PORTFOLIO_ID_VIDEOS: UsersUserIdPortfoliosPortfolioIdVideos,
        PathValues.USERS_USER_ID_PORTFOLIOS_PORTFOLIO_ID_VIDEOS_VIDEO_ID: UsersUserIdPortfoliosPortfolioIdVideosVideoId,
        PathValues.USERS_USER_ID_PRESETS: UsersUserIdPresets,
        PathValues.USERS_USER_ID_PRESETS_PRESET_ID: UsersUserIdPresetsPresetId,
        PathValues.USERS_USER_ID_PRESETS_PRESET_ID_VIDEOS: UsersUserIdPresetsPresetIdVideos,
        PathValues.USERS_USER_ID_PROJECTS: UsersUserIdProjects,
        PathValues.USERS_USER_ID_PROJECTS_PROJECT_ID: UsersUserIdProjectsProjectId,
        PathValues.USERS_USER_ID_PROJECTS_PROJECT_ID_ITEMS: UsersUserIdProjectsProjectIdItems,
        PathValues.USERS_USER_ID_PROJECTS_PROJECT_ID_VIDEOS: UsersUserIdProjectsProjectIdVideos,
        PathValues.USERS_USER_ID_PROJECTS_PROJECT_ID_VIDEOS_VIDEO_ID: UsersUserIdProjectsProjectIdVideosVideoId,
        PathValues.USERS_USER_ID_TEAM_ROLE: UsersUserIdTeamRole,
        PathValues.USERS_USER_ID_TEAM_USERS_TEAM_USER_ID: UsersUserIdTeamUsersTeamUserId,
        PathValues.USERS_USER_ID_UPLOADS_UPLOAD_ID: UsersUserIdUploadsUploadId,
        PathValues.USERS_USER_ID_VIDEOS: UsersUserIdVideos,
        PathValues.USERS_USER_ID_VIDEOS_VIDEO_ID: UsersUserIdVideosVideoId,
        PathValues.USERS_USER_ID_VIDEOS_VIDEO_ID_DESTINATIONS: UsersUserIdVideosVideoIdDestinations,
        PathValues.USERS_USER_ID_VIDEOS_VIDEO_ID_M3U8_PLAYBACK: UsersUserIdVideosVideoIdM3u8Playback,
        PathValues.USERS_USER_ID_WATCHLATER: UsersUserIdWatchlater,
        PathValues.USERS_USER_ID_WATCHLATER_VIDEO_ID: UsersUserIdWatchlaterVideoId,
        PathValues.USERS_USER_ID_WEBINARS: UsersUserIdWebinars,
        PathValues.USERS_USER_ID_WEBINARS_WEBINAR_ID: UsersUserIdWebinarsWebinarId,
        PathValues.USERS_USER_ID_WEBINARS_WEBINAR_ID_EMAIL_SETTINGS: UsersUserIdWebinarsWebinarIdEmailSettings,
        PathValues.USERS_USER_ID_WEBINARS_WEBINAR_ID_REGISTRANTS: UsersUserIdWebinarsWebinarIdRegistrants,
        PathValues.USERS_USER_ID_WEBINARS_WEBINAR_ID_REGISTRANTS_REGISTRANT_ID: UsersUserIdWebinarsWebinarIdRegistrantsRegistrantId,
        PathValues.VIDEOS: Videos,
        PathValues.VIDEOS_VIDEO_ID: VideosVideoId,
        PathValues.VIDEOS_VIDEO_ID_ALBUMS: VideosVideoIdAlbums,
        PathValues.VIDEOS_VIDEO_ID_ANIMATED_THUMBSETS: VideosVideoIdAnimatedThumbsets,
        PathValues.VIDEOS_VIDEO_ID_ANIMATED_THUMBSETS_PICTURE_ID: VideosVideoIdAnimatedThumbsetsPictureId,
        PathValues.VIDEOS_VIDEO_ID_ANIMATED_THUMBSETS_PICTURE_ID_STATUS: VideosVideoIdAnimatedThumbsetsPictureIdStatus,
        PathValues.VIDEOS_VIDEO_ID_AVAILABLE_ALBUMS: VideosVideoIdAvailableAlbums,
        PathValues.VIDEOS_VIDEO_ID_AVAILABLE_CHANNELS: VideosVideoIdAvailableChannels,
        PathValues.VIDEOS_VIDEO_ID_CATEGORIES: VideosVideoIdCategories,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS: VideosVideoIdChapters,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS_TEMPORARY_PICTURES: VideosVideoIdChaptersTemporaryPictures,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS_TEMPORARY_PICTURES_UID: VideosVideoIdChaptersTemporaryPicturesUid,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS_CHAPTER_ID: VideosVideoIdChaptersChapterId,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS_CHAPTER_ID_PICTURES: VideosVideoIdChaptersChapterIdPictures,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS_CHAPTER_ID_PICTURES_UID: VideosVideoIdChaptersChapterIdPicturesUid,
        PathValues.VIDEOS_VIDEO_ID_COMMENTS: VideosVideoIdComments,
        PathValues.VIDEOS_VIDEO_ID_COMMENTS_COMMENT_ID: VideosVideoIdCommentsCommentId,
        PathValues.VIDEOS_VIDEO_ID_COMMENTS_COMMENT_ID_REPLIES: VideosVideoIdCommentsCommentIdReplies,
        PathValues.VIDEOS_VIDEO_ID_CREDITS: VideosVideoIdCredits,
        PathValues.VIDEOS_VIDEO_ID_CREDITS_AVAILABLE_USERS: VideosVideoIdCreditsAvailableUsers,
        PathValues.VIDEOS_VIDEO_ID_CREDITS_CREDIT_ID: VideosVideoIdCreditsCreditId,
        PathValues.VIDEOS_VIDEO_ID_FRAGMENTS: VideosVideoIdFragments,
        PathValues.VIDEOS_VIDEO_ID_LIKES: VideosVideoIdLikes,
        PathValues.VIDEOS_VIDEO_ID_PICTURES: VideosVideoIdPictures,
        PathValues.VIDEOS_VIDEO_ID_PICTURES_PICTURE_ID: VideosVideoIdPicturesPictureId,
        PathValues.VIDEOS_VIDEO_ID_PRESETS_PRESET_ID: VideosVideoIdPresetsPresetId,
        PathValues.VIDEOS_VIDEO_ID_PRIVACY_DOMAINS: VideosVideoIdPrivacyDomains,
        PathValues.VIDEOS_VIDEO_ID_PRIVACY_DOMAINS_DOMAIN: VideosVideoIdPrivacyDomainsDomain,
        PathValues.VIDEOS_VIDEO_ID_PRIVACY_USERS: VideosVideoIdPrivacyUsers,
        PathValues.VIDEOS_VIDEO_ID_PRIVACY_USERS_USER_ID: VideosVideoIdPrivacyUsersUserId,
        PathValues.VIDEOS_VIDEO_ID_SESSIONS_STATUS: VideosVideoIdSessionsStatus,
        PathValues.VIDEOS_VIDEO_ID_TAGS: VideosVideoIdTags,
        PathValues.VIDEOS_VIDEO_ID_TAGS_WORD: VideosVideoIdTagsWord,
        PathValues.VIDEOS_VIDEO_ID_TEXTTRACKS: VideosVideoIdTexttracks,
        PathValues.VIDEOS_VIDEO_ID_TEXTTRACKS_TEXTTRACK_ID: VideosVideoIdTexttracksTexttrackId,
        PathValues.VIDEOS_VIDEO_ID_TIMELINETHUMBNAILS: VideosVideoIdTimelinethumbnails,
        PathValues.VIDEOS_VIDEO_ID_TIMELINETHUMBNAILS_THUMBNAIL_ID: VideosVideoIdTimelinethumbnailsThumbnailId,
        PathValues.VIDEOS_VIDEO_ID_TRANSCRIPTS_TEXTTRACK_ID: VideosVideoIdTranscriptsTexttrackId,
        PathValues.VIDEOS_VIDEO_ID_TRIM: VideosVideoIdTrim,
        PathValues.VIDEOS_VIDEO_ID_VERSIONS: VideosVideoIdVersions,
        PathValues.VIDEOS_VIDEO_ID_VERSIONS_VERSION_ID: VideosVideoIdVersionsVersionId,
        PathValues.VIDEOS_VIDEO_ID_VIDEOS: VideosVideoIdVideos,
        PathValues.WEBINARS_WEBINAR_ID: WebinarsWebinarId,
    }
)
