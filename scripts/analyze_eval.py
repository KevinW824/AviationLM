import pandas as pd


def compute_source_accuracy(df, gold_col='gold_sources', pred_col='predicted_sources'):
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
    df = compute_source_accuracy(df, gold_col='sources', pred_col='response_sources')
    source_accuracy = df['source_correct'].mean()
    print(f"\nSource accuracy: {source_accuracy:.2f} (Exact match presence)")

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

Source accuracy: 0.87 (Exact match presence)
'''
