
---

# Landslide Sensor Data Analysis

This project involves data cleaning and analysis of landslide sensor data collected from various sensors installed at 10 locations around the Mandi district. The dataset includes attributes such as temperature, humidity, pressure, rainfall, light, and moisture.

## Dataset Details

- **dates**: Date of data collection.
- **stationid**: Indicates the location of the sensor.
- **temperature**: Atmospheric temperature around the sensor in Celsius.
- **humidity**: The concentration of water vapor present in the air (in g.m-3).
- **pressure**: Atmospheric pressure in millibars (mb).
- **rain**: Measure of rainfall in ml.
- **lightavgw/o0**: The average light throughout the daytime (in lux units).
- **lightmax**: The maximum lux count by the sensor.
- **moisture**: Indicates the water stored in the soil (measured between 0 to 100 percent).

## Project Tasks

1. **Plotting Missing Values**
   - Plot a graph of the attribute names (x-axis) with the number of missing values in them (y-axis).

2. **Handling Missing Values**
   - **Step 2a**: Drop tuples with missing values in the `stationid` attribute. Print the total number of tuples deleted.
   - **Step 2b**: Drop tuples having equal to or more than one third of attributes with missing values. Print the total number of tuples deleted.
   - **Step 3**: Count and print the number of missing values in each attribute after deletion of tuples. Also, print the total number of missing values in the file.

3. **Filling Missing Values**
   - **Step 4a**: Replace missing values by the mean of their respective attribute. Compute and compare the mean, median, mode, and standard deviation with the original file. Calculate and plot RMSE between the original and replaced values.
   - **Step 4b**: Replace missing values using the linear interpolation technique. Compute and compare the mean, median, mode, and standard deviation with the original file. Calculate and plot RMSE between the original and replaced values.

4. **Outlier Detection and Handling**
   - **Step 5a**: After replacing missing values by interpolation, find and list outliers in the `temperature` and `rain` attributes. Obtain the boxplot for these attributes.
   - **Step 5b**: Replace outliers by the median of the attribute. Plot the boxplot again and observe the difference.

## Usage

### Prerequisites

- Python 3.x
- pandas
- matplotlib
- numpy

### Steps to Run the Code

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/landslide-data-analysis.git
   cd landslide-data-analysis
   ```

2. Install the required libraries:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the Jupyter Notebook to execute the analysis:
   ```sh
   jupyter notebook
   ```

## Conclusion

This project demonstrates efficient data cleaning and analysis techniques on landslide sensor data. It highlights handling missing values using mean and interpolation methods, and outlier detection and treatment using interquartile range and median replacement.

## License

This project is licensed under the MIT License.

---
