import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    df = pd.read_cvs(file)
    return df
def exercise_1(df):
    return df.columns.values.tolist()

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(n=k,axis=0)

def exercise_4(df):
    return df.type.unique()

def exercise_5(df):
    # Return a Pandas series of the top 10 transaction destinations with frequency
    return df['nameDest'].value_counts()[:10]


def exercise_6(df):
    fraudDetected = df.loc[df['isFraud']=='1']
    return fraudDetected

def exercise_7(df):
    # Bonus. Return a dataframe that contains the number of distinct destinations that each source has interacted with to, 
    # sorted in descending order.
    return df.groupby('nameOrig').count()['nameDest'].sort_values(ascending=False)



def visual_1(df):
    def transaction_counts(df):
        df.plot.bar(x='type',stacked=True,title='Transaction Counts')
        # df2[['abuse'f,'nff']].plot(kind='bar', stacked=True)
        # df[['type','isFraud']].groupby(['type']).count().plot(kind='bar',stacked=True, title='Transaction Counts')

    def transaction_counts_split_by_fraud(df):
        grouped = df.groupby(df['type'])
        return grouped

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction counts')
    axs[0].set_xlabel('type')
    axs[0].set_ylabel('count')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('transaction counts split by fraud')
    axs[1].set_xlabel('transaction type')
    axs[1].set_ylabel('coount')
    fig.suptitle('split by fraud')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return ("A bar graph of transaction counts split by fraud.")

    

def visual_2(df):
    def query(df):
        df.query('type == "CASH_OUT"')
    plot = query(df).plot.scatter(x='original account balance delca',y='Destination account balance delta')
    plot.set_title('Origin account balance delta v. Destination account balance delta scatter plot for Cash Out transactions')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return 'This is an Origin account balance delta v. Destination account balance delta scatter plot for Cash Out transactions'


def exercise_custom(df):
    top10 = df.nlargest(10,["amount"])
    return top10
    
def visual_custom(df):
    top10 = exercise_custom(df)
    plot = top10.plot.scatter(x= 'amount', 
                    y= 'dollars',
                    c = 'DarkBlue')
    return plot

