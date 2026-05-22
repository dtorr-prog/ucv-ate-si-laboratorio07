from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


def register_pipelines() -> dict[str, Pipeline]:

    pipelines = find_pipelines()

    return {
        "__default__": pipelines["image_processing"],
    }