#"/Users/jacob.hu/Desktop/Jacob/Personal/Important/data science stuff/DatasetEconomic/realcs.py"

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
import streamlit as st
import re
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

filepath = ""

df = pd.read_csv(filepath + "inflation_interest_unemployment.csv")

df.columns = df.columns.to_series().apply(lambda x: re.sub("\(.*\)", "", x).replace("%", "percent").replace(" ", "_"))

tempDict = {'Inflation_for_consumer_prices_annual_percent': 'Inflation for Consumer Prices in Annual Percent',
'Inflation_for_GDP_deflator_annual_percent': 'Inflation for GDP Deflator in Annual Percent',
 'Real_interest_rate_percent': 'Real Interest Rate in Percentage',
 'Deposit_interest_rate_percent': 'Deposit Interest Rate in Percentage',
 'Lending_interest_rate_percent': 'Lending Interest Rate in Percentage',
 'Unemployment_total_percent_of_total_labor_force_national_estimate': 'National Estimate for Unemployment Rate of Total Labor Force',
 'Unemployment_total_percent_of_total_labor_force_modeled_ILO_estimate': 'Modeled ILO Estimate for Unemployment Rate of Total Labor Force'}

# sidebar menu
with st.sidebar: 
	selected = option_menu(
		menu_title = 'Navigation Pane',
		options = ['Abstract', 'Background Information', 'Data Cleaning', 'Exploratory Analysis','Data Analysis', 'Interactive', 'Conclusion', 'Bibliography'],
		menu_icon = 'arrow-down-right-circle-fill',
		icons = ['bookmark-check', 'book', 'apple', 'boxes', 'bar-chart', 
		'check2-circle','blockquote-left'],
		default_index = 0,
		)

if selected == 'Abstract':
	st.markdown('<h1>Abstract</h1>', unsafe_allow_html = True)
	
	st.markdown("In today's interconnected world, analyzing economic data of countries has become increasingly important for understanding global economic trends and identifying opportunities for growth and development. The ability to compare economic data across countries can provide valuable insights into how different economic policies and practices impact a nation's economic performance. In this case study paper, we will compare the economic data of several countries, examining key indicators such as GDP, inflation, unemployment rates, and trade balances. By examining these indicators, we will gain a deeper understanding of the economic strengths and weaknesses of each country, as well as the factors that contribute to their economic success or struggles. Through this analysis, we will draw conclusions about the ways in which countries can leverage their economic strengths and address their economic challenges to achieve sustainable growth and prosperity.")

	st.markdown('In this study, we will closely examine the economic data collected from each country and compare the difference between the national average of economic in different countries. Ultimately, a conclusion will be implemented to determine which country has a higher advantage or lower advatage in a economic area.')

	st.markdown('<a href = "https://data.worldbank.org">All Data Retrived From The World Bank</a>', unsafe_allow_html = True)

if selected == 'Background Information':
	st.markdown('<h1>Background Information</h1>', unsafe_allow_html = True)

	st.markdown('Comparing economic data for countries is an important process for understanding how different economies are performing and identifying areas for improvement. There are several steps involved in comparing economic data for countries.<br><br>The importance of comparing economic data for countries cannot be overstated. It provides valuable insights into how different economies are performing and can help identify areas for improvement. By comparing economic data across countries, policymakers can learn from the successes and failures of others, develop best practices, and implement policies that are most likely to promote economic growth and stability. Furthermore, investors and businesses can use economic data to make informed decisions about where to invest and operate, while researchers can use it to develop theories and test hypotheses about the nature of economic systems.', unsafe_allow_html = True)

	st.dataframe(df.sample(20))

if selected == 'Data Cleaning':
	st.markdown('<h1>Data Cleaning</h1>', unsafe_allow_html = True)

	st.markdown('In order to conduct analysis smoothly, it is crucial to remove or replace any incorrect or missing values. Through data cleaning, not only the dataset will become easier to interpret, the process also help us to familarize with the information contained in it. <br><br> To clean an economic dataset using Python, start by importing necessary libraries such as pandas and numpy. Load the dataset into a pandas DataFrame and explore its structure and content. Identify missing values and decide on an approach to handle them, such as removing rows or imputing values. Check for and remove any duplicate records that could affect analysis. Examine the data for inconsistencies and standardize them, ensuring consistent capitalization and representation. Adjust data types as needed, converting columns to datetime or numeric formats. Remove irrelevant columns that are not pertinent to the analysis. If necessary, normalize or scale numeric variables to a common range. Finally, save the cleaned dataset for future use. These steps provide a foundation for data cleaning in Python, allowing for accurate and reliable analysis of economic data.', unsafe_allow_html = True)

