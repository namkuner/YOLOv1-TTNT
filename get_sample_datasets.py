import pandas as pd
def read_csv(num_of_sample):
    df = pd.read_csv("data/train.csv", nrows=num_of_sample)
    df.to_csv(f"data/{num_of_sample}_examples.csv", index=False)

if __name__ == "__main__":
    read_csv(1000)