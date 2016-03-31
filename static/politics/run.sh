for congress in {103..113}
do
	echo $congress

	echo 'House of Representatives'

	echo 'scraping...'
	python scrape_votes.py $congress h > votes.tsv
	echo 'processing...'
	python get_reps.py votes.tsv
	python reshape_votes.py votes.tsv
	python count_votes.py vote_matrix.tsv
	echo 'analyzing...'
	echo -e 'x\ty' > 2d_matrix.tsv
	python ~/tools/tsne/reduce.py dist_matrix.tsv >> 2d_matrix.tsv
	python join_data.py reps.tsv rep_ids.tsv 2d_matrix.tsv
	cp data.tsv $congress.h.tsv
	python get_common_votes.py vote_matrix.tsv > $congress.h.links.tsv
	echo 'done'

	echo 'Senate'

	echo 'scraping...'
	python scrape_votes.py $congress s > votes.tsv
	echo 'processing...'
	python get_reps.py votes.tsv
	python reshape_votes.py votes.tsv
	python count_votes.py vote_matrix.tsv
	echo 'analyzing...'
	echo -e 'x\ty' > 2d_matrix.tsv
	python ~/tools/tsne/reduce.py dist_matrix.tsv >> 2d_matrix.tsv
	python join_data.py reps.tsv rep_ids.tsv 2d_matrix.tsv
	cp data.tsv $congress.s.tsv
	python get_common_votes.py vote_matrix.tsv > $congress.s.links.tsv
	echo 'done'

done