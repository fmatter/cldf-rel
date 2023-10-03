from cldf_rel import CLDFDataset


def test_load():
    ds = CLDFDataset("/home/florianm/Dropbox/research/cariban/yawarana/yawarana-corpus-cldf/cldf/metadata.json")
    ds["wordforms"]["kerejpe-old"].wordformparts
    ds["wordforms"]["kerejpe-old"].language