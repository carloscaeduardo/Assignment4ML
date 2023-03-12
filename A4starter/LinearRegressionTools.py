import numpy as np
import PartB as temp_helper
import PartC as pc
import matplotlib as plt

MONTH_NAMES = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]


def r_squared(y, estimated):
    """
    Calculate the R-squared error term.

    Args:
        y: 1-d NumPy array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d NumPy array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    return (1 - (sum((y - estimated)**2))/(sum((y - np.mean(y))**2)))


def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.

    Args:
        x: an 1-d NumPy array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d NumPy array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d NumPy array of values estimated by a linear
            regression model
        model: a NumPy array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - np.mean(x))**2).sum()
    SE = np.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]
