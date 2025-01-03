import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open("books.csv","r") as datafile:
    data = pd.read_csv(datafile,delimiter=",")
    
bins = [0, 2, 3, 4, 5]  # Define rating intervals
labels = ["0-2", "2-3", "3-4", "4-5"]  # Labels for each bin
data["rating_category"] = pd.cut(data["average_rating"], bins=bins, labels=labels, include_lowest=True)

sns.scatterplot(x="average_rating", y="# num_pages", size="# num_pages", sizes=(20, 180), data=data)

plt.xlabel("Average Rating")
plt.ylabel("Number of Pages")
plt.title("Average Rating and Number of Pages")
plt.savefig("Ratings-and-Pages.png")