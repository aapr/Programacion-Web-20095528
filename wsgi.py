from app import app as application

import sys
sys.path.insert(0,"/app/")

if __name__ == "__main__":
	application.run(host='0.0.0.0', port='5528')
