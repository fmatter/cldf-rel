import pytest
from pycldf import Dataset
import pathlib


@pytest.fixture(scope="module")
def data():
    return pathlib.Path(__file__).parent / "data"


@pytest.fixture
def dataset1(data):
    return Dataset.from_metadata(data / "cldf/metadata.json")


@pytest.fixture
def metadata(data):
    return data / "cldf/metadata.json"
