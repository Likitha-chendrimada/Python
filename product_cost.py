def filter_high_rated_expensive(df):
    # Filter products that satisfy all conditions
    filtered_df=df[ (df['rating']>=4.5) & (df['quantity_in_stock']>0)& (df['price']>=300) ]
    # Select required columns
    result=filtered_df[ ['product_id','product_name','rating','quantity_in_stock','price']]
    return result
