#C:\Users\joshi\Documents\Billionaires Statistics Dataset.csv"
'''import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Excel file
file_path = 'Billionaires Statistics Dataset.csv'  # Replace with your file name or path
df = pd.read_csv(file_path)

# Step 2: Inspect the data
print("Column names:", df.columns)
print("First few rows of the data:")
print(df.head())

# Step 3: Visualize the categorical variable (e.g., 'Gender')
if 'Gender' in df.columns:
    plt.figure(figsize=(10, 5))
    gender_counts = df['Gender'].value_counts()
    plt.bar(gender_counts.index, gender_counts.values, color=['blue', 'pink', 'green'])
    plt.title("Distribution of Gender")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.show()
else:
    print("'Gender' column not found in the dataset.")

# Step 4: Visualize the continuous variable (e.g., 'Age')
if 'Age' in df.columns:
    plt.figure(figsize=(10, 5))
    plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
    plt.title("Distribution of Age")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()
else:
    print("'Age' column not found in the dataset.")'''
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded CSV file
file_path = 'Billionaires Statistics Dataset.csv'
df = pd.read_csv(file_path)

# Inspect the dataset
print("Column names:", df.columns)
print("First few rows of the dataset:")
print(df.head())

# Gender Distribution
if 'gender' in df.columns:
    gender_counts = df['gender'].value_counts()
    plt.figure(figsize=(8, 5))
    plt.bar(gender_counts.index, gender_counts.values, color=['blue', 'pink', 'green'])
    plt.title("Distribution of Gender")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.show()
else:
    print("'gender' column not found in the dataset.")

# Age Distribution
if 'age' in df.columns:
    age_data = df['age'].dropna()  # Remove NaN values
    plt.figure(figsize=(8, 5))
    plt.hist(age_data, bins=10, color='skyblue', edgecolor='black')
    plt.title("Distribution of Age")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()
else:
    print("'age' column not found in the dataset.")

# Optional: Age Distribution by Gender
if 'age' in df.columns and 'gender' in df.columns:
    plt.figure(figsize=(8, 5))
    for gender in df['gender'].unique():
        subset = df[df['gender'] == gender]['age'].dropna()
        plt.hist(subset, bins=10, alpha=0.5, label=f"{gender}")
    plt.title("Age Distribution by Gender")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()
else:
    print("Either 'age' or 'gender' column not found in the dataset.")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the uploaded CSV file
file_path = 'Billionaires Statistics Dataset.csv'
df = pd.read_csv(file_path)

# Inspect the dataset
print("Column names:", df.columns)
print("First few rows of the dataset:")
print(df.head())

# Check if 'gender' and 'age' columns are present
if 'gender' in df.columns and 'age' in df.columns:
    # Drop rows with missing values for age and gender
    df_clean = df.dropna(subset=['age', 'gender'])

    # Set up the plot
    plt.figure(figsize=(10, 6))
    
    # Plot the distribution of age by gender using seaborn's histplot
    sns.histplot(data=df_clean, x='age', hue='gender', kde=True, bins=15, multiple="stack", palette="Set2")
    
    # Customize the plot
    plt.title("Age Distribution by Gender")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.legend(title="Gender")
    
    # Display the plot
    plt.show()
else:
    print("Either 'age' or 'gender' column not found in the dataset.")'''




#C:\Users\joshi\Documents\Billionaires Statistics Dataset.csv"


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the uploaded CSV file
file_path = 'Billionaires Statistics Dataset.csv'
df = pd.read_csv(file_path)

# Inspect the dataset
print("Column names:", df.columns)
print("First few rows of the dataset:")
print(df.head())

# Check if 'gender' and 'age' columns are present
if 'gender' in df.columns and 'age' in df.columns:
    # Drop rows with missing values for age and gender
    df_clean = df.dropna(subset=['age', 'gender'])

    # Set up the plot
    plt.figure(figsize=(10, 6))
    
    # Plot the distribution of age by gender using seaborn's histplot
    sns.histplot(data=df_clean, x='age', hue='gender', kde=True, bins=15, multiple="stack", palette="Set2")
    
    # Customize the plot
    plt.title("Age Distribution by Gender")
    plt.xlabel("Age")
    plt.ylabel("Frequency")

    # Manually set the legend
    handles, labels = plt.gca().get_legend_handles_labels()  # Get current legend handles and labels
    plt.legend(handles, labels, title="Gender")  # Reapply the legend with the correct title
    
    # Display the plot
    plt.show()
else:
    print("Either 'age' or 'gender' column not found in the dataset.")




