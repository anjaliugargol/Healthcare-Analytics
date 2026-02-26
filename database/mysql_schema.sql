-- =========================================
-- Database: ER Healthcare Analytics
-- =========================================

CREATE DATABASE IF NOT EXISTS er_healthcare;

USE er_healthcare;

-- =========================================
-- Table: ER Analytics
-- =========================================

CREATE TABLE IF NOT EXISTS er_analytics (
    Visit_Id INT PRIMARY KEY,
    Hospital_Name VARCHAR(100),
    Arrival_Time VARCHAR(50),
    Day VARCHAR(20),
    Hour INT,
    Season VARCHAR(20),
    Waiting_Time_Min INT,
    Doctor_Available BOOLEAN,
    Patients_In_ER INT,
    Equipment_usage_percent FLOAT,
    Overcrowded BOOLEAN,
    Disposition VARCHAR(50)
);



-- =========================================
-- Sample Analysis Queries
-- =========================================

-- 1. Peak Admission Hours
SELECT Hour, COUNT(*) AS total_visits
FROM er_analytics
GROUP BY Hour
ORDER BY total_visits DESC;

-- 2. Overcrowding Frequency
SELECT Overcrowded, COUNT(*) AS count
FROM er_analytics
GROUP BY Overcrowded;

-- 3. Average Waiting Time by Season
SELECT Season, AVG(Waiting_Time_Min) AS avg_waiting_time
FROM er_analytics
GROUP BY Season;
