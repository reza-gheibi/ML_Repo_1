import os
import pandas as pd

# Add the absolute path to src/ so Python can find it
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from data_loader import load_data

def test_load_data():
    test_file = "data/sample_test.csv"
    assert os.path.exists(test_file), "Sample file missing"
    df = load_data(test_file)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
