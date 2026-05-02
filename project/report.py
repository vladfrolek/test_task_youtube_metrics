def generate_clickbait_report(videos):
    clickbait_videos = []
    report_fields = [
        'title',
        'ctr',
        'retention_rate'
    ]
    for video in videos:
        if video['ctr']>15 and video['retention_rate']<40:
            report_row={key:video[key] for key in report_fields}
            clickbait_videos.append(report_row)
    sorted_clickbait_videos = sorted(
        clickbait_videos,
        key = lambda x: x['ctr'],
        reverse=True
    )
    return sorted_clickbait_videos
