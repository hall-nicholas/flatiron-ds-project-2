<h3/><i/>Phase 2 Project</i></h3>
<h1/><b/>Home Restoration Proposal</b> <i/>for King County Restorations</i></h1>

<h3/><b/>For King & County, Ltd.</b></h3>
<ul/>
  <li/>Patrick Arnold</li> 
  <li/>Nick Hall</li>
  <li/>Dan Moreira</li>
</ul>

<br/>

![seattle1](https://user-images.githubusercontent.com/103558721/190694582-8d94c976-ba14-410a-b0e6-d712229b125f.PNG)

<h1/><i/>Table of Contents</i></h1>

<ol/>
  <li/><b/>Repository Navigation</b></li>
  <li/><b/>Project Summary</b></li>
  <li/><b/>References</b></li>
</ol>

<br/>

<h1/><i/>Repository Navigation</i></h1>

<h3/><b/>Repository Set-up</b></h3>
<p/>The original dataset used in this project can be found <a/ href="https://github.com/learn-co-curriculum/dsc-phase-2-project-v2-5/tree/main/data">in this GitHub repository</a>. The "kc_house_data.csv" must be placed into a subfolder named "data/" in order for any of the Jupyter Notebooks or Python files to work.</p>

<h3/><b/>Important Files</b></h3>
<ul/>
  <li/><b/>code/Main_Notebook.ipynb</b> contains the main notebook containing our analysis</li>
  <li/><b/>code/functions.py</b> contains the functions used to clean and import the data</li>
  <li/>All other files in the <b/>code/</b> directory contain EDA done to explore the data</li>
</ul>

<p/>The final presentation can be found <a/ href="https://docs.google.com/presentation/d/19iopGJAfOxZJyg056lAqL57Pn16e-AuI7tTFj9KLAVU/edit?usp=sharing">here</a>.</p>

<br/>

![neighborhood1](https://user-images.githubusercontent.com/103558721/190694688-be76783d-00bc-4301-b428-6023e6b68174.PNG)

<br/>

<h1/><i/>Project Summary</i></h1>

<h2/><b/>Business Overview</b></h2>
<p/>King County Restorations is looking to invest in real estate, specifically buying and restoring older homes to resell in King County, Washington. 
Our goal is to utilize records from the King County database to create predictive/descriptive models of the current housing market for analysis, ultimately guiding King County Restorations in making profitable decisions when investing.</p>

![house1](https://user-images.githubusercontent.com/103558721/190694751-b2f6c534-9916-4ff8-b689-7230e5152613.PNG)

<h2/><b/>Objectives & Approach</b></h2>
<p/>The questions we sought to answer included:</p>
<ol/>
  <li/>Is home restoration in King County a profitable venture?</li>
  <li/>What variables go into determing the sale price of a house?</li>
  <li/>How much value can we add to a house after comparing the weight each variable has on price?</li>
</ol>

<p/>Home restoration is a niche industry with a limited amount of contractors with the skillset to properly work on houses of older construction. Houses older than 50 years are eligible for official Historic status (criterion varying by state). As such, we took into consideration structural limitations (e.g. first floor expansions, building additional floors, etc.)</p>

![neighborhood2](https://user-images.githubusercontent.com/103558721/190694961-1e8d1f21-1b50-4291-843d-522834694ffb.PNG)

</p>We started with over 30,000 records and narrowed our search to homes built over 50 years ago leaving us with data from about 13,000 properties. 
Features we considered when creating our model included:</p>

<ul/>
  <li/>Number of bedrooms</li>
  <li/>Number of bathrooms</li>
  <li/>Square footage of living space</li>
  <li/>Square footage of basement</li>
  <li/>Square footage of garage</li>
  <li/>Square footage of patio</li>
  <li/>Condition (scale of 1-5)*</li>
  <li/>Grade (scale of 1-13)*</li>
</ul>

<p/>*For further detail, please visit <a/ href=https://info.kingcounty.gov/assessor/esales/Glossary.aspx?type=r>the King County website</a>.</p>

<h2/><b/>Bottom Line</b></h2>
<ol/>
  <li/>Moving up one grade would amount to a sale price increase of <b/>~$230,000</b></li>
  <li/>Addition a bathroom increased sale price by <b/>~$48,000</b></li>
  <li/>Installation of a medium sized (168ft) outdoor patio increased sale price by <b/>~$12,000</b></li>
</ol>

<h2/><b/>Statistical Model</b></h2>
<p/>Our research has shown a negative relationship between sale price and the year it was built/age. The older the house the less it sold for. 
We built a model to represent the market that would allow us to predict future sale prices as well as calculate the varability of features like # of bathrooms, # bedrooms, condition- allowing us to determine how much each would affect appraisal.</p>

<p/>Limitations for our model included:</p>
<ol/>
  <li/>Diminishing Returns when considering the bedroom to bathroom ratio</li>
  <li/>Locality of features</li>
  <li/>Preservation of house character</li>
</ol>

![regression](https://user-images.githubusercontent.com/103558721/190690142-1e2a6885-299c-4d09-a55e-d4376c859fef.PNG)

<p/>After running and evaluating several models we narrowed down the "ready to implement" features to capitalize on with the highest Return on Investment (ROI).</p>

<h2/><b/>Value of Renovation</b></h2>

<p/>We first started by addressing the profitability of restoration calculating the effect renovations had on houses.</p>

![renovationeda](https://user-images.githubusercontent.com/103558721/190695731-7044680e-271b-4a4a-b9c0-00b2efc18a73.PNG)

<p/>Our model shows that median sale price for houses built before 1972 was $810k… The median sale price for houses without renovations was $800k compared to homes that had been renovated being about one million – proving that house renovations significantly add value - increasing sale prices by up to $200,000</p>

<h2/><b/>House Grade</b></h2>

![gradeeda](https://user-images.githubusercontent.com/103558721/190696832-0b232fde-d642-4963-9d37-07f4572bcdfe.PNG)

<p/>Our modeling has shown a significant relationship in the grade of house to the sale price. 

Grades of 6 and below were considered "below average", 7 being "average", and 8 and up being considered "above average".

There is substantial variation in price difference between low grade and above average house grades.</p>

![gradevpriceeda](https://user-images.githubusercontent.com/103558721/190696879-45f0cd6c-8a0e-47ec-8a8c-8ddd2b6340a8.PNG)

<p/>We have grouped and quantified the median price for a low grade house ($565k); when we jump up to an average grade house – (at grade 7) we see the median price go up to $800k – up to a 41%  increase. When considering houses that are above average grade – grade 8 or higher, the value increases up to 75% equating to median sales price of $1.4m</p>

<h2/><b/>Bathrooms</b></h2>

![bathroomtopriceeda](https://user-images.githubusercontent.com/103558721/190697660-01ec5dd1-11f3-4af8-ad5a-06323e9569cd.PNG)

<p/>In our analysis we found a positive relationship between number of bathrooms and sale price. When comparing the median price of a 1 bathroom house to a 2 bathroom house, alone we see an increase in price of more than $100k. The addition of bathrooms or half bathrooms continually adds value.</p> 

<h1/><i/>References</i></h1>
<ul/>
  <li/><a/ href="https://www.landscapingnetwork.com/patios/size.html">www.landscapingnetwork.com</a> - used to determine adequate patio specifications</li>
  <li/><a/ href="https://info.kingcounty.gov/assessor/esales/Glossary.aspx?type=r">info.kingcounty.gov</a> - used to source information about King County housing data</li>
</ul>
<h3/>Image Credits</h3>
<ul/>
  <li/><a/ href="https://www.wood-finishes-direct.com/blog/ultimate-guide-to-wooden-beams/">www.wood-finishes-direct.com</a></li>
  <li/><a/ href="https://www.instagram.com/p/BmuSGQJljJb/">www.instagram.com</a></li>
  <li/><a/ href="https://www.istockphoto.com/photo/downtown-seattle-streets-from-above-gm832526062-136686217?utm_medium=organic&utm_source=google&utm_campaign=iptcurl">www.istockphoto.com</a></li>
  <li/><a/ href="https://www.seattletimes.com/pacific-nw-magazine/a-capitol-hill-family-remodels-its-historic-home-with-an-appreciative-attitude-of-stewardship/">www.seattletimes.com</a></li>
  <li/><a/ href="https://www.pexels.com/photo/high-angle-shot-of-suburban-neighborhood-1546168/">www.pexels.com</a> (1)</li>
  <li/><a/ href="https://www.pexels.com/photo/aerial-view-of-buildigns-1642125/">www.pexels.com</a> (2)</li>
  <li/><a/ href="https://www.pexels.com/photo/house-lights-turned-on-106399/">www.pexels.com</a> (3)</li>
  <li/><a/ href="https://www.pexels.com/photo/brown-wooden-house-infront-of-swimming-pool-under-blue-sky-32870/">www.pexels.com</a> (4)</li>
  <li/><a/ href="https://www.pexels.com/photo/aerial-view-of-city-buildings-3964406/">www.pexels.com</a> (5)</li>
</ul>