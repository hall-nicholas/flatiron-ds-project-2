#### Phase 2 Project
# Home Restoration Proposal for King County Restorations 

![seattle1](https://user-images.githubusercontent.com/103558721/190694582-8d94c976-ba14-410a-b0e6-d712229b125f.PNG)


### Prepared by team 'For King & County':
Patrick Arnold, Nick Hall, Dan Moreira,

![neighborhood1](https://user-images.githubusercontent.com/103558721/190694688-be76783d-00bc-4301-b428-6023e6b68174.PNG)

## Business Overview
King County Restorations is looking to invest in real estate, specifically buying and restoring older homes to resell in King County, Washington. 
Our goal is to utilize records from the King County database to create predictive/descriptive models of the current housing market for analysis, ultimately guiding King County Restorations in making profitable decisions when investing.
![house1](https://user-images.githubusercontent.com/103558721/190694751-b2f6c534-9916-4ff8-b689-7230e5152613.PNG)

## Objectives and Approach
The questions we sought to answer included:
1) Is home restoration in King County a profitable venture? 
2) What variables go into determing the sale price of a house? 
3) How much value can we add to a house after comparing the weight each variable has on price?



Home restoration is a niche industry with a limited amount of contractors with the skillset to properly work on houses of older construction. Houses older than 50 years are eligible for official Historic status (criterion varying by state). As such, we took into consideration structural limitations (e.g. first floor expansions, building additional floors, etc.) 
![neighborhood2](https://user-images.githubusercontent.com/103558721/190694961-1e8d1f21-1b50-4291-843d-522834694ffb.PNG)

We started with over 30,000 records and narrowed our search to homes built over 50 years ago leaving us with data from about 13,000 properties. 
Features we considered when creating our model included:

- Number of Bedrooms
- Number of Bathrooms
- Sq. footage of living space
- Sq. footage of basement 
- Sq. footage of garage 
- Sq. footage of patio
- Condition of house (rated from 1-5)*
- Grade of house (rated from 1-13)*

*For further detail, please visit https://info.kingcounty.gov/assessor/esales/Glossary.aspx?type=r

## Bottom Line
#### 1)Moving up one grade would amount to a sale price increase of ~$230,000 
#### 2)Addition a bathroom increased sale price by ~$48,000
#### 3)Installation of a medium sized (168ft) outdoor patio increased sale price by ~$12,000


## Statistical Modeling
Our research has shown a negative relationship between sale price and the year it was built/age. The older the house the less it sold for. 
We built a model to represent the market that would allow us to predict future sale prices as well as calculate the varability of features like # of bathrooms, # bedrooms, condition- allowing us to determine how much each would affect appraisal. 

Limitations for our model included: 
- Diminishing Returns when considering the bedroom to bathroom ratio
- Locality of features 
- Preservation of house character 

![regression](https://user-images.githubusercontent.com/103558721/190690142-1e2a6885-299c-4d09-a55e-d4376c859fef.PNG)


After running and evaluating several models we narrowed down the "ready to implement" features to capitalize on with the highest Return on Investment (ROI). 



### Value of Renovation

We first started by addressing the profitability of restoration calculating the effect renovations had on houses. 

![renovationeda](https://user-images.githubusercontent.com/103558721/190695731-7044680e-271b-4a4a-b9c0-00b2efc18a73.PNG)

Our model shows that median sale price for houses built before 1972 was $810k… The median sale price for houses without renovations was $800k compared to homes that had been renovated being about one million – proving that house renovations significantly add value - increasing sale prices by up to $200,000 

### House Grade 
![gradeeda](https://user-images.githubusercontent.com/103558721/190696832-0b232fde-d642-4963-9d37-07f4572bcdfe.PNG)


Our modeling has shown a significant relationship in the grade of house to the sale price. 
_House Grades of 1-6 being considered below average, 7- being average, and 8 and up being above average._ 
There is substantial variation in price difference between low grade and above average house grades. 

![gradevpriceeda](https://user-images.githubusercontent.com/103558721/190696879-45f0cd6c-8a0e-47ec-8a8c-8ddd2b6340a8.PNG)

We have grouped and quantified the median price for a low grade house ($565k); when we jump up to an average grade house – (at grade 7) we see the median price go up to $800k – up to a 41%  increase. When considering houses that are above average grade – grade 8 or higher, the value increases up to 75% equating to median sales price of $1.4m


### Installation of Bathrooms

![bathroomtopriceeda](https://user-images.githubusercontent.com/103558721/190697660-01ec5dd1-11f3-4af8-ad5a-06323e9569cd.PNG)
In our analysis we found a positive relationship between number of bathrooms and sale price. When comparing the median price of a 1 bathroom house to a 2 bathroom house, alone we see an increase in price of more than $100k. The addition of bathrooms or half bathrooms continually adds value.  


