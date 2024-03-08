# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.channels_channel_id_videos_video_id_comments.post import AddNewCommentRaw
from vimeo_python_sdk.paths.videos_video_id_comments.post import CommentRaw
from vimeo_python_sdk.paths.videos_video_id_comments_comment_id.get import Comment0Raw
from vimeo_python_sdk.paths.videos_video_id_comments_comment_id.delete import Comment1Raw
from vimeo_python_sdk.paths.videos_video_id_comments_comment_id.patch import Comment2Raw
from vimeo_python_sdk.paths.videos_video_id_comments.get import CommentsRaw
from vimeo_python_sdk.paths.videos_video_id_comments_comment_id_replies.post import CreateReplyRaw
from vimeo_python_sdk.paths.channels_channel_id_videos_video_id_comments.get import GetAllRepliesRaw
from vimeo_python_sdk.paths.videos_video_id_comments_comment_id_replies.get import GetAllReplies0Raw


class VideosVideoCommentsApiRaw(
    AddNewCommentRaw,
    CommentRaw,
    Comment0Raw,
    Comment1Raw,
    Comment2Raw,
    CommentsRaw,
    CreateReplyRaw,
    GetAllRepliesRaw,
    GetAllReplies0Raw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
