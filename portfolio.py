import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


if "countries" not in st.session_state:
    st.session_state.countries = ["Zimbabwe"]

st.title(":violet[Theophilus Tawona Portfolio Site]")
st.subheader("Data Scientist\Mechanical Engineer")
st.divider()


tab1, tab2, tab3 = st.tabs(["About Me", "Projects", "Contact"])

with tab1:
    st.markdown("""
    Hello!👋 My Name is Theophilus Tawona and I am a self taught data analyst
    and this is my portfolio to showcase the skills I have gained over the years. I have a keen eye for detail and a love for problem-solving,
    I am driven to extract meaningful insights from complex datasets.
                
    I'm particularly interested in applying data analysis to engineering,
    marketing, energy, agriculture, and finance. My recent project analyzing 
    the global production of tobacco over the years show cases my exploratory data
    analysis and dashboarding skills. I am excited to leverage my skills to contribute to innovative projects and data-driven decising-making.
""")
    st.divider()
    st.markdown("#### :green[Skills]")
    

    st.markdown("""
    * Data Analysis
    * Machine learning(Time series analysis, Supervised and Unsupervised)
    * Dashboarding(Tablau, Power BI)
    * Programming(Python, SQL, Javascript)
    * Deeplearning(Tensorflow)
    * Data Modelling
    * Resilient
    * Adaptable
        


""")
    st.divider()
    st.markdown("#### :green[Education]")
   

    st.markdown("""
        * Bsc(Honors) in Mechanical Engineering - University of Zimbabwe



""")
    st.divider()
    st.markdown("### :green[Certifications]")



    st.markdown("""
        * ###### :blue[Accenture]
            * Data Analysis and Visualization Virtual Experience
        * ###### :blue[Cisco]
            * Data Analytics Essentials
            * Introduction to Data Science
        * ###### :blue[Deloite]
            * Technology Virtual Experience
""")
    
    st.markdown(""" :red[For verification of the certifications above visit my [linkedin](https://www.linkedin.com/in/theophilus-tawona) page and 
                navigate to the liscences and certifications section]""")
    st.divider()
    
    st.markdown("#### :green[Experience]")
    with st.popover("Read Me"):
        st.markdown("""
    Although my background and work experience do not directly have
    a link to data science, I used every opportunity I got to 
    analyze data using my tool sets and to profer data driven solutions.
                    
    Currently I am doing freelance work developing internal tools for companies.
""")
    
    st.markdown("""
    * ###### Finance Administrator - Mafadi Property Management-Contract
    * ###### Mechanical Engineering Intern - Zimplats
    * ###### Mechanical Engineering Intern - Proplastics
""")

with tab2:

    df = pd.read_csv("tobacco-production.csv")
    df['Year'] = df["Year"].astype(str)
    df.rename(columns={"Tobacco | 00000826 || Production | 005510 || tonnes": "tonnes"}, inplace=True)

    def line_plot():
        st.subheader("Interactive Tobacco Production Line Plot")

        # Select countries
        selected_countries = st.multiselect("Select Countries", df["Entity"].unique())

        # Create a plotly figure
        fig = go.Figure()

        # Iterate over selected countries and trace
        for country in selected_countries:
            country_data = df[df["Entity"] == country]
            fig.add_trace(go.Scatter(x=country_data["Year"], y=country_data["tonnes"],
                                     mode="lines", name=country))

        #Update the layout
        fig.update_layout(title="Tobacco Production by Country",
                          xaxis_title="Year", yaxis_title="Tobacco Production(tonnes)")

        #Display the chart
        st.plotly_chart(fig)

    def bar_plot():
        start_year, end_year = st.slider(
            label="Select Date Range",
            min_value=df["Year"].astype(int).min(),
            max_value=df["Year"].astype(int).max(),
            value=(df["Year"].astype(int).min(), df["Year"].astype(int).min() )
        )

        filtered_df = df[(df["Year"].astype(int)>= start_year) & (df["Year"].astype(int)<=end_year)]

        col1, col2 = st.columns([3,2])

        #Group by country and sum production
        top_producers = filtered_df.dropna(subset=["Code"]).groupby("Entity")["tonnes"].sum().reset_index()

        #sort to get top 10 producers
        top_10_producers = top_producers.nlargest(10, "tonnes")

        col1.plotly_chart(px.bar(data_frame=top_10_producers, x="Entity",
                                       y="tonnes"))
        col2.dataframe(top_10_producers, hide_index=True)

    def map_plot():
        data = df.dropna(subset=["Code"])

        #Create a year selection
        year = st.slider(label="Select Year", min_value=data["Year"].astype(int).min(), max_value=data["Year"].astype(int).max(),
                             value=data["Year"].astype(int).min())
            
        #Filter the dataframe for the selected year
        yearly_data = data[data["Year"].astype(int)==year]
        yearly_data = yearly_data[yearly_data["Entity"]!="World"]

        #Plotting the map
        fig = px.choropleth(yearly_data, locations="Entity",
                    locationmode="country names", color="tonnes", hover_name="Entity",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    labels={"tonnes":"Tobacco Production"},
                    title=f'Tobacco Production by Country {year}')
            
        st.plotly_chart(fig)

    st.markdown("#### Global Tobacco Production Exploratory Data Analysis")
    st.markdown("""
    This project explores the changes in the global production of tobacco.
""")
    
    pro_tab1, pro_tab2, pro_tab3 = st.tabs(["Table", "Charts", "Map"])

    with pro_tab1:
        st.dataframe(df, use_container_width=True)
    with pro_tab2:
        line_plot()

        with st.expander("More"):
            st.write("""
The above is an interactive visualization showing how tobacco production has changed
            since the 1960s. Below is a bar plot showing the top 10 tobacco producers
            at any given time. Use the slider to interact with the plot.
""")   
            bar_plot()

    with pro_tab3:
        map_plot()




    
with tab3:

    st.markdown("""
    :green[I am happy to work with anyone thats interested. In order to contact me use the form below
    or contact me using the links(preferable) provided.]
                
    * :red[linkedin]: https://www.linkedin.com/in/theophilus-tawona
    * :red[email]: theophilustawona@gmail.com
""")

    with st.form(key="Contact-Form", clear_on_submit=True):
        st.subheader("Contact Me ")
        st.text_input("Subject")
        st.text_area("Description")
        st.form_submit_button("Submit")