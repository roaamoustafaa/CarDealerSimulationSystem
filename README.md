
<a name="_page0_x72.00_y368.63"></a>**Car Dealer Simulation System**

<a name="_page1_x72.00_y72.00"></a>**Table of Content**

[**Car Dealer Simulation System 1** ](#_page0_x72.00_y368.63)[Table of Content 2** ](#_page1_x72.00_y72.00)[Problem ***Car Dealer**](#_page2_x72.00_y87.87)

1. [Problem formulation & Objectives 3 ](#_page2_x72.00_y126.22)[Problem Statement 3 ](#_page2_x72.00_y143.41)[Objectives 3](#_page2_x72.00_y226.88)
1. [System Components. 3 ](#_page2_x72.00_y373.83)[Entities 3 ](#_page2_x72.00_y391.02)[Attributes 3 ](#_page2_x72.00_y459.95)[Activities 3 ](#_page2_x72.00_y528.88)[State Variables 3 ](#_page2_x72.00_y613.68)[Events 4](#_page3_x72.00_y72.00)
1. [System analysis including cumulative distribution tables, calendar table (for 10 days)](#_page3_x72.00_y232.04)

[Demand Cumulative Distribution Table 4 ](#_page3_x72.00_y265.10)[Lead Time Cumulative Distribution Table 4 ](#_page3_x72.00_y477.96)[Calendet Table(10- Days) ](#_page4_x72.00_y72.00)

4. [Experimental Design Parameters 6](#_page5_x72.00_y72.00)
4. [Justification of experiment parameters values 7](#_page6_x72.00_y72.00)
4. [Results Analysis: Using graphs & discussions : stating the results for the 5 questions. 8 ](#_page7_x72.00_y89.19)[Theoretical & Experimental Avg Demand 8 ](#_page7_x72.00_y280.94)[Theoretical & Experimental Avg Lead Time = 9](#_page8_x72.00_y135.47)
4. [Conclusion 11](#_page10_x72.00_y103.74)

<a name="_page2_x72.00_y87.87"></a>**Problem***(Car Dealer)*

1. **Problem<a name="_page2_x72.00_y126.22"></a> formulation & Objectives ( / 2 )**

<a name="_page2_x72.00_y143.41"></a>**Problem Statement**

The dealership is constrained by showroom and inventory space, fluctuating daily demand, and variability in delivery lead times. These factors introduce complexity in deciding when to order and how many cars to order to maintain an efficient operation

<a name="_page2_x72.00_y226.88"></a>**Objectives**

**Minimize Stockouts & Inventory Mangamnet :** Ensure that the customer demand is met without significant delays.

**Maximize Net Profit:** Optimize the balance between holding costs, ordering costs, and sales revenue.

**Optimize Review Period (N):** Determine the best cycle for reviewing inventory levels and placing orders.

2. **System<a name="_page2_x72.00_y373.83"></a> Components. ( / 2 )**

<a name="_page2_x72.00_y391.02"></a>**Entities**

**Cars:** Each car in inventory or showroom.

**Orders:** Each order placed to replenish the inventory.

<a name="_page2_x72.00_y459.95"></a>**Attributes**

**Car Availability**: Whether a car is available in the showroom or inventory. **Order Status:** The current status of an order (placed, in-transit, delivered).

<a name="_page2_x72.00_y528.88"></a>**Activities**

**Selling Cars:** The process when a customer demands and purchases a car.

**Replenishing Inventory:** The activity of ordering and receiving cars to maintain inventory levels.

<a name="_page2_x72.00_y613.68"></a>**State Variables**

**Number of Cars in Showroom:** The current number of cars displayed in the showroom. **Number of Cars in Inventory**: The current number of cars in the storage inventory. **Pending Orders:** The number of cars ordered but not yet received.

<a name="_page3_x72.00_y72.00"></a>**Events**

**Customer Arrival:** When a customer arrives to demand a car.

**Sale Completion**: When a car is sold and removed from the showroom. **Order Placement**: When a new order is placed to the supplier.

**Order Arrival:** When the ordered cars arrive and are added to the inventory![](Aspose.Words.1fd71133-1f68-411d-8bb2-19bda7085a83.003.png)

3. **System analysis including cumulative distribution tables, calendar table (for <a name="_page3_x72.00_y232.04"></a>10 days) ( / 8 )**

<a name="_page3_x72.00_y265.10"></a>**Demand Cumulative Distribution Table**



|**Demand**|**Probability**|**Cumulative Probability**|**Random-Digit Assignment**|
| - | - | - | :- |
|0|0\.20|0\.20|0-20|
|1|0\.34|0\.54|21-54|
|2|0\.36|0\.90|55-90|
|3|0\.10|1|91-000|

<a name="_page3_x72.00_y477.96"></a>**Lead Time Cumulative Distribution Table**



|**Lead Time**|**Probability**|**Cumulative Probability**|**Random-Digit Assignment**|
| - | - | - | :- |
|0|0\.40|0\.40|0-40|
|1|0\.35|0\.75|41-75|
|2|0\.25|1|76-000|

<a name="_page4_x72.00_y72.00"></a>**Calendet Table(10- Days)**

If new order , we didn’t make a holding cost for it

Cost = each cost like the holding and orders

N=3 , inventory = 4 , Showroom = 4 , order delivered in day 3 Holding cost for the END of the day:)



<table><tr><th colspan="1" rowspan="2" valign="top"><b>Day</b></th><th colspan="1" rowspan="2" valign="top"><b>R_Demand</b></th><th colspan="1" rowspan="2" valign="top"><b>Demand</b></th><th colspan="1" rowspan="2" valign="top"><b>R_lead</b></th><th colspan="1" rowspan="2" valign="top"><b>Lead Time</b></th><th colspan="2" valign="top"><b>Showroom</b></th><th colspan="2" valign="top"><b>inventory</b></th><th colspan="1" rowspan="1" valign="top"><b>Cost</b></th><th colspan="1" rowspan="1" valign="top"><b>Profit</b></th><th colspan="1" rowspan="2" valign="top"><b>Profit After Costs</b></th></tr>
<tr><td colspan="1"><b>Start</b></td><td colspan="1" valign="top"><b>End</b></td><td colspan="1" valign="top"><b>Start</b></td><td colspan="1" valign="top"><b>End</b></td></tr>
<tr><td colspan="1">1</td><td colspan="1">15</td><td colspan="1">0</td><td colspan="1">35</td><td colspan="1">1</td><td colspan="1">4</td><td colspan="1">4</td><td colspan="1">3</td><td colspan="1">3</td><td colspan="1">3,000</td><td colspan="1">0</td><td colspan="1">0</td></tr>
<tr><td colspan="1" valign="top">2</td><td colspan="1" valign="top">25</td><td colspan="1" valign="top">1</td><td colspan="1" valign="top">78</td><td colspan="1" valign="top">3</td><td colspan="1" valign="top">4</td><td colspan="1" valign="top">4</td><td colspan="1" valign="top">3</td><td colspan="1" valign="top">2</td><td colspan="1" valign="top">22000 Order payed</td><td colspan="1" valign="top">10\.000</td><td colspan="1" valign="top">-</td></tr>
<tr><td colspan="1" valign="top"><b>3</b></td><td colspan="1" valign="top"><b>40</b></td><td colspan="1" valign="top"><b>1</b></td><td colspan="1" valign="top"><b>60</b></td><td colspan="1" valign="top"><b>2</b></td><td colspan="1" valign="top"><b>5</b></td><td colspan="1" valign="top"><b>5</b></td><td colspan="1" valign="top"><b>6</b></td><td colspan="1" valign="top"><b>5</b></td><td colspan="1" valign="top"><b>5.000</b></td><td colspan="1" valign="top"><b>10.000</b></td><td colspan="1" valign="top"><b>5.000</b></td></tr>
<tr><td colspan="1" valign="top">4</td><td colspan="1" valign="top">82</td><td colspan="1" valign="top">2</td><td colspan="1" valign="top">5</td><td colspan="1" valign="top">1</td><td colspan="1" valign="top">5</td><td colspan="1" valign="top">5</td><td colspan="1" valign="top">5</td><td colspan="1" valign="top">3</td><td colspan="1" valign="top">3.000</td><td colspan="1" valign="top">20\.000</td><td colspan="1" valign="top">17\.000</td></tr>
<tr><td colspan="1" valign="top">5</td><td colspan="1" valign="top">55</td><td colspan="1" valign="top">2</td><td colspan="1" valign="top">45</td><td colspan="1" valign="top">2</td><td colspan="1" valign="top">5</td><td colspan="1" valign="top">5</td><td colspan="1" valign="top">8</td><td colspan="1" valign="top"><p>6</p><p><b><i>(order)</i></b></p></td><td colspan="1" valign="top">26\.000</td><td colspan="1" valign="top">20\.000</td><td colspan="1" valign="top">-</td></tr>
<tr><td colspan="1" valign="top"><b>6</b></td><td colspan="1" valign="top"><b>90</b></td><td colspan="1" valign="top"><b>3</b></td><td colspan="1" valign="top"><b>25</b></td><td colspan="1" valign="top"><b>1</b></td><td colspan="1" valign="top"><b>5</b></td><td colspan="1" valign="top"><b>5</b></td><td colspan="1" valign="top"><b>6</b></td><td colspan="1" valign="top"><b>3</b></td><td colspan="1" valign="top"><b>3.000</b></td><td colspan="1" valign="top"><b>30.000</b></td><td colspan="1" valign="top"><b>27.000</b></td></tr>
<tr><td colspan="1" valign="top">7</td><td colspan="1" valign="top">3</td><td colspan="1" valign="top">0</td><td colspan="1" valign="top">70</td><td colspan="1" valign="top">2</td><td colspan="1" valign="top">5</td><td colspan="1" valign="top">5</td><td colspan="1" valign="top">3</td><td colspan="1" valign="top">10</td><td colspan="1" valign="top">30\.000</td><td colspan="1" valign="top">0</td><td colspan="1" valign="top">0</td></tr>
<tr><td colspan="1" valign="top">8</td><td colspan="1" valign="top">65</td><td colspan="1" valign="top">2</td><td colspan="1" valign="top">80</td><td colspan="1" valign="top">3</td><td colspan="1" valign="top">5</td><td colspan="1" valign="top">5</td><td colspan="1" valign="top">10</td><td colspan="1" valign="top">8</td><td colspan="1" valign="top">8\.000</td><td colspan="1" valign="top">20\.000</td><td colspan="1" valign="top">12\.000</td></tr>
<tr><td colspan="1" valign="top"><b>9</b></td><td colspan="1" valign="top"><b>48</b></td><td colspan="1" valign="top"><b>1</b></td><td colspan="1" valign="top"><b>40</b></td><td colspan="1" valign="top"><b>1</b></td><td colspan="1" valign="top"><b>5</b></td><td colspan="1" valign="top"><b>5</b></td><td colspan="1" valign="top"><b>10</b></td><td colspan="1" valign="top"><b>9</b></td><td colspan="1" valign="top"><b>9.000</b></td><td colspan="1" valign="top"><b>10.000</b></td><td colspan="1" valign="top"><b>1.000</b></td></tr>
<tr><td colspan="1" valign="top">10</td><td colspan="1" valign="top">99</td><td colspan="1" valign="top">3</td><td colspan="1" valign="top">10</td><td colspan="1" valign="top">1</td><td colspan="1" valign="top">5</td><td colspan="1" valign="top">5</td><td colspan="1" valign="top">9</td><td colspan="1" valign="top">7</td><td colspan="1" valign="top">27\.000</td><td colspan="1" valign="top">30\.000</td><td colspan="1" valign="top">3.000</td></tr>
</table>


Initial order 5 cars

**. -> Order places at the end of this day .-> sold car .-> order deilverd**

4. **Experimental<a name="_page5_x72.00_y72.00"></a> Design Parameters ( / 2 )**
- **Demand Distributio :** demand\_probabilities
- **Lead Time Distribution :** lead\_time\_probabilities
- **Maximum Showroom Capacity** MAX\_CARS
- **Maximum Inventory Capacity**: MAX\_CARS
- **Review Period (N) :** REVIEW\_PERIOD\_N
- **Net Profit per Car :** PROFIT\_PER\_CAR
- **Holding Expenses per Car :** HOLDING\_COST
- **Cost of Making and Shipping an Order :** ORDER\_COST

- ![Simulation Project - Design Parameters  ](https://i.ibb.co/mvKgwGw/Aspose-Words-1fd71133-1f68-411d-8bb2-19bda7085a83-004.png)


![](Aspose.Words.1fd71133-1f68-411d-8bb2-19bda7085a83.004.png)

5. **Justification<a name="_page6_x72.00_y72.00"></a> of experiment parameters values ( / 2 )**
- **Demand Distribution:** the probabilities for demands (0.2, 0.34, 0.36, 0.1 for demands of 0, 1, 2, 3 cars respectively) could be based on historical sales data indicating the likelihood of different sales volumes per day.
- **Lead Time Distribution:** The probabilities for lead times (0.4, 0.35, 0.25 for lead times of 1, 2, 3 days respectively) might be derived from supplier performance data or industry standards, reflecting the variability in delivery times.
- **Showroom and Inventory Capacities:** The maximum capacities of the showroom

  **(5 cars)** and inventory **(10 cars)** are determined based on the available physical space and storage capacity. These values ensure that the car dealer can display and store a reasonable number of cars.

- **Review Period(N)**: The review period of **3 days** is chosen based on the car dealer's operational efficiency and the frequency at which inventory needs to be replenished. A shorter review period may lead to more frequent orders but higher costs, while a longer review period may result in stockouts and lost opportunities.
- **Net Profit per Car:** The net profit per car of **10,000 LE** represents the revenue generated by selling a car after deducting all associated costs, such as holding expenses and order costs. This value may vary based on factors such as car pricing, market conditions, and profit margins.
- **Holding Expenses per Car:** The holding expenses per car per day of **1,000 LE** represent the daily cost incurred by the car dealer for storing a car in inventory or showroom. This cost may include expenses such as storage, maintenance, and depreciation.
- **Cost of Making and Shipping an Order:** The cost of making and shipping an order of **20,000 LE** represents the expenses incurred by the car dealer for each order placed to fill the inventory and showroom. This cost includes factors such as transportation, handling, and administrative expenses associated with ordering new cars.
6. **Results Analysis: Using graphs & discussions : stating the results for the 5 <a name="_page7_x72.00_y89.19"></a>questions. ( / 9 )**

1- **The average ending units in showroom and the inventory.**

4\.5 ≃5 Unit

**2- The number of days when a shortage condition ![](Aspose.Words.1fd71133-1f68-411d-8bb2-19bda7085a83.005.jpeg)occurs.** 

5 Days 

3- **The average net profit for the car dealer.** 

103,800 LE 

**4- Does the theoretical average demand of the demand distribution match the experimental one?**

<a name="_page7_x72.00_y280.94"></a>**Theoretical & Experimental Avg Demand**

Theoretical Demand = (0×0.2)+(1×0.34)+(2×0.36)+(3×0.1)

Theoretical Demand = **1.36**

Experimental avf Demand = **1.48**

![Simulation Project - Lead Time ](https://i.ibb.co/2t6Zgvf/Aspose-Words-1fd71133-1f68-411d-8bb2-19bda7085a83-007.jpg)

***The experimental average demand of 1.48 is higher than the theoretical average demand of 1.36***
| Note |
|------|
| This indicates that the actual demand observed in the experiment is slightly higher than what was predicted by the theoretical mode |

![]**5- Does the theoretical average lead time of the lead time distribution match the experimental one?**

<a name="_page8_x72.00_y135.47"></a>**Theoretical & Experimental Avg Lead Time =** Theoretical Lead Time =(1×0.4)+(2×0.35)+(3×0.25) Theoretical Lead Time =1.85

Experimental avg Lead= 1.71

![Simulation Project - Lead Time ](https://i.ibb.co/bB4npSs/Aspose-Words-1fd71133-1f68-411d-8bb2-19bda7085a83-009.jpg)

***The difference between the two values is relatively small.***
| Note |
|------|
| The experimental average lead time is slightly lower than the theoretical lead time. This could indicate that the actual system, as observed in the experiment, is performing slightly better or more efficiently than what was predicted by the theoretical model. |

![](Aspose.Words.1fd71133-1f68-411d-8bb2-19bda7085a83.008.png)

![](Aspose.Words.1fd71133-1f68-411d-8bb2-19bda7085a83.009.jpeg)
**6- Is there a better value for the review period variable N to maximize the**
**Car dealer net profit?**

Yes, there is a better value for the review period variable N to maximize the car dealer's net profit. The simulations indicate that setting it with various verable make the profit higher,. But , suggesting that adjusting the review period to 4 days is the most profitable strategy according to the simulated conditions.

![](Aspose.Words.1fd71133-1f68-411d-8bb2-19bda7085a83.010.jpeg)

7. **Conclusion**

<a name="_page10_x72.00_y103.74"></a>we examined the car dealer management challenges faced by a car dealership.

Our goal was to minimize stockouts, optimize inventory management, and maximize net profit. Based on our simulation experiments and analysis of the results, we can draw the following conclusions:

- The average number of cars in the showroom and inventory was around 4.5 units, indicating a relatively stable inventory level.
- Stockouts occurred for approximately 5 days, suggesting that while they were infrequent, improvements can still be made to minimize them further.
- The average net profit for the car dealer was 103,800 LE, representing a balance between holding costs, ordering costs, and sales revenue.
- The actual demand observed in the experiment was slightly higher than what was predicted by the theoretical model, indicating the need for adjustments in demand forecasting.
- The actual lead time observed in the experiment was slightly lower than the theoretical lead time, suggesting that the system performed slightly better than predicted.
- By setting the review period to 4 days, the car dealer achieved the highest average net profit of 97,300 LE. Adjusting the review period proved to be a profitable strategy.

By considering factors such as showroom and inventory capacity, review period, demand distribution, and lead time, car dealers can optimize their operations, minimize stockouts, and improve profitability. The findings from this simulation provide valuable insights for decision-making and enhancing inventory management strategies in the car dealership.
11
