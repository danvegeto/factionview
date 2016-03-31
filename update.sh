set -v
mkdir static/data
python download.py
python get_correlations.py
python reduce.py
python join_data.py