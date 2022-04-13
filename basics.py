def mean (list):
    x_mean = sum(list) / len(list)
    return x_mean

def error(list,y):
    y_errors = [i - y for i in list]
    return y_errors

def variance (list):
    data_mean = mean(list)
    sum_of_squares = sum((i-data_mean)**2 for i in list)
    return sum_of_squares

def std_dev (list, deg_of_freedom=1):
    sum_of_sqaures = variance(list)
    pvar = sum_of_sqaures / (len(list) - deg_of_freedom)
    sd = pvar ** 0.5
    return sd

def covariance (list):
    covar = 0.0
    data_x = list;
    data_y = list;
    x_mean = mean(data_x)
    y_mean = mean(data_y)
    for i in range(len(data_x)):
        covar += (data_x[i] - x_mean) * (data_y[i] - y_mean)
    return covar
