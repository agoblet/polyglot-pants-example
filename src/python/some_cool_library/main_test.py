import time

from some_cool_library.main import generate_df


def test_generate_df_should_have_correct_length():
    got = generate_df()

    assert len(got) == 3


def test_slow():
    time.sleep(10)
