from project.report import generate_clickbait_report


def test_clickbait_video_in_report():
    videos= [
        {
            'title':'Video 1',
            'ctr':20,
            'retention_rate':30
        }
    ]

    result = generate_clickbait_report(videos)
    assert len(result) == 1
    assert result[0]['title'] == "Video 1"
    assert result[0]['ctr'] == 20
    assert result[0]['retention_rate'] == 30


def test_video_with_low_ctr_not_in_report():
    videos= [
        {
            'title':'Video 2',
            'ctr':10,
            'retention_rate':30

        }
    ]
    result = generate_clickbait_report(videos)
    assert len(result) == 0


def test_video_with_high_retention_rate_not_in_report():
    videos= [
        {
            'title':'Video 3',
            'ctr':20,
            'retention_rate':50

        }
    ]
    result = generate_clickbait_report(videos)
    assert len(result) == 0


def test_boundary_values_not_in_report():
    videos = [
        {
            'title': 'Video with ctr 15',
            'ctr': 15,
            'retention_rate': 30,
        },
        {
            'title': 'Video with retention 40',
            'ctr': 20,
            'retention_rate': 40,
        },
    ]
    result = generate_clickbait_report(videos)
    assert len(result) == 0


def test_report_sorted_by_ctr_desc():
    videos = [
        {
            'title': 'Video A',
            'ctr': 18,
            'retention_rate': 30,
        },
        {
            'title': 'Video B',
            'ctr': 25,
            'retention_rate': 20,
        },
        {
            'title': 'Video C',
            'ctr': 21,
            'retention_rate': 35,
        },
    ]

    result = generate_clickbait_report(videos)
    assert result[0]['title'] == 'Video B'
    assert result[1]['title'] == 'Video C'
    assert result[2]['title'] == 'Video A'


def test_report_contains_only_required_fields():
    videos = [
        {
            'title': 'Video 1',
            'ctr': 20,
            'retention_rate': 30,
            'views': 1000,
            'likes': 100,
            'avg_watch_time': 5.5,
        }
    ]
    result = generate_clickbait_report(videos)
    assert len(result) == 1
    assert set(result[0].keys()) == {'title', 'ctr', 'retention_rate'}