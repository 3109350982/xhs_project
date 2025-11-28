# settings.py
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

SETTINGS = {
    # SQLite 数据库
    "DB_PATH": os.path.join(ROOT_DIR, "xhs_data.db"),

    # 许可证缓存与服务器地址（你可以直接换成你现在抖音用的那个验证接口）
    "LICENSE_CACHE_PATH": os.path.join(ROOT_DIR, "license_cache.json"),
    "LICENSE_SERVER": "https://license.cjylkr20241008.top",

    # 浏览器用户数据目录（用于保存小红书登录态）
    "BROWSER_USER_DATA_DIR": os.path.join(ROOT_DIR, "xhs_browser_profile"),

    # 小红书相关配置
    "XHS": {
        # 关键词搜索页面 URL 模板（type=51 综合）
        "SEARCH_URL_TEMPLATE": "https://www.xiaohongshu.com/search_result?keyword={kw}&type=51",

        "SELECTORS": {
            # 列表/搜索卡片
            "grid_card":        "section.note-item",
            "item_link":        'section.note-item a.cover.mask.ld[href^="/explore/"]',
            "item_title":       "section.note-item div.footer a.title span",
            "item_counts":      "section.note-item .card-bottom-wrapper .count",
            "grid_title_link":  "div.footer a.title",
            "item_like_count":  "section.note-item .footer .interactions span",
            "item_comment_count": "section.note-item .footer .interactions span:last-child",
            "item_publish_time": "",
            "item_collect_count": "",
            "grid_publish_time": ".card-bottom-wrapper .time span",
            "search_result_item": "section.note-item",

            # 详情页（备用）
            "detail_publish_time": "div.note-content .date span",

            # 评论区（监听/回复）
            "comment_list_root":  'div.comments-el div[name="list"]',
            "comment_item":       "div.comment-item",
            "comment_text":       "div.content span.note-text > span",
            "comment_time":       "div.info > div.date > span",
            "comment_location":   "div.info .location",
            "comment_count":      "div.interactions .count",
            "comment_user":       "div.comment-item .author a.name",
            "comment_container":  "div.comments-container",
            "comment_reply_btn":  "div.interactions .reply-icon-container, svg.reds-icon.reply-icon",
            "comment_reply_button": "div.comment-item svg.reply-icon",

            # 发评论
            "comment_input":       "#content_textarea[contenteditable='true']",
            "comment_send_button": "svg.reply-icon",
        }
    }
}
