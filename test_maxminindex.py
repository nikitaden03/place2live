import pytest
import pandas as pd
from where import max_min_index

df = pd.DataFrame(data={
    'country': ['Russia', 'UK', 'USA', 'Germany', 'China'],
    'col1': [10.6, 78.4, 88, 14, -5],
    'col2': [47, 11, 30, 0, -77],
    'col3': [0, 0, 0, 10, 100],
    'col4': [-10, -100, 10, 100, 78]
})


@pytest.mark.parametrize("name_index", [
    ('col1'),
    ('col2'),
    ('col3'),
    ('col4')
])
def test_max_min_index(name_index):
    """test the output of the max_min_index function."""
    b = max_min_index(name_index, df) == ([
        df[name_index].max(), df['country'][df[name_index].idxmax()]
        ], [df[name_index].min(), df['country'][df[name_index].idxmin()]])
    if not b:
        raise AssertionError
