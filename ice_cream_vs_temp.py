import plotly.express as px
import csv

with open("./data/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temprature.csv") as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x="Temperature", y="Ice-Cream Sales( ₹ )", color="week")
      fig.show()
