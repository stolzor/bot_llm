from typing import List
import os

import numpy as np
import pandas as pd
from datasets import Dataset, load_dataset, concatenate_datasets

from logger import get_logger
from .config import *


logger = get_logger(__name__, "prepare_data.log")


def prepare_empatic_data(empatic_data: Dataset) -> Dataset:
    """Prepare empatic dataset for LLM

    Args:
        empatic_data (Dataset): samples of dialogs

    Returns:
        Dataset: prepare dataset
    """
    logger.info("Start preprocessing empatic_data")
    empatic_data = empatic_data.map(
        lambda row: {"utterance": row["utterance"].replace("_comma_", ",")}
    )
    empatic_data = empatic_data.filter(
        lambda row: row["context"] in empatic_top_context
    )

    for condition in empatic_data.keys():
        df = (
            empatic_data[condition]
            .to_pandas()
            .groupby("conv_id")["utterance"]
            .apply(list)
        )
        empatic_data[condition] = Dataset.from_pandas(pd.DataFrame(df))

    prepare_empatic_data = empatic_data.rename_column("utterance", "dialog")
    prepare_empatic_data = prepare_empatic_data.remove_columns(["conv_id"])

    return prepare_empatic_data


def prepare_daily_data(daily_dataset: Dataset) -> Dataset:
    """Prepare daily_dialog dataset for LLM

    Args:
        daily_dataset (Dataset): samples of dialogs

    Returns:
        Dataset: prepare dataset
    """
    logger.info("Start preprocessing daily_dialog")
    daily_dataset = daily_dataset.map(
        lambda x: {"emotion_score": np.isin(x["emotion"], [0, 4, 6]).mean()}
    )
    daily_dataset = daily_dataset.filter(lambda x: x["emotion_score"] == 1)

    prepare_daily_dataset = daily_dataset.remove_columns(
        ["act", "emotion", "emotion_score"]
    )

    return prepare_daily_dataset


def concat_data(data: List[Dataset]) -> List[pd.DataFrame]:
    """Concat data

    Args:
        data (List[Dataset]): list of data

    Returns:
        List[pd.DataFrame]: concated data
    """
    logger.info("Start concat data")
    total_data = []

    keys = ["train", "validation", "test"]

    for condition in keys:
        values = list(map(lambda d: d[condition], data))
        total_data.append(pd.DataFrame(concatenate_datasets(values)))

    total_data = pd.concat(total_data, axis=0)

    return total_data


def preprocess_prompt(row: List[str]) -> str:
    logger.info("Preprocess rows in all data")
    response = "\n".join(
        [
            f"Person: {text}" if i % 2 == 0 else f"You: {text}"
            for i, text in enumerate(row)
        ]
    )
    return PROMPT_TEMPLATE.format(
        intro=system_prompt, instruction=instruction_prompt, response=response
    )


def create_dir() -> None:
    """Create dir if not exists"""
    logger.info("Check exists dir")
    os.makedirs(os.path.join(os.getcwd(), "data"), exist_ok=True)


def get_data() -> None:
    """Preprocessing data and save"""
    logger.info("Start download empatic_data")
    empatic_data = prepare_empatic_data(load_dataset("empathetic_dialogues"))
    logger.info("End preprocessing empatic_data")

    logger.info("Start download daily_dialog")
    daily_dialog = prepare_daily_data(load_dataset("daily_dialog"))
    logger.info("End preprocessing daily_dialog")

    data = concat_data([empatic_data, daily_dialog])
    logger.info("End concat data")

    data["text"] = data["dialog"].apply(lambda x: preprocess_prompt(x))
    create_dir()

    to_save = os.path.join(os.getcwd(), "data", "total_data.parquet")
    data.to_parquet(to_save, index=False)

    logger.info(f"Save to {to_save}")
    return to_save


if __name__ == "__main__":
    path = get_data()
    print(path)
