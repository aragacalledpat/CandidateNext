import sys, os
sys.path.insert (0,'/var/www/api/CandidateNext/candix_api')
os.chdir("/var/www/api/CandidateNext/candix_api")
from main import app as application
