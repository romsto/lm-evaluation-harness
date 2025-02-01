from rouge_score import rouge_scorer


ROUGE_SCORER = None


def process_results(references, predictions):
    return rouge_scores(references["highlights"], predictions[0])


def rouge_scores(reference: str, prediction: str):
    global ROUGE_SCORER
    rouge_types = ["rouge1", "rouge2", "rougeLsum"]
    if ROUGE_SCORER is None:
        ROUGE_SCORER = rouge_scorer.RougeScorer(rouge_types)

    # Some highlights have spaces before periods, which messes up the ROUGE scorer.
    result = ROUGE_SCORER.score(reference.replace(" . ", ". "), prediction)
    return {type: result[type].fmeasure * 100 for type in rouge_types}
