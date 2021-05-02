from downloader import Downloader

cookie = """
device_session_id=192a6e45-0b8e-44fe-a785-f0fa47386a0f; show-like-copy=0; visitor_tracking=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26utm_term%3D%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D; first_landing=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26utm_term%3D%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D; G_ENABLED_IDPS=google; g_state={\"i_l\":0}; ss_hide_default_banner=1619167156.712; dismiss_transcripts_tooltip=1; PHPSESSID=551ce23a7f020f21f5a75645330bc52e; YII_CSRF_TOKEN=VXJiTkFqUVAzRlhqWVJSWnJ5R2VwcVFVdmI3UkxiNnRfZiN0hXmzX1hT5ZEy9yqMP7MZIPN6Zwi1C3g_UL6aqQ%3D%3D; __stripe_mid=5e543a01-0549-4438-be44-0ab535657690a98519
"""

dl = Downloader(cookie=cookie)

text = input("Course link here : ")

# download by class URL:
dl.download_course_by_url(text)

# or by class ID:
# dl.download_course_by_class_id(189505397)
