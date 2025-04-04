
import sys
import matplotlib
import streamlit as st
import pandas as pd
import preprocessor as pro, helper as h
import g_to_p as g

# Sidebar configuration
st.sidebar.title(" Whatsapp Chat Analyser")
df_file = st.sidebar.file_uploader(label="Upload Dataset", type=["csv", "xlsx"])

if df_file is not None:  
    if df_file.name.endswith('.csv'):          # Load the uploaded file
        df = pd.read_csv(df_file)
    elif df_file.name.endswith('.xlsx'):       # Load the uploaded file
        df = pd.read_excel(df_file)
    
    st.write("Uploaded Successfully!")
    st.write("Preview:")
    st.dataframe(df.head(1))                   # Display the first row
    
    df_processed = pro.preprocessor(df) # Process the uploaded DataFrame
    st.write("Processed Data Preview:")
    st.dataframe(df_processed.head(1))

    users = df_processed['User'].unique().tolist()                    # list of total users 
    users.insert(0,"Overall")
    user_sel = st.sidebar.selectbox("Select User to Analyse", users)    # selected user 
    
    year_ = df_processed['Year'].unique().tolist()
    year_.insert(0,"Overall")
    year = st.sidebar.selectbox("Select Year", year_)

#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

    if st.sidebar.button("Click to Analyse"):

#_______________________________________________________________________________________________________
# total msg 
#___________________________________________________________________________________________________

        if user_sel == "Overall" and year != "Overall":
             total_mg = h.fetch_stats(df_processed[(df_processed["Year"] == year)])
        elif user_sel != "Overall" and year != "Overall":
             total_mg = h.fetch_stats(df_processed[(df_processed["Year"] == year) & (df_processed["User"] == user_sel)])
        elif user_sel != "Overall" and year == "Overall":
            total_mg = h.fetch_stats(df_processed[(df_processed["User"] == user_sel)])
        else:
             total_mg = h.fetch_stats(df_processed)

#_______________________________________________________________________________________________________
# words in message 
#___________________________________________________________________________________________________

        # words_mg = h.total_words_(user_sel,df_processed)

        if user_sel == "Overall" and year != "Overall":
             words_mg = h.total_words_(user_sel,df_processed[(df_processed["Year"] == year)])
        elif user_sel != "Overall" and year != "Overall":
             words_mg = h.total_words_(user_sel,df_processed[(df_processed["Year"] == year) & (df_processed["User"] == user_sel)])
        elif user_sel != "Overall" and year == "Overall":
            words_mg = h.total_words_(user_sel,df_processed[(df_processed["User"] == user_sel)])
        else:
             words_mg = h.total_words_(user_sel,df_processed)

#_______________________________________________________________________________________________________
# top_words
#___________________________________________________________________________________________________

        if user_sel == "Overall" and year != "Overall":
             top_words = h.top_words(df_processed['Message'][(df_processed["Year"] == year) ])
        elif user_sel != "Overall" and year != "Overall":
             top_words = h.top_words(df_processed['Message'][(df_processed["Year"] == year) & (df_processed["User"] == user_sel)])
        elif user_sel != "Overall" and year == "Overall":
             top_words = h.top_words(df_processed['Message'][(df_processed["User"] == user_sel)])
        else:
             top_words = h.top_words(df_processed['Message'])

        x_,z_ = h.top_users(top_words)  

#_______________________________________________________________________________________________________
# media sent (c3)
#___________________________________________________________________________________________________
# media_mg = h.media_(user_sel,df_processed)

        if user_sel == "Overall" and year != "Overall":
             media_mg = h.media_(df_processed[(df_processed["Year"] == year) ])
        elif user_sel != "Overall" and year != "Overall":
             media_mg = h.media_(df_processed[(df_processed["Year"] == year) & (df_processed["User"] == user_sel)])
        elif user_sel != "Overall" and year == "Overall":
             media_mg = h.media_(df_processed[(df_processed["User"] == user_sel)])
        else:
             media_mg = h.media_(df_processed)

#_______________________________________________________________________________________________________
#percentage contribution (c4)
#___________________________________________________________________________________________________
# perct_mg = h.chat_cont_(user_sel,df_processed)

        if user_sel == "Overall" and year != "Overall":
             perct_mg = h.chat_cont_(user_sel,df_processed[(df_processed["Year"] == year)])
        elif user_sel != "Overall" and year != "Overall":
             perct_mg = h.chat_cont_(user_sel,df_processed[(df_processed["Year"] == year)])
        elif user_sel != "Overall" and year == "Overall":
             perct_mg = h.chat_cont_(user_sel,df_processed)
        else:
             perct_mg = h.chat_cont_(user_sel,df_processed)

#_______________________________________________________________________________________________________
# Avg mesagae  
#___________________________________________________________________________________________________

        # def avg_mg():
             


        # if user_sel == "Overall" and year != "Overall":
        #      avg_mg_v = h.avg_mg(df_processed[(df_processed["Year"] == year)],)
        # elif user_sel != "Overall" and year != "Overall":
        #      media_mg = h.media_(df_processed[(df_processed["Year"] == year) & (df_processed["User"] == user_sel)])
        # elif user_sel != "Overall" and year == "Overall":
        #      media_mg = h.media_(df_processed[(df_processed["User"] == user_sel)])
        # else:
        #      media_mg = h.media_(df_processed)


#_______________________________________________________________________________________________________

