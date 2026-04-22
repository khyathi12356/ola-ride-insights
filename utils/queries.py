QUERIES = {

"1. Successful Bookings":
"""
SELECT *
FROM rides
WHERE Booking_Status = 'Success'
""",

"2. Avg Ride Distance by Vehicle":
"""
SELECT Vehicle_Type,
       ROUND(AVG(Ride_Distance), 2) AS avg_ride_distance
FROM rides
GROUP BY Vehicle_Type
""",

"3. Customer Cancellations":
"""
SELECT COUNT(*) AS total_customer_cancellations
FROM rides
WHERE Booking_Status = 'Canceled by Customer'
""",

"4. Driver Cancellations due to personal & car issues":
"""
SELECT COUNT(*) AS driver_cancellations
FROM rides
WHERE Canceled_Rides_by_Driver LIKE '%Personal%Car%'
""",

"5. Top 5 Customers":
"""
SELECT Customer_ID,
       COUNT(Booking_ID) AS total_rides
FROM rides
GROUP BY Customer_ID
ORDER BY total_rides DESC
LIMIT 5
""",

"6. Max and min driver ratings for Prime Sedan":
"""
SELECT 
    MAX(Driver_Ratings) AS max_rating,
    MIN(Driver_Ratings) AS min_rating
FROM rides
WHERE Vehicle_Type = 'Prime Sedan'
  AND Driver_Ratings IS NOT NULL
""",

"7. UPI Rides":
"""
SELECT *
FROM rides
WHERE LOWER(Payment_Method) = 'upi'
""",

"8. Average customer rating per vehicle type":
"""
SELECT Vehicle_Type,
       ROUND(AVG(Customer_Rating), 2) AS avg_customer_rating
FROM rides
GROUP BY Vehicle_Type
""",

"9. Total booking value of successful rides":
"""
SELECT SUM(Booking_Value) AS total_revenue
FROM rides
WHERE Booking_Status = 'Success'
""",

"10. All incomplete rides with reason":
"""
SELECT Booking_ID,
       Customer_ID,
       Vehicle_Type,
       Ride_Distance,
       Incomplete_Rides_Reason
FROM rides
WHERE Incomplete_Rides_Reason IS NOT NULL
AND Incomplete_Rides_Reason <> 'Not Applicable'
"""
}
