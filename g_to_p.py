import matplotlib.patches as mp
from helper import top_users as t
import matplotlib.pyplot as plt


def top_user_plot(x,z):
    
    fig1, ax1 = plt.subplots()
    
    ax1.bar(x.index,x.values, color = ['red' if i in z else 'blue' for i in x.index])

    most_active = mp.Patch(color='red', label=(f"Top {len(z)} "))
    ax1.legend(handles=[most_active])
    #plt.xticks(rotation = 90)
    return fig1

#--------------------------------------------------------------------------------------------------------------------

def top_message(x,z):
    
    fig2, ax2 = plt.subplots()
            
    ax2.bar(x.index,x.values, color = ['red' if i in z else 'blue' for i in x.index])

    most_active = mp.Patch(color='red', label=(f"Top {len(z)} "))
    ax2.legend(handles=[most_active])
    plt.xticks(rotation = 90)
    return fig2
    

    # Hourly Activity Patterns by Month
# Identify peak activity hours for each month. For example, create a heatmap where rows represent days and columns represent hours, showing the message counts in each cell.
# Detect shifts in activity patterns across months. Is there a specific time range with high activity that changes monthly?
# 2. User Consistency and Engagement Score
# Calculate an "engagement score" for each user based on the frequency and time spent messaging (e.g., average session duration, messages per session).
# Analyze user consistency by measuring how regularly users are active on specific days of the week or hours of the day.
# 3. Day-Level Seasonality
# Examine if certain days (e.g., weekends or Mondays) consistently have higher or lower activity. This can help identify trends like "weekday effect" or "weekend effect."
# Check if there are particular days of each month (like the 1st, 15th, or end of month) with significant changes in message counts.
# 4. Time Gaps and Response Speed Analysis
# Calculate the average time gap between consecutive messages for each user. This can help understand users’ responsiveness or inactivity periods.
# Identify patterns in response speed, like whether users respond faster in the mornings or evenings.
# 5. User Retention and Returning User Analysis
# Identify which users are “returning users” by checking activity patterns across months and finding users active in multiple months.
# Create retention cohorts, such as "new users in January," and track their activity in subsequent months to analyze retention.
# 6. Periodic Activity Fluctuation Detection
# Apply Fourier Transform or similar time-series techniques to detect any hidden periodic cycles in message volume (e.g., weekly or monthly cycles).
# Highlight if there are predictable peaks and troughs, which could indicate regular events or habits among users.
# 7. Hourly Activity Variability by User Type
# Identify users who have unusual activity patterns, like very late or early hour activity.
# Classify users based on when they are most active (e.g., “morning users,” “evening users”) and analyze differences between these groups.
# 8. Monthly and Quarterly Trends Analysis
# Detect trends across longer intervals like quarters or semesters to see if there’s consistent growth, decline, or seasonality in user activity.
# Break down user activity trends over time (e.g., average messages per user) to understand overall engagement levels.
# 9. Identify Inactive Users and Churn Prediction
# Analyze the time since each user’s last message and flag users who may be at risk of inactivity or churn.
# Build a simple model to predict churn based on users’ recent activity patterns.
# 10. Sequential Patterns in User Activity
# Use sequential pattern mining to find common patterns, like specific times or days when users tend to message most.
# Discover if users follow a particular sequence of high-activity times, which can give insights into user habits.