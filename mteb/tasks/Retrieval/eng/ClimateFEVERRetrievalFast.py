from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class ClimateFEVERFast(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="ClimateFEVER-Fast",
        description="CLIMATE-FEVER is a dataset adopting the FEVER methodology that consists of 1,535 real-world claims regarding climate-change. ",
        reference="https://www.sustainablefinance.uzh.ch/en/research/climate-fever.html",
        dataset={
            "path": "mteb/ClimateFEVER_test_top_250_only_w_correct",
            "revision": "latest",
        },
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
        bibtex_citation="""@misc{diggelmann2021climatefever,
      title={CLIMATE-FEVER: A Dataset for Verification of Real-World Climate Claims}, 
      author={Thomas Diggelmann and Jordan Boyd-Graber and Jannis Bulian and Massimiliano Ciaramita and Markus Leippold},
      year={2021},
      eprint={2012.00614},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}""",
        descriptive_stats={
            "n_samples": None,
            "avg_character_length": {
                "test": {
                    "average_document_length": 1252.2511669715511,
                    "average_query_length": 122.23336745138178,
                    "num_documents": 63412,
                    "num_queries": 977,
                    "average_relevant_docs_per_query": 2.7768924302788847,
                }
            },
        },
    )
