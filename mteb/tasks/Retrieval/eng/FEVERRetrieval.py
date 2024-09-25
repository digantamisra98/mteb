from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class FEVER(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="FEVER",
        dataset={
            "path": "mteb/fever",
            "revision": "bea83ef9e8fb933d90a2f1d5515737465d613e12",
        },
        description=(
            "FEVER (Fact Extraction and VERification) consists of 185,445 claims generated by altering sentences"
            + " extracted from Wikipedia and subsequently verified without knowledge of the sentence they were"
            + " derived from."
        ),
        reference="https://fever.ai/",
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["train", "dev", "test"],
        eval_langs=["eng-Latn"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation="""@inproceedings{thorne-etal-2018-fever,
    title = "{FEVER}: a Large-scale Dataset for Fact Extraction and {VER}ification",
    author = "Thorne, James  and
      Vlachos, Andreas  and
      Christodoulopoulos, Christos  and
      Mittal, Arpit",
    editor = "Walker, Marilyn  and
      Ji, Heng  and
      Stent, Amanda",
    booktitle = "Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)",
    month = jun,
    year = "2018",
    address = "New Orleans, Louisiana",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N18-1074",
    doi = "10.18653/v1/N18-1074",
    pages = "809--819",
    abstract = "In this paper we introduce a new publicly available dataset for verification against textual sources, FEVER: Fact Extraction and VERification. It consists of 185,445 claims generated by altering sentences extracted from Wikipedia and subsequently verified without knowledge of the sentence they were derived from. The claims are classified as Supported, Refuted or NotEnoughInfo by annotators achieving 0.6841 in Fleiss kappa. For the first two classes, the annotators also recorded the sentence(s) forming the necessary evidence for their judgment. To characterize the challenge of the dataset presented, we develop a pipeline approach and compare it to suitably designed oracles. The best accuracy we achieve on labeling a claim accompanied by the correct evidence is 31.87{\%}, while if we ignore the evidence we achieve 50.91{\%}. Thus we believe that FEVER is a challenging testbed that will help stimulate progress on claim verification against textual sources.",
}""",
        descriptive_stats={
            "n_samples": None,
            "avg_character_length": {
                "train": {
                    "average_document_length": 538.2340070317589,
                    "average_query_length": 47.56034058828886,
                    "num_documents": 5416568,
                    "num_queries": 109810,
                    "average_relevant_docs_per_query": 1.2757034878426372,
                },
                "dev": {
                    "average_document_length": 538.2340070317589,
                    "average_query_length": 47.326282628262824,
                    "num_documents": 5416568,
                    "num_queries": 6666,
                    "average_relevant_docs_per_query": 1.211971197119712,
                },
                "test": {
                    "average_document_length": 538.2340070317589,
                    "average_query_length": 49.60546054605461,
                    "num_documents": 5416568,
                    "num_queries": 6666,
                    "average_relevant_docs_per_query": 1.1906690669066906,
                },
            },
        },
    )

class FEVERHardNegatives(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="FEVERHardNegatives",
        dataset={
            "path": "mteb/FEVER_test_top_250_only_w_correct",
            "revision": "7cca271a26ce6aa55769494e5df9da8284ac7189",
        },
        description=(
            "FEVER (Fact Extraction and VERification) consists of 185,445 claims generated by altering sentences"
            + " extracted from Wikipedia and subsequently verified without knowledge of the sentence they were"
            + " derived from."
        ),
        reference="https://fever.ai/",
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation="""@inproceedings{thorne-etal-2018-fever,
    title = "{FEVER}: a Large-scale Dataset for Fact Extraction and {VER}ification",
    author = "Thorne, James  and
      Vlachos, Andreas  and
      Christodoulopoulos, Christos  and
      Mittal, Arpit",
    editor = "Walker, Marilyn  and
      Ji, Heng  and
      Stent, Amanda",
    booktitle = "Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)",
    month = jun,
    year = "2018",
    address = "New Orleans, Louisiana",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N18-1074",
    doi = "10.18653/v1/N18-1074",
    pages = "809--819",
    abstract = "In this paper we introduce a new publicly available dataset for verification against textual sources, FEVER: Fact Extraction and VERification. It consists of 185,445 claims generated by altering sentences extracted from Wikipedia and subsequently verified without knowledge of the sentence they were derived from. The claims are classified as Supported, Refuted or NotEnoughInfo by annotators achieving 0.6841 in Fleiss kappa. For the first two classes, the annotators also recorded the sentence(s) forming the necessary evidence for their judgment. To characterize the challenge of the dataset presented, we develop a pipeline approach and compare it to suitably designed oracles. The best accuracy we achieve on labeling a claim accompanied by the correct evidence is 31.87{\%}, while if we ignore the evidence we achieve 50.91{\%}. Thus we believe that FEVER is a challenging testbed that will help stimulate progress on claim verification against textual sources.",
}""",
        descriptive_stats={
            "n_samples": {"test": 1000},
            "avg_character_length": {
                "test": {
                    "average_document_length": 689.4130474947403,
                    "average_query_length": 49.62,
                    "num_documents": 503361,
                    "num_queries": 1000,
                    "average_relevant_docs_per_query": 1.1752175217521752,
                }
            },
        },
    )
