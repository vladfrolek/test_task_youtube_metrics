import pytest

from project.reader import read_file, read_files


def test_read_file_returns_rows(tmp_path):
    csv_file = tmp_path / "stats.csv"

    csv_file.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Video 1,20.5,30,1000,100,5.5\n",
        encoding="utf-8",
    )

    result = read_file(csv_file)

    assert len(result) == 1
    assert result[0]["title"] == "Video 1"
    assert result[0]["ctr"] == 20.5
    assert result[0]["retention_rate"] == 30.0


def test_read_file_converts_numeric_fields_to_float(tmp_path):
    csv_file = tmp_path / "stats.csv"

    csv_file.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Video 1,18.2,35,1000,100,5.5\n",
        encoding="utf-8",
    )

    result = read_file(csv_file)

    assert isinstance(result[0]["ctr"], float)
    assert isinstance(result[0]["retention_rate"], float)


def test_read_files_combines_multiple_files(tmp_path):
    csv_file_1 = tmp_path / "stats1.csv"
    csv_file_2 = tmp_path / "stats2.csv"

    csv_file_1.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Video 1,20,30,1000,100,5.5\n",
        encoding="utf-8",
    )

    csv_file_2.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Video 2,25,20,2000,200,4.5\n",
        encoding="utf-8",
    )

    result = read_files([csv_file_1, csv_file_2])

    assert len(result) == 2
    assert result[0]["title"] == "Video 1"
    assert result[1]["title"] == "Video 2"


def test_read_file_raises_error_for_missing_file(tmp_path):
    missing_file = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        read_file(missing_file)