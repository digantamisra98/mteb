from __future__ import annotations

from collections import defaultdict

import datasets

from mteb.abstasks.AbsTaskRetrieval import AbsTaskRetrieval
from mteb.abstasks.MultilingualTask import MultilingualTask
from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import *

_LANGUAGES = {
    "fas": ["fas-Arab"],
    "rus": ["rus-Cyrl"],
    "zho": ["zho-Hans"],
}


def load_neuclir_data(
    path: str,
    langs: list,
    eval_splits: list,
    cache_dir: str | None = None,
    revision: str | None = None,
):
    corpus = {lang: {split: None for split in eval_splits} for lang in langs}
    queries = {lang: {split: None for split in eval_splits} for lang in langs}
    relevant_docs = {lang: {split: None for split in eval_splits} for lang in langs}

    for lang in langs:
        lang_corpus = datasets.load_dataset(
            path, f"corpus-{lang}", cache_dir=cache_dir, revision=revision
        )["corpus"]
        lang_queries = datasets.load_dataset(
            path, f"queries-{lang}", cache_dir=cache_dir, revision=revision
        )["queries"]
        lang_qrels = datasets.load_dataset(
            path, f"{lang}", cache_dir=cache_dir, revision=revision
        )["test"]
        corpus[lang] = {
            "test": {
                str(e["_id"]): {"text": e["text"], "title": e["title"]}
                for e in lang_corpus
            }
        }
        queries[lang] = {"test": {str(e["_id"]): e["text"] for e in lang_queries}}
        relevant_docs[lang]["test"] = defaultdict(dict)
        for item in lang_qrels:
            relevant_docs[lang]["test"][str(item["query-id"])].update(
                {str(item["corpus-id"]): item["score"]}
            )

    corpus = datasets.DatasetDict(corpus)
    queries = datasets.DatasetDict(queries)
    relevant_docs = datasets.DatasetDict(relevant_docs)
    return corpus, queries, relevant_docs


class NeuCLIR2022RetrievalFast(MultilingualTask, AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="NeuCLIR2022Retrieval-Fast",
        description="The task involves identifying and retrieving the documents that are relevant to the queries.",
        reference="https://neuclir.github.io/",
        dataset={
            "path": "mteb/neuclir-2022-fast",
            "revision": "b94a5147a3b3046581c8b4524d9409f94594c5a4",
            "trust_remote_code": True,
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=_LANGUAGES,
        main_score="ndcg_at_20",
        date=("2021-08-01", "2022-06-30"),
        domains=["News", "Written"],
        task_subtypes=[],
        license="odc-by",
        annotations_creators="expert-annotated",
        dialect=[],
        sample_creation="found",
        bibtex_citation="""@article{lawrie2023overview,
  title={Overview of the TREC 2022 NeuCLIR track},
  author={Lawrie, Dawn and MacAvaney, Sean and Mayfield, James and McNamee, Paul and Oard, Douglas W and Soldaini, Luca and Yang, Eugene},
  journal={arXiv preprint arXiv:2304.12367},
  year={2023}
}""",
        descriptive_stats={
            "n_samples": None,
            "avg_character_length": {
                "test": {
                    "average_document_length": 2220.6705525948482,
                    "average_query_length": 65.06432748538012,
                    "num_documents": 63048,
                    "num_queries": 342,
                    "average_relevant_docs_per_query": 19.807142857142857,
                    "hf_subset_descriptive_stats": {
                        "fas": {
                            "average_document_length": 3010.529632371083,
                            "average_query_length": 85.4298245614035,
                            "num_documents": 20265,
                            "num_queries": 114,
                            "average_relevant_docs_per_query": 14.217391304347826,
                        },
                        "rus": {
                            "average_document_length": 2623.860809712729,
                            "average_query_length": 85.58771929824562,
                            "num_documents": 20921,
                            "num_queries": 114,
                            "average_relevant_docs_per_query": 24.177777777777777,
                        },
                        "zho": {
                            "average_document_length": 1102.6741377733053,
                            "average_query_length": 24.17543859649123,
                            "num_documents": 21862,
                            "num_queries": 114,
                            "average_relevant_docs_per_query": 21.040816326530614,
                        },
                    },
                }
            },
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_neuclir_data(
            path=self.metadata_dict["dataset"]["path"],
            langs=self.metadata.eval_langs,
            eval_splits=self.metadata_dict["eval_splits"],
            cache_dir=kwargs.get("cache_dir", None),
            revision=self.metadata_dict["dataset"]["revision"],
        )
        self.data_loaded = True
