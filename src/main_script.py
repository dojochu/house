import src.data_prep as dp
import src.data_analysis as da
import importlib;

data = dp.read_house_data('C:\\Users\\stephanie.kao\\PycharmProjects\\house_price_prediction\\resources\\')
print(data.head(10))
print(data.axes)