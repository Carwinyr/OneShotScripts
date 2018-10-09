from pyspark.sql.types import *
from pyspark.sql.functions import array, col, explode, lit, struct
from pyspark.sql import DataFrame
from typing import Iterable 
from pyspark.sql.functions import first



def melt(
        df: DataFrame, 
        id_vars: Iterable[str], value_vars: Iterable[str], 
        var_name: str="variable", value_name: str="value") -> DataFrame:
    """Convert :class:`DataFrame` from wide to long format."""

    # Create array<struct<variable: str, value: ...>>
    # Here each row will have a different row structure with the column name that
    # will be taken
    _vars_and_vals = array(*(
        struct(lit(c).alias(var_name), col(c).alias(value_name)) 
        for c in value_vars))

    # Add to the DataFrame and explode
    # when exploding only columns that are included in the row structure will
    # be included in the datafrmae
    _tmp = df.withColumn("_vars_and_vals", explode(_vars_and_vals))
    
    # this one will have all the column names necessary
    cols = id_vars + [
            col("_vars_and_vals")[x].alias(x) for x in [var_name, value_name]]
    
    # when returning select from the previous one
    return _tmp.select(*cols)
	

def pivotSummary(
		df:DataFrame) -> DataFrame:
		'''
		Combined with the melt function above this function takes in a summary of a dataframe 
		calculated by `.describe()` function and outputs it in a long and more readable format
		especially in case of dataframes with many variables.
		'''
		
		schema = df.schema
		
		slist = []
		for i in schema:
			slist.append(i.name)
		
		id1 = slist[0]
		
		slist.remove('summary')
		
		longFormat = melt(df, id_vars = [id1], value_vars = slist)
		
		
		wideDF = longFormat.groupBy('variable').pivot('summary', ['count', 'mean', 'stddev', 'min', 'max']).agg(first('value'))
		
		return wideDF