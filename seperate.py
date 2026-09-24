import pandas as pd

chunk_size = 10000

for i, chunk in enumerate(pd.read_csv("download2025.csv", chunksize=chunk_size)):
    chunk.to_csv(f"download2025_part{i+1}.csv", index=False)

for i, chunk in enumerate(pd.read_csv("download2024.csv", chunksize=chunk_size)):
    chunk.to_csv(f"download2024_part{i+1}.csv", index=False)

for i, chunk in enumerate(pd.read_csv("download2023.csv", chunksize=chunk_size)):
    chunk.to_csv(f"download2023_part{i+1}.csv", index=False)

for i, chunk in enumerate(pd.read_csv("download2026.csv", chunksize=chunk_size)):
    chunk.to_csv(f"download2026_part{i+1}.csv", index=False)

print("완료")