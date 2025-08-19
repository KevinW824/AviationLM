import pandas as pd


def compute_recall_at_5(df, gold_col='gold_sources', pred_col='predicted_sources'):
    """
    Compute a boolean source correctness metric: True if the gold source appears
    within the predicted_sources list; False otherwise.
    
    Args:
        df: DataFrame containing the evaluation data
        gold_col (str): Column name containing the gold standard sources
        pred_col (str): Column name containing the predicted sources
        
    Returns:
        DataFrame: Input DataFrame with a new 'source_correct' column added
    """
    correct = []
    for gold, pred in zip(df[gold_col], df[pred_col]):
        gold_str = str(gold).strip()
        pred_list = [p.strip() for p in str(pred).split(';') if p.strip()]
        correct.append(gold_str in pred_list)
    df['source_correct'] = correct
    return df


def compute_mrr_at_k(predicted_sources, gold_sources, k=5):
    """
    Reciprocal Rank contribution for a single example at cutoff k.
    predicted_sources: sequence of predicted source identifiers/strings
    gold_sources: single gold source or sequence of gold sources
    """
    # Normalize gold sources to a set of trimmed strings, supporting both list-like and semicolon-delimited strings
    if isinstance(gold_sources, (list, set, tuple)):
        gold_iter = gold_sources
    else:
        gold_iter = [p.strip() for p in str(gold_sources).split(';')]
    gold_set = {str(g).strip() for g in gold_iter if str(g).strip()}
    if not gold_set:
        return 0.0
    # Normalize predicted sources similarly and respect rank order
    if isinstance(predicted_sources, (list, set, tuple)):
        pred_list = [str(p).strip() for p in predicted_sources if str(p).strip()]
    else:
        pred_list = [p.strip() for p in str(predicted_sources).split(';') if p.strip()]
    for i, src in enumerate(pred_list[:k], start=1):
        if str(src).strip() in gold_set:
            return 1.0 / i
    return 0.0


def compute_df_mrr_at_k(df, gold_col='sources', pred_col='response_sources', k=10):
    """
    Compute MRR@k over a DataFrame without modifying it. Assumes sequence-like columns.
    Returns a float.
    """
    if len(df) == 0:
        return 0.0
    rr = df.apply(lambda r: compute_mrr_at_k(r[pred_col], r[gold_col], k=k), axis=1)
    return float(rr.mean())


if __name__ == '__main__':
    csv_path = 'data/eval/eval_results.csv'

    df = pd.read_csv(csv_path)

    # Ensure score column is numeric
    df['score'] = pd.to_numeric(df['score'], errors='coerce').fillna(0).astype(int)

    num_items = len(df)
    total_score = df['score'].sum()
    max_score = num_items * 5
    average_score = df['score'].mean()
    score_percentage = (total_score / max_score) * 100 if max_score > 0 else 0

    print(f"Number of items: {num_items}")
    print(f"Total score: {total_score}/{max_score} ({score_percentage:.2f}%)")
    print(f"Average score: {average_score:.2f} / 5.00")

    # Score distribution
    dist = df['score'].value_counts().sort_index()
    print("\nScore distribution:") 
    for score, count in dist.items():
        print(f"  Score {score}: {count} items")

    # Compute and display source metrics
    df = compute_recall_at_5(df, gold_col='sources', pred_col='response_sources')
    source_accuracy = df['source_correct'].mean()
    print(f"\nRecall@5: {source_accuracy:.2f} (Exact match presence)")

    # Compute and display MRR@10
    mrr_at_5 = compute_df_mrr_at_k(df, gold_col='sources', pred_col='response_sources', k=5)
    print(f"MRR@5: {mrr_at_5:.4f}")

    # Show worst-performing items
    worst_scores = df.nsmallest(10, 'score')
    print("\nTen lowest-scoring items:")
    for idx, row in worst_scores.iterrows():
        print(f"{idx+1}. Q: {row['instruction']} -> Score: {row['score']}, Source Correct: {row['source_correct']}")


'''
Number of items: 100
Total score: 411/500 (82.20%)
Average score: 4.11 / 5.00

Score distribution:
  Score 1: 7 items
  Score 2: 7 items
  Score 3: 8 items
  Score 4: 24 items
  Score 5: 54 items

Recall@5: 0.87 (Exact match presence)
MRR@5: 0.8042
'''
