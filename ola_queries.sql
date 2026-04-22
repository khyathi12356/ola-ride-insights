USE ola_rides;

SELECT COUNT(*) FROM ola_rides.cleaned_ola_data;

SHOW COLUMNS FROM ola_rides.cleaned_ola_data;

-- 1. Retrieve all successful bookings
SELECT *
FROM ola_rides.cleaned_ola_data
WHERE Booking_Status = 'Success';


-- 2. Average ride distance for each vehicle type
SELECT Vehicle_Type,
       ROUND(AVG(Ride_Distance), 2) AS avg_ride_distance
FROM ola_rides.cleaned_ola_data
GROUP BY Vehicle_Type;


-- 3. Total number of cancelled rides by customers
SELECT COUNT(*) AS total_customer_cancellations
FROM ola_rides.cleaned_ola_data
WHERE Booking_Status = 'Canceled by Customer';

-- 4. Top 5 customers who booked the highest number of rides
SELECT Customer_ID,
       COUNT(Booking_ID) AS total_rides
FROM ola_rides.cleaned_ola_data
GROUP BY Customer_ID
ORDER BY total_rides DESC
LIMIT 5;


-- 5. Rides cancelled by drivers due to personal & car issues
SELECT COUNT(*) AS driver_cancellations
FROM ola_rides.cleaned_ola_data
WHERE Canceled_Rides_by_Driver LIKE '%Personal%Car%';

-- 6. Max and min driver ratings for Prime Sedan
SELECT 
    MAX(Driver_Ratings) AS max_rating,
    MIN(Driver_Ratings) AS min_rating
FROM ola_rides.cleaned_ola_data
WHERE Vehicle_Type = 'Prime Sedan'
  AND Driver_Ratings IS NOT NULL;


-- 7. Rides where payment was made using UPI
SELECT *
FROM ola_rides.cleaned_ola_data
WHERE LOWER(Payment_Method) = 'upi';


-- 8. Average customer rating per vehicle type
SELECT Vehicle_Type,
       ROUND(AVG(Customer_Rating), 2) AS avg_customer_rating
FROM ola_rides.cleaned_ola_data
GROUP BY Vehicle_Type;


-- 9. Total booking value of successful rides
SELECT SUM(Booking_Value) AS total_revenue
FROM ola_rides.cleaned_ola_data
WHERE Booking_Status = 'Success';


-- 10. All incomplete rides with reason
SELECT Booking_ID,
       Customer_ID,
       Vehicle_Type,
       Ride_Distance,
       Incomplete_Rides_Reason
FROM ola_rides.cleaned_ola_data
WHERE Incomplete_Rides_Reason IS NOT NULL
AND Incomplete_Rides_Reason <> 'Not Applicable';