#___________________________________________________________________________________________________



        c1,c2,c3,c4,c5 = st.columns(5)
        
        with c1: 
            # st.header("Total Messages")
            # st.title(total_mg)
            st.metric(label="Total Messages", value= total_mg)

        with c2:
            #st.header("Total words in messages")
            #st.title(words_mg)
            #st.markdown(f"<h2 style='color: #4CAF50; font-family: Arial; font-weight: bold;'>{words_mg}</h2>", unsafe_allow_html=True)

            st.metric(label="Total words in messages", value=words_mg)

        with c3:
            st.metric(label="Total media sent", value = media_mg)

        with c4:
            st.metric(label = "Total contribution", value = (perct_mg))

#____________________________________________________________________________________________

        def centered_header(text, size="20px"):
            st.markdown(
            f"""
            <div style='text-align: center; margin-bottom: -15px; padding-bottom: 0px;'>
            <h3 style='font-size:{size}; margin: 0px; padding: 0px;'><u>{text}</u></h3>
            </div> """, unsafe_allow_html=True)
        
        c1,c2 = st.columns(2)

#--------------------------------------------------------------------------------------------
 # top user
#____________________________________________________________________________________________
        #x,z = h.top_users(df_processed["User"])

        if user_sel == "Overall" and year != "Overall":
            x,z = h.top_users(df_processed["User"][(df_processed["Year"] == year)])
        elif user_sel != "Overall" and year != "Overall":
            x,z = h.top_users(df_processed["User"][(df_processed["Year"] == year)])
        else:
            x,z = h.top_users(df_processed["User"])
        
        with c1:
            centered_header("Most Active Users")
            st.pyplot(g.top_user_plot(x,z))

#--------------------------------------------------------------------------------------------
# top used words  
#____________________________________________________________________________________________
        with c2:
            centered_header("Top Messages")
            st.pyplot(g.top_message(x_,z_))

        # st.markdown("<div style='text-align: center;'><h3 style = 'font-size:20px;'> Word Cloud</h3>", unsafe_allow_html=True)
        # st.pyplot(wrd_cloud)


#--------------------------------------------------------------------------------------------
# word cloud
#____________________________________________________________________________________________
        
        if user_sel == "Overall" and year != "Overall":
             wrd_cloud = h.word_cloud(df_processed[(df_processed["Year"] == year) ])
        elif user_sel != "Overall" and year != "Overall":
             wrd_cloud = h.word_cloud(df_processed[(df_processed["Year"] == year) & (df_processed["User"] == user_sel)])
        elif user_sel != "Overall" and year == "Overall":
             wrd_cloud = h.word_cloud(df_processed[(df_processed["User"] == user_sel)])
        else:
             wrd_cloud = h.word_cloud(df_processed)

        centered_header("Word Cloud")
        st.pyplot(wrd_cloud)


#=----------------------------------------------------------------------------------------------------
# monthly_active_ (problem faced how to adjust multiple graph)
#_____________________________________________________________________________________________________    

        if user_sel == "Overall" and year != "Overall":
            month_active = h.monthly_activity(df_processed[(df_processed["Year"] == year)])
            image_ = h.fig_to_image(month_active)
        elif user_sel != "Overall" and year != "Overall":
            month_active = h.monthly_activity(df_processed[(df_processed["Year"] == year) & (df_processed["User"] == user_sel)])
            image_ = h.fig_to_image(month_active)
        else:
            y = df_processed['Year'].unique().tolist()[::-1][:2]
            month_active = h.monthly_activity(df_processed[df_processed["Year"].isin(y)])
            image_ = h.fig_to_image(month_active)
            
        centered_header("Year Activity")
        st.image(image_)

#=----------------------------------------------------------------------------------------------------
# monthly_active_heatmap
#_____________________________________________________________________________________________________

        if user_sel == "Overall" and year != "Overall":
            month_active = h.active_heatmap(df_processed[(df_processed["Year"] == year)], year)
            image_ = h.fig_to_image(month_active)
        elif user_sel != "Overall" and year != "Overall":
            month_active = h.active_heatmap(df_processed[(df_processed["Year"] == year) & (df_processed["User"] == user_sel)],year)
            image_ = h.fig_to_image(month_active)
        elif user_sel != "Overall" and year == "Overall":
            month_active = h.active_heatmap(df_processed[(df_processed["User"] == user_sel)],year)
            image_ = h.fig_to_image(month_active)
        else:
            #y = df_processed['Year'].unique().tolist()[::-1][:2]
            month_active = h.active_heatmap(df_processed,0)
            image_ = h.fig_to_image(month_active)
        
        centered_header("Year Activity")
        st.image(image_)

else:
    st.markdown("""
<div style="text-align: center; font-family: Arial, sans-serif; border-radius: 10px; padding: 20px; background-color: #FFCDD2; color: #B71C1C;">
    <h2 style="color: #B71C1C;">⚠️ Disclaimer ⚠️</h2>
    <p style="font-size: 16px; font-weight: bold;">
        This Webapp currently supports files in the <code>.csv</code> format.
    </p>
    <p style="font-size: 16px;">
        Please <a href="https://convertio.co/csv-converter/" style="color: #FFFFFF; font-weight: bold; text-decoration: none;">Click here</a> to convert your file to <code>.csv</code> format 
        and then upload it for analysis.
    </p>
</div>
""", unsafe_allow_html=True)




# streamlit run app_1.py