if selected == 'Exploratory Analysis':
	st.markdown('<h1>Exploratory Analysis</h1>', unsafe_allow_html = True)

	st.markdown('In order to see the patter of the confirmed,death and recovered vary between countries and WHO Regions and how they change with time, graphs are a straightforward way of demonstarting these data so that we get the chance to understand them better')

	st.markdown("To play with digital graphs on a webpage, you first need to locate the graph on the page. Once you have located it, you can usually click and drag different parts of the graph to adjust the values. This will allow you to see how the graph changes as you manipulate the data. Some graphs may also have interactive sliders or input fields that allow you to directly input different values and see the results in real-time. Make sure to pay attention to any instructions or guidance provided on the webpage to ensure that you are properly interacting with the graph and getting accurate results.")

	st.markdown("The four graphs displayed below can be used to show economic data for each country by presenting key indicators in a clear and concise way.")
 
	econCols = [col for col in df.columns if col not in ["iso3c", "iso2c", "adminregion", "incomeLevel", "year", "country"]]

	st.subheader('Choropleth based on economic indicators')

	econOptions = st.selectbox("Select feature to display", tempDict.values(), key = 1)

	dfcolumns = [k for k, v in tempDict.items() if v == econOptions][0]

	intChoGraph = px.choropleth(df, locations = "country", locationmode = "country names",animation_frame = "year", color = dfcolumns, height = 800, width = 800, labels = {col:"" for col in econCols})

	intChoGraph.update_layout(legend_title_text = "")

	st.plotly_chart(intChoGraph)

	st.markdown('Due to the nature of the choropleth graph missing values, a conclusion cannot be generated just from this graph. However, this chropleth graph does visualizes the different characteristics of interest rate changes in every country. Notice how as each interest rate characteristic changes by selection, the corresponding contries also change.')

	col1,col2 = st.columns([1,3])

	st.markdown('<h2>Line Plot</h2>', unsafe_allow_html = True)

	#line
	with st.form("Select a region and a numeric feature to study: LINE PLOT"):
		regionOptions = col1.selectbox("Select a region to study", df.adminregion.unique(), key = 2)
		econOptions2 = col1.selectbox("Select feature to display", tempDict.values(), key = 3)
		dfcolumns2 = [k for k, v in tempDict.items() if v == econOptions2][0]
		submitted = st.form_submit_button("Submit")

		if submitted:
			linePlot = px.line(df[df.adminregion == regionOptions], x = "year", y = dfcolumns2, color = "country", log_y = True, labels = tempDict)
			col2.plotly_chart(linePlot)

	col3,col4 = st.columns([1,3])

	st.markdown('<h2>Histogram</h2>', unsafe_allow_html = True)
	
	#histo
	with st.form("Select a region and a numeric feature to study: HISTOGRAM"):
		regionOptions2 = col3.selectbox("Select a region to study", df.adminregion.unique(), key = 4)
		econOptions3 = col3.selectbox("Select feature to display", tempDict.values(), key = 5)
		dfcolumns3 = [k for k, v in tempDict.items() if v == econOptions3][0]
		submitted = st.form_submit_button("Submit")

		if submitted:
			histogram = px.histogram(df[df.adminregion == regionOptions], x = "year", y = dfcolumns3, color = "country", log_y = True, labels = tempDict)
			col4.plotly_chart(histogram)

	col5,col6 = st.columns([1,3])

	st.markdown('<h2>Scatter Plot</h2>', unsafe_allow_html = True)

	#scatter
	with st.form("Select a region and a numeric feature to study: SCATTER-PLOT"):
		regionOptions3 = col5.selectbox("Select a region to study", df.adminregion.unique(), key = 6)
		econOptions4 = col5.selectbox("Select feature to display", tempDict.values(), key = 7)
		dfcolumns3 = [k for k, v in tempDict.items() if v == econOptions4][0]
		submitted = st.form_submit_button("Submit")

		if submitted:
			scatterP = px.scatter(df[df.adminregion == regionOptions], x = "year", y = dfcolumns3, color = "country", log_y = True, labels = tempDict)
			col4.plotly_chart(histogram)

	st.markdown("All the economic graphs and data displayed above can be used to analyze and understand the data analysis section of a case study. By examining the graphs, we can understand the economic performance of each country over time and compare their economic growth rates. The inflation rate data provides insight into the changes in the price of goods and services, which can help in forecasting future economic trends. The unemployment rate data can reveal the labor market conditions in each country and help to assess the potential demand for labor. By analyzing these graphs and economic indicators, we can gain a better understanding of the economic factors impacting the case study and make more informed decisions.")


