import argparse
import os
import psutil
import pandas as pd
import gc
from datetime import datetime


def get_memory_mb():
    return psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024


def parse_large_csv(filepath, chunksize, current_date_str):
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    total_rows = 0
    sum_subscription_days = 0
    initial_memory = get_memory_mb()
    
    for i, chunk in enumerate(pd.read_csv(filepath, chunksize=chunksize)):
        total_rows += len(chunk)
        chunk["Subscription Date"] = pd.to_datetime(chunk["Subscription Date"])
        chunk["Subscription Days"] = (current_date - chunk["Subscription Date"]).dt.days

        sum_subscription_days += chunk["Subscription Days"].sum()
        mean_subscription_days = chunk["Subscription Days"].mean()
        memory_used = get_memory_mb() - initial_memory
        print(f"Chunk {i+1}: {total_rows:,} rows processed, Mean Subscription Days: {round(mean_subscription_days, 2)}, Memory Used: {memory_used:.2f} MB")

        del chunk
        gc.collect()
    avg_subscription_days = sum_subscription_days / total_rows
    print(f"\nOverall average subscription days: {avg_subscription_days:.2f}")


def main():
    parser = argparse.ArgumentParser(description="Parse large CSV files and calculate subscription days")
    parser.add_argument("filepath", help="Path to the CSV file to process")
    parser.add_argument("--chunksize", "-c", type=int, default=100000, 
                       help="Number of rows to process in each chunk (default: 100000)")
    parser.add_argument("--date", "-d", default="2022-05-29",
                       help="Current date in YYYY-MM-DD format (default: 2022-05-29)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.filepath):
        print(f"Error: File '{args.filepath}' not found")
        return 1
    
    try:
        parse_large_csv(args.filepath, args.chunksize, args.date)
    except Exception as e:
        print(f"Error processing file: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())