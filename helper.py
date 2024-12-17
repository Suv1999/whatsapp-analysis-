import matplotlib.pyplot as plt , matplotlib.patches as mp, streamlit as st, numpy as np 

def fetch_stats(df_processed):            # for total messages
    return df_processed.shape[0]
    # if user_sel == "Overall":
    #     return df_processed.shape[0] 
    # else:
    #     return df_processed[df_processed['User'] == user_sel].shape[0]
    
    
#______________________________________________________________________________________
# For words in messages
#------------------------------------------------------------------------------------
def user(x):                              # top words function  
    total_words = []
    for i in x: 
        j = i.split()
        for i in j:
            if len(i) > 4 and i not in ['<Media', 'omitted>','deleted','Missed','voice','message']:
                total_words.append(i)

    return(total_words)


def user_(x):                              # for total_ words function  
    total_words = []
    for i in x: 
        j = i.split()
        for i in j:
            if i not in ['<Media', 'omitted>']:
                total_words.append(i)

    return(total_words)

def total_words_(user_sel,df_processed):    # for total_ words in message 

    if user_sel == "Overall":
        x = df_processed["Message"]
        y = len(user_(x))
        return y
    else:
        x = df_processed[df_processed['User'] == user_sel]["Message"]
        y = len(user_(x))
        return y
    
#---------------------------------------------------------------------------------
  # Total Media ( problem: '<media omitted>' was not printed due to space in it )
#---------------------------------------------------------------------------------

def media_(df_processed):
    x = df_processed[df_processed['Message'].str.strip() == '<Media omitted>'] # .str.strip() Remove any surrounding whitespace
    return x.shape[0]


    # if user_sel == "Overall":  
    #    x = x[x['Message'].str.strip() == '<Media omitted>'] # .str.strip() Remove any surrounding whitespace
    #    return x.shape[0]
    # else:
    #     x = x[(x['Message'].str.strip() == '<Media omitted>') & (x['User'] == user_sel)] 
    #     return x.shape[0]
    
#---------------------------------------------------------------------------------
 # Chat contribution.
#---------------------------------------------------------------------------------

def chat_cont_(user_sel,df_processed):
    # x = df_processed.shape[0]
    # y = df_processed[df_processed['User'] == user_sel].shape[0]

    # return (f"{round(y/x,2)*100} % ")
    
    x = df_processed.shape[0]
    if user_sel in df_processed['User'].unique().tolist():
        y = df_processed[df_processed['User'] == user_sel ].shape[0]
        return (f"{round(y/x,2)*100} % ")
    else:
        return '100%'
    
#----------------------------------------------------------------------------------------------
# top users (Problem: direct plot cant work in streamlit so used fig, ax )
#----------------------------------------------------------------------------------------------

def top_users(x1):
    x_ = x1
    
    x = x_.value_counts().head(10)
    y = len(x)

    if y > 5:
        z = x.index.tolist()[:5]
    else:   
        z = x.index.tolist()[:1]
    return x,z
    
#----------------------------------------------------------------------------------------------
# monthly activity 
#----------------------------------------------------------------------------------------------
def monthly_activity(x_):
    month_order = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]
    month_positions = np.arange(len(month_order))
    year_unique = x_['Year'].unique().tolist()

    # Create a figure for plotting
    fig4, ax = plt.subplots(figsize=(10, 8))
    bar_width = 0.39

    # Plot bars for each year
    for i, year in enumerate(year_unique):
        x = x_['Month'][x_['Year'] == year].value_counts()
        y = x.reindex(month_order, fill_value=0)

        ax.bar(np.arange(len(month_order)) - 0.4 + i * 0.4, y.values, width=bar_width, label=year)
    
    # Set x and y ticks and labels
    ax.set_xticks(month_positions - 0.14)
    ax.set_xticklabels(month_order, rotation=90)
    ax.set_yticks(np.arange(500, 3500, 500))
    ax.legend()

    # Add text labels for each bar
    for i, year in enumerate(year_unique):
        y = x_.loc[x_['Year'] == year, 'Month'].value_counts().reindex(month_order, fill_value=0)
        for j, value in enumerate(y.values):
            ax.text(month_positions[j] - 0.4 + i * 0.4, value, str(value), ha='center', va='bottom', fontsize=8)

    # Return the figure to display it in Streamlit
    return fig4

from io import BytesIO
def fig_to_image(month_active):
    buf = BytesIO()
    month_active.savefig(buf, format="png")
    buf.seek(0)
    plt.close(month_active)  # Close the figure after saving it to the buffer
    return buf



#----------------------------------------------------------------------------------------------
# wordcloud 
#----------------------------------------------------------------------------------------------

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def word_cloud(df_processed):

    fig3, ax3 = plt.subplots(figsize=(4, 5))
    # Combine all the text from the specified column into a single string
    text = " ".join(df_processed['Message'].astype(str).tolist())

    wordcloud = WordCloud(width=1000, height=700, background_color='white').generate(text)
    
    ax3.imshow(wordcloud, interpolation='bilinear')
    ax3.axis("off")

    return fig3


#--------------------------------------------------------------------------------------------------
# top used words 
#--------------------------------------------------------------------------------------------------
import pandas as pd     
def top_words(x):
    x_ = x
    y = user(x_)
    y = pd.Series(y)
    #z = top_users(y)
    return y

#--------------------------------------------------------------------------------------------------
# monthly_active_heatmap   # problem months mismatch some have 12 some have 10 
#--------------------------------------------------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Define the function for the heatmap
def active_heatmap(x_,year):


    month_ = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
              
    yearly_ = x_["Month"].unique().tolist()
    
    month_order = [i for i in month_ if i in yearly_]
    
   
    busy_day = x_.groupby(['Month', 'Day'])['Minute'].count().reset_index()
    busy_day['Month'] = pd.Categorical(busy_day['Month'], categories=month_order, ordered=True)
    
    # Pivot the data to prepare for heatmap
    busy_day_pivot = busy_day.pivot(index='Day', columns='Month', values='Minute')
    
    # Plot heatmap with fig, ax
    fig5, ax = plt.subplots(figsize=(11, 12))
    sns.heatmap(busy_day_pivot, annot=True, cmap="YlGnBu", cbar=True, fmt='g', ax=ax)
    

    ax.set_title(f"Heatmap of Activity of {"All" if year == 0 else year}")
    ax.set_xlabel("Month")
    ax.set_ylabel("Day")
    
    # Display plot in Streamlit
    return fig5

# Example usage (assuming x_ is your DataFrame)
# cative_heatmap(x_)


    