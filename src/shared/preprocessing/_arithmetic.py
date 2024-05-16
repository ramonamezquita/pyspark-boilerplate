import pyspark.sql.functions as F
from pyspark import keyword_only
from sparkml_base_classes import TransformerBaseClass


class TryDivide(TransformerBaseClass):
    """Custom Transformer wrapper class for functions.try_divide().

    Parameters
    ----------
    left: str
        Dividend.

    right: str
        Divisor.
    """

    @keyword_only
    def __init__(self, left: str = None, right: str = None, newcol: str = None):
        super().__init__()

    def _transform(self, ddf):
        return ddf.withColumn(
            self._newcol, F.try_divide(self._left, self._right)
        )