if selected == 'Data Analysis':
	st.markdown('<h1>Data Analysis</h1>', unsafe_allow_html = True)

	st.markdown('<h2>Analysis #1: China</h2>', unsafe_allow_html = True)

	st.markdown('<h3>Comparing Inflation Across Countries</h3>', unsafe_allow_html = True)

	st.markdown("Let's start by comparing the inflation sitation as it has the most data, but also just one single variable making it easy to analyze. The inflation situation will analyze countries from all over the world")

	chinaInflation = px.scatter(df, x = "year", y = "Inflation_for_consumer_prices_annual_percent", animation_frame = "year", color = "year", hover_name = "country")

	st.plotly_chart(chinaInflation)

	st.markdown('<h3>Comparing Types of Interest Rates Across Countries</h3>', unsafe_allow_html = True)

	st.markdown("Let's continue by comparing the interest rates across countries, as it has three very similar variables, making the comparison having both equal amounts of similarities and differences. The interest rate analysis will compare countries from all over the world")

	chinaInterest = px.scatter(df, x = "year", y = "Real_interest_rate_percent", animation_frame = "year", color = "year", hover_name = "country")

	st.plotly_chart(chinaInterest)

	st.markdown('<h3>Comparing Unemployment Across Countries</h3>', unsafe_allow_html = True)

	st.markdown("Finally, lets compare the unemployment situation across countries, where it is merely just a estimate, and not exact like the other two analysis. The unemployment situation will analyze countries from all over the world")

	chinaUnemp = px.scatter(df, x = "year", y = "Unemployment_total_percent_of_total_labor_force_national_estimate", animation_frame = "year", color = "year", hover_name = "country")

	st.plotly_chart(chinaUnemp)

	st.markdown('<h2>Analysis #2: Afghanistan</h2>', unsafe_allow_html = True)

	st.markdown('<h3>Comparing Inflation Across Countries</h3>', unsafe_allow_html = True)

	st.markdown("Let's start by comparing the inflation sitation as it has the most data, but also just one single variable making it easy to analyze. The inflation situation will analyze countries from all over the world")

	afghanaInflation = px.scatter(df, x = "year", y = "Inflation_for_consumer_prices_annual_percent", animation_frame = "year", color = "year", hover_name = "country")

	st.plotly_chart(afghanInflation)
	
	st.markdown('<h3>Comparing Types of Interest Rates Across Countries</h3>', unsafe_allow_html = True)

	st.markdown("Let's continue by comparing the interest rates across countries, as it has three very similar variables, making the comparison having both equal amounts of similarities and differences. The interest rate analysis will compare countries from all over the world")
	
	afghanInterest = px.scatter(df, x = "year", y = "Real_interest_rate_percent", animation_frame = "year", color = "year", hover_name = "country")

	st.plotly_chart(afghanInterest)
	
	st.markdown('<h3>Comparing Unemployment Across Countries</h3>', unsafe_allow_html = True)

	st.markdown("Finally, lets compare the unemployment situation across countries, where it is merely just a estimate, and not exact like the other two analysis. The unemployment situation will analyze countries from all over the world")

	afghanUnemp = px.scatter(df, x = "year", y = "Unemployment_total_percent_of_total_labor_force_national_estimate", animation_frame = "year", color = "year", hover_name = "country")

	st.plotly_chart(afghanUnemp)
	
	st.markdown('<h2>Analysis #3: Belize</h2>', unsafe_allow_html = True)

	st.markdown('<h3>Comparing Inflation Across Countries</h3>', unsafe_allow_html = True)

	st.markdown("Let's start by comparing the inflation sitation as it has the most data, but also just one single variable making it easy to analyze. The inflation situation will analyze countries from all over the world")

	belizeInflation = px.scatter(df, x = "year", y = "Inflation_for_consumer_prices_annual_percent", animation_frame = "year", color = "year", hover_name = "country")

	st.plotly_chart(belizeInflation)
	
	st.markdown('<h3>Comparing Types of Interest Rates Across Countries</h3>', unsafe_allow_html = True)

	st.markdown("Let's continue by comparing the interest rates across countries, as it has three very similar variables, making the comparison having both equal amounts of similarities and differences. The interest rate analysis will compare countries from all over the world")
	
	belizeInterest = px.scatter(df, x = "year", y = "Real_interest_rate_percent", animation_frame = "year", color = "year", hover_name = "country")

	st.plotly_chart(belizeInterest)
	
	st.markdown('<h3>Comparing Unemployment Across Countries</h3>', unsafe_allow_html = True)

	st.markdown("Finally, lets compare the unemployment situation across countries, where it is merely just a estimate, and not exact like the other two analysis. The unemployment situation will analyze countries from all over the world")
	
	belizeUnemp = px.scatter(df, x = "year", y = "Unemployment_total_percent_of_total_labor_force_national_estimate", animation_frame = "year", color = "year", hover_name = "country")

	st.plotly_chart(belizeUnemp)
	
