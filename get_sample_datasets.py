import pandas as pd
def read_csv(type ="train",num_of_sample=1000):
    df = pd.read_csv(f"data/{type}.csv", nrows=num_of_sample)
    df.to_csv(f"data/{type}_{num_of_sample}_examples.csv", index=False)
    return f"data/{type}_{num_of_sample}_examples.csv"
if __name__ == "__main__":
    read_csv(1000)