import pytest
from cldf_rel import CLDFDataset


def test_ds(dataset1):
    ds = CLDFDataset(dataset1, orm=True)
    assert ds["morphemes"]["tri-se"].language == ds["languages"]["tri"]
    assert len(ds["languages"]["apa"].morphemes) == 2
    for k, v in ds["morphemes"]["tri-se"].items():
        if k == "Language_ID":
            assert v == "tri"
    assert "language" in ds["morphemes"]["tri-se"].single_refs
    assert "morphemes" in ds["morphemes"]["tri-se"].language.multi_refs
    with pytest.raises(AttributeError):
        ds["languages"]["apa"].morphs
    assert str(ds["languages"]["apa"]) == "languages: [ID: apa,Name: Apalaí,Macroarea: None,Latitude: None,Longitude: None,Glottocode: None,ISO639P3code: None]"

def test_md(metadata):
    ds = CLDFDataset(metadata, orm=True)
    assert ds["morphemes"]["tri-se"].language == ds["languages"]["tri"]
    assert len(ds["languages"]["apa"].morphemes) == 2
    assert ds["morphemes"]["tri-se"].get("Language_ID") == "tri"

def test_invalid():
    with pytest.raises(ValueError):
        CLDFDataset(10)