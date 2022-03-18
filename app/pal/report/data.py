"""Prepare data for Plotly Dash.
"""

from logging import info
from time import time

import awswrangler as wr
from awswrangler.exceptions import EmptyDataFrame, NoFilesFound
from boto3 import session


S3_DOCS_BUCKET="s3-cloudfront-index"

def create_dataframe_from_parquet(
        path, partition_filter=None, columns=None,
        validate_schema=False, last_modified_begin=None,
        last_modified_end=None):
    """Read parquet stored in S3 compatible storage and returns Pandas
    Dataframe.

    :param path: S3 prefix (accepts Unix shell-style wildcards) (e.g.
        s3://bucket/prefix) or list of S3 objects paths (e.g. [s3://bucket/key0,
        s3://bucket/key1]).
    :param partition_filter: Callback Function filters to apply on PARTITION
        columns (PUSH-DOWN filter). This function MUST receive a single argument
        (Dict[str, str]) where keys are partitions names and values are
        partitions values. Partitions values will be always strings extracted
        from S3. This function MUST return a bool, True to read the partition or
        False to ignore it. Ignored if dataset=False.
    :param columns: Names of columns to read from the file(s).
    :param validate_schema: Check that individual file schemas are all the
        same / compatible. Schemas within a folder prefix should all be the
        same. Disable if you have schemas that are different and want to disable
        this check.
    :param last_modified_begin: Filter the s3 files by the Last modified date of
        the object. The filter is applied only after list all s3 files.
    :param last_modified_end: Filter the s3 files by the Last modified date of
        the object. The filter is applied only after list all s3 files.
    :type path: Union[str, List[str]]
    :type partition_filter: Callable[[Dict[str, str]], bool], optional
    :type columns: List[str], optional
    :type validate_schema: bool, optional
    :type last_modified_begin: datetime, optional
    :type last_modified_end: datetime, optional
    :returns: Pandas DataFrame or None if DataFrame cannot be fetched.
    :rtype: DataFrame
    """
    df = None
    start = time()
    try:
        df = wr.s3.read_parquet(
            path=path,
            path_suffix="parquet",
            ignore_empty=True,
            validate_schema=validate_schema,
            use_threads=True,
            dataset=True,
            columns=columns,
            partition_filter=partition_filter,
            last_modified_begin=last_modified_begin,
            last_modified_end=last_modified_end
        )
        info(f"Create dataframe {path} took: {time() - start}")
        info(df)
        info(df.info(memory_usage="deep"))
    except NoFilesFound:
        return df

    return df


def read_stats():
    """Read Suite Result Analysis data partition from parquet.
    """
    lambda_f = lambda part: True if part["stats_type"] == "sra" else False

    return create_dataframe_from_parquet(
        path=f"s3://{S3_DOCS_BUCKET}/parquet/stats",
        partition_filter=lambda_f
    )
