from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class HotpotQAPLFast(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="HotpotQA-PL-Fast",
        description="HotpotQA is a question answering dataset featuring natural, multi-hop questions, with strong supervision for supporting facts to enable more explainable question answering systems.",
        reference="https://hotpotqa.github.io/",
        dataset={
            "path": "mteb/hotpotqa-pl_test_top_250_only_w_correct",
            "revision": "latest",
            "trust_remote_code": True,
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["pol-Latn"],
        main_score="ndcg_at_10",
        date=("2018-01-01", "2018-12-31"),  # best guess: based on publication date
        domains=["Web", "Written"],
        task_subtypes=["Question answering"],
        license="cc-by-sa-4.0",
        annotations_creators="derived",
        dialect=[],
        sample_creation="machine-translated",
        bibtex_citation="""@misc{wojtasik2024beirpl,
      title={BEIR-PL: Zero Shot Information Retrieval Benchmark for the Polish Language}, 
      author={Konrad Wojtasik and Vadim Shishkin and Kacper Wołowiec and Arkadiusz Janz and Maciej Piasecki},
      year={2024},
      eprint={2305.19840},
      archivePrefix={arXiv},
      primaryClass={cs.IR}
}""",
        descriptive_stats={
            "n_samples": None,
            "avg_character_length": {
                "test": {
                    "average_document_length": 292.26835882093405,
                    "average_query_length": 94.64064821066847,
                    "num_documents": 5233329,
                    "num_queries": 7405,
                    "average_relevant_docs_per_query": 2.0,
                }
            },
        },
    )
