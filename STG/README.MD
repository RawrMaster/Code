**Python >= 3.5** is required.

**Allowed methods:**

- Sorensen
- Jaro winkler
- Jaro
- Jaccard
- AhoCorasik

**Usage:**
run.py [-h] -m {sorensen, jaro_winkler, jaro, jaccard, ahocor} -c CONVERGENCE [-p {fast,slow}]

**Optional arguments:**

  -h, --help            show this help message and exit

  -m {sorensen,jaro_winkler,jaro,jaccard, ahocor}, --method {sorensen,jaro_winkler,jaro,jaccard}
                        Specify method name

  -c CONVERGENCE, --convergence CONVERGENCE
                        Specify a convergence value

  -p {fast,slow}, --performance {fast,slow}
                        Specify a performance mode

**Run:**

python run.py -m jaro -c 0.8

python run.py -m sorensen -c 0.8

**Research:**

python run_research.py �first asd �second asd

python run_research.py -f asdasd -s asdasd

**Previous algorithm:**

python run_prev.py -m jaro -c 0.8 -p fast

python run_prev.py -m sorensen -c 0.8 -p slow
