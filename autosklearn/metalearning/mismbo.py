# -*- encoding: utf-8 -*-

import time

from autosklearn.metalearning.optimizers.metalearn_optimizer.metalearner \
    import MetaLearningOptimizer
from autosklearn.constants \
    import MULTILABEL_CLASSIFICATION, MULTICLASS_CLASSIFICATION, TASK_TYPES_TO_STRING


def suggest_via_metalearning(meta,
        meta_base, dataset_name, metric, task, sparse,
        num_initial_configurations, logger):

    if task == MULTILABEL_CLASSIFICATION:
        task = MULTICLASS_CLASSIFICATION

    task = TASK_TYPES_TO_STRING[task]

    logger.info(task)

    start = time.time()
    ml = MetaLearningOptimizer(
        meta=meta,
        dataset_name=dataset_name,
        configuration_space=meta_base.configuration_space,
        meta_base=meta_base,
        distance='l1',
        seed=1,
        logger=logger,)
    logger.info('Reading meta-data took %5.2f seconds',
                time.time() - start)
    runs = ml.metalearning_suggest_all(exclude_double_configurations=True)
    #print(runs)
    return runs[:num_initial_configurations]
