from SoccerNetExplorer import Explorer

if __name__ == "__main__":
    exp = Explorer("./data")
    exp.sentiment_to_csv()
    exp.master_csv()
