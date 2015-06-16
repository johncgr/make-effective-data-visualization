##Data Visualization Project ReadMe##
**John Gritch**

##### SUMMARY #####

The data visualization is a line chart of the individual index values for the eight major item groups that, all together, comprise the Dallas-Fort Worth Metropolitan Consumer Price Index. Each item group (e.g. Food, Housing, etc.) is calculated seperately so that the relative price changes for that type of good or service can be tracked over time.

 An index value of 200 means that the price of that type of good has doubled since the base period (varies between 1982  - 1984 depending on the item) when the index value is set to 100. In the chart the individual lines can be toggled on or off. 

##### DESIGN #####

**Initial Design Choices Rationale**

I chose to use Consumer Price Index data from the Bureau of Labor Statistics' API. The dataset(s) I used attempt to measure the same thing (a basket of comparable goods and services) over time. For this reason I chose a multi-series line chart.

From the start, I knew that I wanted the lines representing each data series to have a unique color. I also wanted the lines to be interactive so that idividual lines could be displayed or hidden according to the wishes of the user. These three conditions did not fundamentally change over the course of the project, but their iterative updates are recorded below. 


**Version History:** 
1. index1_1_singleseries.html
  + first working version displaying a single line. Built with d3.js

2. index1_2_multiseries.html 
  + added multiple lines to graph and assigned them unique colors 

3. index1_3_clickable.html
  + added interactivity to the legend so that individual lines could be toggled on or off

4. index1_4.html
  + added what I thought was going to be my final data to the graph

5. index1_5_gridlines.html
  + The graphs were looking "flat" and not displaying much of an intuitive trend. I expanded the time period of my data so that the graph showed the indexes from their baseline years (index = 100) of 1982-1984. 
  + new color scheme used to color the lines. The old color scheme was rather ugly. New color scheme based off of an RColorBrewer 8 data class qualitative scheme.
  + color scheme applied to legend to make the graph faster to read 
  + added horizontal gridlines to increase the graph's usable precision
  + made legend text bigger 
  + truncated series index labels to last three letters. The full API series key was visually too long to be used as a label and was causing crowding.
  + added title to explain what the graph was showing.
  + changed y axis label to "Index" as "Price" is not an accurate way to describe a CPI value

6. index2_1.html 
  + taking the general template I built with the index1 series I created index2 which was the first version I intended to show to a reviewer. 
  + index2_1.html added two other visualizations that were meant to provide context for the main visualization titled "CPI Value for DFW Metro Area by Major Item Group". 
  + made graph physically larger
  + ordered the legend so that it corresponds somewhat to the natural order of the data series as read from top to bottom. Hopefully this would make the graph easier and faster to read.

7. index2_2_afterReview1.html
  + added more details to y axis label for clarity
  + changed legend text to indicate that lines were interactive
  + increased the stroke width of data lines for easier interpretation
  + changed labels from BLS API series keys to descriptive names
  + rearranged burnt orange and brown colored data lines to make the graph easier to interpret / easier on the eyes

8. index3_1_dimple.html
  + rebuilt graph in Dimple.js
  + I scrapped the extra visualizations
  + I scrapped my D3.js code and rebuilt with Dimple.js because I realized I could do everything I needed in dimple with a lot less code.

9. index4_1.html
  + constrained the y-value so that it started at 100 
  + fixed typo in Metropolitan
  + added tooltip that pops up when graph is clicked, displaying information about that data point

10. index4_2_OriginalSubmission.html
  + added notes to graph to address a comment made my Reviewer #2 and #3. Ideally these notes would be explained around the graph versus directly on it. However, I think the loss of visual "cleaness" is worth the additional explanations given the Reviewer's comments.
  + changed margins to fix error cutting off graph at Jan. 2009
  + added underline to graph title

11. index4_3.html
  + increase size of svg container, so that explanatory notes can be moved off the graph
  + added notes on how to use graph
  + added data background to address feedback comments
  + added tree diagram
  + added data series for All Items to graph
  + added opacity to the lines
  + removed note that used to obscure graph
  + recolored lines to mostly gray's with some colors for emphasis
  + moved title off the graph

12. index4_4_divColor.html
  + changed circles in tree diagram from steelblue to gray
  + made changes to how to use graph and background
  + changed color scheme so above "average" is pink and below is gray/black.
  + rearranged colors a little to make for a more visualizing pleasing legend 

13. index_final
 + dropped Education/Communication and Recreation for simplicities sake
 + minor edits to background data and line color


##### FEEDBACK #####

**Review #1: Conducted in person, comments on Index2_1.html**

1a. Reviewer #1 made comment that the y-axis could use more explanation or descriptions.
Response: added more details to y axis label

1b. Reviewer #1 made comment that stroke width of lines should be bigger

1c. Reviewer #1 thought the jaggedness and fine detail in lines implied that they should be able to read individual data values. Suggested either smoothing the lines so that the overall trends were emphasized over individual values, or to add more axis lines or to add visualizations.

1d. Reviewer #1 made comment about not understanding why the API keys were there as axis labels or what function they served.
Response: Changed labels from API keys to descriptive name 

1e. Reviewer #1 made comment burnt-orange line and brown line should be placed farther apart because they are similiar.
Respone: Done


**Review #2: conducted over email,  comments on Index3_1.html**
> Reviewer's comments shown verbatim

2a. I don't know exactly what CPI is - purchasing power over time?

2b. First thing I noticed is that medical has had quite a run.

2c. What is other goods and services and why is it so close to medical?

2d. Are the big swings in transportation from oil prices?

2e. Apparel is cheap - I watched the John Oliver show on cheap clothes and sweatshops recently. 

2f. I expected education to be higher with all the discussions on how much the cost of college has risen over the past 20 years.

2g. There's a lot going on - is there something specific you're trying to show? 


**Review #3: conducted in person, comments on Index4.html**

3a. Prompt: "What do you notice in the visualization?" 
Response: "There's an upward trend in all but the purple and maybe the recreation one."

3b. Prompt: "What questions do you have about the data?" 
Response: "Not really sure what the CPI value is."

3c. Prompt: "What relationships do you notice?"
Response: "Medical and other goods seemed to be grouped. Housing, Transportation, and Food seem to be grouped." 

3d. Reviewer Question: "Why do they start later?" Refering to education and recreation.

3e. Reviewer Question: "What are other goods and services?"

3f. Prompt: "Is there something you dont understand about the graphic?" 
Response: "No."

##### RESOURCES #####

**D3.js**
+ https://github.com/mbostock/d3/wiki/API-Reference
+ http://bl.ocks.org/mbostock/3883245
+ http://bl.ocks.org/d3noob/d8be922a10cb0b148cd5
+ http://bl.ocks.org/d3noob/5d621a60e2d1d02086bf
+ https://leanpub.com/D3-Tips-and-Tricks/read

**Dimple.js**
+ http://dimplejs.org/examples_viewer.html?id=lines_horizontal_stacked
+ http://dimplejs.org/advanced_examples_viewer.html?id=advanced_interactive_legends

**Assorted**
+ http://dillinger.io/
+ http://bl.ocks.org/shancarter/raw/4748131/
+ http://colorbrewer2.org/