if selected == 'Interactive':
	st.markdown('<h1>Interactive</h1>', unsafe_allow_html = True)

	interactiveDf = df[['Real_interest_rate_percent', 'Deposit_interest_rate_percent', 'Lending_interest_rate_percent', 'Unemployment_total_percent_of_total_labor_force_national_estimate']].copy()

	intCol1, intCol2 = st.columns([5, 5])

	with st.form("test"):
		intCol1.markdown("Select your desired real interest rate in percentage:")
		realInterest = intCol1.slider("", 0.0, 20.0, 10.0, 0.5, key = "realInterest")
		intCol1.markdown("Select your desired deposit interest rate in percentage:")
		depInterest = intCol1.slider("", 0.0, 20.0, 10.0, 0.5, key = "depInterest")
		intCol2.markdown("Select your desired lending interest rate in percentage:")
		lendInterest = intCol2.slider("", 0.0, 20.0, 10.0, 0.5, key = "lendInterest")
		intCol2.markdown("Select your desired unemployment rate in percentage:")
		unemploy = intCol2.slider("", 0.0, 20.0, 10.0, 0.5, key = "unemploy")
		allUserInputs = np.array([realInterest, depInterest, lendInterest,unemploy])
		submitted = st.form_submit_button("Submit")
		if submitted:
			distances = interactiveDf.apply(lambda row: np.linalg.norm(row - allUserInputs), axis=1)
			dischoropleth = df.copy()
			dischoropleth["Distance"] = distances
			index_of_closest_row = distances.idxmin()
			closestRow = df.loc[index_of_closest_row].reset_index()
			closestRow.columns = ["ATTRIBUTES", "VALUE"]
			userYear = closestRow.loc[closestRow["ATTRIBUTES"] == "year", "VALUE"].iloc[0]
			fig = px.choropleth(dischoropleth.loc[dischoropleth["year"] == userYear], locations = "country", locationmode = "country names", color = "Distance", height = 800, width = 800, labels = tempDict)
			st.plotly_chart(fig)
			st.dataframe(closestRow.replace(tempDict))

if selected == 'Conclusion':
	st.markdown('<h1>Conclusion</h1>', unsafe_allow_html = True)

	st.markdown('<h1>Overall Conclusion</h1>', unsafe_allow_html = True)

	st.markdown("In conclusion, by harnessing the power of Python, we can effectively analyze and compare unemployment, interest rate, and inflation data across different countries. This enables us to gain valuable insights into the economic conditions and trends in various nations. Python's rich ecosystem of data analysis libraries, such as Pandas and Matplotlib, empowers us to efficiently process and visualize the data, facilitating a comprehensive understanding of the global economic landscape. By examining these key indicators, policymakers, economists, and researchers can make informed decisions, devise effective strategies, and monitor the impact of their actions in addressing unemployment, controlling inflation, and managing interest rates in a global context. Python's versatility and data analysis capabilities make it an invaluable tool for studying and comparing economic variables across countries.", unsafe_allow_html = True)

	st.markdown('<h1>Reflection on Process</h1>', unsafe_allow_html = True)

	st.markdown('The process of economic data analysis using Python typically involves several steps, including importing data, cleaning and preprocessing data, conducting exploratory data analysis, and building statistical models. This process can be both challenging and rewarding, as it requires a strong understanding of both economic theory and programming. However, with the right tools and techniques, Python can help economists make sense of complex data and generate meaningful insights that can inform policy decisions and drive innovation. Overall, economic data analysis using Python is an essential skill for anyone interested in working in the field of economics or data science.', unsafe_allow_html = True)

if selected == 'Bibliography':
	st.markdown('<h1>Bibliography</h1>', unsafe_allow_html = True)
