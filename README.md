
# Observing impact of incomplete data on different insight types


 
  - For more detail, please read our full paper:  [Quality Matters: Understanding the Impact of Incomplete Data on Visualization Recommendation](https://www.researchgate.net/publication/342735942_Quality_Matters_Understanding_the_Impact_of_Incomplete_Data_on_Visualization_Recommendation)
  - We used three types of insights in this work: Aggregate-based insight, correlation-based insight, and distribution-based insight
  - We observed impact of missing data with different settings: different missing data percentage, different number of k, etc



### Preparation

For the aggregate-based insight, PostgreSQL engine should be installed first. 

```sh
$ cd 0_generate_data
$ python import_heart_data_to_postgreSQL.py
$ python generate_missing_data_version_postgreSQL.py
```

The second command is for importing heart disease data (csv format) to Postgre engine. Then, the next line is to generate missing data version of heart disease data.


### Aggregate-based Insight


```sh
$ cd aggregate_based_insight
$ python a_seedb_main.py
$ python 3_0_div_missing_a_m_vs_ideal.py #Outstanding-based insight - deviation
$ python 3_0_sim_missing_a_m_vs_ideal.py #Similarity-based insight 
```

The second command line is to generate all possible visualizations with their utility scores. The results are stored in Excel file. 
The next lines are for calculating the Jaccard, RBO, and Cumulative distance scores based on the comparison of recommended visualizatiosn from the incomplete data and the recommended visualizations from the ideal/complete data.  

### Other Insight Types

For other insight types, the postgreSQL is not needed. 
```sh
$ cd other_insight_types
$ python 0_correlation_insights_random.py #Correlation-based insight
$ python 1_kurt_insight_random.py #Kurtosis-based insight
$ python 2_skewness_insight_random.py #Skewness-based insight
```

#### Plot the result

```sh
$ cd plotting
$ python example_plotting_result_impact_missing_data_5_insights_RBO.py
```
Result: 

![](https://raw.githubusercontent.com/rischanlab/impact_incomplete_data_on_insights/master/plotting/RBO_impact_missing_data_5_insights.svg )
