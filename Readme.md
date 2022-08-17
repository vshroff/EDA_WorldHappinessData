**Exploratory Data Analysis of the World Happiness Data**

**Part 1 - Analysing year 2019**

Our data frame gives us information about the happiness score of all the countries in the world, along with information about the GDP, social support, life expectancy, freedom, genorisity and perceptions of corruption.

From plot 1, we can see that GDP, social support etc are directly related to the Happiness score. However, genorisity and preceptions of corruption do not follow any indicative trend.

![PLOT 1](Plot1.png)

However, in the case of genorsity and perceptions - we can see that there are multiple outliers in our data frame. For example, we have examples of countries that have a low happiness score but people are generours and percieve that less corruption exists in the country.

In order to determine the trend for Genorosity and Corruption with the Happiness Score, we can reduce the effects of these outlier datapoints by the following method we will discuss in Part 2 -

**Part 2 - Analysing trends in depth**

In order to get a better understanding of the trend patterns, we can divide the countries into the following types - (using the function createTypeColumnList())

1. Happiest Countries - Score >= 7
2. Happier Countries - Score >= 6
3. Happy Countries - Score >= 5
4. Not Happy Countries - Score < 5

After dividing the countries into the above categories, we can find the average GDP, life expectancy, etc for each of the four sections (using the function createCondensedDf()) to create a condensed data frame.

Now, we have reduced the effects of outliers in our data visualization, and can plot the same below -

![PLOT 2](Plot2.png)

It is interesting to observe, contrary to our expectations, that unlike GDP per capita trends, freedom trends, etc, genorisity of a countries' citizens and their perception of corruption in their country, is not decreasing with the Happiness Score.

Instead, we can observe that in the year 2019, while Genorisity does not seem to be related to the Happiness of the country, the people's perception of corruption is relatively more for the countries with high happiness score.